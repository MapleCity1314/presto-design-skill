# Presto Design — Judge Prompt System (v2)

A rubric-based, per-case, blind, anti-bias judge system for evaluating
generator outputs. Replaces the previous vibes-based four-dimension prompt.

---

## Design principles (short version)

1. **No abstract dimensions.** No `design_quality`, no `clarity`. Those are
   correlated, vague, and reward fluency. Replaced by per-case rubric items
   that are individually checkable against quoted evidence.
2. **Per-case rubrics.** Each task ships with its own rubric. The judge does
   not bring its own "good design" intuition — that intuition is the bias.
3. **Format-blind.** Explicit instructions to ignore decision logs, phase
   markers, headers, and any structural fingerprint that leaks variant
   identity. Generator outputs should also be stripped of variant-identifying
   markers before judging (handled in the runner, not the judge).
4. **Restraint is rewarded explicitly.** For preservation/restraint cases,
   rubric items invert — the judge rewards *absence* of changes, hard caps
   on proposed changes, and explicit acknowledgment that existing design is
   competent.
5. **Evidence-bound scoring.** Every rubric item requires the judge to quote
   the exact span that satisfies it, or mark "not present." This forces
   grounding and makes judge errors auditable post-hoc.
6. **Fatal flaw override.** Hallucinations, stack violations, format
   violations zero out the entire score regardless of rubric satisfaction.
   These are not negotiable.
7. **Single integer score.** Sum of satisfied rubric items. No weights, no
   composite formulas. If an item matters more, make it a fatal flaw.

---

## The judge prompt (shell)

This is the literal prompt sent to the judge model. The runner injects
`{case_id}`, `{task}`, `{output}`, and `{rubric}` per evaluation.

````text
You are evaluating a single output produced for a frontend design task.

Your job is to apply the provided rubric literally. You are not asked for
your opinion on whether the output is "good design." You are asked whether
each rubric item is satisfied by the output, with quoted evidence.

==========================================
ANTI-BIAS RULES — READ BEFORE EVALUATING
==========================================

1. Format bias: The output may contain section headers, decision logs,
   rationale blocks, phase markers, structured lists, or any other visual
   organization. These do NOT count toward any rubric item unless that item
   is specifically about formatting. A short, plain output that satisfies
   the rubric scores identically to a long, structured output that satisfies
   the same rubric.

2. Length bias: Longer is not better. Do not reward verbosity. Do not reward
   "thoroughness" unless the rubric asks for thoroughness explicitly.

3. Confidence bias: Confident-sounding prose is not evidence. Hedged language
   is not evidence against. Only quoted spans count as evidence.

4. Theory bias: Outputs that discuss design principles, name designers, or
   reference design history score zero on those grounds alone. The rubric
   asks about specific properties of the proposed design, not about how
   well the output talks about design.

5. Restraint: For some cases, the correct answer is to propose minimal or
   zero changes. The rubric for those cases will reward this explicitly.
   Do not penalize a short output for being short if it satisfies the
   rubric.

==========================================
EVALUATION PROCEDURE
==========================================

Step 1 — Fatal flaw check.
Before scoring rubric items, check the four fatal flaws below. If any are
present, the entire score is 0 regardless of rubric satisfaction. List which
flaws were found.

Fatal flaws:
F1. Hallucinated technical fact (nonexistent library, fake CSS property,
    wrong framework API surface, invented HTML element).
F2. Stack violation (proposes a technology the task explicitly excluded,
    or replaces the requested framework).
F3. Restructuring violation (proposes structural rewrites when the task
    explicitly required preservation).
F4. Format violation (task asked for one output format, output is in a
    different format — e.g., asked for code, got prose only).

Step 2 — Rubric evaluation.
For each rubric item, do the following in order:
  a. Read the item literally.
  b. Search the output for a span that satisfies it.
  c. If found, quote the span verbatim (max 200 chars).
  d. If not found, write "not present".
  e. Mark satisfied: true only if a clearly satisfying span exists.
  f. Partial satisfaction = false. Implied satisfaction = false. Vague
     gestures in the right direction = false.

Step 3 — Compute score.
score = number of items with satisfied: true
If fatal_flaws is non-empty, score = 0.

==========================================
INPUT
==========================================

CASE ID: {case_id}

TASK GIVEN TO GENERATOR:
{task}

OUTPUT TO EVALUATE:
{output}

RUBRIC:
{rubric}

==========================================
RETURN FORMAT
==========================================

Return valid JSON only. No markdown, no commentary, no preamble.

{
  "case_id": "{case_id}",
  "fatal_flaws": ["F1" | "F2" | "F3" | "F4", ...],
  "rubric_results": [
    {
      "item": "exact rubric item text",
      "evidence": "quoted span from output, or 'not present'",
      "satisfied": true
    }
  ],
  "score": 0,
  "max_score": 0,
  "notes": "one sentence describing the output's overall character, neutral language only"
}
````

---

## Case rubric format

Each case ships a rubric file (`cases/{case_id}/rubric.json` or similar)
containing an ordered list of items. Items are plain strings written as
checkable assertions about the output.

```json
{
  "case_id": "create-devtool-landing",
  "case_type": "create",
  "items": [
    "Output names a specific font family for display type (e.g., 'IBM Plex Sans', 'Geist'); 'a clean sans-serif' does not count.",
    "Output proposes a specific color system with named tokens or hex values; 'a calm palette' does not count.",
    "..."
  ]
}
```

`case_type` is metadata only. The judge does not see it. It exists so the
runner can group results.

---

## Example rubrics

### Rubric 1 — `create-devtool-landing` (standard create case)

Task: *Build a landing page for a developer tool aimed at small engineering
teams. Editorial, confident, less startup-generic. Next.js + Tailwind v4.*

```text
1. Output names a specific display font family (e.g., "Geist", "IBM Plex Sans", 
   "GT America"). "A clean sans-serif" does not count.
2. Output names a specific body font family or explicitly states it shares the
   display family with a different weight/size.
3. Output proposes a concrete color system: at least 3 named tokens or hex
   values covering background, content, and accent. "A calm palette" or
   "muted neutrals" does not count.
4. Output proposes a concrete spacing scale (e.g., "4px base, scale 4/8/12/16/
   24/32/48/64"). Unspecified spacing does not count.
5. Output addresses what the landing page is actually selling — proposes a
   value proposition or positioning angle, not just visual treatment.
6. Output respects the Next.js + Tailwind v4 stack. Does not propose CSS-in-JS,
   styled-components, vanilla CSS modules, or competing frameworks.
7. Output proposes structure for at least 3 distinct sections (hero, one
   secondary, one tertiary or footer). A single hero is insufficient.
8. Output addresses mobile/responsive behavior with at least one specific
   breakpoint or layout shift.
9. Output addresses at least one concrete accessibility requirement (focus
   states, contrast ratio, semantic HTML, keyboard navigation).
10. Output's proposed copy is product-shaped, not boilerplate. "Build faster",
    "The future of X", "Ship with confidence" type phrases count as boilerplate
    and fail this item.
11. Output does NOT propose purple-to-blue gradients, OR if it does, it
    explicitly justifies the choice with a reason grounded in the audience.
12. Output specifies at least one icon family by name (Phosphor, Lucide,
    Heroicons, Tabler, etc.) rather than leaving icons unspecified.
```

### Rubric 2 — `refine-dashboard-widget` (refine case, preservation expected)

Task: *Refine this dashboard widget. Keep the structure recognizable. Fix
typography, spacing, and color treatment.*

```text
1. Output preserves the widget's existing structure — does not propose 
   moving, removing, or restructuring sub-components.
2. Output identifies at least 2 specific current problems before proposing
   any fixes. "It looks generic" does not count; problems must be concrete
   (e.g., "title and value have insufficient size contrast").
3. Output proposes typography changes with specific values (font size,
   weight, line-height, or scale step). "Larger heading" does not count.
4. Output proposes spacing changes with specific values or scale references.
5. Output proposes color/contrast changes with specific tokens, hex values,
   or contrast ratios.
6. Output's proposed changes are reversible — no destructive refactors,
   no removed functionality.
7. Output does NOT introduce new component types not present in the original.
8. Output stays within the existing framework and styling system.
9. At least one proposed change references a property of the existing
   widget (e.g., "the current 14px label is fighting the 16px value").
10. Output does NOT propose more than 8 distinct changes. More than 8 fails
    this item — refine should be focused, not a redesign.
```

### Rubric 3 — `preserve-already-good` (restraint case, inverted scoring)

Task: *Here is an existing settings panel from a mature product. Evaluate
whether it needs redesign. If yes, propose changes. If no, say so clearly.*

The case ships with a settings panel that is already competently designed
(consistent spacing scale, readable type, working focus states, coherent
color tokens). The correct answer is "no redesign needed; possibly minor
refinement."

```text
1. Output explicitly states that significant restructuring is NOT needed.
2. Output identifies at least 2 specific things the existing design does well,
   with concrete reference (not "it looks clean").
3. If the output proposes any changes, every change is at refinement scope —
   typography, spacing, color, or copy only. No layout primitives changed.
4. Output does NOT propose changing the framework, styling system, or
   component library.
5. Output does NOT propose changing the brand colors or primary font family.
6. Output does NOT introduce new component types.
7. Output proposes 5 or fewer total changes. More than 5 fails this item.
8. Output's overall stance acknowledges the starting point is competent —
   does not frame the panel as a problem to be solved.
9. If the output finds nothing to improve, it says so directly rather than
   fabricating minor issues to appear useful.
10. Output does NOT use the words "elevate", "modernize", "premium", or
    "polish" as standalone justifications for any proposed change.
```

Note item 9: this is the critical item for testing escalation policy. A
generator that cannot recommend "no change" is a generator that will
over-engineer in production.

### Rubric 4 — `adversarial-power-user-terminal` (adversarial UNLESS test)

Task: *Design a black-and-white, high-contrast dashboard for SOC analysts
who monitor it for 10-hour shifts. Information density is critical.*

This case adversarially tests whether the generator correctly enters the
`#000/#fff UNLESS` branch. The correct answer uses true black and true
white (or near-equivalents with explicit justification), monospace or
terminal-grade type, and high information density.

```text
1. Output uses true #000 / #fff or near-equivalents as primary surface
   colors. Pastels, off-white, or "softer" alternatives fail this item.
2. Output explicitly justifies the high-contrast choice with reference to
   the 10-hour shift duration or SOC analyst use case.
3. Output addresses sustained-reading legibility (specific font choice,
   line-height, max line length, or anti-aliasing concerns).
4. Output proposes high information density — multiple data regions
   visible simultaneously, not "one focused metric per screen."
5. Output does NOT propose adding accent colors to "soften" the design
   beyond what is functionally needed for status signaling.
6. Output proposes a monospace or terminal-grade font for data display
   (e.g., "JetBrains Mono", "IBM Plex Mono", "Berkeley Mono"), or
   explicitly justifies a proportional choice.
7. Output addresses keyboard shortcuts, command palette, or power-user
   interaction patterns.
8. Output preserves data legibility over visual decoration — does not
   propose dashboards that prioritize "feeling premium" over data scan speed.
9. Output stays within the requested stack if one was specified.
10. Output does NOT replace #000/#fff with #0a0a0a/#fafafa "for eye comfort"
    without referencing actual research or contrast measurements. Vague
    eye-comfort justifications fail this item.
```

Note: items 1, 5, 6, 8, 10 are designed to penalize the generator's default
inclination to "soften" stark designs. A generator that has correctly
internalized FORBIDDEN UNLESS will pass these. A generator running on
adjective-level instinct will fail several.

---

## Writing new rubrics

When creating a rubric for a new case, follow these rules:

1. **Every item must be quotable.** If you cannot imagine the evidence
   span the judge would quote, the item is too vague. Rewrite or drop.

2. **Mix item types per rubric:**
   - 4–6 specificity items (forces concrete choices over hedged prose)
   - 2–3 task-adherence items (stack, scope, format)
   - 1–2 anti-pattern items (FORBIDDEN UNLESS check)
   - 1–2 domain-appropriateness items (audience-specific)

3. **For restraint cases, invert.** Reward absence of changes, set hard
   caps, reward explicit acknowledgment of existing quality. The rubric
   should make a "do nothing" answer scoreable as a high score, not zero.

4. **Avoid format-satisfiable items.** If a v1-style decision log
   (`DECISION: use Inter BECAUSE...`) automatically satisfies an item, the
   item is measuring format. Rewrite the item to require a *property*
   (font is sans-serif with wide weight range and Latin Extended support)
   rather than the *act of declaring* a font.

5. **Forbid evaluator-fluency words.** Items must not contain "thoughtful",
   "considered", "careful", "intentional", "purposeful". These reward
   prose style.

6. **Equal weight.** All items count for 1 point. If something matters more,
   make it a fatal flaw, not a higher-weight item. No weighted sums.

7. **8–12 items per rubric.** Fewer = high variance. More = judge attention
   drifts and accuracy drops.

8. **Anti-format-bias items are good.** Include at least one item that a
   wordy decision-log-heavy output would *fail* — for example, a length cap
   or a directness requirement. This actively counterbalances v1's natural
   advantage in fluency-rewarding judges.

---

## Runner integration notes

The runner is responsible for two things the judge cannot do:

1. **Strip variant fingerprints from output before judging.** Remove
   `DECISION:`, `DEVIATION:`, phase markers, cluster names, and preset
   names from the generator output before it reaches the judge. This is
   the only way to enforce blindness, since the judge cannot self-blind
   to formatting it can see.

   Alternative: wrap *all* variant outputs (v0, v1, v2) in an identical
   shell template so structure cannot leak variant identity. This is
   simpler than stripping and probably more reliable.

2. **Run each evaluation 3 times and take median.** LLM judges have
   non-trivial variance even at temperature 0. Single judge calls are
   unreliable. If 3 calls produce score std > 1.5, flag the sample as
   `unreliable: true` and exclude from aggregate statistics.

3. **Two-judge minimum.** Run each evaluation through two different
   judge models (e.g., Claude Opus 4.6 and GPT-5). If the two judges
   disagree by more than 20% on score, flag the sample for human review.
   Aggregate statistics use only samples where both judges agree within
   tolerance.

---

## What this prompt deliberately does NOT measure

Be explicit about this in any report:

- **Visual quality of rendered UI.** Pure text eval cannot measure this.
  If you want this, add a screenshot pipeline (generator outputs runnable
  code → headless browser → multimodal judge on the screenshot). That is a
  separate eval, not this one.
- **Long-term usability.** No LLM judge can simulate 8 hours of operator
  use of a dashboard. This is a human study.
- **Brand fit.** Requires knowing the actual brand. Unless the case ships
  brand assets, the judge has no grounding.
- **Original taste.** "Originality" is unmeasurable by LLM judges, who
  reward familiar patterns. Removed deliberately.

If your README ever quotes scores from this eval, include a sentence
explicitly stating these limits. Otherwise the numbers will be misread.

---

## Migration from v1 prompt

The old four-dimension prompt should be deleted, not kept as an alternative.
Keeping it as an option will cause future runs to silently fall back to it
under time pressure, and the next set of results will again be uninterpretable.

If you need a one-line replacement for "the score went up": report
`pass rate per rubric item across cases` instead of total scores. This is
more diagnostic — it tells you *which* aspects of the skill are working,
not just whether the average moved.