#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LEGACY FIXTURE WRITER.

Deprecated after the rubric-first eval migration.
Do not use for current generation runs.
"""

import os

BASE = 'E:/code/work/presto-design-skill/experiments/eval/results'

def write_result(variant, case, content):
    path = f'{BASE}/{variant}/{case}/run-01.md'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written {path} ({len(content)} chars)')


# ============================================================
# V0 OUTPUTS (master branch — baseline)
# ============================================================

V0_CREATE_SAAS = """# SignalForge SaaS Landing Page Design — v0

## Design Rationale

This interface will feel sharp and operationally confident because SignalForge is for
engineering managers and CTOs doing incident triage at speed.

**Typography**: Cabinet Grotesk 800 for display communicates precision authority without
Inter's corporate blandness. Geist handles body — readable, no-fuss. Weight contrast
(800 display vs 400 body) creates hierarchy without relying on size alone.

**Palette**: Warm off-black base `oklch(10% 0.012 240)` with amber accent
`oklch(65% 0.19 55)`. Amber reads as urgency-without-panic — appropriate for incident
tooling. No cyan, no purple-to-blue gradient. Light sections use warm cream
`oklch(97% 0.010 60)`. All surfaces OKLCH-tinted — no pure black or white.

**Scope**: Green-field design — full system establishment appropriate.

## Parameters

- VARIANCE: 7 — left-anchored hero, alternating feature layouts, deliberate asymmetry
- MOTION: 5 — entrance animations + hover micro-interactions; no scroll theatrics
- DENSITY: 5 — balanced; enough information to evaluate without overwhelming

---

## Color System

```css
:root {
  --bg:            oklch(10%  0.012 240);
  --surface:       oklch(14%  0.010 240);
  --surface-2:     oklch(18%  0.008 240);
  --border:        oklch(28%  0.008 240);
  --bg-light:      oklch(97%  0.010 60);
  --surface-light: oklch(94%  0.008 60);
  --text:          oklch(95%  0.008 60);
  --text-muted:    oklch(62%  0.008 240);
  --text-on-light: oklch(12%  0.012 60);
  --accent:        oklch(65%  0.19  55);
  --accent-hover:  oklch(70%  0.19  55);
  --accent-dim:    oklch(65%  0.19  55 / 0.15);
  --success:       oklch(64%  0.17  145);
  --error:         oklch(58%  0.21  25);
  --warning:       oklch(72%  0.17  75);
}
```

Reasoning: Amber accent differentiates from the blue/teal/cyan AI-tool default palette.
Warm neutrals (hue 60) for light sections, cool neutrals (hue 240) for dark — prevents
the mixed-gray-temperature problem. 60/30/10 ratio: dark surface dominates, amber appears
only on CTAs and data highlights.

---

## Typography

```css
/* Google Fonts — display=swap on both */
/* https://fonts.googleapis.com/css2?family=Cabinet+Grotesk:wght@400;500;700;800&display=swap */
/* https://fonts.googleapis.com/css2?family=Geist:wght@400;500&display=swap              */

:root {
  --font-display: 'Cabinet Grotesk', sans-serif;
  --font-body:    'Geist', 'DM Sans', sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  --text-xs:   clamp(0.6875rem, 0.6rem + 0.2vw, 0.75rem);
  --text-sm:   clamp(0.8125rem, 0.78rem + 0.2vw, 0.875rem);
  --text-base: clamp(1rem, 0.96rem + 0.25vw, 1.0625rem);
  --text-lg:   clamp(1.125rem, 1.07rem + 0.3vw, 1.25rem);
  --text-xl:   clamp(1.25rem, 1.15rem + 0.5vw, 1.5rem);
  --text-2xl:  clamp(1.5rem, 1.3rem + 1vw, 2rem);
  --text-3xl:  clamp(2rem, 1.6rem + 2vw, 3rem);
  --text-4xl:  clamp(2.75rem, 2rem + 3.5vw, 4.5rem);
  --text-5xl:  clamp(3.5rem, 2.5rem + 5vw, 6rem);
}
```

---

## Layout Architecture

```css
.container {
  max-width: min(100% - clamp(32px, 8vw, 128px), 1280px);
  margin-inline: auto;
}
.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: clamp(16px, 2vw, 24px);
}
```

Key decisions: Hero left-anchored (content cols 1-7, visual 8-12, NOT centered). Features
alternate left/right — never three equal columns. Pricing is a 2-column asymmetric layout,
not a card grid. Dark/light section alternation creates pacing.

---

## Section-by-Section Specifications

### Navigation

Sticky, backdrop-blur(16px) on scroll. Left: wordmark (Cabinet Grotesk 700, 18px, --text).
Center: Products / Docs / Pricing / Blog (Geist 400, 14px, --text-muted, hover --text 150ms).
Right: "Sign in" text link + "Start free trial" amber button (40px tall, pad 0 20px).
Mobile: hamburger (44x44px) triggers full-height right drawer, 48px link targets.

### Hero Section

Padding: clamp(80px, 12vw, 140px) top, clamp(64px, 8vw, 100px) bottom. Background --bg.

**Eyebrow** (above headline): "OBSERVABILITY / INCIDENT INTELLIGENCE"
Uppercase, --text-xs, --text-muted, letter-spacing 0.12em.
A 1px --border line extends rightward from the label to column-6 edge at vertical center.

**Headline** (columns 1-8):
  "From alert
   to resolution,
   before it spreads."
Cabinet Grotesk 800, --text-5xl, line-height 1.0, letter-spacing -0.03em, --text.
Each line break is an intentional compositional decision. text-balance applied.

**Supporting copy** (columns 1-6, max-width 52ch):
"SignalForge correlates your logs, traces, and anomaly signals into one incident timeline.
Engineering teams resolve 40% faster — without an observability PhD."
Geist 400, --text-lg, line-height 1.6, --text-muted.

**CTAs** (flush left below copy):
- Primary "Start free trial": --accent bg, --text color, Cabinet Grotesk 700, 16px, 48px tall,
  padding 0 28px, border-radius 6px. Hover: --accent-hover bg. Active: scale(0.97).
- Secondary "See it in action →": text only, Geist 500, hover underline offset 4px.
- Trust micro-signal: "No credit card · 5-minute setup · SOC 2 Type II" — --text-xs, --text-muted.

**Product visualization** (columns 7-12, vertically centered):
Mock incident timeline panel. --surface-2 background, 1px --border, border-radius 8px, no shadow.
Contents:
- Header: SignalForge micro-logo + "INCIDENT-0042" label + timestamp (JetBrains Mono, --text-xs)
- Log volume bar chart: 24 bars over 24h, amber spike cluster at incident window
- Two trace entries with latency delta badges highlighted in --warning color
- Resolution badge in --success with checkmark
- Thin amber vertical line marks anomaly start time across all rows
Panel extends 40px below section bottom edge — suggests depth, implies the product continues.

### Trust Bar

Full-width band, --bg-light, 32px padding top/bottom.
"Trusted by engineering teams at" left label (Geist 400, 13px, --text-muted on --bg-light).
Six company SVG logotypes — monochrome, --text-on-light at 35% opacity, 70% on hover,
150ms ease-out transition. gap: clamp(32px, 5vw, 64px). NOT cards, NOT equal-width columns.

### Feature Sections (4 alternating)

Layout: 12-column grid. Content: 5 of 12 cols. Visual: 6 of 12 cols, offset 1 col gap.
Alternation: F1 dark/content-left, F2 light/content-right, F3 dark/content-left, F4 light/content-right.

**Feature 1 (dark): "One timeline. Every signal."**
Eyebrow: UNIFIED TIMELINE. Headline: Cabinet Grotesk 700, --text-3xl.
Body: "Your logs, distributed traces, and anomaly detections land in a single ordered view.
No tab-switching. No copy-pasting log lines into Slack." Geist 400, --text-base, max 52ch.
Visual: Annotated timeline component. Log events (small dots), trace spans (horizontal bars),
anomaly markers (amber triangles) on shared time axis. Green bracket marks resolution window.

**Feature 2 (light): "Detects what you didn't know to watch."**
Eyebrow: ANOMALY DETECTION.
Body: "SignalForge learns your service baseline automatically. New service? New baseline within 24 hours."
Visual: Sparkline chart with shaded baseline envelope. Anomaly point circled in amber.
Two stat badges: "Detected in 4m 12s" | "Resolution time 18m 40s"

**Feature 3 (dark): "Alerts that know your schedule."**
Eyebrow: ON-CALL ROUTING.
Body: "Route incidents to the right engineer, not just any engineer. Escalation policies that follow
how your team actually works."
Visual: Mock on-call schedule grid — 7-day horizontal, team rows vertical.
Monochrome except amber highlight on active responder cell. Small routing arrow shows alert path.

**Feature 4 (light): "Correlate. Don't just aggregate."**
Eyebrow: ROOT CAUSE ANALYSIS.
Body: "When a payment service spikes, SignalForge traces it back to the database query that started it."
Visual: Dependency graph, three service nodes. Causal path (2 of 3 edges) highlighted in amber.
Root-cause node: 2px amber border, label "Root cause identified."

### Workflow / Product Story Section

Background: --bg. Padding: clamp(80px, 12vw, 160px).
Section label "HOW IT WORKS" — rotated -90deg, absolute left, --text-xs, letter-spacing 0.15em, --text-muted.

Desktop: 4 steps in horizontal row, connected by ruled line + arrowhead.
Mobile: vertical stack with connecting vertical line.

Step anatomy: Number (Cabinet Grotesk 800, 48px, --accent) + Title (Cabinet Grotesk 700, --text-xl)
+ Body (Geist 400, --text-base, --text-muted, max 40ch, 2 sentences max).

Steps:
1. Alert arrives — "An anomaly in your API latency triggers via your existing PagerDuty or OpsGenie."
2. Timeline builds — "SignalForge correlates the last 15 minutes of logs and traces, chronologically."
3. Root cause surfaced — "The causal chain is rendered: deployment > latency spike > downstream failures."
4. Resolved — "Mark the incident resolved. The timeline archives with full replay for postmortem."

### Pricing Teaser

Background: --bg-light. Layout: 2-column asymmetric (left 5/12, right 7/12). NOT a card grid.

Left: "Simple plans. No observability tax." (Cabinet Grotesk 700, --text-3xl).
Body: "Start free. Scale when your team does. No per-seat pricing on the data you send."
Link: "See full pricing →" in --accent.

Right (horizontal-rule table, NOT cards):
| Plan     | Data/mo  | Retention | Price     |
|----------|----------|-----------|-----------|
| Starter  | 10 GB    | 7 days    | Free      |
| Team     | 100 GB   | 30 days   | $149/mo   |
| Growth   | 1 TB     | 90 days   | $499/mo   |

Team row: 2px left border --accent, Cabinet Grotesk 500 weight throughout. No gradient bg. No badge.
Footnote: "Custom plan available for > 5 TB/mo. Talk to us." --text-xs, --text-muted.

### Final CTA Section

Background: --bg. Padding: 160px top, 120px bottom. Content centered, max-width 720px.

Headline: "Start resolving incidents faster this week."
Cabinet Grotesk 800, --text-4xl, line-height 1.05, centered, text-balance applied.

Subtext: "Free trial. No credit card. Your logs stay yours."
Geist 400, --text-lg, --text-muted, centered, max-width 44ch.

CTAs (centered row, gap 16px): Primary amber filled + secondary ghost "Schedule a demo."

Background accent: Radial gradient from --accent-dim at 20% opacity, 300px radius centered behind
headline. Warm focal warmth — not a neon glow.

---

## Responsive Behavior

**Mobile < 768px**: Single column. Headline drops to --text-3xl. Product visual below CTAs,
full-width, 280px tall. Features: content above, visual below, both full-width. Workflow: vertical
steps. Pricing: stacked with left accent border on Team. Buttons stack vertically, 48px touch targets.

**Tablet 768-1024px**: 2-column maintained for hero and features. Headline at --text-4xl.

---

## Motion Specification

```css
@keyframes fade-up {
  from { opacity: 0; translate: 0 14px; }
  to   { opacity: 1; translate: 0 0; }
}
.hero-eyebrow  { animation: fade-up 400ms cubic-bezier(0.16, 1, 0.3, 1) both; }
.hero-headline { animation: fade-up 500ms cubic-bezier(0.16, 1, 0.3, 1) 80ms both; }
.hero-copy     { animation: fade-up 500ms cubic-bezier(0.16, 1, 0.3, 1) 160ms both; }
.hero-ctas     { animation: fade-up 400ms cubic-bezier(0.16, 1, 0.3, 1) 240ms both; }
.hero-visual   { animation: fade-up 600ms cubic-bezier(0.16, 1, 0.3, 1) 200ms both; }

.btn-primary { transition: background 150ms ease-out, transform 100ms ease-out; }
.btn-primary:hover  { background: var(--accent-hover); }
.btn-primary:active { transform: scale(0.97); }

/* Scroll reveals via IntersectionObserver, threshold 0.15 */
.reveal { opacity: 0; translate: 0 20px;
  transition: opacity 500ms cubic-bezier(0.16, 1, 0.3, 1),
              translate 500ms cubic-bezier(0.16, 1, 0.3, 1); }
.reveal.visible { opacity: 1; translate: 0 0; }

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

---

## Copy Tone Guidance

Avoid: Elevate, Seamless, Next-gen, Game-changer, Delve, Leverage, Unlock.
Use: Direct, operational, specific. Numbers over adjectives.
Good: "Find the problem. Fix it. Move on." / "40% faster resolution." / "Your second-best tool."

---

## Contract Self-Check

- No three-column equal card layout: PASS
- No hero metrics pattern (large number + gradient card): PASS
- No cyan-on-dark, purple gradients, gradient text on headings: PASS
- No pure #000 or #fff — all surfaces OKLCH-tinted: PASS
- Cabinet Grotesk choice defensible (technical authority, engineering audience): PASS
- Amber accent defensible (urgency-without-alarm for incident tooling): PASS
- prefers-reduced-motion covered: PASS
- Touch targets minimum 44px: PASS
- text-balance on multi-line headings: PASS
- No nested cards: PASS
"""

V0_CREATE_DEVTOOL = """# Loam Developer Tool Landing Page — v0

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
"""

V0_CREATE_CONSUMER = """# Dusk Journaling App — Home Screen Design (v0)

## Design Rationale

This interface will feel warm, intimate, and unhurried because Dusk is used by adults at
night as a private ritual — the UI must not produce the alertness or task-completion anxiety
of a productivity app.

**Typography**: Lora (variable serif) for display headings — it reads as handwritten thought
and personal reflection, not corporate task management. DM Sans for body and labels —
readable at small sizes, warm without being cutesy.

**Palette**: Deep warm charcoal surface (not pure black) with soft amber accents. Neither
harsh white nor full darkness — a "lamp on a desk at 11pm" aesthetic. Not dark-mode-as-default
for dev-tool aesthetics — dark because night, warm because comfort.

**Tailwind**: v3 with tailwind.config.js theme.extend. Design tokens defined here.
**Framework**: React + Vite, Framer Motion installed.
**Scope**: Home screen (logged-in, 5 previous entries). Token system built as part of task.

## Parameters

- VARIANCE: 5 — moderate; asymmetric entry area but stable structure
- MOTION: 4 — Framer Motion for purposeful transitions only; mood slider animation, entry focus
- DENSITY: 3 — airy, single-column, generous vertical space between sections

---

## Tailwind Token System

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        dusk: {
          bg:         'oklch(14% 0.016 60)',   /* deep warm charcoal */
          surface:    'oklch(18% 0.014 60)',   /* card surfaces */
          surface2:   'oklch(22% 0.012 60)',   /* elevated panels */
          border:     'oklch(30% 0.012 60)',
          text:       'oklch(92% 0.010 60)',   /* warm off-white */
          muted:      'oklch(62% 0.010 60)',
          faint:      'oklch(42% 0.008 60)',
          accent:     'oklch(72% 0.16 70)',    /* soft amber-gold */
          accentDim:  'oklch(72% 0.16 70 / 0.2)',
          positive:   'oklch(66% 0.14 145)',
          negative:   'oklch(60% 0.16 25)',
        }
      },
      fontFamily: {
        display: ['Lora', 'Georgia', 'serif'],
        sans:    ['DM Sans', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        card: '12px',
        pill: '100px',
      },
      spacing: {
        section: 'clamp(32px, 8vw, 64px)',
      }
    }
  }
}
```

---

## Color Philosophy

Warm charcoal, not pure black. The distinction: `oklch(14% 0.016 60)` reads as "warm room
in darkness" rather than "void." The hue 60 (amber-warm neutral) tints all surfaces
consistently toward warmth.

Amber accent `oklch(72% 0.16 70)` — the color of a candle or reading lamp. Used only on:
the mood slider active state, the primary CTA, and current-day highlights.

No neon. No blue-on-dark. No gradient text on headings.

---

## Typography

```html
<!-- Google Fonts -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500&display=swap">
```

Hierarchy:
- Date heading: Lora italic 400, 28px, --dusk-text
- Prompt/greeting: Lora 400, 22px, --dusk-text
- Body / entry area: DM Sans 400, 17px, line-height 1.7, --dusk-text
- Labels / metadata: DM Sans 400, 13px, --dusk-muted
- Day card titles: DM Sans 500, 14px
- Numbers (mood value): DM Sans 500, tabular-nums

---

## Component Architecture

### Home Screen Layout

Single column, 375px primary width. Max-width 480px centered on tablet.
Padding-inline: 20px. No horizontal overflow.

Top-to-bottom structure:
1. App header (date + settings icon) — 64px tall
2. Greeting section — 48px top margin
3. Mood check-in — 32px top margin
4. Journal entry area — 32px top margin
5. Previous entries row — 40px top margin, 24px bottom margin

---

### 1. App Header

```tsx
// Header.tsx
import { format } from 'date-fns';

export function AppHeader() {
  return (
    <header className="flex items-center justify-between px-5 pt-safe-top pb-4 sticky top-0 z-10"
            style={{ background: 'oklch(14% 0.016 60)' }}>
      <div>
        <p className="font-sans text-xs text-dusk-muted tracking-widest uppercase">
          {format(new Date(), 'EEEE')}
        </p>
        <h1 className="font-display text-dusk-text text-lg leading-tight">
          {format(new Date(), 'MMMM d')}
        </h1>
      </div>
      <button
        aria-label="Open settings"
        className="w-11 h-11 flex items-center justify-center rounded-full
                   text-dusk-muted hover:text-dusk-text transition-colors duration-150
                   focus-visible:outline focus-visible:outline-2 focus-visible:outline-dusk-accent
                   focus-visible:outline-offset-2">
        {/* Phosphor ph:gear-six icon — 20px, currentColor */}
        <svg width="20" height="20" viewBox="0 0 256 256" fill="currentColor">
          {/* gear-six path from Phosphor */}
        </svg>
      </button>
    </header>
  );
}
```

### 2. Greeting Section

```tsx
// Greeting.tsx
export function Greeting({ userName }: { userName: string }) {
  const hour = new Date().getHours();
  const phrase = hour >= 21 ? 'Good evening' : hour >= 18 ? 'Good evening' : 'Welcome back';

  return (
    <section className="px-5 mt-12">
      <p className="font-display italic text-dusk-muted text-sm mb-1">{phrase},</p>
      <h2 className="font-display text-dusk-text text-balance"
          style={{ fontSize: 'clamp(1.5rem, 6vw, 2rem)', lineHeight: 1.15 }}>
        How are you feeling tonight?
      </h2>
    </section>
  );
}
```

### 3. Mood Check-in Slider

This is the most important accessibility requirement. Custom slider with ARIA attributes.

```tsx
// MoodSlider.tsx
import { useState, useCallback } from 'react';
import { motion } from 'framer-motion';

const MOODS = [
  { value: 1, emoji: '😔', label: 'Heavy' },
  { value: 2, emoji: '😕', label: 'Low' },
  { value: 3, emoji: '😐', label: 'Neutral' },
  { value: 4, emoji: '🙂', label: 'Good' },
  { value: 5, emoji: '😌', label: 'Peaceful' },
];

export function MoodSlider() {
  const [mood, setMood] = useState(3);
  const current = MOODS[mood - 1];

  const handleKeyDown = useCallback((e: React.KeyboardEvent) => {
    if (e.key === 'ArrowRight' || e.key === 'ArrowUp') {
      setMood(m => Math.min(5, m + 1));
    }
    if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') {
      setMood(m => Math.max(1, m - 1));
    }
  }, []);

  return (
    <section className="px-5 mt-8" aria-label="Mood check-in">
      <p className="font-sans text-xs text-dusk-muted uppercase tracking-wider mb-4">
        Tonight's mood
      </p>

      {/* Emoji display */}
      <div className="flex justify-center mb-4">
        <motion.span
          key={mood}
          initial={{ scale: 0.7, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ type: 'spring', stiffness: 200, damping: 18 }}
          className="text-5xl select-none"
          aria-hidden="true">
          {current.emoji}
        </motion.span>
      </div>

      {/* Accessible slider input */}
      <div className="relative">
        <input
          type="range"
          min={1}
          max={5}
          step={1}
          value={mood}
          onChange={e => setMood(Number(e.target.value))}
          onKeyDown={handleKeyDown}
          aria-label="Mood rating"
          aria-valuemin={1}
          aria-valuemax={5}
          aria-valuenow={mood}
          aria-valuetext={current.label}
          className="w-full appearance-none h-1 rounded-full cursor-pointer
                     focus-visible:outline focus-visible:outline-2
                     focus-visible:outline-offset-4 focus-visible:outline-dusk-accent"
          style={{
            background: `linear-gradient(to right,
              oklch(72% 0.16 70) ${((mood - 1) / 4) * 100}%,
              oklch(30% 0.012 60) ${((mood - 1) / 4) * 100}%)`,
          }}
        />
        {/* Mood labels */}
        <div className="flex justify-between mt-2">
          {MOODS.map(m => (
            <span key={m.value}
                  className={`font-sans text-xs transition-colors duration-150 ${
                    m.value === mood ? 'text-dusk-text' : 'text-dusk-faint'
                  }`}>
              {m.label}
            </span>
          ))}
        </div>
      </div>

      {/* Screen reader announcement */}
      <p className="sr-only" aria-live="polite">
        Mood set to: {current.label}
      </p>
    </section>
  );
}
```

Slider thumb CSS (in global styles):
```css
input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: oklch(72% 0.16 70);
  border: 3px solid oklch(14% 0.016 60);
  box-shadow: 0 0 0 3px oklch(72% 0.16 70 / 0.25);
  cursor: pointer;
  transition: transform 100ms ease-out;
}
input[type="range"]::-webkit-slider-thumb:active {
  transform: scale(1.15);
}
```

### 4. Journal Entry Area

This must feel like a page, not a form field.

```tsx
// JournalEntry.tsx
import { useState, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

export function JournalEntry() {
  const [content, setContent] = useState('');
  const [focused, setFocused] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Auto-grow textarea
  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setContent(e.target.value);
    const el = e.target;
    el.style.height = 'auto';
    el.style.height = `${el.scrollHeight}px`;
  };

  return (
    <section className="px-5 mt-8">
      <AnimatePresence>
        {!focused && content === '' && (
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="font-display italic text-dusk-faint text-base mb-3 select-none pointer-events-none">
            What's on your mind tonight...
          </motion.p>
        )}
      </AnimatePresence>

      <div
        className={`relative rounded-card transition-all duration-300 ${
          focused
            ? 'bg-dusk-surface2'
            : 'bg-transparent'
        }`}>
        <textarea
          ref={textareaRef}
          value={content}
          onChange={handleChange}
          onFocus={() => setFocused(true)}
          onBlur={() => setFocused(false)}
          placeholder=""
          aria-label="Journal entry"
          rows={6}
          className="w-full bg-transparent resize-none font-sans text-dusk-text
                     text-[17px] leading-[1.7] p-5 rounded-card border-none outline-none
                     placeholder-dusk-faint focus:outline-none min-h-[160px]"
          style={{ caretColor: 'oklch(72% 0.16 70)' }}
        />

        {/* Bottom rule — appears on focus, a page-like decoration */}
        <motion.div
          animate={{ opacity: focused ? 1 : 0.3 }}
          transition={{ duration: 0.3 }}
          className="absolute bottom-0 left-5 right-5 h-px bg-dusk-border"
        />
      </div>

      {/* Save button — only visible when content exists */}
      <AnimatePresence>
        {content.length > 10 && (
          <motion.div
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 8 }}
            transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
            className="flex justify-end mt-3">
            <button
              className="font-sans font-medium text-sm px-5 h-10 rounded-pill
                         bg-dusk-accent text-dusk-bg
                         hover:opacity-90 active:scale-95 transition-all duration-150
                         focus-visible:outline focus-visible:outline-2
                         focus-visible:outline-offset-2 focus-visible:outline-dusk-accent">
              Save entry
            </button>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}
```

Key decisions: No border on the textarea (a form-field signal). Subtle background appears only
on focus. A horizontal rule at the bottom mimics a page. Placeholder is italic serif — feels
like a prompt, not a label.

### 5. Previous Entries Row

NOT three equal-width columns. A horizontally scrollable row of day cards with varying sizes.

```tsx
// PreviousEntries.tsx
import { format, parseISO } from 'date-fns';
import { motion } from 'framer-motion';

interface Entry {
  id: string;
  date: string;
  mood: number;
  preview: string;
}

const MOOD_COLORS = {
  1: 'oklch(60% 0.16 25)',   /* --negative-ish */
  2: 'oklch(62% 0.12 40)',
  3: 'oklch(62% 0.08 60)',   /* neutral */
  4: 'oklch(66% 0.14 145)',
  5: 'oklch(72% 0.16 70)',   /* --accent */
};

export function PreviousEntries({ entries }: { entries: Entry[] }) {
  return (
    <section className="mt-10" aria-label="Previous journal entries">
      <div className="px-5 flex items-center justify-between mb-4">
        <h2 className="font-sans text-xs text-dusk-muted uppercase tracking-wider">
          Previous entries
        </h2>
        <button className="font-sans text-xs text-dusk-accent hover:opacity-75 transition-opacity duration-150
                           focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2
                           focus-visible:outline-dusk-accent">
          See all
        </button>
      </div>

      {/* Horizontal scroll — NOT three equal columns */}
      <div className="flex gap-3 px-5 pb-6 overflow-x-auto snap-x snap-mandatory
                      scrollbar-none -webkit-overflow-scrolling-touch">
        {entries.map((entry, i) => (
          <motion.article
            key={entry.id}
            initial={{ opacity: 0, x: 16 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: i * 0.06, duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
            className="flex-shrink-0 snap-start rounded-card bg-dusk-surface p-4
                       border border-dusk-border cursor-pointer
                       hover:bg-dusk-surface2 transition-colors duration-150
                       focus-within:ring-2 focus-within:ring-dusk-accent focus-within:ring-offset-2
                       focus-within:ring-offset-dusk-bg"
            style={{ width: i === 0 ? '180px' : '152px' }}  /* first card slightly wider */
          >
            <button className="w-full text-left focus:outline-none"
                    aria-label={`Entry from ${format(parseISO(entry.date), 'MMMM d')}`}>
              {/* Mood dot */}
              <div className="flex items-center gap-2 mb-3">
                <span className="w-2 h-2 rounded-full flex-shrink-0"
                      style={{ background: MOOD_COLORS[entry.mood as keyof typeof MOOD_COLORS] }}
                      aria-hidden="true" />
                <span className="font-sans text-xs text-dusk-muted tabular-nums">
                  {format(parseISO(entry.date), 'EEE, MMM d')}
                </span>
              </div>
              {/* Entry preview */}
              <p className="font-display italic text-dusk-text text-sm leading-snug line-clamp-3">
                {entry.preview}
              </p>
            </button>
          </motion.article>
        ))}
      </div>
    </section>
  );
}
```

Card sizing decision: NOT equal-width three columns. Variable widths (180px for most recent,
152px for others) within a horizontal scroll container. This breaks the equal-column grid pattern
while remaining easy to scan. The mood dot (not a full badge) is small and semantic — color
communicates valence without being decorative.

---

## Framer Motion Usage

Used only for:
1. Mood emoji swap animation — spring physics for natural feel when value changes
2. Save button entrance/exit — fade + slight translate, only when content threshold met
3. Entry card stagger on mount — subtle, delayed, not theatrical
4. Placeholder text fade — opacity only, 200ms, no translate

NOT used for: page entrance animation (static load is calmer), nav transitions, decorative effects.

```tsx
// Reduced motion support
import { useReducedMotion } from 'framer-motion';

// In any animated component:
const prefersReduced = useReducedMotion();
const transition = prefersReduced
  ? { duration: 0 }
  : { type: 'spring', stiffness: 200, damping: 18 };
```

---

## Accessibility Checklist

- Mood slider: type="range" with aria-label, aria-valuemin/max/now/text, keyboard arrows. PASS
- Keyboard focus: All interactive elements have focus-visible:outline in --dusk-accent. PASS
- Touch targets: Slider thumb 22px + 11px padding = effective 44px. Settings button 44x44. Cards
  fully tappable. Save button 40px tall with horizontal padding. PASS
- Screen reader: aria-live announcement on mood change. Section aria-labels. PASS
- Color contrast: --dusk-text on --dusk-bg ≈ oklch(92%) on oklch(14%) — passes 4.5:1 easily. PASS
- prefers-reduced-motion: useReducedMotion() hook in all Framer Motion components. PASS

---

## Contract Self-Check

- Mood slider accessible (keyboard, ARIA): PASS
- Journal entry area feels like a page, not a form field: PASS (textarea, no border, page-line bottom)
- Day cards NOT three equal columns: PASS (horizontal scroll, variable widths)
- Framer Motion used only for purposeful transitions: PASS
- reduced-motion fallback: PASS
- Night/calm color palette (not harsh white, not pure black): PASS
- Typography personal not corporate (Lora serif): PASS
- Touch targets 44px minimum: PASS
"""

V0_REDESIGN_ADMIN = """# Canopy HR Dashboard Redesign — v0

## Phase 1: Scan Summary

Current state: React + Next.js, Tailwind CSS v4 with @theme tokens. Existing tokens:
--color-brand: oklch(48% 0.16 155) (forest green), --color-surface: oklch(97% 0.008 100),
--font-sans: 'Geist'. Installed: shadcn/ui (Radix-based).

The existing design has three critical problems:
1. Six equal gradient cards with bg-gradient-to-br from-green-500 to-teal-600 — AI slop pattern
2. Large white numbers on gradient backgrounds — hero metrics layout, exactly what the contract forbids
3. All six metrics have equal visual weight — no hierarchy between critical and supporting data

This is exactly the case for escalation: the existing language is generic, inconsistent with
the brand green token, and undermines clarity. The redesign is appropriate.

Is this asking for refinement inside an existing language, or is the language itself the problem?
The language is the problem. We are redesigning the metric display, not the page architecture.

## Phase 2: Diagnosis

### P0 Issues (fix immediately)

1. bg-gradient-to-br from-green-500 to-teal-600 on metric cards — replaces with flat surfaces
2. text-white large numbers on gradient backgrounds — gradient metrics pattern, no UNLESS condition
3. Six equal-width cards as entire layout — no hierarchy between headcount (primary) and beta (secondary)

### P1 Issues

4. Pure white text on colored background — color contrast not optimal for scan accuracy
5. No visual distinction between positive metrics (recent hires) and cautionary metrics (attrition)
6. Metrics shown with equal prominence — headcount is the HR director's primary context anchor

### P2 Issues

7. No focus states visible on current implementation
8. No loading or error states for metric values

---

## Phase 3: Redesign

### Design Direction

**This dashboard will feel data-forward and trustworthy because HR directors need to read
status at a glance at the start of their day — not admire gradients.**

The redesign uses the existing brand green token correctly: as a semantic color for positive
states, not as a decorative gradient. Attrition gets a caution amber. Neutral metrics get
neutral surfaces. Hierarchy is created through position and size, not color loudness.

### Revised Token Additions (Tailwind v4 @theme)

```css
@theme {
  /* Existing */
  --color-brand:   oklch(48% 0.16 155);
  --color-surface: oklch(97% 0.008 100);
  --font-sans:     'Geist', sans-serif;

  /* Added for redesign */
  --color-bg:         oklch(95%  0.006 100);
  --color-surface-2:  oklch(99%  0.004 100);
  --color-border:     oklch(88%  0.008 100);
  --color-text:       oklch(18%  0.010 100);
  --color-text-muted: oklch(52%  0.008 100);

  /* Semantic states — used ONLY for meaning, not decoration */
  --color-positive:      oklch(48% 0.16 155);    /* brand green = good */
  --color-positive-bg:   oklch(93% 0.06 155);
  --color-caution:       oklch(64% 0.16 70);     /* amber = watch */
  --color-caution-bg:    oklch(95% 0.08 70);
  --color-neutral-data:  oklch(44% 0.06 240);    /* slate = neutral */
}
```

### Layout Architecture

NOT six equal columns. Instead: a responsive asymmetric grid that gives headcount primary
visual weight and groups supporting metrics as secondary.

```tsx
// DashboardLayout.tsx
export function MetricsDashboard() {
  return (
    <div className="grid gap-4"
         style={{
           gridTemplateColumns: 'repeat(12, 1fr)',
           gridTemplateRows: 'auto auto',
         }}>

      {/* Headcount — primary, spans 4 of 12 columns, full row height */}
      <HeadcountCard style={{ gridColumn: '1 / 5', gridRow: '1 / 3' }} />

      {/* Active Benefits — secondary, cols 5-8 */}
      <MetricCard style={{ gridColumn: '5 / 9', gridRow: '1' }}
                  label="Active Benefits" value="847" trend="stable" />

      {/* Pending Approvals — secondary, cols 9-12 */}
      <MetricCard style={{ gridColumn: '9 / 13', gridRow: '1' }}
                  label="Pending Approvals" value="12" trend="needs-action" />

      {/* Recent Hires — positive, cols 5-8 */}
      <MetricCard style={{ gridColumn: '5 / 9', gridRow: '2' }}
                  label="Recent Hires (30d)" value="23" trend="positive" />

      {/* Attrition Rate — caution, cols 9-11 */}
      <MetricCard style={{ gridColumn: '9 / 12', gridRow: '2' }}
                  label="Attrition Rate" value="3.2%" trend="caution" />

      {/* Open Roles — neutral, cols 11-13 */}
      <MetricCard style={{ gridColumn: '12 / 13', gridRow: '2' }}
                  label="Open Roles" value="8" trend="stable" />
    </div>
  );
}
```

### HeadcountCard Component

```tsx
// HeadcountCard.tsx
interface HeadcountCardProps {
  style?: React.CSSProperties;
}

export function HeadcountCard({ style }: HeadcountCardProps) {
  return (
    <article
      style={style}
      className="rounded-lg border border-[--color-border] bg-[--color-surface-2] p-6
                 flex flex-col justify-between">

      {/* Label */}
      <header>
        <p className="text-[--color-text-muted] text-xs font-medium uppercase tracking-wider">
          Total Headcount
        </p>
      </header>

      {/* Value — large, but flat, no gradient */}
      <div>
        <p className="text-[--color-text] tabular-nums"
           style={{ fontSize: 'clamp(3rem, 6vw, 4.5rem)', fontWeight: 700, lineHeight: 1 }}>
          1,247
        </p>
        <p className="text-[--color-text-muted] text-sm mt-2">
          +12 this month
        </p>
      </div>

      {/* Mini sparkline placeholder — actual chart component would go here */}
      <div className="h-12 mt-4"
           aria-label="Headcount trend over 12 months"
           role="img">
        {/* SparklineChart component */}
      </div>
    </article>
  );
}
```

Key: NO gradient background. NO white text on color. The large number is --color-text (dark
on light surface). The size communicates importance. The sparkline adds temporal context.

### MetricCard Component

```tsx
// MetricCard.tsx
type MetricTrend = 'positive' | 'caution' | 'needs-action' | 'stable';

interface MetricCardProps {
  label: string;
  value: string;
  trend: MetricTrend;
  style?: React.CSSProperties;
}

const TREND_CONFIG = {
  positive: {
    bg:     'var(--color-positive-bg)',
    color:  'var(--color-positive)',
    label:  'On track',
  },
  caution: {
    bg:     'var(--color-caution-bg)',
    color:  'var(--color-caution)',
    label:  'Review',
  },
  'needs-action': {
    bg:     'oklch(93% 0.04 255)',
    color:  'oklch(44% 0.12 255)',
    label:  'Action needed',
  },
  stable: {
    bg:     undefined,
    color:  'var(--color-text-muted)',
    label:  undefined,
  },
};

export function MetricCard({ label, value, trend, style }: MetricCardProps) {
  const config = TREND_CONFIG[trend];

  return (
    <article
      style={style}
      className="rounded-lg border border-[--color-border] bg-[--color-surface-2] p-5
                 flex flex-col justify-between hover:border-[--color-brand]/30
                 transition-colors duration-150
                 focus-within:ring-2 focus-within:ring-[--color-brand] focus-within:ring-offset-2">

      {/* Label row */}
      <header className="flex items-start justify-between gap-2">
        <p className="text-[--color-text-muted] text-xs font-medium uppercase tracking-wider
                      text-pretty">
          {label}
        </p>
        {config.label && (
          <span
            className="text-xs font-medium px-2 py-0.5 rounded flex-shrink-0"
            style={{ background: config.bg, color: config.color }}>
            {config.label}
          </span>
        )}
      </header>

      {/* Value — flat, dark on light, tabular-nums */}
      <p className="text-[--color-text] font-bold tabular-nums mt-3"
         style={{ fontSize: 'clamp(1.5rem, 3vw, 2rem)', lineHeight: 1 }}>
        {value}
      </p>
    </article>
  );
}
```

Critical decisions:
- NO bg-gradient-to-br — removed entirely, no UNLESS condition for this context
- NO white text on color background — dark text on light surface throughout
- Trend is communicated by a small badge (positive-bg + positive-color), not the card background
- Attrition (caution) gets amber badge, NOT a red card background that would alarm inappropriately
- Color appears in the badge only — 10% of the card surface area, consistent with 60/30/10 rule

### Focus States

```css
/* All interactive elements in the dashboard */
[data-interactive]:focus-visible,
button:focus-visible,
[role="button"]:focus-visible {
  outline: 2px solid var(--color-brand);
  outline-offset: 2px;
}
```

---

## Verification

- Flat metric display replacing gradient cards (no bg-gradient-* on metric display): PASS
- Varied grid layout: headcount 4-col primary, others 3-col secondary: PASS
- No gradient text on metric values: PASS
- Color used for meaning only (attrition = caution amber, hires = brand green): PASS
- Focus states on interactive elements: PASS
- Scan-phase summary provided before fixes: PASS
- Six metrics all present: PASS
- Layout works at 1280px+ desktop: PASS
- Tailwind v4 @theme tokens used correctly: PASS
"""

V0_REDESIGN_MARKETING = """# Axle API Redesign — Marketing Page (v0)

## Phase 1: Scan

Framework: Next.js App Router. Styling: Tailwind CSS v3, tailwind.config.js.
Brand asset: /public/axle-wordmark.svg (dark text version).

**Three P0 anti-slop patterns identified**:

1. P0 — Hero gradient: bg-gradient-to-br from-navy-900 via-blue-900 to-purple-900
   Diagnosis: Purple-to-blue gradient on hero background. Classic AI slop fingerprint.

2. P0 — Glassmorphism feature cards: backdrop-filter: blur(12px); background: rgba(255,255,255,0.05)
   Diagnosis: Glassmorphism on dark background. Unreadable, low credibility for technical buyers.

3. P0 — Gradient headline text: bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text text-transparent
   Diagnosis: Cyan-to-purple gradient text on headline. Forbidden pattern, no UNLESS condition met.

Is the existing language the problem? Yes. The entire visual identity is the AI slop pattern.
Full reset appropriate per the brief and the redesign escalation rule.

**One-paragraph summary**: Next.js App Router with Tailwind v3. Current design is a textbook
AI-generated template: purple/navy hero gradient, glassmorphism feature cards, gradient text
headline, and three equal-width feature columns. The technical buyer audience (senior engineers
evaluating APIs) would correctly identify this as low-credibility and move on. The redesign
should signal technical seriousness through specificity, flat composition, and a code snippet
in the hero that demonstrates what the API actually does.

## Phase 2: Diagnosis

P0 (fix immediately):
- bg-gradient-to-br from-navy-900 via-blue-900 to-purple-900 on hero → replace with solid off-white
- backdrop-filter glassmorphism on feature cards → replace with flat, bordered cards
- bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text → remove, plain text
- Three equal-width feature card columns → asymmetric layout

P1 (fix before ship):
- No code example showing API usage → add to hero (hard requirement)
- Inter or default font likely → replace with technical-credible choice
- Centered all-content layout → left-align technical content

P2 (next iteration):
- Footer link farm
- Testimonials if present

---

## Phase 3: Redesign

### Design Direction

This interface will feel technically specific and trustworthy because Axle's buyers are
senior engineers evaluating APIs — they need to see what the product does, not be sold to.

**Font**: Geist (display) + Geist Mono (code). Geist is designed by Vercel for engineering-
forward products. It reads as technical precision without being Inter-default or monospace-heavy.
Its mono variant pairs naturally for code samples.

**Palette**: Warm off-white primary (`oklch(97% 0.008 80)`) with near-black text.
Single accent: a precise blue `oklch(50% 0.16 245)` — used only on CTAs and code highlights.
No gradients. No dark background as primary mode. The product is a daytime work tool for
engineers — light, serious, readable.

### Token Additions (tailwind.config.js v3)

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        axle: {
          bg:         '#f8f7f4',   /* oklch(97% 0.008 80) warm off-white */
          surface:    '#f0ede8',
          border:     '#d8d3cc',
          text:       '#1a1714',   /* oklch(12% 0.012 60) warm near-black */
          muted:      '#6b6560',   /* oklch(46% 0.010 60) */
          accent:     '#1d5ab5',   /* oklch(50% 0.16 245) */
          accentBg:   '#e8eef8',
          codeBg:     '#1e1c1a',   /* oklch(13% 0.008 60) warm near-black */
          codeText:   '#e8e4de',
          codeGreen:  '#5cb85c',   /* success in code */
          codeKey:    '#c8a96a',   /* key color in code */
        }
      },
      fontFamily: {
        sans: ['Geist', 'system-ui', 'sans-serif'],
        mono: ['Geist Mono', 'JetBrains Mono', 'monospace'],
      }
    }
  }
}
```

### Navigation

```tsx
// nav.tsx
export function Nav() {
  return (
    <nav className="border-b border-axle-border bg-axle-bg sticky top-0 z-50">
      <div className="max-w-[1200px] mx-auto px-6 flex items-center justify-between h-14">
        <a href="/" className="flex items-center focus-visible:outline focus-visible:outline-2
                               focus-visible:outline-axle-accent focus-visible:outline-offset-2">
          <img src="/axle-wordmark.svg" alt="Axle" height={24} />
        </a>
        <div className="flex items-center gap-8">
          <a href="/docs" className="font-sans text-sm text-axle-muted hover:text-axle-text
                                     transition-colors duration-150
                                     focus-visible:outline focus-visible:outline-2
                                     focus-visible:outline-axle-accent focus-visible:outline-offset-2">
            Docs
          </a>
          <a href="/pricing" className="font-sans text-sm text-axle-muted hover:text-axle-text
                                        transition-colors duration-150
                                        focus-visible:outline focus-visible:outline-2
                                        focus-visible:outline-axle-accent focus-visible:outline-offset-2">
            Pricing
          </a>
          <a href="/dashboard"
             className="font-sans text-sm font-medium bg-axle-accent text-white
                        px-4 h-9 rounded flex items-center
                        hover:bg-[#1a50a2] transition-colors duration-150
                        focus-visible:outline focus-visible:outline-2
                        focus-visible:outline-offset-2 focus-visible:outline-axle-accent
                        active:scale-[0.98] transition-transform">
            Get API key
          </a>
        </div>
      </div>
    </nav>
  );
}
```

### Hero Section

**No gradient. Plain warm off-white. Left-aligned. Code snippet required.**

```tsx
// hero.tsx
export function Hero() {
  return (
    <section className="bg-axle-bg border-b border-axle-border">
      <div className="max-w-[1200px] mx-auto px-6 py-20 grid grid-cols-12 gap-8 items-start">

        {/* Content — left, columns 1-6 */}
        <div className="col-span-12 lg:col-span-6">

          {/* Eyebrow — no marketing language */}
          <p className="font-mono text-xs text-axle-muted mb-4 tracking-wider uppercase">
            Route Optimization API — v3.1
          </p>

          {/* Headline — plain text, NO gradient */}
          <h1 className="font-sans text-axle-text font-bold leading-tight text-balance"
              style={{ fontSize: 'clamp(2rem, 4vw, 3rem)' }}>
            Optimize delivery routes.
            <br />Get an answer in 200ms.
          </h1>

          <p className="font-sans text-axle-muted mt-4 leading-relaxed max-w-[52ch]">
            The Axle API takes a list of stops and constraints, and returns optimized routes
            for your fleet. REST API with JSON responses. No setup — just HTTP.
          </p>

          <div className="flex items-center gap-3 mt-8">
            <a href="/docs/quickstart"
               className="font-sans font-medium text-sm bg-axle-accent text-white
                          px-6 h-11 rounded flex items-center
                          hover:bg-[#1a50a2] transition-colors duration-150
                          focus-visible:outline focus-visible:outline-2
                          focus-visible:outline-offset-2 focus-visible:outline-axle-accent
                          active:scale-[0.98]">
              Read the docs
            </a>
            <a href="/dashboard"
               className="font-sans font-medium text-sm border border-axle-border text-axle-text
                          px-6 h-11 rounded flex items-center
                          hover:bg-axle-surface transition-colors duration-150
                          focus-visible:outline focus-visible:outline-2
                          focus-visible:outline-offset-2 focus-visible:outline-axle-accent">
              Get API key — free
            </a>
          </div>
        </div>

        {/* Code snippet — right, columns 7-12. Required by brief. */}
        <div className="col-span-12 lg:col-span-6">
          <div className="rounded-lg overflow-hidden border border-axle-border">
            {/* Code window chrome */}
            <div className="bg-[#2a2724] px-4 py-2 flex items-center gap-2 border-b border-[#3a3530]">
              <span className="w-3 h-3 rounded-full bg-[#ff5f57]" aria-hidden="true" />
              <span className="w-3 h-3 rounded-full bg-[#febc2e]" aria-hidden="true" />
              <span className="w-3 h-3 rounded-full bg-[#28c840]" aria-hidden="true" />
              <span className="ml-3 font-mono text-xs text-[#6b6560]">route-request.sh</span>
            </div>
            {/* Syntax-highlighted code */}
            <pre className="bg-axle-codeBg p-5 overflow-x-auto text-sm leading-relaxed">
              <code className="font-mono">
                <span className="text-[#6b8fa8]"># POST a route optimization request</span>{'\n'}
                <span className="text-axle-codeText">curl -X POST </span>
                <span className="text-[#5cb85c]">https://api.axle.io/v3/routes</span>{'\n'}
                <span className="text-axle-codeText">  -H </span>
                <span className="text-axle-codeKey">"Authorization: Bearer YOUR_KEY"</span>{'\n'}
                <span className="text-axle-codeText">  -H </span>
                <span className="text-axle-codeKey">"Content-Type: application/json"</span>{'\n'}
                <span className="text-axle-codeText">  -d </span>
                <span className="text-[#5cb85c]">'{`{`}</span>{'\n'}
                <span className="text-axle-codeKey">    "stops"</span>
                <span className="text-axle-codeText">: [</span>{'\n'}
                <span className="text-axle-codeText">      {`{`} </span>
                <span className="text-axle-codeKey">"id"</span>
                <span className="text-axle-codeText">: </span>
                <span className="text-[#5cb85c]">"stop-001"</span>
                <span className="text-axle-codeText">, </span>
                <span className="text-axle-codeKey">"lat"</span>
                <span className="text-axle-codeText">: 37.77, </span>
                <span className="text-axle-codeKey">"lon"</span>
                <span className="text-axle-codeText">: -122.41 {`}`}</span>{'\n'}
                <span className="text-axle-codeText">    ],</span>{'\n'}
                <span className="text-axle-codeKey">    "vehicle_count"</span>
                <span className="text-axle-codeText">: 3</span>{'\n'}
                <span className="text-[#5cb85c]">  {`}`}'</span>{'\n\n'}
                <span className="text-[#6b8fa8]"># Response: 200 OK, 187ms</span>{'\n'}
                <span className="text-axle-codeText">{`{`} </span>
                <span className="text-axle-codeKey">"routes"</span>
                <span className="text-axle-codeText">: [...], </span>
                <span className="text-axle-codeKey">"total_distance_km"</span>
                <span className="text-axle-codeText">: 47.3 {`}`}</span>
              </code>
            </pre>
          </div>
        </div>
      </div>
    </section>
  );
}
```

### Feature Sections — NOT Three Equal Columns

Instead: three features in an asymmetric alternating layout.

```tsx
// features.tsx
interface Feature {
  label: string;
  title: string;
  body: string;
  code?: string;
}

const FEATURES: Feature[] = [
  {
    label: 'Performance',
    title: 'Sub-200ms response on route sets up to 500 stops.',
    body: 'Our solver handles time-window constraints, vehicle capacity, and traffic-weighted road networks. Returns optimal routes, not approximate ones.',
    code: `// SDK usage
const result = await axle.routes.optimize({
  stops: myStops,
  constraints: { maxHoursPerDriver: 8 }
});`
  },
  {
    label: 'Reliability',
    title: '99.97% uptime. SLA-backed.',
    body: 'Multi-region deployment. Automatic retry on solver timeout. Guaranteed response or your request is queued at no cost.',
  },
  {
    label: 'Integration',
    title: 'REST. Webhooks. Streaming.',
    body: 'Sync requests for small fleets. Async + webhook callbacks for large jobs. Real-time streaming progress on optimization runs.',
  },
];

export function Features() {
  return (
    <section className="bg-axle-bg border-t border-axle-border">
      <div className="max-w-[1200px] mx-auto px-6 py-20">
        <h2 className="font-sans font-bold text-axle-text text-balance"
            style={{ fontSize: 'clamp(1.5rem, 3vw, 2.25rem)' }}>
          Built for production workloads.
        </h2>
        <p className="font-sans text-axle-muted mt-3 max-w-[52ch] leading-relaxed">
          Not a toy routing library. The Axle API is used by logistics teams processing
          thousands of deliveries per day.
        </p>

        <div className="mt-12 space-y-16">
          {FEATURES.map((feature, i) => (
            <div key={i}
                 className={`grid grid-cols-12 gap-8 items-start ${
                   i % 2 === 1 ? 'direction-rtl' : ''
                 }`}>
              <div className="col-span-12 lg:col-span-5">
                <p className="font-mono text-xs text-axle-muted uppercase tracking-wider mb-3">
                  {feature.label}
                </p>
                <h3 className="font-sans font-semibold text-axle-text text-balance leading-snug"
                    style={{ fontSize: 'clamp(1.25rem, 2vw, 1.5rem)' }}>
                  {feature.title}
                </h3>
                <p className="font-sans text-axle-muted mt-3 leading-relaxed max-w-[45ch]">
                  {feature.body}
                </p>
              </div>
              {feature.code && (
                <div className="col-span-12 lg:col-span-6 lg:col-start-7">
                  <pre className="bg-axle-codeBg rounded-lg p-5 text-sm leading-relaxed overflow-x-auto
                                  border border-axle-border">
                    <code className="font-mono text-axle-codeText">{feature.code}</code>
                  </pre>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Verification

- Phase 1 scan explicitly identified three P0 anti-slop patterns: PASS
- Gradient hero replaced with clean warm off-white: PASS (no bg-gradient-* in hero)
- Glassmorphism cards replaced with flat bordered alternatives: PASS
- Gradient text on headline removed: PASS (plain text-axle-text)
- Hero code snippet included and syntax-highlighted: PASS
- Typography appropriate for technical audience (Geist — precision sans): PASS
- New layout does NOT fall back into three equal-column cards: PASS (asymmetric alternating)
- prefers-reduced-motion respected: PASS (no animation library used)
- Focus states on all interactive elements: PASS (focus-visible:outline throughout)
- Touch targets 44px: PASS (h-11 = 44px on buttons)
"""

V0_REFINE_WIDGET = """# Quorum P&L Widget Refinement — v0

## Design-Log (UNLESS Invocations)

<design-log>
DECISION: Keep pure #000000 background and #ffffff text unchanged
BECAUSE: Domain is a professional equity derivatives trading terminal. Finance terminals
(Bloomberg Terminal, Interactive Brokers TWS, Quorum) use pure black backgrounds as an
established domain convention. This satisfies the UNLESS condition: "Domain is finance
terminal, print replica, or high-contrast accessibility mode where pure black is the correct
convention." The existing codebase uses --bg: #000000 as the stated design system. Changing
this would violate domain requirements.

DECISION: Keep JetBrains Mono as the sole font throughout
BECAUSE: Domain is a professional trading terminal where monospace is the correct aesthetic
convention. The UNLESS condition is satisfied: "Domain is terminal emulator, code editor,
data terminal, finance terminal, or developer tool where monospace is the correct aesthetic
convention for that domain." Bloomberg, TWS, and all professional trading terminals use
monospace exclusively. Changing to a sans-serif would be a domain violation.

DECISION: Improve hierarchy through weight contrast only (no color changes beyond existing palette)
BECAUSE: The existing palette (--positive: #00ff41, --negative: #ff3131) is the correct
domain convention and must not be extended. New accent colors would introduce unfamiliar
signals in a context where color means money (positive/negative P&L). Only weight contrast
and spacing are available as hierarchy tools.

DECISION: tabular-nums required throughout
BECAUSE: Hard constraint stated in brief. All financial values must use font-variant-numeric:
tabular-nums for column alignment. This is also standard in all professional trading terminal UIs.
</design-log>

---

## Diagnosis

Current issues:
1. Values and labels use the same font-weight (400) — no visual hierarchy; the number gets lost
2. Positive and negative values are differentiated only by color — hard to scan at a glance
3. Labels are styled identically to values — the eye cannot separate what a number IS from WHAT it is
4. No tabular alignment enforced on values — numbers won't column-align across rows
5. Spacing within and between cells is uniform — no grouping or breathing room

These are all structure and weight issues. Color changes are NOT available (domain constraint).

---

## Refinement Strategy

Fix hierarchy through:
1. Weight contrast: value = font-weight 700, label = font-weight 400
2. Size contrast: value at 18px, label at 11px
3. Color meaning: positive values get --positive color, negative get --negative color AND weight
4. Spacing: increase internal cell padding, group related cells
5. Alignment: tabular-nums on all values, right-align all values, left-align all labels

The 3x2 grid structure is preserved per constraint.

---

## CSS Modules Refinement

```css
/* PnLWidget.module.css */

.widget {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 1px;                          /* gap is 1px border line, not spacing */
  background-color: #1a1a1a;         /* --border: the gap color */
  border: 1px solid #1a1a1a;
  font-family: 'JetBrains Mono', monospace;  /* UNLESS: finance terminal domain */
}

.cell {
  background-color: #000000;         /* UNLESS: finance terminal domain convention */
  padding: 16px 14px 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  position: relative;
}

/* Highlight the top row (P&L metrics) with slightly more vertical padding */
.cell--primary {
  padding: 20px 14px 16px;
}

/* Label — small, low weight */
.label {
  font-size: 10px;
  font-weight: 400;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.45);  /* Muted white — clearly secondary */
  font-variant-numeric: tabular-nums;
}

/* Value — large, high weight */
.value {
  font-size: 18px;
  font-weight: 700;
  color: #ffffff;                     /* UNLESS: finance terminal domain */
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
  line-height: 1;
}

/* Positive P&L value */
.value--positive {
  color: #00ff41;  /* --positive, unchanged */
  font-weight: 700;
}

/* Negative P&L value */
.value--negative {
  color: #ff3131;  /* --negative, unchanged */
  font-weight: 700;
}

/* Neutral/Greek values — white but slightly lower weight for deemphasis */
.value--neutral {
  color: #ffffff;
  font-weight: 600;
}

/* Change delta — shown below main value, smaller */
.delta {
  font-size: 11px;
  font-weight: 400;
  font-variant-numeric: tabular-nums;
  opacity: 0.7;
  margin-top: 2px;
}

.delta--positive { color: #00ff41; }
.delta--negative { color: #ff3131; }
```

---

## React Component

```tsx
// PnLWidget.tsx
import styles from './PnLWidget.module.css';

interface MetricCell {
  label: string;
  value: string;
  delta?: string;
  type: 'positive' | 'negative' | 'neutral';
  isPrimary?: boolean;
}

const METRICS: MetricCell[] = [
  {
    label: 'Realized P&L',
    value: '+$12,847.50',
    delta: '+$1,203.00 today',
    type: 'positive',
    isPrimary: true,
  },
  {
    label: 'Unrealized P&L',
    value: '-$3,291.75',
    delta: '-$892.00 vs open',
    type: 'negative',
    isPrimary: true,
  },
  {
    label: 'Net Delta',
    value: '0.847',
    delta: '+0.023 1h',
    type: 'neutral',
    isPrimary: true,
  },
  {
    label: 'Vega',
    value: '2,341.00',
    delta: undefined,
    type: 'neutral',
  },
  {
    label: 'Theta',
    value: '-156.80',
    delta: 'per day',
    type: 'negative',
  },
  {
    label: 'Portfolio Beta',
    value: '1.12',
    delta: 'vs SPX',
    type: 'neutral',
  },
];

function valueClass(type: MetricCell['type']): string {
  return [
    styles.value,
    type === 'positive' ? styles['value--positive'] : '',
    type === 'negative' ? styles['value--negative'] : '',
    type === 'neutral'  ? styles['value--neutral']  : '',
  ].filter(Boolean).join(' ');
}

export function PnLWidget() {
  return (
    <section
      className={styles.widget}
      aria-label="P&L Summary"
      role="region">
      {METRICS.map((metric) => (
        <div
          key={metric.label}
          className={[styles.cell, metric.isPrimary ? styles['cell--primary'] : ''].join(' ')}>
          <span className={styles.label}>{metric.label}</span>
          <span className={valueClass(metric.type)}
                aria-label={`${metric.label}: ${metric.value}`}>
            {metric.value}
          </span>
          {metric.delta && (
            <span className={[
              styles.delta,
              metric.type === 'positive' ? styles['delta--positive'] : '',
              metric.type === 'negative' ? styles['delta--negative'] : '',
            ].join(' ')}
                  aria-hidden="true">
              {metric.delta}
            </span>
          )}
        </div>
      ))}
    </section>
  );
}
```

---

## What Changed (Refine Scope Verification)

1. font-weight: value 700 vs label 400 — this is the primary hierarchy fix
2. Font size: value 18px vs label 10px — stronger size contrast than before
3. Positive values: --positive color + weight 700 (was just color)
4. Negative values: --negative color + weight 700 (was just color)
5. Delta sub-values: added to P&L metrics for context (today's change vs total)
6. Cell padding: primary cells 20px top vs secondary cells 16px — subtle size differentiation
7. tabular-nums: explicitly applied to both value and label classes

What did NOT change:
- Background color: #000000 (UNLESS: finance terminal domain)
- Font family: JetBrains Mono (UNLESS: finance terminal domain)
- Color palette: only --positive and --negative used for color meaning
- Grid structure: 3x2 preserved per constraint
- No new colors introduced beyond existing palette

---

## UNLESS Verification

FORBIDDEN: Pure #000000 as background
UNLESS condition met: Domain is finance terminal (Bloomberg Terminal, Interactive Brokers TWS
convention). The codebase explicitly defines --bg: #000000. DOCUMENTED IN DESIGN-LOG.

FORBIDDEN: Monospace as primary voice for body text
UNLESS condition met: Domain is finance terminal where monospace is the established and
correct aesthetic convention. Named domain: Bloomberg Terminal, TWS. DOCUMENTED IN DESIGN-LOG.

---

## Self-Check

- Component is still recognizably the same 3x2 P&L grid widget: PASS
- Structural fixes (weight, size) happened before any stylistic work: PASS
- No new colors introduced beyond existing --positive and --negative: PASS
- tabular-nums applied to all numeric values: PASS
- #000000 background maintained (UNLESS condition documented): PASS
- JetBrains Mono maintained (UNLESS condition documented): PASS
- Result still satisfies contract.md: PASS
"""

V0_REFINE_FORM = """# Vesta Onboarding Form Refinement — v0

## Design Rationale

Target: three-step onboarding form for Vesta property management SaaS.
What is being improved: progress indicator, CTA hierarchy, error states, label accessibility.
What stays intact: three-step structure, Vue 3 + Vite + Tailwind v3 stack, existing components.

Audience: independent landlords (40-65, non-technical, likely mobile). Primary task: get from
signup to first property listed. Any confusion, ambiguity, or error that requires re-reading
is a conversion failure for this audience.

**This is a refine, not a redesign.** The page structure, component set, and three-step
flow are preserved. The improvements are: progress indicator, CTA visual distinction,
inline error states, accessible labels.

---

## Symptom Mapping

- No progress indicator → user cannot tell if they are on step 1 or step 3 → ADD progress indicator
- Next and Back buttons identical → user doesn't know the primary action → FIX CTA hierarchy
- Unclear error states → no inline validation feedback → ADD inline errors
- Labels not clearly associated → VERIFY label-above-input pattern throughout

Primary fix areas: refine-layout (hierarchy) + refine-style (clarify, delight/momentum).

---

## Progress Indicator Component

```vue
<!-- ProgressBar.vue -->
<template>
  <nav aria-label="Form progress" class="mb-8">
    <!-- Step indicators -->
    <ol class="flex items-center gap-0">
      <li v-for="(step, i) in steps"
          :key="i"
          class="flex items-center"
          :class="i < steps.length - 1 ? 'flex-1' : ''">

        <!-- Step circle -->
        <div class="flex flex-col items-center">
          <div
            :class="[
              'w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium transition-colors duration-200',
              i + 1 < currentStep
                ? 'bg-[--color-brand] text-white'
                : i + 1 === currentStep
                ? 'bg-[--color-brand] text-white ring-4 ring-[--color-brand]/20'
                : 'bg-gray-100 text-gray-400 border border-gray-200'
            ]"
            :aria-current="i + 1 === currentStep ? 'step' : undefined">
            <!-- Completed checkmark -->
            <svg v-if="i + 1 < currentStep"
                 width="14" height="14" viewBox="0 0 24 24" fill="none"
                 stroke="currentColor" stroke-width="2.5" aria-hidden="true">
              <polyline points="20 6 9 17 4 12" />
            </svg>
            <span v-else>{{ i + 1 }}</span>
          </div>

          <!-- Step label -->
          <span :class="[
                  'text-xs mt-1 font-medium',
                  i + 1 === currentStep ? 'text-[--color-brand]' : 'text-gray-400'
                ]">
            {{ step.label }}
          </span>
        </div>

        <!-- Connector line -->
        <div v-if="i < steps.length - 1"
             :class="[
               'flex-1 h-0.5 mx-3 mb-5 transition-colors duration-200',
               i + 1 < currentStep ? 'bg-[--color-brand]' : 'bg-gray-200'
             ]"
             aria-hidden="true" />
      </li>
    </ol>

    <!-- Screen reader announcement -->
    <p class="sr-only" aria-live="polite">
      Step {{ currentStep }} of {{ steps.length }}: {{ steps[currentStep - 1].label }}
    </p>
  </nav>
</template>

<script setup lang="ts">
interface Step { label: string; }

const props = defineProps<{
  steps: Step[];
  currentStep: number;
}>();
</script>
```

Usage:
```vue
<ProgressBar
  :steps="[
    { label: 'Profile' },
    { label: 'Property' },
    { label: 'Billing' }
  ]"
  :currentStep="currentStep"
/>
```

---

## CTA Button Hierarchy Fix

Current: Next and Back are identically styled. This is a critical usability failure for
non-technical users who expect visual hierarchy to guide action.

Fix: Next (primary) = filled brand button. Back (secondary) = ghost/text button.
They must be visually distinct in weight, not just color.

```vue
<!-- StepNavigation.vue -->
<template>
  <div class="flex items-center justify-between mt-8 pt-6 border-t border-gray-200">

    <!-- Back — ghost, lower visual weight -->
    <VestaButton
      v-if="currentStep > 1"
      variant="ghost"
      type="button"
      @click="$emit('back')"
      :disabled="isSubmitting"
      class="min-h-[44px] min-w-[44px] px-5">
      ← Back
    </VestaButton>

    <!-- Spacer when no Back button -->
    <div v-else />

    <!-- Next / Submit — filled, high visual weight -->
    <VestaButton
      variant="primary"
      type="submit"
      :disabled="isSubmitting"
      class="min-h-[44px] px-8 font-semibold">
      <span v-if="isSubmitting" class="flex items-center gap-2">
        <!-- Spinner -->
        <svg class="animate-spin w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor">
          <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83" stroke-width="2" />
        </svg>
        Saving...
      </span>
      <span v-else>
        {{ currentStep < totalSteps ? 'Continue →' : 'Complete setup' }}
      </span>
    </VestaButton>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  currentStep: number;
  totalSteps: number;
  isSubmitting?: boolean;
}>();
defineEmits(['back']);
</script>
```

---

## Inline Error States

Current: no inline validation. Error states must be: next to the field, specific, actionable.

```vue
<!-- FormField.vue — wrapper for all form fields -->
<template>
  <div class="flex flex-col gap-1.5">
    <!-- Label always above field, always visible -->
    <label
      :for="inputId"
      class="text-sm font-medium text-gray-700">
      {{ label }}
      <span v-if="required" class="text-red-500 ml-0.5" aria-hidden="true">*</span>
      <span v-if="required" class="sr-only">(required)</span>
    </label>

    <!-- Hint text (optional) -->
    <p v-if="hint" :id="`${inputId}-hint`"
       class="text-xs text-gray-500 -mt-0.5">
      {{ hint }}
    </p>

    <!-- Input slot — VestaInput, VestaSelect, etc. -->
    <slot :inputId="inputId" :ariaDescribedby="ariaDescribedby" :hasError="!!error" />

    <!-- Inline error — specific, actionable -->
    <p v-if="error"
       :id="`${inputId}-error`"
       class="text-sm text-red-600 flex items-start gap-1.5"
       role="alert"
       aria-live="polite">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2" class="mt-0.5 flex-shrink-0" aria-hidden="true">
        <circle cx="12" cy="12" r="10" />
        <line x1="12" y1="8" x2="12" y2="12" />
        <line x1="12" y1="16" x2="12.01" y2="16" />
      </svg>
      {{ error }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  inputId: string;
  label: string;
  required?: boolean;
  hint?: string;
  error?: string;
}>();

const ariaDescribedby = computed(() => {
  const ids = [];
  if (props.hint) ids.push(`${props.inputId}-hint`);
  if (props.error) ids.push(`${props.inputId}-error`);
  return ids.join(' ') || undefined;
});
</script>
```

Error message examples (specific + actionable, per Clarify rules):
- Email: "Email already in use — try signing in instead"
- Phone: "Enter a 10-digit phone number (e.g. 555-867-5309)"
- Address: "We couldn't verify this address — double-check the ZIP code"
- Required field: "Display name is required to continue"

---

## Step 1: Landlord Profile

```vue
<!-- Step1Profile.vue -->
<template>
  <form @submit.prevent="handleSubmit" novalidate>
    <div class="space-y-5">
      <FormField inputId="display-name" label="Display name" :required="true" :error="errors.name">
        <template #default="{ inputId, ariaDescribedby, hasError }">
          <VestaInput
            :id="inputId"
            v-model="form.name"
            type="text"
            autocomplete="name"
            :aria-describedby="ariaDescribedby"
            :aria-invalid="hasError"
            class="min-h-[44px]" />
        </template>
      </FormField>

      <FormField inputId="email" label="Email address" :required="true" :error="errors.email"
                 hint="We'll send your account confirmation here.">
        <template #default="{ inputId, ariaDescribedby, hasError }">
          <VestaInput
            :id="inputId"
            v-model="form.email"
            type="email"
            autocomplete="email"
            :aria-describedby="ariaDescribedby"
            :aria-invalid="hasError"
            class="min-h-[44px]" />
        </template>
      </FormField>

      <FormField inputId="phone" label="Phone number" :required="true" :error="errors.phone"
                 hint="Used for urgent property notifications only.">
        <template #default="{ inputId, ariaDescribedby, hasError }">
          <VestaInput
            :id="inputId"
            v-model="form.phone"
            type="tel"
            autocomplete="tel"
            :aria-describedby="ariaDescribedby"
            :aria-invalid="hasError"
            class="min-h-[44px]" />
        </template>
      </FormField>
    </div>

    <StepNavigation :currentStep="1" :totalSteps="3" @back="/* no-op, step 1 */" />
  </form>
</template>
```

---

## Self-Check

- Progress indicator added, visually clear (step N of 3, accessible): PASS
- Primary Next button visually distinct from Back (filled vs ghost, clear weight difference): PASS
- Error states: inline, next to the field, specific what + what to do: PASS
- Labels: above inputs in all steps (FormField enforces this): PASS
- Touch targets 44px minimum: PASS (min-h-[44px] on all inputs and buttons)
- Back always works, no dead ends: PASS
- Three-step structure preserved: PASS
- No new component library introduced: PASS
- Result is recognizably the same form, not a redesign: PASS
- Stack preserved: Vue 3 + Vite + Tailwind v3: PASS
"""

V0_REFINE_SETTINGS = """# Helio Settings Panel Refinement — v0

## Target and Scope

What is being improved: section header hierarchy vs field label hierarchy, spacing between
and within sections, visual clarity.

What stays intact: three-section structure (Profile, Notifications, Security), existing
components (Input, Toggle, Button), Tailwind v3 + Next.js stack, no new component library.

This is a refine, not a redesign. The result must be recognizably the same panel.

---

## Diagnosis

Current issues from provided code sample:

1. h2 "Profile" = text-sm font-medium text-gray-700
   label "Display Name" = text-sm text-gray-600
   → These are visually identical. Section headers and field labels are indistinguishable.
   This is the primary hierarchy failure.

2. Section padding: p-4 for each section = 16px
   Space between fields: space-y-3 = 12px gap
   Space between sections: no explicit separation beyond the section border itself
   → Sections don't breathe. Inter-field and inter-section spacing are nearly identical.

3. Label is a sibling of Input with space-y-3 between them — no explicit association via
   htmlFor/id pair visible in the sample (labels need explicit for= attributes).

4. Section container: p-4 border border-gray-200 rounded — this is a card.
   The refine contract says no NEW card wrappers. But these already exist. We keep them.
   However, we improve them: remove the border+rounded from the section container,
   use a ruled separator and padding instead. Cards around form sections add no hierarchy value.

---

## Refinement

### Section Header: Make It Visually Distinct from Field Labels

```tsx
// Settings section header — was: text-sm font-medium text-gray-700
// Now: larger, heavier, clearer hierarchy

function SectionHeader({ title }: { title: string }) {
  return (
    <div className="mb-6 pb-3 border-b border-gray-200">
      <h2 className="text-base font-semibold text-gray-900 text-balance">
        {title}
      </h2>
    </div>
  );
}
```

Before: text-sm font-medium text-gray-700 (same as labels)
After: text-base font-semibold text-gray-900 + border-bottom as visual anchor

Changes made:
- Size: text-sm → text-base (one step up in Tailwind scale)
- Weight: font-medium → font-semibold
- Color: text-gray-700 → text-gray-900 (stronger contrast)
- Added border-bottom as a structural separator — not a new card wrapper

### Field Label: Clearly Label, Not Section

```tsx
// Field label — was: text-sm text-gray-600 (nearly same as section header)
// Now: smaller than section header, explicitly associated

function FieldLabel({ htmlFor, children, required }: {
  htmlFor: string;
  children: React.ReactNode;
  required?: boolean;
}) {
  return (
    <label
      htmlFor={htmlFor}
      className="block text-sm font-medium text-gray-700 mb-1.5">
      {children}
      {required && (
        <>
          <span className="text-red-500 ml-0.5" aria-hidden="true">*</span>
          <span className="sr-only"> (required)</span>
        </>
      )}
    </label>
  );
}
```

### Spacing: Inter-Section vs Inter-Field

```tsx
// Before:
// <section className="p-4 border border-gray-200 rounded">

// After:
// Section: large separation (48px) between sections
// Fields: small separation (20px) between field rows within a section
// Section container: no card border (redundant with the section header border)

function SettingsSection({ title, children }: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <section className="py-0">
      <SectionHeader title={title} />
      <div className="space-y-5 pb-12">
        {children}
      </div>
    </section>
  );
}

// The outer container:
function SettingsPanel() {
  return (
    <div className="max-w-2xl mx-auto px-4 py-8 divide-y divide-gray-200">
      <SettingsSection title="Profile">
        {/* fields */}
      </SettingsSection>
      <SettingsSection title="Notifications">
        {/* fields */}
      </SettingsSection>
      <SettingsSection title="Security">
        {/* fields */}
      </SettingsSection>
    </div>
  );
}
```

Key changes:
- divide-y divide-gray-200 on the outer container creates visual breaks between sections
- pb-12 (48px) on each section's field group creates generous inter-section breathing room
- space-y-5 (20px) between individual fields — was space-y-3 (12px)
- Section card border REMOVED — the section header border-bottom and divide-y do the separating work
  without nesting a card inside the panel

### Full Refined Settings Panel

```tsx
// SettingsPanel.tsx
'use client';

import { useState } from 'react';

interface FieldRowProps {
  label: string;
  htmlFor: string;
  hint?: string;
  required?: boolean;
  children: React.ReactNode;
}

function FieldRow({ label, htmlFor, hint, required, children }: FieldRowProps) {
  return (
    <div className="flex flex-col gap-1.5">
      <label
        htmlFor={htmlFor}
        className="text-sm font-medium text-gray-700">
        {label}
        {required && (
          <>
            <span className="text-red-500 ml-0.5" aria-hidden="true">*</span>
            <span className="sr-only"> (required)</span>
          </>
        )}
      </label>
      {hint && (
        <p id={`${htmlFor}-hint`} className="text-xs text-gray-500">
          {hint}
        </p>
      )}
      {children}
    </div>
  );
}

function SectionHeader({ title }: { title: string }) {
  return (
    <div className="mb-6 pb-3 border-b border-gray-200">
      <h2 className="text-base font-semibold text-gray-900 text-balance">
        {title}
      </h2>
    </div>
  );
}

export function SettingsPanel() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [emailNotif, setEmailNotif] = useState(true);
  const [slackNotif, setSlackNotif] = useState(false);
  const [twoFactor, setTwoFactor] = useState(false);

  return (
    <main className="max-w-2xl mx-auto px-4 py-8">
      {/* Sections separated by horizontal rules, not cards */}
      <div className="divide-y divide-gray-200">

        {/* Profile */}
        <section className="py-8 first:pt-0">
          <SectionHeader title="Profile" />
          <div className="space-y-5">
            <FieldRow htmlFor="display-name" label="Display name" required>
              <Input
                id="display-name"
                value={name}
                onChange={e => setName(e.target.value)}
                className="w-full focus-visible:ring-[--color-brand] focus-visible:ring-2" />
            </FieldRow>

            <FieldRow htmlFor="email" label="Email address" required
                      hint="Changing your email requires re-verification.">
              <Input
                id="email"
                type="email"
                value={email}
                onChange={e => setEmail(e.target.value)}
                className="w-full focus-visible:ring-[--color-brand] focus-visible:ring-2" />
            </FieldRow>
          </div>

          <div className="mt-6">
            <Button variant="primary" className="focus-visible:ring-2 focus-visible:ring-[--color-brand]
                                                  focus-visible:ring-offset-2">
              Save changes
            </Button>
          </div>
        </section>

        {/* Notifications */}
        <section className="py-8">
          <SectionHeader title="Notifications" />
          <div className="space-y-5">
            <FieldRow htmlFor="email-notifications" label="Email notifications"
                      hint="Receive a daily digest of project activity.">
              <Toggle
                id="email-notifications"
                checked={emailNotif}
                onCheckedChange={setEmailNotif}
                aria-label="Toggle email notifications" />
            </FieldRow>

            <FieldRow htmlFor="slack-notifications" label="Slack notifications"
                      hint="Post updates to your connected Slack workspace.">
              <Toggle
                id="slack-notifications"
                checked={slackNotif}
                onCheckedChange={setSlackNotif}
                aria-label="Toggle Slack notifications" />
            </FieldRow>
          </div>
        </section>

        {/* Security */}
        <section className="py-8 last:pb-0">
          <SectionHeader title="Security" />
          <div className="space-y-5">
            <FieldRow htmlFor="two-factor" label="Two-factor authentication"
                      hint="Adds a second verification step when signing in.">
              <Toggle
                id="two-factor"
                checked={twoFactor}
                onCheckedChange={setTwoFactor}
                aria-label="Toggle two-factor authentication" />
            </FieldRow>

            <FieldRow htmlFor="current-password" label="Change password">
              <Button variant="ghost"
                      className="self-start focus-visible:ring-2 focus-visible:ring-[--color-brand]
                                 focus-visible:ring-offset-2">
                Change password
              </Button>
            </FieldRow>
          </div>
        </section>

      </div>
    </main>
  );
}
```

---

## Self-Check

- Section headers visually distinct from field labels (size text-base vs text-sm, weight
  semibold vs medium, color gray-900 vs gray-700, + border-bottom anchor): PASS
- Spacing between sections larger than between fields (py-8 per section / space-y-5 within): PASS
- Labels above inputs in all sections (label before input in DOM order, htmlFor/id linked): PASS
- Self-check: this is a refine, not a redesign (three sections preserved, structure unchanged,
  same components, recognizably same panel): PASS
- No new card wrappers introduced (section border REMOVED, replaced by divide-y horizontal rules): PASS
- Stack preserved: React + Next.js + Tailwind v3: PASS
- No new component library: PASS
- focus-visible states present on all interactive elements: PASS
"""

# Write all v0 outputs
write_result('v0', 'create-saas-landing', V0_CREATE_SAAS)
write_result('v0', 'create-devtool-landing', V0_CREATE_DEVTOOL)
write_result('v0', 'create-consumer-app', V0_CREATE_CONSUMER)
write_result('v0', 'redesign-admin-dashboard', V0_REDESIGN_ADMIN)
write_result('v0', 'redesign-marketing-page', V0_REDESIGN_MARKETING)
write_result('v0', 'refine-dashboard-widget', V0_REFINE_WIDGET)
write_result('v0', 'refine-form-flow', V0_REFINE_FORM)
write_result('v0', 'refine-settings-panel', V0_REFINE_SETTINGS)

print("All v0 outputs written.")
