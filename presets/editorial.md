# Preset: Editorial

High-end, typographically driven, magazine-quality design. Synthesizes: `high-end-visual-design`, `design-taste-frontend`, `stitch-design-taste` (editorial config).

Apply this preset on top of any cluster. It constrains the aesthetic layer — the cluster still handles workflow.

---

## Parameters (adjust per project)

| Parameter | Default | Range | Effect |
|-----------|---------|-------|--------|
| `Variance` | 8/10 | 1–10 | How distinctive/unexpected the output is |
| `Motion` | 6/10 | 1–10 | Intensity of animation and interaction |
| `Density` | 4/10 | 1–10 | Information density (4 = editorial spacing) |

---

## Color System

### Option A: Warm Editorial
```css
:root {
  --bg:         oklch(97%  0.015 60);   /* warm cream */
  --surface:    oklch(94%  0.012 60);
  --text:       oklch(15%  0.015 60);   /* warm near-black */
  --text-muted: oklch(48%  0.015 60);
  --accent:     oklch(52%  0.20  30);   /* terracotta / rust */
  --accent-2:   oklch(68%  0.12  85);   /* amber, used sparingly */
}
```

### Option B: Dark Luxury
```css
:root {
  --bg:         oklch(10%  0.012 270);  /* deep cool dark */
  --surface:    oklch(15%  0.010 270);
  --text:       oklch(94%  0.010 60);   /* warm off-white */
  --text-muted: oklch(60%  0.008 60);
  --accent:     oklch(78%  0.15  85);   /* gold/amber */
  --accent-2:   oklch(65%  0.18  160);  /* emerald, for success states */
}
```

### Option C: Swiss Modernist
```css
:root {
  --bg:         oklch(99%  0.004 100);  /* near-white, slightly warm */
  --surface:    oklch(96%  0.004 100);
  --text:       oklch(12%  0.008 100);  /* near-black */
  --text-muted: oklch(50%  0.008 100);
  --accent:     oklch(50%  0.22  30);   /* signal red */
}
```

**Rules for all options**:
- No purple or blue-to-purple gradients.
- No neon on dark backgrounds.
- No multi-color gradient text.
- Color ratio: 60% dominant / 30% secondary / 10% accent.

---

## Typography

Display and body should create genuine contrast — not just size difference.

**Pairing A (organic/editorial)**: `Fraunces` (display, variable) + `Geist` (body)
**Pairing B (geometric)**: `Archivo Black` (headings) + `DM Sans` (body)
**Pairing C (luxury)**: `Cormorant Garamond` (display) + `Libre Baskerville` (body)
**Pairing D (modernist)**: `Neue Haas Grotesk` or `Aktiv Grotesk` (all) — weight-only hierarchy

```css
--font-display: 'Fraunces', 'Cormorant Garamond', serif;
--font-body: 'Geist', 'DM Sans', sans-serif;

/* Editorial scale — more dramatic than default */
--text-xs:    0.6875rem;  /* 11px */
--text-sm:    0.8125rem;  /* 13px */
--text-base:  1rem;
--text-lg:    1.1875rem;  /* 19px */
--text-xl:    1.5rem;     /* 24px */
--text-2xl:   2rem;       /* 32px */
--text-3xl:   2.75rem;    /* 44px */
--text-4xl:   3.75rem;    /* 60px */
--text-5xl:   5rem;       /* 80px — hero, large displays only */
--text-6xl:   7rem;       /* 112px — editorial statement */
```

Rules:
- Size contrast between adjacent hierarchy levels: minimum 1.4×.
- Display headings: `font-weight: 300` or `900` — not the safe middle.
- Use variable fonts when available — `font-variation-settings` for fine-tuned weight.
- No `letter-spacing` modification on body text. Display: subtle negative tracking at large sizes.

---

## Layout

Editorial layout creates drama through contrast and asymmetry:

```css
/* Column grid — expose the structure */
.layout {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
  max-width: 1280px;
  margin-inline: auto;
  padding-inline: clamp(24px, 5vw, 80px);
}

/* Content doesn't fill all 12 columns — intentional offset */
.hero-headline { grid-column: 1 / 9; }
.hero-aside    { grid-column: 10 / 13; align-self: end; }

/* Section rhythm */
.section { padding-block: clamp(64px, 10vw, 160px); }
```

Rules:
- Not everything spans full width. Use offset and asymmetry to create hierarchy.
- Use the grid's gutter as a design element — some elements bleed into it.
- Full-bleed images and color blocks should be intentional punctuation.
- Text: max-width `65ch` for prose, `48ch` for captions.

---

## Motion (Motion: 6/10)

More expressive than minimalist, still purposeful:

```css
--ease-reveal: cubic-bezier(0.16, 1, 0.3, 1);    /* expo out */
--ease-spring: cubic-bezier(0.34, 1.2, 0.64, 1); /* very gentle overshoot */
```

- Entrance: `translate(0, 20px) → translate(0, 0)` + opacity, `500ms ease-reveal`.
- Scroll reveals: `IntersectionObserver` at 15% threshold.
- Hover on cards: `scale(1.01)` + subtle shadow increase, `250ms ease-reveal`.
- Image parallax: 0.1–0.15 multiplier.
- Page transitions: View Transitions API when supported.
- Spring physics: allowed on isolated delight moments. `stiffness: 100, damping: 20`.

---

## High-End Details

1. **Dual-bezier shadow architecture**: base shadow for depth + ambient shadow for softness.
   ```css
   box-shadow:
     0 1px 2px oklch(0% 0 0 / 0.04),    /* ambient */
     0 4px 16px oklch(0% 0 0 / 0.08);   /* depth */
   ```

2. **Optical adjustments**: visually center content that mathematical centering makes feel off.

3. **Image treatment**: `object-position` fine-tuning for correct crop; `filter: contrast(1.05) saturate(0.95)`.

4. **Micro-typography**: `text-rendering: optimizeLegibility`, `font-kerning: auto`, `-webkit-font-smoothing: antialiased`.

5. **Dividers**: use ruled lines (`border-bottom: 1px solid var(--border)`) with asymmetric padding — heavy above, light below — not equal space on both sides.
