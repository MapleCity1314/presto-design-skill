# Eval Structure

This directory now uses a rubric-first eval layout aligned with [`judge-prompt.md`](./judge-prompt.md).

## Layout

- `cases/<case-id>/task.md`: generator task input
- `cases/<case-id>/rubric.json`: per-case rubric items used by the judge
- `runner.ts`: generation, judging, and reporting
- `cases.manifest.json`: canonical case and variant list for the current matrix
- `eval.config.example.json`: minimal config template for a real run
- `results/generations/`: structured generator outputs plus metadata sidecars
- `results/judgments/`: per-judge, per-attempt JSON outputs
- `results/reports/summary.md`: coverage and reliability report

## Contract

- Generation runs and judge repeats default to `3` per cell.
- Judge runs require at least two models via `EVAL_JUDGE_MODELS=model-a,model-b`.
- Generation runs require explicit `EVAL_GENERATOR_MODEL`; there is no implicit default model anymore.
- Every structured output must carry generator metadata.
- Every structured judgment must carry judge model, prompt hash, rubric hash, and attempt metadata.

## Commands

```powershell
node .\node_modules\ts-node\dist\bin.js runner.ts --generate
node .\node_modules\ts-node\dist\bin.js runner.ts --judge
node .\node_modules\ts-node\dist\bin.js runner.ts --report
node .\node_modules\ts-node\dist\bin.js runner.ts --validate
node .\node_modules\ts-node\dist\bin.js runner.ts --all
node .\node_modules\ts-node\dist\bin.js runner.ts --print-generate-prompt --variant v0 --case create-saas-landing
node .\node_modules\ts-node\dist\bin.js runner.ts --print-judge-prompt --variant v0 --case create-saas-landing --run-id 01
```

Optional flags:

- `--variant v0|v1|v2`
- `--case <case-id>`
- `--run-count 3`
- `--judge-repeats 3`
- `--run-id 01`
- `--judge-model gpt-5.4`
- `--attempt 01`
- `--force`
- `--dry-run`

Subagent/manual ingestion helpers:

- `--ingest-generation-file <path> --variant <v> --case <case> --run-id <id>`
- `--ingest-judgment-file <path> --variant <v> --case <case> --run-id <id> --judge-model <model> --attempt <id>`

## Environment

Required for generation and judging:

- `OPENAI_API_KEY`
- `EVAL_GENERATOR_MODEL`
- `EVAL_JUDGE_MODELS`

Recommended:

- `EVAL_RUN_COUNT=3`
- `EVAL_JUDGE_REPEATS=3`

Before a real run, copy values from `eval.config.example.json` into env vars so generator and judge provenance are explicit.

## External Execution

The structured artifact contract is executor-agnostic. In Codex, generator and judge runs may be produced by subagents instead of the OpenAI API path in `runner.ts`, as long as they write the same files:

- `results/generations/<variant>/<case-id>/run-XX.md`
- `results/generations/<variant>/<case-id>/run-XX.meta.json`
- `results/judgments/<variant>/<case-id>/run-XX/<judge-model>/attempt-YY.json`

That keeps the repo infra focused on case definitions, metadata contracts, validation, and reporting, while the execution path can be API-driven or agent-driven.

## Legacy Data

The old `results/v*/...` and `results/scores/...` trees remain on disk for auditability, but they are treated as legacy-only inputs:

- they were produced under the deprecated four-dimension judge;
- they do not reliably record generator provenance;
- they do not record judge prompt hashes;
- they should not be mixed with structured rubric-first results.

The report surfaces them only to quantify missing coverage and explain why the old matrix is not decision-grade.
