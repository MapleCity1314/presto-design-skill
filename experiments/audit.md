# Phase 0 Audit — Presto Design Skill

Audited: 2026-04-09. Baseline = `master` branch, commit `ea5f360`.

---

## 1. Content Classification

### Legend
- `PROCESS` — flow steps, required phases, self-check lists
- `CONSTRAINT_VERB` — verb-level, executable, verifiable by grep / counting / structured self-check
- `CONSTRAINT_ADJECTIVE` — adjective-level rules ("should feel", "avoid generic", "prefer editorial") — requires taste to verify
- `AESTHETIC_DESCRIPTION` — prose teaching the agent what good design looks like
- `BASELINE_VERIFIABLE` — production baseline items with objective pass/fail

---

### `contract.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| "Design rationale (mandatory)" header + "Before implementation, the agent must state..." | `PROCESS` | Required pre-code ritual; verifiable structurally |
| "If the agent cannot explain the decision, the design is not locked yet." | `CONSTRAINT_ADJECTIVE` | "Cannot explain" is self-assessed; no external verifier |
| Anti-AI-Slop intro: "These are common failure modes, not timeless truths..." | `PROCESS` | Meta-framing, not a rule itself |
| "If a project-specific reason justifies one of these patterns..." | `CONSTRAINT_ADJECTIVE` | "Stronger than 'it looks modern'" is not verifiable |
| Typo: "Never default to Inter, Roboto, Arial... without a project-specific reason" | `CONSTRAINT_ADJECTIVE` | The font name is greppable; "without a project-specific reason" is unverifiable |
| "Never use monospace as lazy 'tech' vibes shorthand." | `CONSTRAINT_ADJECTIVE` | "Lazy vibes" is intent-inference, not output-verifiable |
| "Never place large rounded icons above every heading by default." | `CONSTRAINT_VERB` | Greppable icon placement pattern |
| "Never default to `#000` or `#fff` without checking tinted neutrals" | `CONSTRAINT_ADJECTIVE` | "Would improve the palette" is subjective |
| "Never default to cyan-on-dark, purple-to-blue gradients, or neon accents" | `CONSTRAINT_VERB` | Specific color patterns — greppable in CSS output |
| "Never default to gradient text on metrics, headings, or hero numbers" | `CONSTRAINT_VERB` | `background-clip: text` is greppable |
| "Never default to dark mode plus glowing accent as the primary design decision" | `CONSTRAINT_ADJECTIVE` | "Primary design decision" is not output-verifiable |
| "Never wrap everything in cards." | `CONSTRAINT_VERB` | Count card wrappers vs non-card sibling elements |
| "Never nest cards inside cards." | `CONSTRAINT_VERB` | Greppable structural pattern |
| "Never default to hero metrics layout" | `CONSTRAINT_VERB` | Layout pattern is recognizable and structural |
| "Never default to three equal-width cards as the entire layout" | `CONSTRAINT_VERB` | CSS grid/flex widths are greppable |
| "Never center-align all content." | `CONSTRAINT_ADJECTIVE` | "All content" — degree qualifier makes it unverifiable |
| "Never animate layout properties (width, height, top, left, margin, padding)" | `BASELINE_VERIFIABLE` | `transition:` + layout property names are greppable |
| "Never exceed 200ms for interaction feedback" | `BASELINE_VERIFIABLE` | Duration values greppable |
| "Never use bounce or elastic easing as the default interaction language" | `CONSTRAINT_VERB` | Easing keywords greppable |
| "Always prefer ease-out variants such as cubic-bezier(0.25, 1, 0.5, 1)" | `CONSTRAINT_VERB` | Easing greppable |
| "Always respect prefers-reduced-motion" | `BASELINE_VERIFIABLE` | Media query presence is greppable |
| Change policy (all 4 bullets) | `PROCESS` | Escalation logic; not a code-verifiable rule |
| Production baseline (all 8 items) | `BASELINE_VERIFIABLE` | Focus states, touch targets, semantic HTML, etc. — all objective |
| Technical baseline Tailwind (all items) | `CONSTRAINT_VERB` | Most greppable (h-screen, tabular-nums, cn, etc.) |
| Output completeness (no truncation) | `BASELINE_VERIFIABLE` | Verifiable: does output contain `// ...`? |

**Summary for `contract.md`**: 8 `BASELINE_VERIFIABLE`, 8 `CONSTRAINT_VERB`, 6 `CONSTRAINT_ADJECTIVE`, 2 `PROCESS`, 0 `AESTHETIC_DESCRIPTION`.

The anti-slop section is structurally FORBIDDEN rules but lacks UNLESS branches — it relies on agent self-judgment ("without a project-specific reason") rather than verifiable conditions.

---

### `SKILL.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| §1 Context Check — 3-step check order | `PROCESS` | — |
| §2 Design Parameters — table (VARIANCE/MOTION/DENSITY + numeric ranges) | `PROCESS` | The parameter system is routing logic |
| §2 Parameter descriptions: "asymmetric and experimental", "cinematic, spring-heavy", "compact cockpit" | `AESTHETIC_DESCRIPTION` | Vocabulary but no verifiable mapping to code output |
| §2 Calibration rule ("must produce visible downstream decisions") | `CONSTRAINT_ADJECTIVE` | "Visible downstream decisions" — auditor-dependent |
| §2 Quick anchors table | `AESTHETIC_DESCRIPTION` | Maps words to words ("visually risky", "operational") |
| §2 User override signals table | `PROCESS` | Routes user signals to parameter values |
| §3 Intent-to-Cluster routing table | `PROCESS` | — |
| §4 Aesthetic-to-Preset routing table | `PROCESS` | — |
| §5 Contract — pre-code rationale requirement | `PROCESS` | — |
| §6 GSAP Integration | `PROCESS` | Conditional load rule |
| §7 Tailwind Integration | `PROCESS` | Conditional load rule + version-sensing |
| §8 Execution / Respect-the-stack rule | `PROCESS` | — |

**Summary for `SKILL.md`**: heavy `PROCESS` with two `AESTHETIC_DESCRIPTION` blocks in the parameter descriptions. The AESTHETIC_DESCRIPTION here is soft — it's mostly vocabulary anchors, not design-theory prose.

---

### `clusters/create.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| Tailwind checkpoint | `PROCESS` | — |
| Context confirmed check | `PROCESS` | — |
| Aesthetic direction list ("Brutally minimal · Maximalist · Retro-futuristic...") | `AESTHETIC_DESCRIPTION` | Vocabulary menu — no mapping to verifiable choices |
| "The direction must be intentional, not incidental. Bold maximalism and refined minimalism both work. Vague 'clean and modern' does not." | `CONSTRAINT_ADJECTIVE` | "Intentional" and "refined minimalism" are taste-evaluated |
| "What is the one thing a user will remember..." | `AESTHETIC_DESCRIPTION` | Design philosophy, not a verifiable rule |
| Step 1: Commit to design decision in writing | `PROCESS` | — |
| Step 2 Typography: "Choose fonts that are beautiful, unique, and fit the direction. Pair a distinctive display font with a refined body font." | `AESTHETIC_DESCRIPTION` | "Beautiful", "distinctive", "refined" — no verifier |
| Step 2: "Use a modular type scale with fluid sizing (clamp)." | `CONSTRAINT_VERB` | `clamp()` is greppable |
| Step 2: "Vary weights and sizes to create clear hierarchy" | `CONSTRAINT_VERB` | Count distinct weight/size values |
| Step 2: `text-balance`, `text-pretty`, `tabular-nums` | `BASELINE_VERIFIABLE` | Greppable |
| Step 2: `@font-face` with `font-display: swap` | `CONSTRAINT_VERB` | Greppable |
| Step 3 Color: "Commit to a cohesive palette. A dominant color with sharp accents outperforms timid, evenly-distributed palettes." | `AESTHETIC_DESCRIPTION` | "Timid, evenly-distributed" — taste judgment |
| Step 3: Use OKLCH | `CONSTRAINT_VERB` | Greppable color notation |
| Step 3: Tint neutrals toward brand hue | `CONSTRAINT_VERB` | Verifiable with OKLCH hue values |
| Step 3: 60/30/10 ratio | `CONSTRAINT_VERB` | Auditable by counting color usage |
| Step 3: "Gray text on colored backgrounds looks washed out" | `AESTHETIC_DESCRIPTION` | Explanatory rationale |
| Step 3: "does every color serve a purpose? Remove decorative-only colors." | `CONSTRAINT_ADJECTIVE` | "Serve a purpose" / "decorative-only" — subjective |
| Step 4 Layout: "Create rhythm through varied spacing — not uniform padding everywhere." | `AESTHETIC_DESCRIPTION` | "Rhythm" is not verifiable |
| Step 4: "Use asymmetry and unexpected compositions. Break the grid intentionally for emphasis." | `AESTHETIC_DESCRIPTION` | "Unexpected", "intentional for emphasis" — taste |
| Step 4: `clamp()` for spacing | `CONSTRAINT_VERB` | Greppable |
| Step 4: Flex for 1D, Grid for 2D | `CONSTRAINT_VERB` | Verifiable |
| Step 4: No cards, no nested cards, responsive touch targets | `CONSTRAINT_VERB` | Greppable |
| Step 5 Visual Details: "Details separate good from great." | `AESTHETIC_DESCRIPTION` | Philosophy sentence |
| Step 5: "Custom borders, subtle textures, micro-typographic refinements." | `AESTHETIC_DESCRIPTION` | Vocabulary without threshold |
| Step 5: "Shadows: directional and purposeful, not default drop shadows on rounded rectangles." | `CONSTRAINT_ADJECTIVE` | "Directional and purposeful" — not verifiable |
| Step 5: Icon tooling (`better-icons`) | `CONSTRAINT_VERB` | Executable commands |
| Step 5: "Interaction surfaces: clear affordances, obvious focus states." | `BASELINE_VERIFIABLE` | Focus states = greppable |
| Step 6 Motion: all timing values | `CONSTRAINT_VERB` / `BASELINE_VERIFIABLE` | Ranges are greppable |
| Step 7: Output every file complete | `BASELINE_VERIFIABLE` | — |
| Step 8: Self-check list | `PROCESS` + `CONSTRAINT_VERB` | — |
| Aesthetic Defaults: "geometric or humanist sans for display, paired with a refined body font. Warm-neutral OKLCH base, one strong accent." | `AESTHETIC_DESCRIPTION` | "Refined", "warm-neutral" — vague without OKLCH values |

**Summary for `clusters/create.md`**: ~6 `AESTHETIC_DESCRIPTION`, ~10 `CONSTRAINT_VERB`, ~3 `CONSTRAINT_ADJECTIVE`, ~4 `PROCESS`, ~3 `BASELINE_VERIFIABLE`.

The AESTHETIC_DESCRIPTION content is concentrated in the framing paragraphs (direction vocabulary, "rhythm", "intentional asymmetry") and in Step 3/4/5 rationale sentences.

---

### `clusters/redesign.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| Core rule / Escalation rule | `PROCESS` | — |
| Phase 1 Scan | `PROCESS` | — |
| "Output a one-paragraph summary" | `PROCESS` | — |
| Phase 2 Diagnose: all P0 Typography items | `CONSTRAINT_VERB` | Font names greppable, sizes measurable |
| Phase 2: P1/P2 Typography items | `CONSTRAINT_VERB` | `65ch`, `tabular-nums`, tracking all greppable |
| Phase 2: P0 Color items ("purple/blue AI gradient", "pure #000/#fff") | `CONSTRAINT_VERB` | Color values greppable |
| Phase 2: P1/P2 Color items (saturation, mixed grays, shadows) | `CONSTRAINT_VERB` | OKLCH values greppable |
| Phase 2: P2 Color "Flat design with zero texture", "Perfectly even linear gradients" | `CONSTRAINT_ADJECTIVE` | "Zero texture" / "perfectly even" — requires judgment |
| Phase 2: P0 Layout items (three equal columns, hero metrics) | `CONSTRAINT_VERB` | Structural patterns |
| Phase 2: P1/P2 Layout items (centering, max-width, padding) | `CONSTRAINT_VERB` | Mostly verifiable |
| Phase 2: P2 Layout "No overlap or depth" | `CONSTRAINT_ADJECTIVE` | "Depth" is aesthetic |
| Phase 2: P0 Interactivity (hover states, focus ring, error states) | `BASELINE_VERIFIABLE` | — |
| Phase 2: P1/P2 Interactivity | `CONSTRAINT_VERB` / `BASELINE_VERIFIABLE` | Mostly greppable |
| Phase 2: Content / AI copy clichés | `CONSTRAINT_VERB` | Word list is greppable |
| Phase 2: Component patterns | `CONSTRAINT_VERB` | Structural patterns |
| Phase 2: Iconography | `CONSTRAINT_VERB` | Library names greppable |
| Phase 2: Code Quality | `BASELINE_VERIFIABLE` | Semantic HTML, alt text, etc. |
| Phase 2: Strategic Omissions | `BASELINE_VERIFIABLE` | Checklist items |
| Phase 3 Fix Priority | `PROCESS` | Ordering guide |
| Upgrade Techniques: Typography (variable font animation, text mask reveals, outlined-to-fill) | `AESTHETIC_DESCRIPTION` | Technique descriptions — aspirational |
| Upgrade Techniques: Layout (broken grid, parallax card stacks, split-screen scroll, whitespace maximization) | `AESTHETIC_DESCRIPTION` | "Whitespace maximization: aggressive negative space to force focus on a single hero element" — pure aesthetic |
| Upgrade Techniques: Motion (staggered entry, spring physics, scroll-driven reveals) | `AESTHETIC_DESCRIPTION` | Technique vocabulary; concrete timing values make it borderline `CONSTRAINT_VERB` |
| Upgrade Techniques: Surface (noise overlay, tinted shadows, spotlight borders) | `AESTHETIC_DESCRIPTION` | Technique descriptions; the CSS code blocks make them executable |
| Final Self-Check | `PROCESS` | — |
| Constraints | `CONSTRAINT_VERB` | — |

**Summary for `clusters/redesign.md`**: The checklist body is primarily `CONSTRAINT_VERB` and `BASELINE_VERIFIABLE`. The "Upgrade Techniques" section is entirely `AESTHETIC_DESCRIPTION`. The P0 "purple/blue gradient" items duplicate `contract.md` anti-slop rules verbatim.

---

### `clusters/refine.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| Boundary note | `PROCESS` | — |
| Diagnose routing table | `PROCESS` | — |
| Execution Order (5 steps) | `PROCESS` | — |
| High-Frequency Failure Modes | `CONSTRAINT_VERB` | All greppable structural patterns |
| Required Self-Check | `PROCESS` + `BASELINE_VERIFIABLE` | — |

**Summary for `clusters/refine.md`**: almost entirely `PROCESS` with a few `CONSTRAINT_VERB`. No `AESTHETIC_DESCRIPTION`.

---

### `clusters/refine-layout.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| Arrange (audit spacing, flatten hierarchy, break monotony) | `CONSTRAINT_VERB` | Most specific enough to verify |
| "Mandatory check: if your layout solution is still 'three equal cards in one row', you have not refined enough." | `CONSTRAINT_VERB` | — |
| Distill (cut content, reduce to 1-2 colors, simplify layout) | `CONSTRAINT_VERB` | Counting-verifiable |
| Normalize | `CONSTRAINT_VERB` | Token replacement is greppable |
| Adapt (responsive) — all steps, code examples | `BASELINE_VERIFIABLE` | Concrete media queries, `clamp()` |
| Extract | `CONSTRAINT_VERB` | 3+ occurrences rule is verifiable |
| Layout Exit Checklist | `PROCESS` + `CONSTRAINT_VERB` | — |

**Summary for `clusters/refine-layout.md`**: almost entirely `CONSTRAINT_VERB` and `BASELINE_VERIFIABLE`. No `AESTHETIC_DESCRIPTION`.

---

### `clusters/refine-style.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| Typeset: hierarchy audit, scale, line length, line height, weight | `CONSTRAINT_VERB` | All measurable |
| Typeset: "if using Inter, Roboto, Arial... replace them. Choose something with character." | `CONSTRAINT_ADJECTIVE` | "Character" is aesthetic judgment |
| Colorize: OKLCH system setup | `CONSTRAINT_VERB` | Concrete values |
| Colorize: "Gray text on colored background is the most common colorize bug" + code examples | `CONSTRAINT_VERB` | Pattern is verifiable |
| Colorize: "If the component already has enough visual noise, simplify before adding color." | `CONSTRAINT_ADJECTIVE` | "Enough visual noise" — not verifiable |
| Bolder: typography drama code examples | `CONSTRAINT_VERB` | Specific CSS values |
| Bolder: "avoid cyan or purple gradients, glassmorphism, or neon on dark" | `CONSTRAINT_VERB` | Greppable |
| Bolder: "Avoid turning every refine request into a hero treatment." | `CONSTRAINT_ADJECTIVE` | — |
| Quiet (all steps) | `CONSTRAINT_VERB` | Mostly measurable (saturation, weight, duration) |
| Clarify | `CONSTRAINT_VERB` | Copy pattern rules |
| Onboard | `CONSTRAINT_VERB` | — |
| Delight | `CONSTRAINT_VERB` | "< 1s, skippable, prefers-reduced-motion" — verifiable |
| Polish (full checklist) | `BASELINE_VERIFIABLE` | All greppable |
| Icons | `CONSTRAINT_VERB` | — |

**Summary for `clusters/refine-style.md`**: predominantly `CONSTRAINT_VERB` and `BASELINE_VERIFIABLE`, with 3 `CONSTRAINT_ADJECTIVE` spots ("character", "enough visual noise", "hero treatment"). No significant `AESTHETIC_DESCRIPTION`.

---

### `clusters/motion.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| Strategy First (3 questions) | `PROCESS` | — |
| "If the answer is 'nothing, it just looks cool' — reconsider." | `CONSTRAINT_ADJECTIVE` | Intent-dependent |
| "Any non-compositor property... Refuse to animate them." | `CONSTRAINT_VERB` | Property names greppable |
| Timing Reference table | `CONSTRAINT_VERB` | All numeric ranges |
| Easing Reference | `CONSTRAINT_VERB` | CSS values greppable |
| "Never use: bounce, elastic. They read as dated." | `CONSTRAINT_ADJECTIVE` | "Dated" is aesthetic judgment; keyword is greppable |
| Performance Rules | `BASELINE_VERIFIABLE` | `will-change`, blur limits — verifiable |
| CSS Animation code blocks | `CONSTRAINT_VERB` | — |
| GSAP section | `CONSTRAINT_VERB` | API documentation |
| Six Motion Categories | `PROCESS` | — |

**Summary for `clusters/motion.md`**: mostly `CONSTRAINT_VERB` with light `AESTHETIC_DESCRIPTION`. Notably clean.

---

### `clusters/fix.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| Phase 1 Technical Audit (all scoring rubrics) | `BASELINE_VERIFIABLE` | All have objective criteria |
| AI Anti-Patterns scoring | `CONSTRAINT_VERB` | Pattern list is greppable |
| Phase 2 UX Review (Nielsen heuristics) | `CONSTRAINT_ADJECTIVE` | "Does the user always know what's happening?" — requires judgment |
| "Emotional journey" check | `AESTHETIC_DESCRIPTION` | "Where does user feel accomplished/anxious" — taste |
| AI Slop copy test | `CONSTRAINT_VERB` | Word list greppable |
| Phase 3 Fix Routing table | `PROCESS` | — |
| Accessibility Fix Priorities | `BASELINE_VERIFIABLE` | — |
| Harden section | `BASELINE_VERIFIABLE` | Concrete edge cases |
| Metadata (full spec) | `BASELINE_VERIFIABLE` | — |

**Summary for `clusters/fix.md`**: almost entirely `BASELINE_VERIFIABLE` with some `CONSTRAINT_ADJECTIVE` in the UX review section. The "Emotional journey" bullet is the only true `AESTHETIC_DESCRIPTION`.

---

### `clusters/overdrive.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| "Propose Before Building" | `PROCESS` | — |
| "What Extraordinary Means by Context" table | `AESTHETIC_DESCRIPTION` | "Sensory: scroll-driven reveals, shader backgrounds..." — vocabulary |
| "Rule: something about the implementation exceeds what users expect..." | `CONSTRAINT_ADJECTIVE` | "Exceeds expectations" — not verifiable |
| The Toolkit — all code blocks | `CONSTRAINT_VERB` | Executable code |
| Industrial Brutalist Mode — palette + code | `CONSTRAINT_VERB` | OKLCH values greppable |
| Industrial typography rules | `CONSTRAINT_VERB` | Font names, letter-spacing values |
| Industrial layout rules | `CONSTRAINT_ADJECTIVE` | "Rigid grid. Expose the structure." — intent, not verifiable |
| Industrial motion: "No easing — or very minimal. Mechanical snapping." | `CONSTRAINT_ADJECTIVE` | "Mechanical snapping" — aesthetic descriptor |
| Quality Bar for Overdrive | `PROCESS` + `BASELINE_VERIFIABLE` | 60fps, 375px, reduced-motion |

**Summary for `clusters/overdrive.md`**: mix of `AESTHETIC_DESCRIPTION` (vocabulary for what "extraordinary" means) and `CONSTRAINT_VERB` (toolkit code). The Industrial mode mixes concrete CSS values with aesthetic adjectives.

---

### `presets/editorial.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| "Aesthetic Intent": "Every layout is a deliberate composition. Typography is the architecture. Color is used with precision — a single strong palette choice executed with confidence. Spacing is dramatic: sections breathe, content is given room to exist. The design feels like it was made by a human with taste, not assembled from components." | `AESTHETIC_DESCRIPTION` | Pure design philosophy prose |
| Variance engine: 5 aesthetic directions (Organic editorial, Geometric precision, Dark luxury, Swiss modernist, New wave) | `AESTHETIC_DESCRIPTION` | Vocabulary menu |
| Parameters table | `PROCESS` | — |
| Color System — 3 options with OKLCH values | `CONSTRAINT_VERB` | Greppable |
| Color rules (no purple gradients, no neon, 60/30/10) | `CONSTRAINT_VERB` | — |
| Typography pairings | `CONSTRAINT_VERB` | Font names greppable |
| Editorial type scale (CSS variables) | `CONSTRAINT_VERB` | — |
| Typography rules (1.4× contrast, weight at extremes, no letter-spacing on body) | `CONSTRAINT_VERB` | Measurable |
| Layout code block + rules | `CONSTRAINT_VERB` | Greppable |
| "Not everything spans full width. Offset and asymmetry create tension." | `AESTHETIC_DESCRIPTION` | "Tension" — aesthetic |
| Motion (CSS easing values, timing) | `CONSTRAINT_VERB` | — |
| High-End Details (dual-bezier shadow, optical adjustments, image treatment, micro-typography) | `CONSTRAINT_VERB` | CSS values greppable |
| "images benefit from object-position fine-tuning, filter: contrast(1.05) saturate(0.95) for a print-like quality" | `AESTHETIC_DESCRIPTION` | "Print-like quality" is aesthetic |

**Summary for `presets/editorial.md`**: The "Aesthetic Intent" section and variance engine are pure `AESTHETIC_DESCRIPTION`. The rest is mostly `CONSTRAINT_VERB` with concrete CSS. This preset has the highest concentration of `AESTHETIC_DESCRIPTION` in the skill.

---

### `presets/minimalist.md`

| Paragraph / Section | Label | Notes |
|---|---|---|
| "Aesthetic Intent": "Clean, editorial, focused. Typography does the heavy lifting. Color is used for meaning, not decoration. Whitespace is the primary structural tool. Nothing competes for attention..." | `AESTHETIC_DESCRIPTION` | Philosophy prose |
| Color System (OKLCH values + rules) | `CONSTRAINT_VERB` | — |
| Typography (font names, scale, CSS) | `CONSTRAINT_VERB` | — |
| Layout rules | `CONSTRAINT_VERB` | Mostly measurable |
| Motion | `CONSTRAINT_VERB` | All timing values |
| Component Style (CSS code) | `CONSTRAINT_VERB` | — |

**Summary for `presets/minimalist.md`**: only the "Aesthetic Intent" paragraph is `AESTHETIC_DESCRIPTION`. The rest is `CONSTRAINT_VERB`.

---

### `context/teach-impeccable.md`

Entirely `PROCESS`. No `AESTHETIC_DESCRIPTION` or `CONSTRAINT_VERB` — it's a structured context-gathering workflow.

---

### `gsap-integration.md` + `tailwind-integration.md`

Entirely `PROCESS` + `CONSTRAINT_VERB`. No `AESTHETIC_DESCRIPTION`. Clean, technical, specific.

---

## 2. Duplication Map

Topics where knowledge appears in multiple files:

### Typography

| File | Location | What appears |
|---|---|---|
| `contract.md` | Anti-AI-slop | Never default to Inter/Roboto/Arial as primary display font |
| `clusters/create.md` | Step 2 | Font pairing guidance, modular scale, `clamp()`, `text-balance` |
| `clusters/redesign.md` | Phase 2 Typography | P0 font checklist, specific replacements (Geist, Outfit, etc.), letter-spacing, line-height |
| `clusters/refine-style.md` | Typeset | Same hierarchy rules, scale, `65ch`, font pairing (replace Inter) |
| `presets/editorial.md` | Typography | Editorial-specific pairings, dramatic scale, extreme weights |
| `presets/minimalist.md` | Typography | Minimalist pairings, weight-hierarchy approach |

**Duplication**: "never default to Inter/Roboto/Arial" appears in `contract.md` AND in `clusters/redesign.md` (P0 item) AND in `clusters/refine-style.md` (Typeset step 5). Same rule, three places.

### Color

| File | Location | What appears |
|---|---|---|
| `contract.md` | Anti-AI-slop | No pure black/white, no cyan/purple, no gradient text |
| `clusters/create.md` | Step 3 | OKLCH, 60/30/10, tint neutrals |
| `clusters/redesign.md` | Phase 2 Color | Same OKLCH values, same "pure #000/#fff" P0 item |
| `clusters/refine-style.md` | Colorize | OKLCH token system, gray-on-color bug |
| `presets/editorial.md` | Color | Concrete palette options |
| `presets/minimalist.md` | Color | Warm monochrome palette |

**Duplication**: The "never use pure `#000` or `#fff`" rule with OKLCH alternatives appears in `contract.md`, `clusters/redesign.md` (verbatim), and the OKLCH color system appears in `clusters/create.md`, `clusters/refine-style.md`, and both presets. The off-black value `oklch(8% 0.01 240)` appears identically in `clusters/redesign.md` and `clusters/overdrive.md`.

### Layout Anti-Patterns

| File | Location | What appears |
|---|---|---|
| `contract.md` | Anti-AI-slop | No card soup, no nested cards, no 3-equal-column, no hero metrics |
| `clusters/create.md` | Step 4 | No cards, no nested cards |
| `clusters/redesign.md` | Phase 2 Layout | P0: 3-equal-column, hero metrics (identical to contract.md) |
| `clusters/refine-layout.md` | Arrange, Distill | 3-equal-column rule, nested cards |
| `clusters/fix.md` | AI Anti-Patterns scoring | 3-equal cards, hero metrics, glassmorphism |

**Duplication**: "three equal-width cards as the entire layout" appears in `contract.md`, `clusters/redesign.md`, `clusters/refine-layout.md`, and `clusters/fix.md`. Same rule, four files. "Hero metrics layout" appears in `contract.md` and `clusters/redesign.md`.

### Motion Baseline

| File | Location | What appears |
|---|---|---|
| `contract.md` | Anti-slop + Production baseline | No layout-property animation, no bounce/elastic, 200ms max feedback, prefers-reduced-motion |
| `clusters/create.md` | Step 6 | Timing ranges |
| `clusters/motion.md` | Entire cluster | Comprehensive |
| `clusters/redesign.md` | Phase 2 Interactivity | 150-200ms, no layout animation |
| `clusters/fix.md` | Technical Audit | Animator layout properties |
| `gsap-integration.md` | Duration alignment | Maps contract timing to GSAP |

**Duplication**: The "never animate layout properties" rule appears in `contract.md`, `clusters/redesign.md`, `clusters/fix.md`, and `clusters/motion.md`. The 200ms interaction feedback cap appears in `contract.md` and `clusters/motion.md`.

### Icons

| File | Location | What appears |
|---|---|---|
| `clusters/create.md` | Step 5 | `better-icons` tooling, preferred collections |
| `clusters/redesign.md` | Phase 2 Iconography | Same `better-icons` commands, "never mix libraries" |
| `clusters/refine-style.md` | Icons section | Same library table, same commands |

**Duplication**: `better-icons` commands and "never mix libraries in the same project" appear identically in three cluster files.

---

## 3. Router Necessity Check

For each cluster: rules that are *only* meaningful in that cluster vs. rules that are general design knowledge. Flag clusters with <30% cluster-specific content.

### `clusters/create.md` — ~55% cluster-specific

Cluster-specific:
- Aesthetic direction commitment step (Step 1 design sentence)
- Step 2-7 build workflow (building from scratch, not refining)
- "Aesthetic Defaults" (VARIANCE 8 / MOTION 6 / DENSITY 4 defaults)

General (also in contract.md or other clusters):
- Font guidelines (in contract.md + redesign.md + refine-style.md)
- Color guidelines (in contract.md + redesign.md + refine-style.md)
- Layout anti-patterns (in contract.md + redesign.md + refine-layout.md)
- Motion timing (in contract.md + motion.md)

**Assessment**: Not thin. The build-from-scratch workflow and commitment steps are genuinely unique.

### `clusters/refine.md` — ~65% cluster-specific

Cluster-specific:
- Symptom-to-sub-file routing table
- "Refine vs redesign" boundary
- Execution order (structure-first rule)
- Required Self-Check ("still recognizably the same component")

General:
- High-Frequency Failure Modes mirror contract.md anti-slop rules

**Assessment**: Not thin. The routing logic and refine/redesign boundary are unique.

### `clusters/refine-layout.md` — ~80% cluster-specific

Almost entirely unique. The Arrange/Distill/Normalize/Adapt/Extract taxonomy doesn't appear elsewhere. **No router-thinness problem.**

### `clusters/refine-style.md` — ~70% cluster-specific

The Typeset/Colorize/Bolder/Quiet/Clarify/Onboard/Delight/Polish sections are unique to this cluster. The OKLCH system duplicates from presets but the refine application is specific. **No router-thinness problem.**

### `clusters/redesign.md` — ~45% cluster-specific**

Cluster-specific:
- Three-phase workflow (Scan → Diagnose → Fix)
- P0/P1/P2 priority system
- Per-category checklist format
- Upgrade Techniques section (mostly AESTHETIC_DESCRIPTION)
- Strategic Omissions list

General (duplicates from `contract.md`):
- "Never default to Inter" → contract.md anti-slop
- "Never pure #000/#fff" → contract.md anti-slop (verbatim)
- "Never three equal-width cards" → contract.md anti-slop
- "Never hero metrics layout" → contract.md anti-slop
- Focus states → contract.md production baseline
- Semantic HTML → contract.md production baseline
- Content copy clichés → new in redesign.md only ✓

**Assessment**: Not below 30%, but has the most duplication of any cluster. The checklist format is the cluster-specific value; many checklist items are contract.md rules restated.

### `clusters/motion.md` — ~85% cluster-specific

Timing table, easing reference, GSAP API detail, six motion categories — almost all unique. The `prefers-reduced-motion` rule duplicates contract.md but it's appropriate to restate here. **No router-thinness problem.**

### `clusters/fix.md` — ~80% cluster-specific

The audit scoring rubric, Nielsen heuristics, fix routing table, metadata spec — unique. The AI anti-patterns scoring duplicates contract.md items but serves a different purpose (scoring, not prohibition). **No router-thinness problem.**

### `clusters/overdrive.md` — ~75% cluster-specific

The toolkit (WebGL, spring physics, scroll-driven, View Transitions) is unique. Industrial Brutalist mode is unique and does not appear elsewhere. **No router-thinness problem.**

---

## Summary: Key Findings

### AESTHETIC_DESCRIPTION content — where it is concentrated

1. **`presets/editorial.md`**: The "Aesthetic Intent" paragraph + variance engine (5 aesthetic directions) — ~150 words of pure design philosophy with no verifiable claim.
2. **`clusters/create.md`**: Step 2 framing ("beautiful, unique"), Step 3 framing ("dominant color with sharp accents outperforms timid palettes"), Step 4 framing ("rhythm through varied spacing", "asymmetry and unexpected compositions"), Step 5 framing ("Details separate good from great"), Aesthetic Defaults.
3. **`clusters/redesign.md`**: "Upgrade Techniques" section (Variable font animation, parallax card stacks, split-screen scroll, whitespace maximization, noise overlay).
4. **`SKILL.md`**: Parameter description prose in §2 ("bleeding edges, overlap, rotated text, unexpected composition", "compact cockpit").
5. **`presets/minimalist.md`**: "Aesthetic Intent" paragraph — minor.
6. **`clusters/overdrive.md`**: "What Extraordinary Means by Context" table.

### CONSTRAINT_ADJECTIVE content — where UNLESS upgrades are needed most

In `contract.md`:
- "Never default to Inter/Roboto/Arial... **without a project-specific reason**" — needs UNLESS with observable conditions
- "Never default to #000 or #fff **without checking** whether tinted neutrals would improve" — "would improve" is unverifiable
- "**Never center-align all** content." — degree qualifier makes it unverifiable
- "If a project-specific reason justifies one of these patterns, the reason must be **explicit and stronger than** 'it looks modern.'" — gatekeeping by taste

### BASELINE_VERIFIABLE items — the skill's strongest content

All greppable: focus states, `prefers-reduced-motion`, touch targets, no layout-property animation, no truncation, semantic HTML, `tabular-nums`, `text-balance`.

### Duplication assessment

The most heavily duplicated rules are also the contract's strongest: the 3-equal-column anti-pattern, hero metrics layout, and `prefers-reduced-motion` requirement appear 3-4 times each across the repo. This is redundancy-by-design (each cluster is meant to be standalone) but means edits to these rules require touching multiple files.
