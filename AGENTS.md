# Repository Guidelines

## Project Structure & Module Organization
This repository publishes a single root skill. Keep the top-level layout stable:

- `SKILL.md`: primary entry point and routing logic for the skill.
- `clusters/`: intent-specific workflows such as `create.md`, `refine.md`, and `motion.md`.
- `presets/`: optional aesthetic overlays such as `minimalist.md` and `editorial.md`.
- `context/`: supporting prompts used when design context is missing.
- `contract.md`: non-negotiable output rules for every cluster.
- `gsap-integration.md`: motion-specific guidance when GSAP is relevant.
- `evals/`: evaluation cases, judge prompt, and recorded outputs under `evals/results/`.
- `agents/openai.yaml`: agent configuration.

## Build, Test, and Development Commands
There is no application build step in this repository. The main workflows are inspection and evaluation.

- `rg --files`: list repository files quickly.
- `Get-Content SKILL.md`: inspect the root skill before editing related docs.
- `git diff`: review documentation changes before committing.
- `git log --pretty=format:"%s" -6`: check recent commit style.

If you run external skill or eval tooling locally, document the exact command in the relevant README before relying on it.

## Coding Style & Naming Conventions
Use concise Markdown with clear headings and short sections. Match the existing tone: instructional, direct, and specific. Prefer sentence-case prose inside sections and kebab-case file names such as `refine-layout.md`. Keep related guidance in the existing file rather than creating duplicate docs.

When updating prompts, preserve routing terminology (`cluster`, `preset`, `contract`) and keep examples concrete. Avoid decorative formatting and long narrative explanations.

## Testing Guidelines
Validation is primarily manual and fixture-based. When changing routing, contract rules, or presets:

- verify links and referenced paths still exist;
- check affected examples in `evals/cases/`;
- review corresponding outputs in `evals/results/` for regressions.

If you add a new eval case, name it with a numeric prefix and short slug, for example `04-new-layout-audit.json`.

## Commit & Pull Request Guidelines
Recent history uses short imperative subjects, often Conventional Commit style, for example `feat: prepare presto-design for github release` and `chore: add mit license`. Follow that pattern.

Pull requests should include:

- a brief summary of the skill or documentation change;
- impacted paths, such as `SKILL.md` or `clusters/motion.md`;
- before/after notes for any eval updates;
- screenshots only when the change affects rendered examples in `evals/results/`.
