# Architecture Notes — Material Gap vs Ablation Prompt

Written: 2026-04-09. Stopping here pending Presto decision on how to proceed with Phase 1+.

---

## The Gap

The ablation prompt (Phase 2) assumes:

> "For each variant (V0, V1, V2) × each case × 3 runs = 72 total generations, invoke the skill against the case (use whatever invocation path the repo already supports)"

**There is no invocation path in this repo.** The skill is entirely text-based prompt guidance. It is not a CLI, not a script, not an API wrapper. The files are loaded into a Claude conversation context as system-level prompt content — the "runner" is the human or a configured IDE extension.

What the repo contains:
- `SKILL.md` — router prompt (loaded as a Claude skill)
- `clusters/*.md` — sub-prompts conditionally loaded based on routing
- `presets/*.md` — aesthetic overlay prompts
- `contract.md` — constraint prompt
- `agents/openai.yaml` — interface display configuration (name, short description, default prompt display text)

There is no:
- CLI entrypoint
- `package.json` with a start script
- API client
- Existing test harness
- Judge configuration
- Any executable code at all

---

## What Building the Runner Actually Requires

To run 72 generations, the runner.ts would need to:

1. **Load variant context**: for each variant (V0/V1/V2), assemble the complete skill prompt by concatenating `SKILL.md` + `contract.md` (variant-specific) + the relevant cluster files into a single system prompt.

2. **Call an LLM API**: send each test case as a user message with the assembled skill as system context. The most natural choice is the Anthropic API (Claude) or OpenAI API — both require API keys and incur token costs.

3. **Handle multi-file output**: skill outputs are long multi-file code blocks. Storage and parsing need to handle this.

4. **Anonymization**: strip variant labels before judging. This requires careful output templating.

5. **Invoke a judge**: the judge prompt goes to a separate LLM call (or a local model if available). "Gemma or whatever judge is available locally" — no local model is configured in this repo, and there is no Ollama config, Hugging Face setup, or similar.

**Estimated API cost for 72 generations**: with a test case + skill context averaging ~6k tokens input and ~3k tokens output, at Claude Sonnet pricing, 72 calls ≈ 72 × 9k tokens ≈ 648k tokens. At current Sonnet pricing (~$3/M input, $15/M output): ~$2 input + ~$3 output = **~$5 for generations alone**. Judge scoring adds another ~$2-4. Total: **~$7-10 for one full run**.

---

## Decision Points That Require Presto Input

### 1. Runner API target
Which LLM do you want to generate against?
- **Claude (Anthropic API)**: most faithful to how the skill is actually used. Requires `ANTHROPIC_API_KEY`.
- **OpenAI**: `agents/openai.yaml` suggests this was the intended interface. Requires `OPENAI_API_KEY`.
- **Both**: ablation validity is improved if you run against the same model as your production use case.

### 2. Judge model
The prompt says "Gemma or whatever judge is available locally." No local judge is configured. Options:
- **Use a different Claude/GPT model as judge**: cheap, available, but same-company bias for Claude outputs.
- **Use a local model via Ollama**: requires installing Ollama + Gemma. Zero cost but significant setup.
- **Manual scoring by Presto**: eliminates automation but removes model-bias from judging entirely. With only 72 outputs and n=3 per cell, manual scoring is 3-4 hours of work, not unreasonable.

### 3. Scope of runner.ts
Options:
- **Full automation**: build the runner in TypeScript with API calls, anonymization, and judge invocation. Takes ~2-4 hours to build, but runs unattended. Requires Node.js + API keys.
- **Semi-automated**: build the test case files and the skill assembly logic, but run generations manually through Claude.ai or Cursor. Cheaper to build, higher human time to run.
- **Case files only**: produce the 8 case files and judge prompt so Presto can run them in any environment. Lowest engineering cost.

### 4. Variant file structure for V1/V2
The ablation branches will modify `contract.md` and possibly cluster files. The runner needs to know which files to concatenate for each variant context. The simplest approach: each branch has a `skill-context.md` that pre-concatenates the full system prompt for that variant, ready to paste or inject via API.

---

## Recommendation Before Proceeding

Before building Phase 1 (branches) and Phase 2 (runner), Presto should decide:

1. **What API** will power the 72 generations? (Anthropic Claude / OpenAI / manual)
2. **What model** will be the judge? (local Gemma / another API model / human)
3. **What level of runner automation** is wanted?

If the answer to #3 is "minimal — just give me the case files and I'll run them through the interface I already use," then Phase 2 reduces to: write 8 case files + judge prompt + a Markdown assembly guide. That is ~2 hours of work. The runner.ts becomes optional scaffolding.

If the answer is "full automation, TypeScript runner, API calls," that is ~6-8 hours of additional engineering work before any data is generated.

---

## What Is Safe to Proceed With Now (Without Presto Input)

Phase 1 (branches) can proceed immediately — creating `variant/v1-verb-level` and `variant/v2-stripped` is pure text editing with no infrastructure dependency.

Phase 2 case files and judge prompt can also be written without resolving the runner question — they are API-agnostic.

**Only the runner.ts and the actual generation + scoring require the decisions above.**
