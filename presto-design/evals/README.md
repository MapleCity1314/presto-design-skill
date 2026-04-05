# Evals

This directory holds the evaluation suite for `presto-design`.

## Layout

- [`evals.json`](./evals.json): the consolidated eval definition file used by the current harness flow
- [`cases/`](./cases): one JSON file per case for easier editing and review
- [`judge-prompt.md`](./judge-prompt.md): qualitative scoring rubric
- [`results/`](./results): recorded benchmark outputs by iteration

## Conventions

- Keep case names short, descriptive, and stable.
- Prefer one primary design intent per case.
- Put objective checks in assertions and reserve subjective checks for the judge prompt.
- Update both `cases/` and `evals.json` together until the harness is switched to per-case discovery.

## Current cases

- [`cases/01-redesign-saas-landing.json`](./cases/01-redesign-saas-landing.json)
- [`cases/02-create-dashboard-tool.json`](./cases/02-create-dashboard-tool.json)
- [`cases/03-refine-typography-color.json`](./cases/03-refine-typography-color.json)
