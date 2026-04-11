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

const DEFAULT_RUN_COUNT = Number(process.env.EVAL_RUN_COUNT || 3);
const DEFAULT_JUDGE_REPEATS = Number(process.env.EVAL_JUDGE_REPEATS || 3);
const DEFAULT_GENERATOR_MODEL = process.env.EVAL_GENERATOR_MODEL || "";
const DEFAULT_JUDGE_MODELS = (process.env.EVAL_JUDGE_MODELS || "")
  .split(",")
  .map((value) => value.trim())
  .filter(Boolean);
const API_DELAY_MS = Number(process.env.EVAL_API_DELAY_MS || 1000);
const LEGACY_RUN_COUNT = 10;

const repoRoot = path.resolve(__dirname, "..", "..");
const evalRoot = __dirname;
const casesRoot = path.join(evalRoot, "cases");
const casesManifestPath = path.join(evalRoot, "cases.manifest.json");
const resultsRoot = path.join(evalRoot, "results");
const generationsRoot = path.join(resultsRoot, "generations");
const judgmentsRoot = path.join(resultsRoot, "judgments");
const reportsRoot = path.join(resultsRoot, "reports");
const legacyOutputsRoot = resultsRoot;
const legacyScoresRoot = path.join(resultsRoot, "scores");
const judgePromptPath = path.join(evalRoot, "judge-prompt.md");

function parseArgs(argv) {
  const options = {
    generate: false,
    judge: false,
    report: false,
    validate: false,
    printGeneratePrompt: false,
    printJudgePrompt: false,
    ingestGenerationFile: null,
    ingestJudgmentFile: null,
    all: false,
    variant: null,
    case: null,
    runId: null,
    judgeModel: null,
    attempt: null,
    dryRun: false,
    force: false,
    runCount: DEFAULT_RUN_COUNT,
    judgeRepeats: DEFAULT_JUDGE_REPEATS
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

    if (arg === "--report") {
      options.report = true;
      continue;
    }

    if (arg === "--validate") {
      options.validate = true;
      continue;
    }

    if (arg === "--print-generate-prompt") {
      options.printGeneratePrompt = true;
      continue;
    }

    if (arg === "--print-judge-prompt") {
      options.printJudgePrompt = true;
      continue;
    }

    if (arg === "--ingest-generation-file") {
      options.ingestGenerationFile = argv[index + 1] || null;
      index += 1;
      continue;
    }

    if (arg === "--ingest-judgment-file") {
      options.ingestJudgmentFile = argv[index + 1] || null;
      index += 1;
      continue;
    }

    if (arg === "--all") {
      options.all = true;
      continue;
    }

    if (arg === "--dry-run") {
      options.dryRun = true;
      continue;
    }

    if (arg === "--force") {
      options.force = true;
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

    if (arg === "--run-id") {
      options.runId = argv[index + 1] || null;
      index += 1;
      continue;
    }

    if (arg === "--judge-model") {
      options.judgeModel = argv[index + 1] || null;
      index += 1;
      continue;
    }

    if (arg === "--attempt") {
      options.attempt = argv[index + 1] || null;
      index += 1;
      continue;
    }

    if (arg === "--run-count") {
      options.runCount = Number(argv[index + 1] || options.runCount);
      index += 1;
      continue;
    }

    if (arg === "--judge-repeats") {
      options.judgeRepeats = Number(argv[index + 1] || options.judgeRepeats);
      index += 1;
      continue;
    }

    throw new Error(`Unknown argument: ${arg}`);
  }

  if (options.all) {
    options.generate = true;
    options.judge = true;
    options.report = true;
    options.validate = true;
  }

  if (
    !options.generate &&
    !options.judge &&
    !options.report &&
    !options.validate &&
    !options.printGeneratePrompt &&
    !options.printJudgePrompt &&
    !options.ingestGenerationFile &&
    !options.ingestJudgmentFile
  ) {
    throw new Error("Specify one of --generate, --judge, --report, --validate, --print-generate-prompt, --print-judge-prompt, --ingest-generation-file, --ingest-judgment-file, or --all.");
  }

  if (options.variant && !Object.prototype.hasOwnProperty.call(VARIANT_SOURCES, options.variant)) {
    throw new Error(`Invalid --variant value: ${options.variant}. Expected one of ${Object.keys(VARIANT_SOURCES).join(", ")}.`);
  }

  if (!Number.isInteger(options.runCount) || options.runCount < 1) {
    throw new Error(`Invalid --run-count: ${options.runCount}`);
  }

  if (!Number.isInteger(options.judgeRepeats) || options.judgeRepeats < 1) {
    throw new Error(`Invalid --judge-repeats: ${options.judgeRepeats}`);
  }

  if ((options.printGeneratePrompt || options.printJudgePrompt) && !options.variant) {
    throw new Error("--print-generate-prompt and --print-judge-prompt require --variant.");
  }

  if ((options.printGeneratePrompt || options.printJudgePrompt) && !options.case) {
    throw new Error("--print-generate-prompt and --print-judge-prompt require --case.");
  }

  if (options.printJudgePrompt && !options.runId) {
    throw new Error("--print-judge-prompt requires --run-id.");
  }

  if (options.ingestGenerationFile && (!options.variant || !options.case || !options.runId)) {
    throw new Error("--ingest-generation-file requires --variant, --case, and --run-id.");
  }

  if (options.ingestJudgmentFile && (!options.variant || !options.case || !options.runId || !options.judgeModel || !options.attempt)) {
    throw new Error("--ingest-judgment-file requires --variant, --case, --run-id, --judge-model, and --attempt.");
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

function readJson(filePath, fallback) {
  if (!fs.existsSync(filePath)) {
    return fallback;
  }

  return JSON.parse(readText(filePath));
}

function writeJson(filePath, value) {
  writeText(filePath, `${JSON.stringify(value, null, 2)}\n`);
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

function sha256(value) {
  return crypto.createHash("sha256").update(value).digest("hex");
}

function slugify(value) {
  return value.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
}

function median(values) {
  if (values.length === 0) return NaN;
  const sorted = [...values].sort((a, b) => a - b);
  const mid = Math.floor(sorted.length / 2);
  return sorted.length % 2 === 1 ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;
}

function mean(values) {
  if (values.length === 0) return NaN;
  return values.reduce((sum, value) => sum + value, 0) / values.length;
}

function stddev(values) {
  if (values.length < 2) return NaN;
  const avg = mean(values);
  const variance = values.reduce((sum, value) => sum + (value - avg) ** 2, 0) / (values.length - 1);
  return Math.sqrt(variance);
}

function fmt(value, digits = 2) {
  return Number.isNaN(value) ? "n/a" : value.toFixed(digits);
}

function pct(numerator, denominator) {
  if (!denominator) return "n/a";
  return `${((numerator / denominator) * 100).toFixed(1)}%`;
}

function runIdsFor(count) {
  return Array.from({ length: count }, (_, index) => String(index + 1).padStart(2, "0"));
}

function outputPathFor(variant, caseSlug, runId) {
  return path.join(generationsRoot, variant, caseSlug, `run-${runId}.md`);
}

function outputMetaPathFor(variant, caseSlug, runId) {
  return path.join(generationsRoot, variant, caseSlug, `run-${runId}.meta.json`);
}

function judgmentPathFor(variant, caseSlug, runId, judgeModel, attempt) {
  return path.join(judgmentsRoot, variant, caseSlug, `run-${runId}`, slugify(judgeModel), `attempt-${attempt}.json`);
}

function buildGenerationSystemPrompt() {
  return [
    "You are an autonomous UI design evaluation agent.",
    "You will be given a full Presto Design skill variant and one evaluation case.",
    "Produce the strongest possible assistant output that faithfully follows the supplied skill and solves the case.",
    "Return the final generator output only.",
    "Do not self-score."
  ].join("\n");
}

function buildGenerationUserPrompt(variant, testCase) {
  return [
    "## Variant",
    variant,
    "",
    "## Skill context",
    loadSystemPrompt(variant),
    "",
    "## Eval case",
    testCase.task,
    "",
    "## Task",
    "Read the skill context and the eval case. Generate the final skill output only."
  ].join("\n");
}

function normalizeOutputForJudge(outputText) {
  return outputText
    .split(/\r?\n/)
    .map((line) =>
      line
        .replace(/<\/?design-log>/gi, "")
        .replace(/^#{1,6}\s*/, "")
        .replace(/^\s*DECISION:\s*/i, "")
        .replace(/^\s*BECAUSE:\s*/i, "")
        .replace(/^\s*DEVIATION:\s*/i, "")
        .replace(/\b-v[0-9]+\b/gi, "")
    )
    .filter((line) => !/^\s*(Context Phase|Design Parameters|What Changed|VERIFICATION)\s*$/i.test(line))
    .join("\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function renderRubric(caseDef) {
  return caseDef.rubric.items.map((item, index) => `${index + 1}. ${item}`).join("\n");
}

function buildJudgePrompt(caseDef, outputText) {
  return readText(judgePromptPath)
    .replaceAll("{case_id}", caseDef.slug)
    .replace("{task}", caseDef.task.trim())
    .replace("{output}", normalizeOutputForJudge(outputText))
    .replace("{rubric}", renderRubric(caseDef));
}

function extractJson(text) {
  try {
    return JSON.parse(text);
  } catch (error) {
    const fenced = text.match(/```(?:json)?\s*([\s\S]*?)```/i);
    if (fenced) {
      return JSON.parse(fenced[1]);
    }

    const objectMatch = text.match(/\{[\s\S]*\}/);
    if (!objectMatch) {
      throw error;
    }

    return JSON.parse(objectMatch[0]);
  }
}

async function withRetryOnce(taskName, fn) {
  try {
    return await fn();
  } catch (error) {
    const status = error?.status ?? error?.statusCode ?? error?.response?.status;
    if (status !== 429) {
      throw error;
    }

    console.warn(`${taskName}: received 429, retrying once after ${API_DELAY_MS}ms`);
    await sleep(API_DELAY_MS);
    return fn();
  }
}

async function createChatCompletion(openaiClient, taskName, model, messages, jsonMode) {
  return withRetryOnce(taskName, async () => {
    const response = await openaiClient.chat.completions.create({
      model,
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

function discoverCases() {
  const manifest = fs.existsSync(casesManifestPath) ? readJson(casesManifestPath, null) : null;
  const caseIds =
    manifest?.cases?.map((entry) => entry.case_id) ||
    fs
      .readdirSync(casesRoot, { withFileTypes: true })
      .filter((entry) => entry.isDirectory())
      .sort((a, b) => a.name.localeCompare(b.name))
      .map((entry) => entry.name);

  return caseIds.map((slug) => {
      const taskPath = path.join(casesRoot, slug, "task.md");
      const rubricPath = path.join(casesRoot, slug, "rubric.json");

      if (!fs.existsSync(taskPath)) {
        throw new Error(`Missing task.md for case ${slug}`);
      }

      if (!fs.existsSync(rubricPath)) {
        throw new Error(`Missing rubric.json for case ${slug}`);
      }

      return {
        slug,
        taskPath,
        rubricPath,
        task: readText(taskPath),
        rubric: readJson(rubricPath, null)
      };
    });
}

function validateCaseDefinition(caseDef) {
  const problems = [];

  if (caseDef.rubric?.case_id !== caseDef.slug) {
    problems.push(`rubric.case_id mismatch: expected ${caseDef.slug}, got ${caseDef.rubric?.case_id}`);
  }

  if (!Array.isArray(caseDef.rubric?.items)) {
    problems.push("rubric.items must be an array");
  } else {
    if (caseDef.rubric.items.length < 8 || caseDef.rubric.items.length > 12) {
      problems.push(`rubric.items length must be 8-12; got ${caseDef.rubric.items.length}`);
    }

    caseDef.rubric.items.forEach((item, index) => {
      if (typeof item !== "string" || item.trim().length === 0) {
        problems.push(`rubric item ${index + 1} must be a non-empty string`);
      }
    });
  }

  if (!caseDef.task.includes("Task") && !caseDef.task.includes("Task description")) {
    problems.push("task.md should include a task description section");
  }

  return problems;
}

function validateStructuredResults(caseSlugs, runCount) {
  const problems = [];
  const generationRows = collectStructuredGenerationRows(caseSlugs, runCount);
  const judgmentRows = loadStructuredJudgments(caseSlugs, runCount);

  for (const row of generationRows) {
    if (!row.metadata) {
      problems.push(`missing generation metadata: ${row.outputPath}`);
      continue;
    }

    if (!row.metadata.generator_model) {
      problems.push(`generation metadata missing generator_model: ${row.outputPath}`);
    }
  }

  for (const row of judgmentRows) {
    if (!row.metadata.judge_model) {
      problems.push(`judgment metadata missing judge_model: ${row.path}`);
    }
    if (!row.metadata.judge_prompt_hash) {
      problems.push(`judgment metadata missing judge_prompt_hash: ${row.path}`);
    }
    if (!row.metadata.rubric_hash) {
      problems.push(`judgment metadata missing rubric_hash: ${row.path}`);
    }
  }

  return problems;
}

function runValidation(options) {
  const cases = discoverCases();
  const caseProblems = [];
  for (const caseDef of cases) {
    const problems = validateCaseDefinition(caseDef);
    for (const problem of problems) {
      caseProblems.push(`${caseDef.slug}: ${problem}`);
    }
  }

  const resultProblems = validateStructuredResults(
    cases.map((entry) => entry.slug),
    options.runCount
  );

  if (caseProblems.length === 0 && resultProblems.length === 0) {
    console.log("validate: OK");
    return;
  }

  for (const problem of [...caseProblems, ...resultProblems]) {
    console.error(`validate: ${problem}`);
  }

  throw new Error(`Validation failed with ${caseProblems.length + resultProblems.length} issue(s).`);
}

function printGeneratePrompt(options) {
  const testCase = selectCases(discoverCases(), options.case)[0];
  const payload = {
    variant: options.variant,
    case_id: testCase.slug,
    system: buildGenerationSystemPrompt(),
    user: buildGenerationUserPrompt(options.variant, testCase)
  };
  process.stdout.write(`${JSON.stringify(payload, null, 2)}\n`);
}

function printJudgePrompt(options) {
  const testCase = selectCases(discoverCases(), options.case)[0];
  const outputPath = outputPathFor(options.variant, testCase.slug, options.runId);
  if (!fs.existsSync(outputPath)) {
    throw new Error(`Missing generation output for --print-judge-prompt: ${outputPath}`);
  }

  const payload = {
    variant: options.variant,
    case_id: testCase.slug,
    run_id: options.runId,
    system: "Apply the rubric literally. Return JSON only.",
    user: buildJudgePrompt(testCase, readText(outputPath))
  };
  process.stdout.write(`${JSON.stringify(payload, null, 2)}\n`);
}

function ingestGenerationFromFile(options) {
  const sourcePath = path.resolve(process.cwd(), options.ingestGenerationFile);
  if (!fs.existsSync(sourcePath)) {
    throw new Error(`Missing generation source file: ${sourcePath}`);
  }

  const outputText = readText(sourcePath).trim();
  const outputPath = outputPathFor(options.variant, options.case, options.runId);
  const metaPath = outputMetaPathFor(options.variant, options.case, options.runId);

  const meta = {
    variant: options.variant,
    case_id: options.case,
    run_id: options.runId,
    generator_model: DEFAULT_GENERATOR_MODEL || "subagent-manual",
    generated_at: new Date().toISOString(),
    prompt_hash: "manual-subagent-ingest",
    judge_prompt_version: "v2",
    source_file: sourcePath
  };

  writeText(outputPath, `${outputText}\n`);
  writeJson(metaPath, meta);
  console.log(`ingested generation -> ${outputPath}`);
}

function ingestJudgmentFromFile(options) {
  const sourcePath = path.resolve(process.cwd(), options.ingestJudgmentFile);
  if (!fs.existsSync(sourcePath)) {
    throw new Error(`Missing judgment source file: ${sourcePath}`);
  }

  const payload = extractJson(readText(sourcePath));
  const outPath = judgmentPathFor(options.variant, options.case, options.runId, options.judgeModel, options.attempt);

  writeJson(outPath, {
    metadata: {
      variant: options.variant,
      case_id: options.case,
      run_id: options.runId,
      judge_model: options.judgeModel,
      judge_attempt: options.attempt,
      judged_at: new Date().toISOString(),
      judge_prompt_hash: "manual-subagent-ingest",
      judge_prompt_version: "v2",
      rubric_hash: "manual-subagent-ingest",
      source_file: sourcePath
    },
    result: payload
  });

  console.log(`ingested judgment -> ${outPath}`);
}

function selectCases(allCases, caseSlug) {
  if (!caseSlug) {
    return allCases;
  }

  const selected = allCases.filter((entry) => entry.slug === caseSlug);
  if (selected.length === 0) {
    throw new Error(`No case found for slug: ${caseSlug}`);
  }

  return selected;
}

async function generateOutputs(options, openaiClient) {
  const generatorModel = DEFAULT_GENERATOR_MODEL;
  if (!generatorModel && !options.dryRun) {
    throw new Error("Missing EVAL_GENERATOR_MODEL. Refusing to run generation with an implicit default model.");
  }

  const selectedVariants = options.variant ? [options.variant] : Object.keys(VARIANT_SOURCES);
  const selectedCases = selectCases(discoverCases(), options.case);

  for (const variant of selectedVariants) {
    for (const testCase of selectedCases) {
      for (const runId of runIdsFor(options.runCount)) {
        const outputPath = outputPathFor(variant, testCase.slug, runId);
        const metaPath = outputMetaPathFor(variant, testCase.slug, runId);

        if (!options.force && fs.existsSync(outputPath) && fs.existsSync(metaPath)) {
          console.log(`skip generate ${variant}/${testCase.slug}/${runId} (output exists)`);
          continue;
        }

        console.log(`generate ${variant}/${testCase.slug}/${runId}`);

        if (options.dryRun) {
          continue;
        }

        const systemPrompt = buildGenerationSystemPrompt();
        const userPrompt = buildGenerationUserPrompt(variant, testCase);
        const outputText = await createChatCompletion(
          openaiClient,
          `generate ${variant}/${testCase.slug}/${runId}`,
          generatorModel,
          [
            { role: "system", content: systemPrompt },
            { role: "user", content: userPrompt }
          ],
          false
        );

        const meta = {
          variant,
          case_id: testCase.slug,
          run_id: runId,
          generator_model: generatorModel,
          generated_at: new Date().toISOString(),
          prompt_hash: sha256(`${systemPrompt}\n\n${userPrompt}`),
          judge_prompt_version: "v2"
        };

        writeText(outputPath, `${outputText.trim()}\n`);
        writeJson(metaPath, meta);
        await sleep(API_DELAY_MS);
      }
    }
  }
}

async function judgeExistingOutputs(options, openaiClient) {
  if (!options.dryRun && DEFAULT_JUDGE_MODELS.length < 2) {
    throw new Error("EVAL_JUDGE_MODELS must list at least two comma-separated judge models.");
  }

  const selectedVariants = options.variant ? [options.variant] : Object.keys(VARIANT_SOURCES);
  const selectedCases = selectCases(discoverCases(), options.case);
  const judgePrompt = readText(judgePromptPath);
  const judgePromptHash = sha256(judgePrompt);

  for (const variant of selectedVariants) {
    for (const testCase of selectedCases) {
      for (const runId of runIdsFor(options.runCount)) {
        const outputPath = outputPathFor(variant, testCase.slug, runId);
        if (!fs.existsSync(outputPath)) {
          continue;
        }

        const outputText = readText(outputPath);
        const prompt = buildJudgePrompt(testCase, outputText);

        for (const judgeModel of DEFAULT_JUDGE_MODELS) {
          for (const attempt of runIdsFor(options.judgeRepeats)) {
            const judgmentPath = judgmentPathFor(variant, testCase.slug, runId, judgeModel, attempt);

            if (!options.force && fs.existsSync(judgmentPath)) {
              console.log(`skip judge ${variant}/${testCase.slug}/${runId}/${judgeModel}/${attempt} (exists)`);
              continue;
            }

            console.log(`judge ${variant}/${testCase.slug}/${runId}/${judgeModel}/${attempt}`);

            if (options.dryRun) {
              continue;
            }

            const raw = await createChatCompletion(
              openaiClient,
              `judge ${variant}/${testCase.slug}/${runId}/${judgeModel}/${attempt}`,
              judgeModel,
              [
                { role: "system", content: "Apply the rubric literally. Return JSON only." },
                { role: "user", content: prompt }
              ],
              true
            );

            const parsed = extractJson(raw);
            const wrapped = {
              metadata: {
                variant,
                case_id: testCase.slug,
                run_id: runId,
                judge_model: judgeModel,
                judge_attempt: attempt,
                judged_at: new Date().toISOString(),
                judge_prompt_hash: judgePromptHash,
                judge_prompt_version: "v2",
                rubric_hash: sha256(JSON.stringify(testCase.rubric))
              },
              result: parsed
            };

            writeJson(judgmentPath, wrapped);
            await sleep(API_DELAY_MS);
          }
        }
      }
    }
  }
}

function loadStructuredGenerationMeta(variant, caseSlug, runId) {
  return readJson(outputMetaPathFor(variant, caseSlug, runId), null);
}

function loadStructuredJudgments(caseSlugs, runCount) {
  const rows = [];
  const allowedCases = new Set(caseSlugs);
  const allowedRunIds = new Set(runIdsFor(runCount));

  function walk(dirPath) {
    if (!fs.existsSync(dirPath)) {
      return;
    }

    for (const entry of fs.readdirSync(dirPath, { withFileTypes: true })) {
      const absolutePath = path.join(dirPath, entry.name);
      if (entry.isDirectory()) {
        walk(absolutePath);
        continue;
      }

      if (!entry.isFile() || !entry.name.endsWith(".json")) {
        continue;
      }

      const payload = readJson(absolutePath, null);
      if (!payload?.metadata || !payload?.result) {
        continue;
      }

      const variant = payload.metadata.variant;
      const caseSlug = payload.metadata.case_id;
      const runId = payload.metadata.run_id;

      if (!Object.prototype.hasOwnProperty.call(VARIANT_SOURCES, variant)) {
        continue;
      }

      if (!allowedCases.has(caseSlug) || !allowedRunIds.has(runId)) {
        continue;
      }

      rows.push({
        variant,
        caseSlug,
        runId,
        judgeModelSlug: slugify(payload.metadata.judge_model || "unknown"),
        judgeModel: payload.metadata.judge_model || "unknown",
        attempt: payload.metadata.judge_attempt || entry.name.replace(/\.json$/, ""),
        path: absolutePath,
        metadata: payload.metadata,
        result: payload.result
      });
    }
  }

  walk(judgmentsRoot);
  return rows;
}

function collectStructuredGenerationRows(caseSlugs, runCount) {
  const rows = [];

  for (const variant of Object.keys(VARIANT_SOURCES)) {
    for (const caseSlug of caseSlugs) {
      for (const runId of runIdsFor(runCount)) {
        const outputPath = outputPathFor(variant, caseSlug, runId);
        const meta = loadStructuredGenerationMeta(variant, caseSlug, runId);
        if (!fs.existsSync(outputPath)) {
          continue;
        }

        rows.push({
          variant,
          caseSlug,
          runId,
          outputPath,
          metadata: meta
        });
      }
    }
  }

  return rows;
}

function collectLegacyScoreRows(caseSlugs) {
  const rows = [];

  for (const variant of Object.keys(VARIANT_SOURCES)) {
    for (const caseSlug of caseSlugs) {
      for (const runId of runIdsFor(LEGACY_RUN_COUNT)) {
        const scorePath = path.join(legacyScoresRoot, variant, caseSlug, `run-${runId}.json`);
        if (!fs.existsSync(scorePath)) {
          continue;
        }

        const payload = readJson(scorePath, null);
        if (!payload) {
          continue;
        }

        rows.push({
          variant,
          caseSlug,
          runId,
          payload,
          scorePath
        });
      }
    }
  }

  return rows;
}

function buildRunSummaries(judgments) {
  const grouped = new Map();

  for (const judgment of judgments) {
    const key = `${judgment.variant}::${judgment.caseSlug}::${judgment.runId}::${judgment.judgeModel}`;
    if (!grouped.has(key)) {
      grouped.set(key, []);
    }
    grouped.get(key).push(judgment);
  }

  const judgeSummaries = [];
  for (const [key, rows] of grouped.entries()) {
    const [variant, caseSlug, runId, judgeModel] = key.split("::");
    const scores = rows
      .map((row) => row.result?.score)
      .filter((value) => typeof value === "number");

    judgeSummaries.push({
      variant,
      caseSlug,
      runId,
      judgeModel,
      attempts: rows.length,
      medianScore: median(scores),
      stdScore: stddev(scores),
      unreliable: rows.length >= 2 && !Number.isNaN(stddev(scores)) && stddev(scores) > 1.5
    });
  }

  const byRun = new Map();
  for (const summary of judgeSummaries) {
    const key = `${summary.variant}::${summary.caseSlug}::${summary.runId}`;
    if (!byRun.has(key)) {
      byRun.set(key, []);
    }
    byRun.get(key).push(summary);
  }

  const runSummaries = [];
  for (const [key, judgeRows] of byRun.entries()) {
    const [variant, caseSlug, runId] = key.split("::");
    const reliableJudges = judgeRows.filter((row) => !row.unreliable && !Number.isNaN(row.medianScore));
    const judgeScores = reliableJudges.map((row) => row.medianScore);
    const spread = judgeScores.length >= 2 ? Math.max(...judgeScores) - Math.min(...judgeScores) : NaN;

    runSummaries.push({
      variant,
      caseSlug,
      runId,
      judgeCount: judgeRows.length,
      reliableJudgeCount: reliableJudges.length,
      finalScore: median(judgeScores),
      judgeSpread: spread,
      disagreement: judgeScores.length >= 2 ? spread > 0.2 * Math.max(...judgeScores) : false,
      judgeRows
    });
  }

  return { judgeSummaries, runSummaries };
}

function generateReport(options) {
  const cases = discoverCases();
  const caseSlugs = cases.map((entry) => entry.slug);
  const structuredGenerations = collectStructuredGenerationRows(caseSlugs, options.runCount);
  const structuredJudgments = loadStructuredJudgments(caseSlugs, options.runCount);
  const legacyScores = collectLegacyScoreRows(caseSlugs);
  const { runSummaries } = buildRunSummaries(structuredJudgments);

  const expectedStructuredGenerations = Object.keys(VARIANT_SOURCES).length * caseSlugs.length * options.runCount;
  const expectedStructuredJudgments =
    expectedStructuredGenerations * Math.max(DEFAULT_JUDGE_MODELS.length, 2) * options.judgeRepeats;
  const expectedLegacyScores = Object.keys(VARIANT_SOURCES).length * caseSlugs.length * LEGACY_RUN_COUNT;

  const lines = [];
  lines.push("# Presto Design Eval Report");
  lines.push("");
  lines.push(`Generated: ${new Date().toISOString()}`);
  lines.push(`Target generation runs per cell: ${options.runCount}`);
  lines.push(`Target judge repeats per model: ${options.judgeRepeats}`);
  lines.push(`Configured judge models: ${DEFAULT_JUDGE_MODELS.length > 0 ? DEFAULT_JUDGE_MODELS.join(", ") : "none configured"}`);
  lines.push("");
  lines.push("## Key Findings");
  lines.push("");

  const missingLegacy = expectedLegacyScores - legacyScores.length;
  lines.push(
    `- Legacy score coverage is ${legacyScores.length}/${expectedLegacyScores}; ${pct(
      missingLegacy,
      expectedLegacyScores
    )} of the old matrix is missing.`
  );

  const v2LegacyRuns = legacyScores.filter((entry) => entry.variant === "v2").length;
  const expectedV2LegacyRuns = caseSlugs.length * LEGACY_RUN_COUNT;
  lines.push(
    `- Legacy v2 coverage is ${v2LegacyRuns}/${expectedV2LegacyRuns}; this variant was barely exercised in the old run set.`
  );

  lines.push(
    `- Structured coverage is ${structuredGenerations.length}/${expectedStructuredGenerations} generations and ${structuredJudgments.length}/${expectedStructuredJudgments} judgments.`
  );

  const legacyGeneratorWarning =
    fs.existsSync(path.join(evalRoot, "gen_outputs.py")) || fs.existsSync(path.join(evalRoot, "gen_v1.py"));
  lines.push(
    `- Generator provenance is ${structuredGenerations.some((entry) => entry.metadata?.generator_model) ? "recorded for structured runs" : "missing for current usable runs"}; legacy fixture-writer scripts ${legacyGeneratorWarning ? "are present" : "were not found"}.`
  );
  lines.push(
    `- Judge provenance is ${structuredJudgments.length > 0 ? "recorded per judgment file" : "missing on usable runs"}; legacy scores do not record judge model or prompt hash.`
  );

  const lowNCells = [];
  for (const variant of Object.keys(VARIANT_SOURCES)) {
    for (const caseSlug of caseSlugs) {
      const n = structuredGenerations.filter((entry) => entry.variant === variant && entry.caseSlug === caseSlug).length;
      if (n < options.runCount) {
        lowNCells.push({ variant, caseSlug, n });
      }
    }
  }

  if (lowNCells.length === Object.keys(VARIANT_SOURCES).length * caseSlugs.length && legacyScores.length > 0) {
    lines.push("- Every structured cell is still below target n, and the only populated legacy cells are effectively per-cell n=1.");
  } else if (lowNCells.length > 0) {
    lines.push(`- ${lowNCells.length} structured cells are below target n=${options.runCount}.`);
  } else {
    lines.push(`- All structured cells meet target n=${options.runCount}.`);
  }

  lines.push("");
  lines.push("## Coverage");
  lines.push("");
  lines.push("| Dataset | Completed | Expected | Missing |");
  lines.push("| --- | --- | --- | --- |");
  lines.push(`| Structured generations | ${structuredGenerations.length} | ${expectedStructuredGenerations} | ${expectedStructuredGenerations - structuredGenerations.length} |`);
  lines.push(`| Structured judgments | ${structuredJudgments.length} | ${expectedStructuredJudgments} | ${expectedStructuredJudgments - structuredJudgments.length} |`);
  lines.push(`| Legacy scores | ${legacyScores.length} | ${expectedLegacyScores} | ${missingLegacy} |`);
  lines.push("");
  lines.push("## Per-Cell Runs");
  lines.push("");
  lines.push("| Case | v0 | v1 | v2 |");
  lines.push("| --- | --- | --- | --- |");

  for (const caseSlug of caseSlugs) {
    const cols = Object.keys(VARIANT_SOURCES).map((variant) => {
      const structuredN = structuredGenerations.filter((entry) => entry.variant === variant && entry.caseSlug === caseSlug).length;
      const legacyN = legacyScores.filter((entry) => entry.variant === variant && entry.caseSlug === caseSlug).length;
      return `${structuredN}/${options.runCount} structured; ${legacyN}/${LEGACY_RUN_COUNT} legacy`;
    });
    lines.push(`| ${caseSlug} | ${cols.join(" | ")} |`);
  }

  lines.push("");
  lines.push("## Judge Reliability");
  lines.push("");

  if (runSummaries.length === 0) {
    lines.push("No structured judgments found. Reliability analysis is unavailable until the new judge pipeline is run.");
  } else {
    const unreliableRuns = runSummaries.filter((entry) => entry.judgeRows.some((row) => row.unreliable));
    const disagreementRuns = runSummaries.filter((entry) => entry.disagreement);
    lines.push(`Runs with unreliable single-judge repeats: ${unreliableRuns.length}`);
    lines.push(`Runs with >20% inter-judge disagreement: ${disagreementRuns.length}`);
    lines.push("");
    lines.push("| Variant | Mean final score | Std final score | Reliable runs |");
    lines.push("| --- | --- | --- | --- |");

    for (const variant of Object.keys(VARIANT_SOURCES)) {
      const variantRuns = runSummaries.filter((entry) => entry.variant === variant && !Number.isNaN(entry.finalScore));
      const values = variantRuns.map((entry) => entry.finalScore);
      lines.push(`| ${variant} | ${fmt(mean(values))} | ${fmt(stddev(values))} | ${variantRuns.length} |`);
    }

    lines.push("");
    lines.push("### Delta vs Noise");
    lines.push("");

    const variants = Object.keys(VARIANT_SOURCES);
    for (let i = 0; i < variants.length; i += 1) {
      for (let j = i + 1; j < variants.length; j += 1) {
        const left = variants[i];
        const right = variants[j];
        const leftValues = runSummaries
          .filter((entry) => entry.variant === left && !Number.isNaN(entry.finalScore))
          .map((entry) => entry.finalScore);
        const rightValues = runSummaries
          .filter((entry) => entry.variant === right && !Number.isNaN(entry.finalScore))
          .map((entry) => entry.finalScore);

        if (leftValues.length < 2 || rightValues.length < 2) {
          lines.push(`- ${left} vs ${right}: insufficient structured data for a noise-floor comparison.`);
          continue;
        }

        const diff = Math.abs(mean(leftValues) - mean(rightValues));
        const noiseFloor = Math.max(stddev(leftValues), stddev(rightValues));
        const verdict = diff <= noiseFloor ? "below noise floor" : "above noise floor";
        lines.push(`- ${left} vs ${right}: diff=${fmt(diff)}, noise=${fmt(noiseFloor)} -> ${verdict}.`);
      }
    }
  }

  lines.push("");
  lines.push("## Legacy Compatibility");
  lines.push("");
  lines.push("- Legacy scores use the deprecated four-dimension schema (`design_quality`, `clarity`, `actionability`, `adherence`).");
  lines.push("- New judge-prompt requires per-case rubric items, fatal flaws, evidence spans, repeated judging, and judge metadata.");
  lines.push("- Do not mix legacy totals with structured v2 judge results in the same chart.");

  const reportPath = path.join(reportsRoot, "summary.md");
  writeText(reportPath, `${lines.join("\n")}\n`);
  console.log(`report written -> ${reportPath}`);
}

async function main() {
  const options = parseArgs(process.argv.slice(2));

  if ((options.generate || options.judge) && !options.dryRun) {
    ensureEnv("OPENAI_API_KEY");
  }

  ensureDir(generationsRoot);
  ensureDir(judgmentsRoot);
  ensureDir(reportsRoot);

  const needsOpenAiClient = (options.generate || options.judge) && !options.dryRun;
  const openaiClient = needsOpenAiClient ? new (loadOpenAiSdk())({ apiKey: process.env.OPENAI_API_KEY }) : null;

  if (options.generate) {
    await generateOutputs(options, openaiClient);
  }

  if (options.judge) {
    await judgeExistingOutputs(options, openaiClient);
  }

  if (options.report) {
    generateReport(options);
  }

  if (options.validate) {
    runValidation(options);
  }

  if (options.printGeneratePrompt) {
    printGeneratePrompt(options);
  }

  if (options.printJudgePrompt) {
    printJudgePrompt(options);
  }

  if (options.ingestGenerationFile) {
    ingestGenerationFromFile(options);
  }

  if (options.ingestJudgmentFile) {
    ingestJudgmentFromFile(options);
  }
}

main().catch((error) => {
  const message = error instanceof Error ? error.stack || error.message : String(error);
  console.error(message);
  process.exit(1);
});
