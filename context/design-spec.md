# DESIGN.md Generation Workflow

Generate or update a `DESIGN.md` in the project root. This is the visual counterpart to `AGENTS.md` — a living design specification that tells the Design Agent how the product should look and feel.

---

## When to run

- No `DESIGN.md` exists and the user wants design work done.
- The user explicitly asks to create, update, or regenerate the design spec.
- Route here from `SKILL.md` §1 when design context is missing.

---

## Three generation paths

### Path A — Agent-generated (from vibe prompt)

The user provides a short description like *"A playful coffee shop ordering app with warm colors, rounded corners, and a friendly feel"*.

Pattern: **[product type] + [mood/atmosphere ×2-3] + [key visual traits ×2-3]**.

1. Parse the vibe prompt into design decisions.
2. Choose concrete values for every section below.
3. Write `DESIGN.md`.

### Path B — Brand-derived (from URL or image)

The user provides an existing brand asset (URL, screenshot, logo, style guide).

1. Extract: dominant colors (hex), typography (identify fonts or closest matches), spacing feel, elevation style, component patterns.
2. Translate extracted values into the section structure below.
3. Write `DESIGN.md`.

### Path C — Hand-written (direct edit)

The user provides explicit values or edits the markdown directly. Respect their precision — do not override hex values, font names, or sizing with "better" alternatives unless asked.

---

## DESIGN.md section structure

Sections are ordered. Irrelevant sections can be omitted, but order must not change.

```markdown
# DESIGN.md

## Overview

[1-3 sentences describing the product's visual atmosphere.
Playful or professional? Dense or spacious? Warm or clinical?
This section is the tiebreaker when other sections don't cover a decision.]

## Colors

### Primary
- `#hex` — role (e.g., "CTAs, active states, primary actions")

### Secondary
- `#hex` — role (e.g., "secondary buttons, selected states, supporting accents")

### Tertiary
- `#hex` — role (e.g., "badges, tags, decorative accents")

### Neutral
- `#hex` background
- `#hex` surface
- `#hex` border
- `#hex` text-primary
- `#hex` text-muted

[Agent derives surface/on-primary/error/outline variants from these groups automatically.]

## Typography

### Headline
- Family: [font name]
- Weight: [weight range, e.g., 600–900]
- Size: [size range, e.g., 24–64px or clamp expression]

### Body
- Family: [font name]
- Weight: [weight range, e.g., 400–500]
- Size: [size range, e.g., 14–18px]

### Label
- Family: [font name]
- Weight: [weight range]
- Size: [size range, e.g., 11–14px]

[Same family across groups = unified feel. Mixed families = intentional contrast.]

## Elevation

[How depth is communicated. Examples:
- "Layered shadows with warm tint, 3 levels: sm/md/lg"
- "No shadows. Depth via border weight + surface color stepping"
- "Subtle directional shadow (light from top-left), cards only"]

## Components

### Buttons
- Border radius: [value]
- Padding: [value]
- Variants: [primary, secondary, ghost, destructive...]
- States: [hover, active, disabled, focus]

### Inputs
- Border radius: [value]
- Border: [style]
- States: [default, focus, error, disabled]

### Chips / Tags
- Border radius: [value]
- Variants: [filled, outlined]

### Lists
- Spacing: [gap between items]
- Dividers: [yes/no, style]

### Checkboxes / Radio
- Style: [rounded, square, custom]

### Tooltips
- Style: [background, text color, arrow, max-width]

[Only include component categories relevant to the product. Add others as needed.]

## Do's and Don'ts

### Do
- [Hard constraint, e.g., "Maintain WCAG AA 4.5:1 contrast on all text"]
- [Hard constraint, e.g., "Use primary color sparingly — max once per viewport"]

### Don't
- [Hard constraint, e.g., "Don't mix rounded and sharp corners in the same surface"]
- [Hard constraint, e.g., "Don't use gradients on text"]
```

---

## Writing rules

- **Markdown is the collaboration layer.** It can be vague ("warm rounded feel") or precise (`#2665fd / 8px`). Write at the precision level the user wants to lock.
- **Vague values are design intent.** The agent translates them to concrete values at implementation time.
- **Precise values are constraints.** The agent uses them literally.
- **Hex values must include the role description.** A naked hex is ambiguous.
- **Typography entries must state family.** "Sans-serif" alone is not a spec — name the font.
- **Do's and Don'ts are hard guardrails**, not suggestions. They override cluster defaults.

---

## After writing DESIGN.md

1. Confirm the spec with the user. Summarize: overview vibe, primary + accent colors, headline + body fonts, elevation strategy, key constraints.
2. If the user was mid-task (e.g., asked to create a page), resume the task. DESIGN.md is now the active design authority — clusters read it before making typography, color, elevation, and component decisions.
3. If `.impeccable.md` exists with a `## Design Context` section, that context (audience, brand personality, principles) is still valid and complements DESIGN.md. DESIGN.md specifies *how it looks*; design context specifies *who it's for and why*.
