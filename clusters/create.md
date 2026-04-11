# Cluster: Create

Build distinctive, production-grade UI from scratch. Synthesizes: `frontend-design`, `baseline-ui`, `full-output-enforcement`, `teach-impeccable`, `design-taste-frontend`.

## Preparation

Tailwind checkpoint: if the project uses Tailwind, load `tailwind-integration.md` and detect whether it is v3 or v4 before choosing where tokens live.

1. **Context confirmed** (per SKILL.md §1) — you have audience, tone, and use cases.
2. **DESIGN.md check** — if `DESIGN.md` exists, read it now. Its colors, typography, elevation, and component specs are your starting point. Skip the aesthetic direction selection below and use the spec. If DESIGN.md is vague on a dimension, fill it in consistent with the Overview section's stated intent.
3. **Aesthetic direction chosen** — if no DESIGN.md and a preset is loaded, follow it. Otherwise, commit to one of these directions before writing a line of code:
   - Brutally minimal · Maximalist · Retro-futuristic · Organic/natural
   - Luxury/refined · Playful/toy-like · Editorial/magazine · Brutalist/raw
   - Art deco/geometric · Soft/pastel · Industrial/utilitarian
   - ...or synthesize something true to the project's personality.

   **The direction must be intentional, not incidental.** Bold maximalism and refined minimalism both work. Vague "clean and modern" does not.

3. **Ask yourself**: What is the one thing a user will remember about this interface? Design to make that thing unforgettable.
4. **Check the escalation level**: are you establishing a new language, or working inside an existing one? If the project already has a coherent visual system, strengthen it before replacing it.

## Implementation Workflow

### Step 1: Commit to a design decision in writing

Before any code, state in one sentence: *"This interface will feel [X] because this product is for [Y] doing [Z]."* This anchors every subsequent decision.

Then state three short reasons:

- why this typography direction fits the audience
- why this palette and surface language fit the product
- why this amount of visual change is appropriate

### Step 2: Typography

Choose fonts that are beautiful, unique, and fit the direction. Pair a distinctive display font with a refined body font.

- Use a modular type scale with fluid sizing (`clamp`).
- Vary weights and sizes to create clear hierarchy — don't flatten everything to the same size.
- Use `text-balance` on headings, `text-pretty` on body copy.
- Numbers in data contexts: `tabular-nums`.
- **Loading**: use `@font-face` with `font-display: swap`, or Google Fonts `display=swap`.

### Step 3: Color

Commit to a cohesive palette. A dominant color with sharp accents outperforms timid, evenly-distributed palettes.

- Use OKLCH for perceptual uniformity: `oklch(L% C H)`.
- Tint your neutrals toward your brand hue.
- Color ratio: 60% dominant / 30% secondary / 10% accent.
- Gray text on colored backgrounds looks washed out — use a dark shade of the background hue instead.
- Check: does every color serve a purpose? Remove decorative-only colors.

### Step 4: Layout & Space

Create rhythm through varied spacing — not uniform padding everywhere.

- Use asymmetry and unexpected compositions. Break the grid intentionally for emphasis.
- `clamp()` for fluid spacing that breathes on larger screens.
- Flex for 1D, Grid for 2D. Don't default to Grid for everything.
- No cards around content that doesn't need containment.
- No nested cards.
- Responsive: minimum touch targets 44×44px. Body text min 16px on mobile.

### Step 5: Visual Details

Details separate good from great.

- Custom borders, subtle textures, micro-typographic refinements.
- Shadows: directional and purposeful, not default drop shadows on rounded rectangles.
- Icons: choose a coherent set and retrieve the actual SVGs - don't write paths from memory. Use `better-icons`:

  ```bash
  # Search across 200+ libraries
  better-icons search "arrow right" --limit 10
  better-icons search "home" --prefix ph   # Phosphor only

  # Get SVG (outputs to stdout — pipe into your file)
  better-icons get ph:house > src/icons/house.svg
  better-icons get heroicons:check-circle --color currentColor

  # Batch download all results
  better-icons search "navigation" -d ./src/icons
  ```

  Preferred collections for quality design: `ph` (Phosphor), `heroicons`, `tabler`, `lucide`, `solar`. Pick **one** and stay consistent. Never mix Lucide + Phosphor + MDI in the same project.

  If the MCP `better-icons` server is available, prefer `recommend_icons` for use-case-based discovery:
  ```
  recommend_icons({ use_case: "navigation menu", style: "outline", limit: 10 })
  ```

  Fallback when icon tooling is unavailable:
  - inspect `package.json` and existing imports for installed icon libraries
  - stay within one already-installed family if it is acceptable
  - prefer package imports over hand-writing SVG paths from memory
  - if no icon system exists, keep icon changes conservative and note the limitation
- Interaction surfaces: clear affordances, obvious focus states.

### Step 6: Motion (if appropriate)

Keep it purposeful:

- Entrance: `200–500ms ease-out`, translate + fade.
- Interaction feedback: `100–150ms` max.
- State changes: `200–300ms`.
- Stagger for lists: `50–100ms` delay per item.
- See `clusters/motion.md` if motion is a primary concern.

### Step 7: Produce complete code

Output every file in full. No stubs. No truncation. Working, runnable, production-grade code.

### Step 8: Self-check before final output

Verify these before you stop:

- No primary UI relies on inline styles when the styling system can express it
- In Tailwind projects, reusable values live in theme tokens or CSS variables before reaching for arbitrary values
- The composition does not collapse into three equal-width cards as the whole layout
- Cards do not stack background + border + shadow without a hierarchy reason
- The chosen fonts, colors, motion level, and spacing model can each be defended in one sentence
- Typography, color, and spacing choices all support the same intentional direction
- The result still satisfies `contract.md`

## Aesthetic Defaults (no preset loaded)

Apply current SKILL.md parameters (default: Variance 8 / Motion 6 / Density 4). Translate to:
- Font: a geometric or humanist sans for display, paired with a refined body font. Warm-neutral OKLCH base, one strong accent.
- Motion: purposeful micro-interactions only — no performative animation for its own sake.
