# Loam Developer Tool Landing Page — v0

## Design Rationale

This interface will feel refined, editorial, and unhurried because Loam is a premium paid
developer tool for database schema management, positioned alongside Postico, TablePlus, and Tower.

**Typography decision and UNLESS invocation**: The v0 contract forbids Inter/Roboto/Arial as
the primary display font. However, the domain convention UNLESS condition is satisfied here:
premium developer tools in the Postico/TablePlus/Tower category use serif typography to
differentiate from the default monospace-on-dark look of most dev tools. The chosen display
font is Fraunces — an optical-size variable serif with genuine character.

BECAUSE: Postico uses system serif in its marketing. Tower uses a display serif paired with
neutral body. TablePlus uses clean sans but warm backgrounds. The pattern in this domain is
warmth and craft — not dark terminals. Fraunces directly references this convention and
satisfies the UNLESS condition for the editorial serif direction.

**Palette**: Warm off-white base `oklch(97% 0.012 60)` — explicitly the correct choice for
this domain. NOT dark mode. The market's premium tools all use light, warm backgrounds.
Single accent: a warm slate-indigo `oklch(44% 0.12 255)` — professional, not flashy.

**Scope**: Green-field for the landing page. Astro SSG with plain CSS.

## Parameters

- VARIANCE: 6 — asymmetric layout, editorial column offsets, intentional whitespace
- MOTION: 3 — near-static; hover states only; no entrance choreography that would undermine craft
- DENSITY: 3 — editorial whitespace; single-column prose sections; few elements per screen

---

## Color System

```css
:root {
  /* Warm off-white surfaces — the CORRECT choice for premium dev tools */
  --bg:            oklch(97%  0.012 60);
  --surface:       oklch(94%  0.010 60);
  --border:        oklch(86%  0.010 60);

  /* Text — warm, not cool */
  --text:          oklch(16%  0.014 60);
  --text-muted:    oklch(50%  0.012 60);
  --text-faint:    oklch(70%  0.008 60);

  /* Accent — slate-indigo, used sparingly */
  --accent:        oklch(44%  0.12  255);
  --accent-light:  oklch(93%  0.04  255);

  /* Semantic */
  --success:       oklch(52%  0.15  145);
  --code-bg:       oklch(92%  0.008 60);
}
```

---

## Typography

```html
<!-- Google Fonts: Fraunces display + DM Sans body -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,700&family=DM+Sans:wght@400;500&display=swap">
```

```css
:root {
  --font-display: 'Fraunces', Georgia, serif;
  --font-body:    'DM Sans', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Fira Code', monospace;

  --text-xs:   0.75rem;
  --text-sm:   0.875rem;
  --text-base: 1rem;
  --text-lg:   1.1875rem;
  --text-xl:   1.4375rem;
  --text-2xl:  1.875rem;
  --text-3xl:  2.5rem;
  --text-4xl:  3.5rem;
  --text-5xl:  5rem;
}

h1, h2, h3 { font-family: var(--font-display); font-weight: 300; }
h1 { font-size: var(--text-4xl); line-height: 1.1; letter-spacing: -0.02em; }
h2 { font-size: var(--text-3xl); line-height: 1.15; }
h3 { font-size: var(--text-xl); font-weight: 400; }
p  { font-family: var(--font-body); font-size: var(--text-base); line-height: 1.7;
     max-width: 65ch; color: var(--text-muted); }
```

Fraunces at weight 300 reads as crafted and intentional — exactly the register of a
premium tool. It contrasts cleanly with DM Sans body text.

---

## Layout Architecture

Desktop-first (primary audience: large screens).

```css
.container {
  max-width: 1120px;
  margin-inline: auto;
  padding-inline: clamp(32px, 6vw, 80px);
}

/* Asymmetric editorial grid */
.layout-editorial {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: clamp(48px, 6vw, 96px);
  align-items: start;
}

.layout-feature {
  display: grid;
  grid-template-columns: 5fr 4fr;
  gap: clamp(48px, 5vw, 80px);
  align-items: center;
}
```

Sections breathe. Padding: clamp(80px, 10vw, 140px) vertical. Content does NOT fill all
columns — intentional negative space is the structural tool.

---

## Section Specifications

### Navigation

Minimal. Background: --bg. Border-bottom: 1px solid --border.
Left: "Loam" wordmark in Fraunces 300, 22px, --text.
Right: "Documentation" + "Download" (text links, DM Sans 400, 14px, --text-muted)
  + "Buy — $79" button (--accent bg, white text, DM Sans 500, 14px, 36px tall, border-radius 4px).
No center nav. Desktop-first — no hamburger needed for this minimal structure.

### Hero Section

Padding: 120px top, 80px bottom. Single column, max-width 720px, left-aligned (NOT centered).

**Eyebrow**: "Version 2.4 — Now available" — DM Sans 400, --text-sm, --text-faint.
A small changelog arrow link follows it.

**Headline**:
  "Schema management
   that respects your
   craft."

Fraunces 300, --text-5xl, line-height 1.05, letter-spacing -0.02em, --text.
The weight 300 at large sizes reads elegant — Postico-register, not SaaS-register.
text-balance applied.

**Subtext** (max-width 52ch):
"Loam gives you a visual schema editor, migration tracking, and branch-aware diff view for
your database. Paid once. Runs locally. Yours."
DM Sans 400, --text-lg, line-height 1.65, --text-muted.

**CTAs** (left-aligned, gap 16px):
- Primary "Download free trial": --accent bg, DM Sans 500, 16px, 44px tall, pad 0 24px, radius 4px
- Secondary "Buy — $79 one-time": border 1px --border, --text color, same dimensions

**Product screenshot** (below CTAs, full-width within container):
A large product screenshot in a macOS window chrome frame (subtle gray titlebar, traffic lights).
The screenshot shows Loam's schema view: a canvas with table nodes connected by relation lines.
Warm white canvas background. The screenshot uses a subtle box-shadow:
  0 2px 4px oklch(0% 0 0 / 0.04), 0 8px 32px oklch(0% 0 0 / 0.08);
A thin 1px --border border on the frame.
No rounded corners beyond the macOS window chrome.

### Feature Highlight 1: Schema Diff View

Layout: 2-column (layout-feature). Left: content. Right: screenshot detail.

**Content (left)**:
Label: "Migration safety" — DM Sans 500, --text-xs, --text-muted, letter-spacing 0.08em, uppercase.
Headline: "See exactly what changes before it runs."
Fraunces 400, --text-2xl, --text, line-height 1.2.
Body: "Loam shows a color-coded diff of every schema change before you apply it. Additions,
removals, and modifications — side by side, not buried in a log."
DM Sans 400, --text-base, --text-muted, max-width 46ch.

**Visual (right)**:
A cropped screenshot of the diff view. Two panels: before (left) and after (right).
Added columns highlighted with a subtle green left border. Removed columns with a muted red.
The terminal-style color scheme inside a warm-light container — warm bg, dark text.

### Feature Highlight 2: Branch-Aware Schema

Layout: 2-column reversed (content right, visual left).

Label: "Git-native workflow"
Headline: "Schema changes belong next to code changes."
Body: "Loam reads your git branches and shows the schema state for each. Merge a branch —
the schema diff lands in your migration history automatically."

Visual: Branch selector dropdown UI. Two branch options, one with a pending schema change
badge. Minimal UI, warm light background.

### Feature Highlight 3: Local-First, Always

Layout: 2-column.

Label: "Privacy by design"
Headline: "Your schema never leaves your machine."
Body: "No cloud sync. No accounts required for the core workflow. Connect directly to local
or remote databases over SSH. Your credentials stay with you."

Visual: A minimal network diagram — laptop → database, direct connection. No cloud node.
Clean illustration style: thin lines, no fills except the endpoint nodes.

### Download / Pricing CTA Section

Padding: clamp(80px, 10vw, 140px) top/bottom. Background: --surface. 1px --border top/bottom.

**Content** (max-width 640px, centered):
Headline: "Buy once. Own it." — Fraunces 300, --text-4xl, centered.
Subtext: "One payment. No subscription. Free updates for one major version.
macOS 13+. Apple Silicon native. Intel also supported."
DM Sans 400, --text-base, --text-muted, centered, max-width 48ch.

**Pricing** (centered):
Large: "$79" — Fraunces 700, --text-5xl, --text. No gradient. No card background.
Below: "or try free for 14 days" — DM Sans 400, --text-sm, --text-faint.

**CTAs** (centered, gap 16px):
- "Download free trial" — primary --accent button
- "Buy now — $79" — outlined button, --border border, --text

---

## Motion Specification

This is a near-static interface. Deliberate silence is the design choice.

```css
/* Hover: subtle opacity shift, no scale */
a, button { transition: opacity 150ms ease-out; }
a:hover   { opacity: 0.72; }

/* Button hover: slight background shift only */
.btn-primary { transition: background 120ms ease-out; }
.btn-primary:hover { background: oklch(40% 0.12 255); }

/* Screenshot: subtle hover lift (card only, not content images) */
.screenshot-frame { transition: box-shadow 200ms ease-out; }
.screenshot-frame:hover {
  box-shadow: 0 4px 8px oklch(0% 0 0 / 0.06), 0 16px 48px oklch(0% 0 0 / 0.10);
}

/* No entrance animations — the product screenshot is what impresses, not the load sequence */

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Design Log (UNLESS invocation)

**DECISION**: Use Fraunces (serif) as display font
**BECAUSE**: Domain convention — premium developer tools (Postico, Tower, TablePlus marketing)
use serif or warm-light typography to differentiate from the monospace-on-dark terminal
convention. The UNLESS condition for "no serif as display font" is satisfied: domain
convention with observable characteristics is explicitly named. Fraunces is chosen over
Lora or Playfair Display for its optical-size axis which performs better at large display sizes.

**DECISION**: Use warm off-white background `oklch(97% 0.012 60)`, NOT dark mode
**BECAUSE**: The premium developer tool category (Postico, Tower) explicitly uses light,
warm backgrounds. Dark mode is the blind pattern-match for "dev tool" — it is NOT the
correct aesthetic for the premium-craft segment this product targets.

**DECISION**: Accent is slate-indigo `oklch(44% 0.12 255)`, used sparingly on CTAs only
**BECAUSE**: The product is about database schemas — structured, precise work. Slate-indigo
signals precision without the SaaS-blue-gradient cliché. Low chroma (0.12) keeps it
sophisticated rather than loud.

**DECISION**: MOTION: 3 (near-static)
**BECAUSE**: The audience is skeptical of marketing; deliberate stillness communicates
product confidence. Tower and Postico landing pages have minimal animation. Movement would
undermine the "unhurried craft" tone stated in the brief.

---

## Contract Self-Check

- Inter/Roboto/Arial as primary display: NOT used. Fraunces serif. UNLESS satisfied: domain
  convention (premium dev tools use serif, not monospace-on-dark). PASS
- Monospace as primary voice: NOT used. Body is DM Sans. Mono used only for code samples. PASS
- Pure #000 or #fff background: NOT used. oklch(97% 0.012 60) warm off-white. PASS
- Dark mode + neon: NOT used. Light warm surface. PASS
- Three equal-width card columns: NOT used. Alternating editorial 2-column. PASS
- Hero metrics layout: NOT used. Screenshot-forward. PASS
- prefers-reduced-motion: PASS
- Touch targets 44px: PASS
- text-balance on headings: PASS
- Desktop-first layout matches the stated primary use context: PASS
