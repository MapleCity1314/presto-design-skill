// @ts-nocheck

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
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
const GENERATION_MODEL = "claude-sonnet-4-6";
const JUDGE_MODEL = "gpt-4o";
const API_DELAY_MS = 1000;

const repoRoot = path.resolve(__dirname, "..", "..");
const evalRoot = __dirname;
const casesDir = path.join(evalRoot, "cases");
const resultsRoot = path.join(evalRoot, "results");
const anonymousDir = path.join(resultsRoot, "anonymous");
const scoresDir = path.join(resultsRoot, "scores");
const mappingPath = path.join(resultsRoot, "mapping.json");
const judgePromptPath = path.join(evalRoot, "judge-prompt.md");

function parseArgs(argv) {
  const options = {
    generate: false,
    anonymize: false,
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

    if (arg === "--anonymize") {
      options.anonymize = true;
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
    options.anonymize = true;
    options.judge = true;
    options.report = true;
  }

  if (!options.generate && !options.anonymize && !options.judge && !options.report) {
    throw new Error("Specify one of --generate, --anonymize, --judge, --report, or --all.");
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

function loadAnthropicSdk() {
  return require("@anthropic-ai/sdk").default;
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
  return FILE_LIST.map((relativePath) => readVariantFile(variant, relativePath)).join("\n\n");
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

function extractAnthropicText(response) {
  const blocks = Array.isArray(response?.content) ? response.content : [];
  const texts = blocks
    .filter((block) => block && block.type === "text" && typeof block.text === "string")
    .map((block) => block.text);

  if (texts.length === 0) {
    throw new Error("Anthropic response did not include any text content.");
  }

  return texts.join("\n").trim();
}

function extractJson(text) {
  try {
    return JSON.parse(text);
  } catch (error) {
    const match = text.match(/\{[\s\S]*\}/);
    if (!match) {
      throw error;
    }

    return JSON.parse(match[0]);
  }
}

async function generateOutputs(options, anthropic) {
  const selectedVariants = options.variant ? [options.variant] : Object.keys(VARIANT_SOURCES);
  const allCases = discoverCases();
  const selectedCases = options.case ? allCases.filter((entry) => entry.slug === options.case) : allCases;

  if (options.case && selectedCases.length === 0) {
    throw new Error(`No case found for slug: ${options.case}`);
  }

  const systemPrompts = {};
  for (const variant of selectedVariants) {
    systemPrompts[variant] = loadSystemPrompt(variant);
  }

  for (const variant of selectedVariants) {
    for (const testCase of selectedCases) {
      for (const runId of RUN_IDS) {
        const outputPath = path.join(resultsRoot, variant, testCase.slug, `${runId}.md`);

        if (fs.existsSync(outputPath)) {
          console.log(`skip generate ${variant}/${testCase.slug}/${runId} (exists)`);
          continue;
        }

        console.log(`generate ${variant}/${testCase.slug}/${runId} -> ${outputPath}`);

        if (options.dryRun) {
          continue;
        }

        const content = await withRetryOnce(`generate ${variant}/${testCase.slug}/${runId}`, async () => {
          const response = await anthropic.messages.create({
            model: GENERATION_MODEL,
            max_tokens: 4096,
            system: systemPrompts[variant],
            messages: [
              {
                role: "user",
                content: testCase.prompt
              }
            ]
          });

          return extractAnthropicText(response);
        });

        writeText(outputPath, `${content.trim()}\n`);
        await sleep(API_DELAY_MS);
      }
    }
  }
}

function findExistingOutputId(mapping, variant, caseSlug, runId) {
  for (const [outputId, entry] of Object.entries(mapping)) {
    if (entry.variant === variant && entry.case === caseSlug && entry.run === runId) {
      return outputId;
    }
  }

  return null;
}

function anonymizeOutputs(options) {
  ensureDir(anonymousDir);
  ensureDir(resultsRoot);

  const mapping = readJson(mappingPath, {});
  const allCases = discoverCases();
  const selectedVariants = options.variant ? [options.variant] : Object.keys(VARIANT_SOURCES);
  const selectedCaseSlugs = options.case ? new Set([options.case]) : new Set(allCases.map((entry) => entry.slug));

  for (const variant of selectedVariants) {
    for (const caseSlug of selectedCaseSlugs) {
      for (const runId of RUN_IDS) {
        const sourcePath = path.join(resultsRoot, variant, caseSlug, `${runId}.md`);
        if (!fs.existsSync(sourcePath)) {
          continue;
        }

        const existingId = findExistingOutputId(mapping, variant, caseSlug, runId);
        if (existingId) {
          const existingAnonymousPath = path.join(anonymousDir, `${existingId}.md`);
          if (fs.existsSync(existingAnonymousPath)) {
            console.log(`skip anonymize ${variant}/${caseSlug}/${runId} -> ${existingId} (exists)`);
            continue;
          }
        }

        const outputId = existingId || crypto.randomUUID();
        const targetPath = path.join(anonymousDir, `${outputId}.md`);
        console.log(`anonymize ${variant}/${caseSlug}/${runId} -> ${outputId}`);

        mapping[outputId] = {
          variant,
          case: caseSlug,
          run: runId
        };

        if (options.dryRun) {
          continue;
        }

        writeText(targetPath, readText(sourcePath));
        writeJson(mappingPath, mapping);
      }
    }
  }

  if (!options.dryRun) {
    writeJson(mappingPath, mapping);
  }
}

async function judgeOutputs(options, openaiClient) {
  ensureDir(scoresDir);

  const mapping = readJson(mappingPath, {});
  const judgeSystem = readText(judgePromptPath);
  const cases = discoverCases();
  const caseBySlug = new Map(cases.map((entry) => [entry.slug, entry]));
  const entries = Object.entries(mapping).sort(([left], [right]) => left.localeCompare(right));

  for (const [outputId, entry] of entries) {
    if (options.variant && entry.variant !== options.variant) {
      continue;
    }

    if (options.case && entry.case !== options.case) {
      continue;
    }

    const anonymousPath = path.join(anonymousDir, `${outputId}.md`);
    const scorePath = path.join(scoresDir, `${outputId}.json`);

    if (!fs.existsSync(anonymousPath)) {
      console.warn(`skip judge ${outputId} (missing anonymous file)`);
      continue;
    }

    if (fs.existsSync(scorePath)) {
      console.log(`skip judge ${outputId} (exists)`);
      continue;
    }

    const caseRecord = caseBySlug.get(entry.case);
    if (!caseRecord) {
      throw new Error(`Missing case file for slug referenced in mapping: ${entry.case}`);
    }

    const userPrompt = `## Task\n${caseRecord.prompt}\n\n## Output to score (ID: ${outputId})\n${readText(anonymousPath)}`;
    console.log(`judge ${outputId} -> ${scorePath}`);

    if (options.dryRun) {
      continue;
    }

    const score = await withRetryOnce(`judge ${outputId}`, async () => {
      const response = await openaiClient.chat.completions.create({
        model: JUDGE_MODEL,
        response_format: { type: "json_object" },
        messages: [
          { role: "system", content: judgeSystem },
          { role: "user", content: userPrompt }
        ]
      });

      const content = response?.choices?.[0]?.message?.content;
      if (!content) {
        throw new Error(`OpenAI response for ${outputId} did not include message content.`);
      }

      return extractJson(content);
    });

    writeJson(scorePath, score);
    await sleep(API_DELAY_MS);
  }
}

const ADVERSARIAL_CASES = new Set(["refine-dashboard-widget", "create-devtool-landing"]);
const SCORE_DIMENSIONS = ["design_quality", "clarity", "actionability", "adherence"] as const;
type Dimension = typeof SCORE_DIMENSIONS[number];

function mean(values: number[]): number {
  if (values.length === 0) return NaN;
  return values.reduce((a, b) => a + b, 0) / values.length;
}

function stddev(values: number[]): number {
  if (values.length < 2) return NaN;
  const m = mean(values);
  const variance = values.reduce((s, x) => s + (x - m) ** 2, 0) / (values.length - 1);
  return Math.sqrt(variance);
}

function fmt(n: number): string {
  return isNaN(n) ? "—" : n.toFixed(2);
}

function generateReport(_options: ReturnType<typeof parseArgs>): void {
  const mapping: Record<string, { variant: string; case: string; run: string }> = readJson(mappingPath, {});
  const entries = Object.entries(mapping);

  if (entries.length === 0) {
    console.warn("report: mapping.json is empty — run --anonymize and --judge first.");
    return;
  }

  // Load all scores
  interface ScoreRecord {
    output_id: string;
    scores: Record<Dimension, number>;
    total: number;
    reasoning?: string;
    adversarial_result?: string;
  }

  const scores: Array<{ outputId: string; variant: string; caseSlug: string; run: string; score: ScoreRecord }> = [];

  for (const [outputId, entry] of entries) {
    const scorePath = path.join(scoresDir, `${outputId}.json`);
    if (!fs.existsSync(scorePath)) continue;
    const score: ScoreRecord = readJson(scorePath, null);
    if (!score) continue;
    scores.push({ outputId, variant: entry.variant, caseSlug: entry.case, run: entry.run, score });
  }

  if (scores.length === 0) {
    console.warn("report: no score files found — run --judge first.");
    return;
  }

  const variants = ["v0", "v1", "v2"];
  const cases = discoverCases().map((c) => c.slug);

  // --- Per-dimension table: variant × dimension ---
  const lines: string[] = [];
  lines.push("# Presto Design Ablation — Results Report\n");
  lines.push(`Generated: ${new Date().toISOString()}`);
  lines.push(`Scores loaded: ${scores.length} / ${entries.length} outputs\n`);

  lines.push("## 1. Per-Dimension Table (mean ± std across all cases)\n");
  const dimHeader = SCORE_DIMENSIONS.map((d) => d.replace("_", "\\_")).join(" | ");
  lines.push(`| Variant | ${dimHeader} | total |`);
  lines.push(`| --- | ${SCORE_DIMENSIONS.map(() => "---").join(" | ")} | --- |`);

  for (const variant of variants) {
    const vScores = scores.filter((s) => s.variant === variant);
    const dimCols = SCORE_DIMENSIONS.map((dim) => {
      const vals = vScores.map((s) => s.score.scores?.[dim]).filter((v): v is number => typeof v === "number");
      return `${fmt(mean(vals))} ± ${fmt(stddev(vals))}`;
    });
    const totalVals = vScores.map((s) => s.score.total).filter((v): v is number => typeof v === "number");
    lines.push(`| **${variant}** | ${dimCols.join(" | ")} | ${fmt(mean(totalVals))} ± ${fmt(stddev(totalVals))} |`);
  }

  lines.push("\n## 2. Per-Case Table (mean total score per variant)\n");
  const variantHeader = variants.join(" | ");
  lines.push(`| Case | ${variantHeader} |`);
  lines.push(`| --- | ${variants.map(() => "---").join(" | ")} |`);

  for (const caseSlug of cases) {
    const isAdversarial = ADVERSARIAL_CASES.has(caseSlug);
    const label = isAdversarial ? `**${caseSlug}** ⚡` : caseSlug;
    const cols = variants.map((variant) => {
      const vals = scores
        .filter((s) => s.variant === variant && s.caseSlug === caseSlug)
        .map((s) => s.score.total)
        .filter((v): v is number => typeof v === "number");
      return `${fmt(mean(vals))} (n=${vals.length})`;
    });
    lines.push(`| ${label} | ${cols.join(" | ")} |`);
  }

  lines.push("\n## 3. Adversarial Case Results\n");
  lines.push("These cases test whether the FORBIDDEN UNLESS mechanism correctly permits the forbidden pattern.");
  lines.push("Review `reasoning` fields in the score JSON files to determine CORRECT/INCORRECT.\n");
  lines.push("| Case | v0 mean total | v1 mean total | v2 mean total | Notes |");
  lines.push("| --- | --- | --- | --- | --- |");

  for (const caseSlug of [...ADVERSARIAL_CASES]) {
    const cols = variants.map((variant) => {
      const vals = scores
        .filter((s) => s.variant === variant && s.caseSlug === caseSlug)
        .map((s) => s.score.total)
        .filter((v): v is number => typeof v === "number");
      return vals.length > 0 ? fmt(mean(vals)) : "—";
    });
    lines.push(`| **${caseSlug}** | ${cols.join(" | ")} | Review reasoning in scores/ |`);
  }

  lines.push("## 4. Variance Analysis\n");
  lines.push("High std = unstable skill. Compare across variants.\n");
  lines.push("| Variant | std(total) | std(design\\_quality) | std(adherence) |");
  lines.push("| --- | --- | --- | --- |");

  for (const variant of variants) {
    const vScores = scores.filter((s) => s.variant === variant);
    const totalStd = stddev(vScores.map((s) => s.score.total).filter((v): v is number => typeof v === "number"));
    const dqStd = stddev(vScores.map((s) => s.score.scores?.design_quality).filter((v): v is number => typeof v === "number"));
    const adhStd = stddev(vScores.map((s) => s.score.scores?.adherence).filter((v): v is number => typeof v === "number"));
    lines.push(`| **${variant}** | ${fmt(totalStd)} | ${fmt(dqStd)} | ${fmt(adhStd)} |`);
  }

  lines.push("\n## 5. Dimension-Specific Winners\n");

  for (const dim of [...SCORE_DIMENSIONS, "total"] as const) {
    const winner = variants.reduce((best, variant) => {
      const vals = scores
        .filter((s) => s.variant === variant)
        .map((s) => (dim === "total" ? s.score.total : s.score.scores?.[dim as Dimension]))
        .filter((v): v is number => typeof v === "number");
      const m = mean(vals);
      if (isNaN(best.mean) || m > best.mean) return { variant, mean: m };
      return best;
    }, { variant: "—", mean: NaN });

    const row = variants.map((v) => {
      const vals = scores
        .filter((s) => s.variant === v)
        .map((s) => (dim === "total" ? s.score.total : s.score.scores?.[dim as Dimension]))
        .filter((v2): v2 is number => typeof v2 === "number");
      return fmt(mean(vals));
    });
    lines.push(`- **${dim}**: winner = ${winner.variant} (${variants.map((v, i) => `${v}=${row[i]}`).join(", ")})`);
  }

  const reportPath = path.join(resultsRoot, "report.md");
  ensureDir(path.dirname(reportPath));
  writeText(reportPath, lines.join("\n") + "\n");
  console.log(`report written -> ${reportPath}`);
}

async function main() {
  const options = parseArgs(process.argv.slice(2));

  if (options.generate) {
    ensureEnv("ANTHROPIC_API_KEY");
  }

  if (options.judge) {
    ensureEnv("OPENAI_API_KEY");
  }

  ensureDir(resultsRoot);

  const anthropic = options.generate
    ? new (loadAnthropicSdk())({ apiKey: process.env.ANTHROPIC_API_KEY })
    : null;
  const openaiClient = options.judge
    ? new (loadOpenAiSdk())({ apiKey: process.env.OPENAI_API_KEY })
    : null;

  if (options.generate) {
    await generateOutputs(options, anthropic);
  }

  if (options.anonymize) {
    anonymizeOutputs(options);
  }

  if (options.judge) {
    await judgeOutputs(options, openaiClient);
  }

  if (options.report) {
    generateReport(options);
  }
}

main().catch((error) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(message);
  process.exit(1);
});
