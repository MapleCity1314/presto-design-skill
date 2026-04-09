// @ts-nocheck

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const FILE_LIST = [
  "SKILL.md",
  "contract.md",
  "clusters/create.md",
  "clusters/refine.md",
  "clusters/refine-layout.md",
  "clusters/refine-style.md",
  "clusters/redesign.md",
  "clusters/motion.md",
  "clusters/fix.md",
  "clusters/overdrive.md",
  "presets/editorial.md",
  "presets/minimalist.md"
];

const VARIANT_SOURCES = {
  v0: { type: "working-tree" },
  v1: { type: "git", ref: "variant/v1-verb-level" },
  v2: { type: "git", ref: "variant/v2-stripped" }
};

const RUN_IDS = Array.from({ length: 10 }, (_, index) => String(index + 1).padStart(2, "0"));
const AGENT_MODEL = process.env.EVAL_AGENT_MODEL || "gpt-4.1";
const API_DELAY_MS = 1000;

const repoRoot = path.resolve(__dirname, "..", "..");
const evalRoot = __dirname;
const casesDir = path.join(evalRoot, "cases");
const resultsRoot = path.join(evalRoot, "results");
const scoresRoot = path.join(resultsRoot, "scores");
const judgePromptPath = path.join(evalRoot, "judge-prompt.md");

function parseArgs(argv) {
  const options = {
    generate: false,
    judge: false,
    report: false,
    all: false,
    variant: null,
    case: null,
    dryRun: false
  };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];

    if (arg === "--generate") {
      options.generate = true;
      continue;
    }

    if (arg === "--judge") {
      options.judge = true;
      continue;
    }

    if (arg === "--all") {
      options.all = true;
      continue;
    }

    if (arg === "--report") {
      options.report = true;
      continue;
    }

    if (arg === "--dry-run") {
      options.dryRun = true;
      continue;
    }

    if (arg === "--anonymize") {
      console.warn("--anonymize is deprecated and ignored. Self-judging runs no longer anonymize outputs.");
      continue;
    }

    if (arg === "--variant") {
      options.variant = argv[index + 1] || null;
      index += 1;
      continue;
    }

    if (arg === "--case") {
      options.case = argv[index + 1] || null;
      index += 1;
      continue;
    }

    throw new Error(`Unknown argument: ${arg}`);
  }

  if (options.all) {
    options.generate = true;
    options.report = true;
  }

  if (!options.generate && !options.judge && !options.report) {
    throw new Error("Specify one of --generate, --judge, --report, or --all.");
  }

  if (options.variant && !Object.prototype.hasOwnProperty.call(VARIANT_SOURCES, options.variant)) {
    throw new Error(`Invalid --variant value: ${options.variant}. Expected one of v0, v1, v2.`);
  }

  return options;
}

function ensureEnv(name) {
  if (!process.env[name]) {
    throw new Error(`Missing required environment variable: ${name}`);
  }
}

function loadOpenAiSdk() {
  return require("openai").default;
}

function ensureDir(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true });
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function readText(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function writeText(filePath, content) {
  ensureDir(path.dirname(filePath));
  fs.writeFileSync(filePath, content, "utf8");
}

function writeJson(filePath, value) {
  writeText(filePath, `${JSON.stringify(value, null, 2)}\n`);
}

function readJson(filePath, fallback) {
  if (!fs.existsSync(filePath)) {
    return fallback;
  }

  return JSON.parse(readText(filePath));
}

function gitPath(relativePath) {
  return relativePath.split(path.sep).join("/");
}

function readVariantFile(variant, relativePath) {
  const source = VARIANT_SOURCES[variant];

  if (source.type === "working-tree") {
    return readText(path.join(repoRoot, relativePath));
  }

  const spec = `${source.ref}:${gitPath(relativePath)}`;
  return execSync(`git show ${spec}`, {
    cwd: repoRoot,
    encoding: "utf8",
    stdio: ["ignore", "pipe", "pipe"]
  });
}

function loadSystemPrompt(variant) {
  return FILE_LIST.map((relativePath) => `# FILE: ${relativePath}\n${readVariantFile(variant, relativePath)}`).join("\n\n");
}

function discoverCases() {
  return fs
    .readdirSync(casesDir)
    .filter((entry) => entry.endsWith(".md"))
    .sort()
    .map((entry) => {
      const slug = path.basename(entry, ".md");
      return {
        slug,
        path: path.join(casesDir, entry),
        prompt: readText(path.join(casesDir, entry))
      };
    });
}

async function withRetryOnce(taskName, fn) {
  try {
    return await fn();
  } catch (error) {
    if (!isRateLimitError(error)) {
      throw error;
    }

    console.warn(`${taskName}: received 429, retrying once after ${API_DELAY_MS}ms`);
    await sleep(API_DELAY_MS);
    return fn();
  }
}

function isRateLimitError(error) {
  const status = error?.status ?? error?.statusCode ?? error?.response?.status;
  return status === 429;
}

function extractJson(text) {
  try {
    return JSON.parse(text);
  } catch (error) {
    const fenced = text.match(/```(?:json)?\s*([\s\S]*?)```/i);
    if (fenced) {
      return JSON.parse(fenced[1]);
    }

    const match = text.match(/\{[\s\S]*\}/);
    if (!match) {
      throw error;
    }

    return JSON.parse(match[0]);
  }
}

function outputPathFor(variant, caseSlug, runId) {
  return path.join(resultsRoot, variant, caseSlug, `${runId}.md`);
}

function scorePathFor(variant, caseSlug, runId) {
  return path.join(scoresRoot, variant, caseSlug, `${runId}.json`);
}

function buildGenerationSystemPrompt() {
  return [
    "You are an autonomous UI design evaluation agent.",
    "You will be given a full Presto Design skill variant and one evaluation case.",
    "First, act as the generator: produce the strongest possible assistant output that faithfully follows the supplied skill and solves the case.",
    "The generated output should read like a real skill response, not meta commentary about evaluation.",
    "Then stop. Do not self-score in this step."
  ].join("\n");
}

function buildGenerationUserPrompt(variant, testCase) {
  return [
    `## Variant`,
    variant,
    "",
    "## Skill context",
    loadSystemPrompt(variant),
    "",
    "## Eval case",
    testCase.prompt,
    "",
    "## Task",
    "Read the skill context and the eval case. Generate the final skill output only."
  ].join("\n");
}

function buildJudgeUserPrompt(variant, testCase, outputText, judgeSystem) {
  return [
    "## Variant",
    variant,
    "",
    "## Eval case",
    testCase.prompt,
    "",
    "## Judge rubric",
    judgeSystem,
    "",
    "## Output to score",
    outputText,
    "",
    "Return valid JSON only with this exact shape:",
    "{",
    '  "output_id": "string",',
    '  "scores": {',
    '    "design_quality": 0,',
    '    "clarity": 0,',
    '    "actionability": 0,',
    '    "adherence": 0',
    "  },",
    '  "total": 0,',
    '  "reasoning": "short explanation"',
    "}"
  ].join("\n");
}

async function createChatCompletion(openaiClient, taskName, messages, jsonMode) {
  return withRetryOnce(taskName, async () => {
    const response = await openaiClient.chat.completions.create({
      model: AGENT_MODEL,
      response_format: jsonMode ? { type: "json_object" } : undefined,
      messages
    });

    const content = response?.choices?.[0]?.message?.content;
    if (!content) {
      throw new Error(`${taskName}: model response did not include message content.`);
    }

    return content.trim();
  });
}

async function generateOutputs(options, openaiClient) {
  const selectedVariants = options.variant ? [options.variant] : Object.keys(VARIANT_SOURCES);
  const allCases = discoverCases();
  const selectedCases = options.case ? allCases.filter((entry) => entry.slug === options.case) : allCases;

  if (options.case && selectedCases.length === 0) {
    throw new Error(`No case found for slug: ${options.case}`);
  }

  const judgeSystem = readText(judgePromptPath);

  for (const variant of selectedVariants) {
    for (const testCase of selectedCases) {
      for (const runId of RUN_IDS) {
        const outputPath = outputPathFor(variant, testCase.slug, runId);
        const scorePath = scorePathFor(variant, testCase.slug, runId);

        if (fs.existsSync(outputPath) && fs.existsSync(scorePath)) {
          console.log(`skip generate ${variant}/${testCase.slug}/${runId} (output + score exist)`);
          continue;
        }

        console.log(`agent run ${variant}/${testCase.slug}/${runId}`);

        if (options.dryRun) {
          continue;
        }

        const outputText = fs.existsSync(outputPath)
          ? readText(outputPath)
          : await createChatCompletion(
              openaiClient,
              `generate ${variant}/${testCase.slug}/${runId}`,
              [
                { role: "system", content: buildGenerationSystemPrompt() },
                { role: "user", content: buildGenerationUserPrompt(variant, testCase) }
              ],
              false
            );

        writeText(outputPath, `${outputText.trim()}\n`);
        await sleep(API_DELAY_MS);

        const score = await createChatCompletion(
          openaiClient,
          `judge ${variant}/${testCase.slug}/${runId}`,
          [
            { role: "system", content: "You are grading a generated UI design skill output. Be strict, specific, and return JSON only." },
            { role: "user", content: buildJudgeUserPrompt(variant, testCase, outputText, judgeSystem) }
          ],
          true
        );

        const parsed = extractJson(score);
        parsed.output_id = `${variant}/${testCase.slug}/${runId}`;
        writeJson(scorePath, parsed);
        await sleep(API_DELAY_MS);
      }
    }
  }
}

async function judgeExistingOutputs(options, openaiClient) {
  const selectedVariants = options.variant ? [options.variant] : Object.keys(VARIANT_SOURCES);
  const allCases = discoverCases();
  const selectedCases = options.case ? allCases.filter((entry) => entry.slug === options.case) : allCases;

  if (options.case && selectedCases.length === 0) {
    throw new Error(`No case found for slug: ${options.case}`);
  }

  const judgeSystem = readText(judgePromptPath);

  for (const variant of selectedVariants) {
    for (const testCase of selectedCases) {
      for (const runId of RUN_IDS) {
        const outputPath = outputPathFor(variant, testCase.slug, runId);
        const scorePath = scorePathFor(variant, testCase.slug, runId);

        if (!fs.existsSync(outputPath)) {
          continue;
        }

        if (fs.existsSync(scorePath)) {
          console.log(`skip judge ${variant}/${testCase.slug}/${runId} (score exists)`);
          continue;
        }

        console.log(`judge existing ${variant}/${testCase.slug}/${runId}`);

        if (options.dryRun) {
          continue;
        }

        const outputText = readText(outputPath);
        const score = await createChatCompletion(
          openaiClient,
          `judge ${variant}/${testCase.slug}/${runId}`,
          [
            { role: "system", content: "You are grading a generated UI design skill output. Be strict, specific, and return JSON only." },
            { role: "user", content: buildJudgeUserPrompt(variant, testCase, outputText, judgeSystem) }
          ],
          true
        );

        const parsed = extractJson(score);
        parsed.output_id = `${variant}/${testCase.slug}/${runId}`;
        writeJson(scorePath, parsed);
        await sleep(API_DELAY_MS);
      }
    }
  }
}

const ADVERSARIAL_CASES = new Set(["refine-dashboard-widget", "create-devtool-landing"]);
const SCORE_DIMENSIONS = ["design_quality", "clarity", "actionability", "adherence"];

function mean(values) {
  if (values.length === 0) return NaN;
  return values.reduce((a, b) => a + b, 0) / values.length;
}

function stddev(values) {
  if (values.length < 2) return NaN;
  const m = mean(values);
  const variance = values.reduce((sum, value) => sum + (value - m) ** 2, 0) / (values.length - 1);
  return Math.sqrt(variance);
}

function fmt(value) {
  return Number.isNaN(value) ? "n/a" : value.toFixed(2);
}

function collectScores() {
  const cases = discoverCases();
  const caseSlugs = cases.map((entry) => entry.slug);
  const variants = Object.keys(VARIANT_SOURCES);
  const scores = [];

  for (const variant of variants) {
    for (const caseSlug of caseSlugs) {
      for (const runId of RUN_IDS) {
        const scorePath = scorePathFor(variant, caseSlug, runId);
        if (!fs.existsSync(scorePath)) {
          continue;
        }

        const score = readJson(scorePath, null);
        if (!score) {
          continue;
        }

        scores.push({
          variant,
          caseSlug,
          run: runId,
          score
        });
      }
    }
  }

  return scores;
}

function generateReport() {
  const scores = collectScores();
  const variants = Object.keys(VARIANT_SOURCES);
  const cases = discoverCases().map((entry) => entry.slug);

  if (scores.length === 0) {
    console.warn("report: no score files found - run --generate or --judge first.");
    return;
  }

  const expectedOutputs = variants.length * cases.length * RUN_IDS.length;
  const lines = [];
  lines.push("# Presto Design Ablation Results Report\n");
  lines.push(`Generated: ${new Date().toISOString()}`);
  lines.push(`Agent model: ${AGENT_MODEL}`);
  lines.push(`Scores loaded: ${scores.length} / ${expectedOutputs}\n`);

  lines.push("## 1. Per-Dimension Table (mean +/- std across all cases)\n");
  const dimHeader = SCORE_DIMENSIONS.map((dimension) => dimension.replace("_", "\\_")).join(" | ");
  lines.push(`| Variant | ${dimHeader} | total |`);
  lines.push(`| --- | ${SCORE_DIMENSIONS.map(() => "---").join(" | ")} | --- |`);

  for (const variant of variants) {
    const variantScores = scores.filter((entry) => entry.variant === variant);
    const dimCols = SCORE_DIMENSIONS.map((dimension) => {
      const values = variantScores
        .map((entry) => entry.score?.scores?.[dimension])
        .filter((value) => typeof value === "number");
      return `${fmt(mean(values))} +/- ${fmt(stddev(values))}`;
    });
    const totalValues = variantScores.map((entry) => entry.score?.total).filter((value) => typeof value === "number");
    lines.push(`| **${variant}** | ${dimCols.join(" | ")} | ${fmt(mean(totalValues))} +/- ${fmt(stddev(totalValues))} |`);
  }

  lines.push("\n## 2. Per-Case Table (mean total score per variant)\n");
  lines.push(`| Case | ${variants.join(" | ")} |`);
  lines.push(`| --- | ${variants.map(() => "---").join(" | ")} |`);

  for (const caseSlug of cases) {
    const label = ADVERSARIAL_CASES.has(caseSlug) ? `**${caseSlug}** [adversarial]` : caseSlug;
    const cols = variants.map((variant) => {
      const values = scores
        .filter((entry) => entry.variant === variant && entry.caseSlug === caseSlug)
        .map((entry) => entry.score?.total)
        .filter((value) => typeof value === "number");
      return `${fmt(mean(values))} (n=${values.length})`;
    });
    lines.push(`| ${label} | ${cols.join(" | ")} |`);
  }

  lines.push("\n## 3. Adversarial Case Results\n");
  lines.push("These cases test whether the FORBIDDEN UNLESS mechanism is applied correctly.");
  lines.push("| Case | v0 mean total | v1 mean total | v2 mean total | Notes |");
  lines.push("| --- | --- | --- | --- | --- |");

  for (const caseSlug of [...ADVERSARIAL_CASES]) {
    const cols = variants.map((variant) => {
      const values = scores
        .filter((entry) => entry.variant === variant && entry.caseSlug === caseSlug)
        .map((entry) => entry.score?.total)
        .filter((value) => typeof value === "number");
      return values.length > 0 ? fmt(mean(values)) : "n/a";
    });
    lines.push(`| **${caseSlug}** | ${cols.join(" | ")} | Review per-run reasoning in scores/ |`);
  }

  lines.push("\n## 4. Variance Analysis\n");
  lines.push("High std means the skill is less stable across repeated runs.\n");
  lines.push("| Variant | std(total) | std(design\\_quality) | std(adherence) |");
  lines.push("| --- | --- | --- | --- |");

  for (const variant of variants) {
    const variantScores = scores.filter((entry) => entry.variant === variant);
    const totalStd = stddev(variantScores.map((entry) => entry.score?.total).filter((value) => typeof value === "number"));
    const dqStd = stddev(
      variantScores.map((entry) => entry.score?.scores?.design_quality).filter((value) => typeof value === "number")
    );
    const adherenceStd = stddev(
      variantScores.map((entry) => entry.score?.scores?.adherence).filter((value) => typeof value === "number")
    );
    lines.push(`| **${variant}** | ${fmt(totalStd)} | ${fmt(dqStd)} | ${fmt(adherenceStd)} |`);
  }

  lines.push("\n## 5. Dimension-Specific Winners\n");

  for (const dimension of [...SCORE_DIMENSIONS, "total"]) {
    const winner = variants.reduce(
      (best, variant) => {
        const values = scores
          .filter((entry) => entry.variant === variant)
          .map((entry) => (dimension === "total" ? entry.score?.total : entry.score?.scores?.[dimension]))
          .filter((value) => typeof value === "number");
        const currentMean = mean(values);
        if (Number.isNaN(best.mean) || currentMean > best.mean) {
          return { variant, mean: currentMean };
        }
        return best;
      },
      { variant: "n/a", mean: NaN }
    );

    const row = variants.map((variant) => {
      const values = scores
        .filter((entry) => entry.variant === variant)
        .map((entry) => (dimension === "total" ? entry.score?.total : entry.score?.scores?.[dimension]))
        .filter((value) => typeof value === "number");
      return fmt(mean(values));
    });

    lines.push(`- **${dimension}**: winner = ${winner.variant} (${variants.map((variant, index) => `${variant}=${row[index]}`).join(", ")})`);
  }

  const reportPath = path.join(resultsRoot, "report.md");
  writeText(reportPath, `${lines.join("\n")}\n`);
  console.log(`report written -> ${reportPath}`);
}

async function main() {
  const options = parseArgs(process.argv.slice(2));

  if ((options.generate || options.judge) && !options.dryRun) {
    ensureEnv("OPENAI_API_KEY");
  }

  ensureDir(resultsRoot);
  ensureDir(scoresRoot);

  const needsOpenAiClient = (options.generate || options.judge) && !options.dryRun;
  const openaiClient = needsOpenAiClient ? new (loadOpenAiSdk())({ apiKey: process.env.OPENAI_API_KEY }) : null;

  if (options.generate) {
    await generateOutputs(options, openaiClient);
  }

  if (options.judge) {
    await judgeExistingOutputs(options, openaiClient);
  }

  if (options.report) {
    generateReport();
  }
}

main().catch((error) => {
  const message = error instanceof Error ? error.stack || error.message : String(error);
  console.error(message);
  process.exit(1);
});
