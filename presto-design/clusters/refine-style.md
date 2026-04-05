# Refine - Style

Aesthetic and content fixes: typography, color, intensity, copy, experience, icons, polish. Loaded by `refine.md` when symptoms are style-related.

Important: style work in `refine` should strengthen an existing structure, not paper over a broken one. If containment, spacing, or hierarchy are wrong, send the work back through `refine-layout.md` first.

---

## Typeset (typography)

1. Audit hierarchy: can you scan the page and immediately understand the structure? If not, increase size and weight contrast.
2. Scale: use a modular scale (1.25x or 1.333x). Adjacent sizes too close -> increase ratio.
3. Line length: 45-75 characters for body. Too wide -> `max-width: 65ch`.
4. Line height: body 1.5-1.7. Headings 1.1-1.3. Captions and labels 1.4.
5. Font pairing: if using Inter, Roboto, Arial, or system defaults as the primary voice, replace them. Choose something with character.
6. Weight: use `font-weight: 500` or `600` for UI labels. Don't default everything to `400`.
7. Numerics: always `tabular-nums` for any changing number.

Do not treat a font swap alone as a successful refine pass.

---

## Colorize (add strategic color)

Use when the palette is too gray, too dark, or too flat.

OKLCH color system - set this up first:

```css
:root {
  --bg:         oklch(97.5% 0.010 60);
  --surface:    oklch(95%   0.008 60);
  --border:     oklch(88%   0.010 60);
  --text:       oklch(18%   0.012 60);
  --text-muted: oklch(52%   0.010 60);
  --accent:     oklch(58%   0.20  30);
  --accent-hi:  oklch(72%   0.18  85);
  --success:    oklch(62%   0.18  155);
  --error:      oklch(55%   0.22  25);
  --warning:    oklch(72%   0.18  75);
  --info:       oklch(60%   0.18  240);
}
```

Gray text on colored background is the most common colorize bug:

```css
/* WRONG: gray text on color looks washed out */
.badge { background: oklch(72% 0.18 155); color: #6b7280; }

/* RIGHT: dark shade of the background hue */
.badge { background: oklch(72% 0.18 155); color: oklch(22% 0.12 155); }
```

60/30/10 ratio: dominant surface 60%, secondary and neutral 30%, accent 10%. If accent appears in headers and buttons and borders and icons, it's overused.

Tinted borders: `border: 1px solid color-mix(in oklch, var(--accent) 15%, var(--border));`

If the component already has enough visual noise, simplify surfaces before adding color.

---

## Bolder (amplify impact)

Use when the design is too safe, too generic, or forgettable.

Typography drama:

```css
/* Before: flat AI hierarchy */
h1 { font-size: 2rem; font-weight: 600; }
p  { font-size: 1rem; font-weight: 400; }

/* After: 5x scale contrast + weight opposition */
h1 { font-size: clamp(3rem, 8vw, 7rem); font-weight: 900; line-height: 1.0; letter-spacing: -0.03em; }
p  { font-size: 1rem; font-weight: 400; line-height: 1.65; }
```

Space drama:

```css
/* Before: safe, cramped */
.section { padding: 40px 24px; }

/* After: give content room to exist */
.section { padding: clamp(80px, 12vw, 160px) clamp(24px, 8vw, 80px); }
```

Color commitment:

```css
/* One color truly dominates, not three at 33% each */
.hero       { background: oklch(22% 0.015 60); color: oklch(97% 0.01 60); }
.cta-button { background: oklch(68% 0.22 30); color: white; }
```

Composition - break the grid:

```css
.feature-image { margin-inline: calc(-1 * clamp(24px, 8vw, 80px)); }

.section-label {
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  position: absolute;
  left: -48px;
  font-size: 0.75rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
}
```

Avoid cyan or purple gradients, glassmorphism, or neon on dark. Avoid turning every refine request into a hero treatment.

---

## Quiet (reduce intensity)

Use when colors feel aggressive, motion is distracting, or the design is overwhelming.

1. Saturation: reduce chroma in OKLCH. Don't just add white.
2. Contrast: step down heading weights, for example `900 -> 700`, `700 -> 500`.
3. Motion: reduce distances and shorten durations.
4. Color count: consolidate to fewer hues. Three shades of one color beats six different ones.
5. Whitespace: increase it. If you can't remove elements, separate them more.

Quieting often means deleting a surface, border, or shadow, not just desaturating it.

---

## Clarify (UX copy)

1. Errors: what happened and what to do next. Never "Something went wrong."
2. Buttons and CTAs: action verbs naming the result. "Save changes" not "Submit".
3. Form labels: visible above the field. Placeholder text disappears on type.
4. Empty states: what's empty, why, what to do. Never just an icon with no text.
5. Tone: active voice, second person. No humor on error states; empathize.
6. Loading states: describe what's actually happening. "Saving your project" not "Loading".

---

## Onboard (first-run experience)

1. Empty state anatomy: what is missing, why it matters, how to fix it, and a visual that isn't a generic illustration.
2. Progressive disclosure: don't show all features at once. Show the next most important thing.
3. Celebration: when the user completes their first meaningful action, acknowledge it. Brief, specific, sincere.
4. Tooltips: triggered by interaction, not auto-playing. Dismissible. Short.

---

## Delight (add joy)

Use sparingly. Joy moments should surprise without blocking.

1. Micro-interactions: button press -> `scale(0.95)`, release with ease-out. Hover -> `scale(1.02-1.05)`.
2. Copy personality: loading messages and empty state captions should be product-specific and warm, not AI cliches.
3. Celebration moments: brief confetti, checkmark animation, or color flash on first completion.
4. All delight moments must complete in under 1 second, be skippable, and respect `prefers-reduced-motion`.

---

## Polish (final pass)

Run at the end of any refine session:

- [ ] All elements align to a consistent grid.
- [ ] Spacing between sibling elements is consistent.
- [ ] No orphaned words at end of headings (`text-balance`).
- [ ] Focus states are visible and styled.
- [ ] All interactive elements have hover + active states.
- [ ] Color contrast: body >= 4.5:1, large text >= 3:1.
- [ ] Touch targets >= 44x44px on mobile.
- [ ] Numbers in tables use `tabular-nums`.
- [ ] Animations pause when `prefers-reduced-motion: reduce`.
- [ ] No stray inline styles remain unless they are genuinely runtime-dynamic or email-specific.
- [ ] Cards do not combine background + border + shadow without a hierarchy reason.
- [ ] The changes improve hierarchy or clarity, not just "make it prettier".

---

## Icons (upgrade icon set)

When icons look generic, mismatched, or are clearly Lucide or Feather defaults with no intentional choice.

1 - Scan what's in use: grep for `import.*lucide`, `import.*heroicons`, or check `scan_project_icons` via MCP.

2 - Pick one library:

| Library | Prefix | Character |
|---------|--------|-----------|
| Phosphor | `ph` | Weight system (thin -> duotone), most flexible |
| Solar | `solar` | Modern, high-quality, bold variants |
| Tabler | `tabler` | Crisp, clean, extensive |
| Heroicons | `heroicons` | Minimal, Tailwind-aligned |

Never mix libraries in the same project.

3 - Search and replace:

```bash
better-icons search "settings" --prefix ph --limit 8
better-icons get ph:gear-six --color currentColor
better-icons search "navigation" --prefix ph -d ./src/icons
```

4 - Consistency: always `currentColor`, consistent default size (20px or 24px).

## Style Exit Checklist

- [ ] Typography, color, or icon decisions are visibly more intentional than before
- [ ] Surface language is simpler or more coherent, not busier
- [ ] Inline styles introduced by previous code were removed where this pass touched the component
- [ ] The result still reads as refinement of the same UI, not a redesign in disguise
