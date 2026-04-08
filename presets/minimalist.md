# Preset: Minimalist

Warm monochrome editorial style. Synthesizes: `minimalist-ui`, `stitch-design-taste` (minimal config).

Apply this preset on top of any cluster. It constrains the aesthetic layer — the cluster still handles workflow.

---

## Color System

```css
:root {
  /* Warm monochrome base */
  --bg:        oklch(98%  0.008 60);   /* barely warm off-white */
  --surface:   oklch(96%  0.006 60);   /* cards, panels */
  --border:    oklch(88%  0.008 60);   /* dividers */
  --text:      oklch(18%  0.010 60);   /* primary text */
  --text-muted:oklch(52%  0.010 60);   /* secondary, captions */

  /* Single accent — amber or slate, pick one */
  --accent:    oklch(62%  0.14  50);   /* warm amber */
  /* --accent: oklch(42%  0.06 240);  /* slate option */
}
```

Rules:
- Maximum 2 non-neutral hues in any view.
- Accent appears only at interactive elements, key data, and calls-to-action.
- No gradients. No tinted shadows. Shadows at most: `0 1px 3px oklch(0% 0 0 / 0.08)`.
- Background tint: the page background is warm, not pure white.

---

## Typography

**Primary font**: a geometric or humanist sans with visible character. Options: `Geist`, `Satoshi`, `Plus Jakarta Sans`, `DM Sans`. Avoid `Inter`.

**Display/heading font**: same family (weight variation) or a matching serif for contrast: `Fraunces`, `Lora`, `Playfair Display`.

```css
--font-body:    'Geist', 'Satoshi', sans-serif;
--font-display: 'Fraunces', serif;   /* optional — for editorial feel */

--text-xs:   0.75rem;   /* 12px — labels, captions */
--text-sm:   0.875rem;  /* 14px — secondary content */
--text-base: 1rem;      /* 16px — body */
--text-lg:   1.125rem;  /* 18px — emphasized body */
--text-xl:   1.25rem;   /* 20px — small headings */
--text-2xl:  1.5rem;    /* 24px */
--text-3xl:  1.875rem;  /* 30px */
--text-4xl:  2.25rem;   /* 36px */
--text-5xl:  3rem;      /* 48px — hero */

/* Hierarchy through weight, not just size */
h1 { font-size: var(--text-4xl); font-weight: 600; line-height: 1.15; }
h2 { font-size: var(--text-2xl); font-weight: 500; line-height: 1.25; }
h3 { font-size: var(--text-xl);  font-weight: 500; }
p  { font-size: var(--text-base); line-height: 1.65; max-width: 65ch; }
```

---

## Layout

- **Generous whitespace**: section padding 80–120px vertical on desktop.
- **Tight grouping**: related elements 8–16px apart, sections 64–96px apart.
- **Max content width**: 680px for prose. 960px for UI. 1200px for data-heavy views.
- **Single column for text**: don't break prose into multiple columns.
- **Grid sparingly**: use for portfolios, galleries, card grids. Minimum 280px column.
- **No decoration**: borders only at structural boundaries. No rounded pill badges unless they carry semantic meaning.

---

## Motion

Minimal, purposeful, near-invisible:

- Entrance: opacity fade only. `200ms ease-out`. No translate. No scale.
- Hover: `opacity: 0.7` or subtle color shift. No scale transforms.
- Transitions: `150ms` max. `ease-out` only.
- No looping animations. No scroll-triggered reveals unless the content truly warrants them.
- Silence is the default.

---

## Component Style

```css
/* Card — flat, no decoration */
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 4px;   /* minimal rounding */
  padding: 24px;
}

/* Button — outline as primary affordance */
.btn-primary {
  background: var(--text);
  color: var(--bg);
  border: none;
  padding: 10px 20px;
  font-weight: 500;
  border-radius: 4px;
  transition: opacity 120ms ease-out;
}
.btn-primary:hover { opacity: 0.8; }

/* Link — underline as affordance, no color change */
a { text-decoration: underline; text-underline-offset: 3px; color: inherit; }
a:hover { opacity: 0.65; }
```
