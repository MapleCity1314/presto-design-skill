# Cluster: Refine

Improve existing UI without rebuilding from scratch. This cluster is for targeted upgrades, not wholesale reinvention.

Boundary: if the request implies replacing the whole page structure, hero concept, or information architecture, route to `redesign.md` instead.

## Diagnose First

| Symptom | Sub-file | Section |
|---------|----------|---------|
| Crowded / unbalanced / monotonous layout | `refine-layout.md` | Arrange |
| Too much visual noise, too many elements | `refine-layout.md` | Distill |
| Doesn't work on mobile / needs responsive work | `refine-layout.md` | Adapt |
| Mixed spacing/token conventions | `refine-layout.md` | Normalize |
| Lots of duplicated UI patterns | `refine-layout.md` | Extract |
| Typography feels generic or hard to read | `refine-style.md` | Typeset |
| Colors feel flat, grayish, or over-saturated | `refine-style.md` | Colorize |
| Design feels timid, safe, forgettable | `refine-style.md` | Bolder |
| Design feels aggressive, overstimulating | `refine-style.md` | Quiet |
| Text is confusing, labels unclear, errors unhelpful | `refine-style.md` | Clarify |
| First-run experience is confusing or empty | `refine-style.md` | Onboard |
| Missing moments of joy / feels mechanical | `refine-style.md` | Delight |
| Final pixel-level inconsistencies | `refine-style.md` | Polish |
| Icons look generic or styles are mismatched | `refine-style.md` | Icons |

Multiple symptoms: load the sub-file that covers the most symptoms. Work in this order when both files apply: `refine-layout.md` first, then `refine-style.md`.

## Execution Order

Refine work should be deliberately narrow and ordered. Follow this sequence:

1. Name the target in one sentence: what is being improved, and what should stay intact.
2. Decide scope:
   - `refine` = keep the component or page structure recognizable, improve hierarchy, styling, and implementation quality in place.
   - `redesign` = replace the composition, restructure sections, or introduce a substantially new concept.
3. Fix structure first: spacing, containers, hierarchy, responsiveness, duplicated patterns.
4. Fix visual language second: typography, color, iconography, copy, motion intensity.
5. Fix implementation last: remove inline styles, unify tokens, merge duplicate variants, move ad-hoc values into the project's styling system.

Do not jump straight to color and font changes if the real issue is layout or containment.

## High-Frequency Failure Modes

Treat these as refine bugs, not optional polish:

- Inline `style={{...}}` on normal app UI that should live in CSS, Tailwind classes, tokens, or styled primitives
- Cards using background + border + shadow all at once without a clear hierarchy reason
- Three equal-width columns as the whole solution to a layout problem
- New decorative wrappers that increase nesting instead of simplifying the surface language
- Superficial font/color swaps that leave spacing and hierarchy untouched

## Required Self-Check

Before finishing any refine task, verify:

- The result is still recognizably the same component or page, not a stealth redesign
- Structural fixes happened before stylistic polish
- Inline styles were removed unless the target is email HTML or a truly dynamic one-off value
- At least one source of unnecessary visual noise was removed, not merely restyled
- The final output still satisfies `contract.md`

## Sub-files

- `refine-layout.md` - Arrange, Distill, Normalize, Adapt, Extract
- `refine-style.md` - Typeset, Colorize, Bolder, Quiet, Clarify, Onboard, Delight, Polish, Icons
