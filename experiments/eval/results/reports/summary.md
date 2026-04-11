# Presto Design Eval Report

Generated: 2026-04-10T02:38:03.279Z
Target generation runs per cell: 3
Target judge repeats per model: 3
Configured judge models: none configured

## Key Findings

- Legacy score coverage is 17/240; 92.9% of the old matrix is missing.
- Legacy v2 coverage is 1/80; this variant was barely exercised in the old run set.
- Structured coverage is 3/72 generations and 4/432 judgments.
- Generator provenance is recorded for structured runs; legacy fixture-writer scripts are present.
- Judge provenance is recorded per judgment file; legacy scores do not record judge model or prompt hash.
- Every structured cell is still below target n, and the only populated legacy cells are effectively per-cell n=1.

## Coverage

| Dataset | Completed | Expected | Missing |
| --- | --- | --- | --- |
| Structured generations | 3 | 72 | 69 |
| Structured judgments | 4 | 432 | 428 |
| Legacy scores | 17 | 240 | 223 |

## Per-Cell Runs

| Case | v0 | v1 | v2 |
| --- | --- | --- | --- |
| create-consumer-app | 0/3 structured; 1/10 legacy | 0/3 structured; 1/10 legacy | 0/3 structured; 0/10 legacy |
| create-devtool-landing | 0/3 structured; 1/10 legacy | 0/3 structured; 1/10 legacy | 0/3 structured; 0/10 legacy |
| create-saas-landing | 1/3 structured; 1/10 legacy | 1/3 structured; 1/10 legacy | 1/3 structured; 1/10 legacy |
| redesign-admin-dashboard | 0/3 structured; 1/10 legacy | 0/3 structured; 1/10 legacy | 0/3 structured; 0/10 legacy |
| redesign-marketing-page | 0/3 structured; 1/10 legacy | 0/3 structured; 1/10 legacy | 0/3 structured; 0/10 legacy |
| refine-dashboard-widget | 0/3 structured; 1/10 legacy | 0/3 structured; 1/10 legacy | 0/3 structured; 0/10 legacy |
| refine-form-flow | 0/3 structured; 1/10 legacy | 0/3 structured; 1/10 legacy | 0/3 structured; 0/10 legacy |
| refine-settings-panel | 0/3 structured; 1/10 legacy | 0/3 structured; 1/10 legacy | 0/3 structured; 0/10 legacy |

## Judge Reliability

Runs with unreliable single-judge repeats: 0
Runs with >20% inter-judge disagreement: 0

| Variant | Mean final score | Std final score | Reliable runs |
| --- | --- | --- | --- |
| v0 | 10.00 | n/a | 1 |
| v1 | 10.00 | n/a | 1 |
| v2 | 10.00 | n/a | 1 |

### Delta vs Noise

- v0 vs v1: insufficient structured data for a noise-floor comparison.
- v0 vs v2: insufficient structured data for a noise-floor comparison.
- v1 vs v2: insufficient structured data for a noise-floor comparison.

## Legacy Compatibility

- Legacy scores use the deprecated four-dimension schema (`design_quality`, `clarity`, `actionability`, `adherence`).
- New judge-prompt requires per-case rubric items, fatal flaws, evidence spans, repeated judging, and judge metadata.
- Do not mix legacy totals with structured v2 judge results in the same chart.
