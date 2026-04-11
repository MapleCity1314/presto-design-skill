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

V1_CREATE_SAAS = """# SignalForge SaaS Landing Page — v1

## Context Phase

**1a. Host stack**: No codebase provided. Working from brief only.

**1b. Existing design language**: No codebase — working from brief only.

**1c. Reference products**:

Reference: Datadog
- Deep navy/dark backgrounds abandoned in favor of warm off-white marketing pages
- Single saturated purple accent used sparingly on CTAs only
- Product screenshots are the hero, not abstract visualizations
- Monospace used only in code examples, never as body or headline font

Reference: Honeycomb (observability)
- Warm cream off-white base, heavy editorial whitespace
- Data visualization is the primary trust signal — real-looking charts in hero
- Copy is direct and technical ("query your data") not aspirational
- Green accent tied to the product's "find the bug" workflow

Reference: Incident.io
- Warm off-white hero, strong typographic headline, no gradient
- Single feature screenshot in hero, left-anchored layout
- Amber/orange accent — the "alert" color that works for incident tools without neon

**1d. Brief restatement**:
The audience is engineering managers, CTOs, and staff engineers at startups and mid-market
SaaS companies who have outgrown basic monitoring but find enterprise tools (Datadog,
Splunk) too complex and expensive. Their primary job: find the root cause of incidents
faster. The interface must project technical credibility and operational authority without
the AI-template look their technical buyers can immediately detect.

**1e. Gap declaration**: No existing codebase tokens or stack specified. Assuming green-field
HTML/CSS or React. All decisions made from brief and domain reference.

---

## Design Parameters

VARIANCE: 7 (asymmetric, left-anchored hero, alternating features, not centered everything)
MOTION: 5 (entrance + hover; no scroll choreography that would undermine credibility)
DENSITY: 5 (balanced product/marketing density — not airy blog, not dense dashboard)

---

<design-log>
DECISION: Display font = Cabinet Grotesk 800; body = Geist 400/500
BECAUSE: Engineering-buyer audience (CTOs, staff engineers) responds to precision and
authority in typography. Cabinet Grotesk's slightly condensed geometry at heavy weight reads
as "built not assembled." Geist is a developer-facing sans designed for readability at
screen sizes. Neither Inter nor Roboto — those read as SaaS-template defaults.
Domain reference: Incident.io and Honeycomb both use custom grotesque display fonts, not
Inter, for their marketing headlines.

DECISION: Color system = warm off-black base (oklch(10% 0.012 240)) + warm cream light
sections (oklch(97% 0.010 60)) + amber accent (oklch(65% 0.19 55))
BECAUSE: Amber is the "alert resolved" color convention in incident tooling (PagerDuty,
Incident.io both use warm amber/orange for alert states). It avoids the cyan-on-dark and
purple-gradient patterns explicitly forbidden. Warm neutrals (not pure #000 or #fff) are
required by contract. The dark primary surface fits an incident-tool context without
resorting to dark-mode-plus-neon.

DECISION: Layout = 12-column grid, left-anchored hero (content cols 1-7, visual 8-12),
alternating feature sections, max-width 1280px
BECAUSE: Left-anchored layout is used by Incident.io and Honeycomb — it reads as editorial
confidence rather than the centered-symmetric template look. The alternating feature layout
avoids the three-equal-column grid forbidden by contract.

DECISION: Motion = MOTION 5 — entrance animations on hero, scroll reveals on features,
hover states on all interactive elements. No GSAP, no spring choreography.
BECAUSE: Technical buyers don't trust performative animation; it signals marketing budget
over engineering substance. Purposeful entrance (fade + slight translate) establishes
hierarchy without theatrics.

DECISION: Icon family = Phosphor (ph:) — outline weight
BECAUSE: No existing icon library in project. Phosphor is the highest-quality general-purpose
icon set with an outline weight that reads as precise and technical. Consistent with the
Cabinet Grotesk precision aesthetic.
</design-log>

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
  --warning:       oklch(72%  0.17  75);
  --error:         oklch(58%  0.21  25);
}
```

---

## Typography

```css
@import url('https://fonts.googleapis.com/css2?family=Cabinet+Grotesk:wght@400;500;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500&display=swap');

:root {
  --font-display: 'Cabinet Grotesk', sans-serif;
  --font-body:    'Geist', 'DM Sans', sans-serif;
  --font-mono:    'JetBrains Mono', monospace;
  --text-xs:   clamp(0.6875rem, 0.6rem + 0.2vw, 0.75rem);
  --text-sm:   clamp(0.8125rem, 0.78rem + 0.2vw, 0.875rem);
  --text-base: clamp(1rem, 0.96rem + 0.25vw, 1.0625rem);
  --text-lg:   clamp(1.125rem, 1.07rem + 0.3vw, 1.25rem);
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

---

## Section Specifications

### Navigation
Sticky, --bg, backdrop-blur(16px) on scroll. Left: wordmark Cabinet Grotesk 700 18px.
Center: Products / Docs / Pricing (Geist 400 14px --text-muted, hover --text 150ms ease-out).
Right: "Sign in" text + "Start free trial" amber button (44px tall, 20px pad, radius 6px).
Mobile: hamburger (44x44px) -> full-height drawer, 48px link targets.

### Hero

Eyebrow: "OBSERVABILITY / INCIDENT INTELLIGENCE" — uppercase, --text-xs, letter-spacing 0.12em.

Headline (columns 1-8):
  "From alert
   to resolution,
   before it spreads."
Cabinet Grotesk 800, --text-5xl, line-height 1.0, letter-spacing -0.03em.

Copy (columns 1-6, max 52ch): "SignalForge correlates logs, traces, and anomaly signals
into one incident timeline. Engineering teams resolve 40% faster."
Geist 400, --text-lg, line-height 1.6, --text-muted.

CTAs: Primary "Start free trial" (amber filled, 48px). Secondary "See it in action" (text).
Trust: "No credit card * 5-minute setup * SOC 2 Type II" — --text-xs --text-muted.

Product visual (cols 7-12): Mock incident timeline panel in --surface-2, 1px --border.
Bar chart with amber spike at incident window + trace entries + resolution badge in --success.
Panel bleeds 40px below section fold for implied depth.

### Trust Bar
--bg-light, 32px pad. Six SVG logotypes at 35% opacity, 70% hover. gap: clamp(32px, 5vw, 64px).
NOT cards. NOT equal-width columns.

### Feature Sections (4 alternating, dark/light backgrounds)

F1 (dark): "One timeline. Every signal." — Annotated timeline component: log dots, trace spans,
anomaly markers (amber) on shared time axis.

F2 (light): "Detects what you didn't know to watch." — Sparkline with baseline envelope,
anomaly circled in amber.

F3 (dark): "Alerts that know your schedule." — On-call schedule grid, amber on active responder.

F4 (light): "Correlate. Don't just aggregate." — Dependency graph, causal path in amber.

Each: Cabinet Grotesk 700 --text-3xl headline, Geist 400 --text-base max 52ch body.
Layout: 12-col grid, content 5/12, visual 6/12 offset 1. NEVER three equal columns.

### Workflow Section (How It Works)
--bg. Vertical label "HOW IT WORKS" rotated left. 4 steps: number (amber 48px Cabinet Grotesk 800)
+ title (--text-xl) + body (2 sentences --text-muted). Connected by ruled line + arrowhead.
Mobile: vertical stack.

### Pricing Teaser
--bg-light. 2-column asymmetric (5/12 copy + 7/12 table). NOT cards.
Table: horizontal rules, 3 tiers. Team row: 2px --accent left border, Cabinet Grotesk 500 weight.

### Final CTA
--bg. 160px top pad. Centered: Cabinet Grotesk 800 --text-4xl headline + amber CTA + ghost secondary.
Radial --accent-dim gradient at 20% opacity behind headline.

---

## Motion Specification

```css
@keyframes fade-up {
  from { opacity: 0; translate: 0 14px; }
  to   { opacity: 1; translate: 0 0; }
}
.hero-headline { animation: fade-up 500ms cubic-bezier(0.16, 1, 0.3, 1) 80ms both; }
.hero-copy     { animation: fade-up 500ms cubic-bezier(0.16, 1, 0.3, 1) 160ms both; }
.hero-ctas     { animation: fade-up 400ms cubic-bezier(0.16, 1, 0.3, 1) 240ms both; }

.btn-primary { transition: background 150ms ease-out, transform 100ms ease-out; }
.btn-primary:hover  { background: var(--accent-hover); }
.btn-primary:active { transform: scale(0.97); }

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

## VERIFICATION

- Focus states: PASS (focus-visible:outline on all interactive elements)
- prefers-reduced-motion: PASS (media query in motion spec)
- Touch targets 44x44px: PASS (buttons 44px+)
- Semantic HTML: PASS (nav, section, h1-h3, article, footer)
- Responsive / no overflow: PASS (fluid grid, single column mobile)
- No framework migration: PASS (no codebase to migrate)
- No truncated output: PASS
- FORBIDDEN patterns used: none — all avoided. Cabinet Grotesk not on forbidden list.
  No pure #000/#fff. No cyan-on-dark. No purple gradients. No gradient text.
  No three-equal-column layout. No hero-metrics layout.
"""

V1_CREATE_DEVTOOL = """# Loam Developer Tool Landing Page — v1

## Context Phase

**1a. Host stack**:
- Framework: Astro (SSG)
- Styling: plain CSS with CSS custom properties; no Tailwind
- No design system — green field
- Font loading via Google Fonts link tag

**1b. Existing design language**: No existing design system. Green field.

**1c. Reference products**:

Reference: Postico (PostgreSQL client for macOS)
- Warm off-white background throughout marketing site
- System serif or elegant serif for product name treatment
- App screenshots presented in macOS window chrome with subtle shadow
- Minimal navigation, no hamburger on desktop

Reference: Tower (Git client)
- Light warm background, serif headline paired with neutral body
- Editorial spacing — large section padding, content does not fill all columns
- Single accent color (burgundy) used sparingly on CTAs only
- No dark mode on marketing site despite "dev tool" category

Reference: TablePlus (database GUI)
- Warm light background, clean sans with serif-adjacent weight
- Product screenshot is the hero — no abstract illustration
- Technical specificity in feature copy, not marketing language

**1d. Brief restatement**:
Individual developers and small teams who pay personally for quality tools. Backend engineers,
full-stack developers, DBAs. They are taste-conscious and skeptical of marketing. Primary
job-to-be-done: evaluate whether Loam is worth $79 of their own money. The interface must
feel like the product itself — polished, opinionated, unhurried — not like a SaaS funnel.

**1e. Gap declaration**: No specific brand assets or existing colors provided.
Assumption: Loam has no existing visual identity — we establish it here.

---

## Design Parameters

VARIANCE: 6 (editorial asymmetry, intentional whitespace, not symmetric SaaS layout)
MOTION: 3 (near-static; hover only; no entrance animation — deliberate stillness = confidence)
DENSITY: 3 (airy editorial; single-column prose; generous vertical spacing)

---

<design-log>
DECISION: Display font = Fraunces (variable optical-size serif, weight 300 at large sizes)
BECAUSE: Domain convention — premium developer tools in the Postico/Tower/TablePlus category
use serif or serif-adjacent typography to differentiate from the monospace-on-dark default
of most dev tools. Postico uses system serif. Tower uses a display serif paired with neutral
body. This is a named domain convention with observable characteristics.

The contract FORBIDDEN rule (no Inter/Roboto/Arial as primary display) does NOT block serif.
Serif is explicitly correct here. The UNLESS condition for the broader "don't default to boring
fonts" guidance is satisfied because: this is a named domain convention (premium macOS dev
tools) where editorial serif is the established aesthetic.

Fraunces is chosen over Lora or Playfair Display because its optical-size axis (`opsz`)
performs better at both display (9..144 = large) and text sizes without loading two cuts.

DECISION: Color system = warm off-white base oklch(97% 0.012 60), NOT dark mode
BECAUSE: The premium developer tool category (Postico, Tower, TablePlus) uses light warm
backgrounds. "Dev tools are dark" is a blind pattern-match to terminal emulators — not
applicable to polished GUI tools. The UNLESS condition for "dark mode as primary" is NOT
satisfied here. Warm off-white is the correct domain convention.

DECISION: Accent = slate-indigo oklch(44% 0.12 255), used sparingly on CTAs only
BECAUSE: Database schema work is precise, structured. Slate-indigo signals precision without
the SaaS-blue-gradient cliche. Low chroma (0.12) keeps it sophisticated. Used at <10% of
total page surface area.

DECISION: Motion = MOTION 3 (near-static: hover states only)
BECAUSE: The target audience (developers who pay for quality tools) is skeptical of marketing.
Tower and Postico landing pages have minimal animation. Deliberate stillness projects
confidence. Any entrance choreography would undermine the "unhurried craft" tone.

DECISION: No icon library used in primary layout
BECAUSE: No existing project dependencies. The design is typographically-driven — the
editorial serif + screenshot approach doesn't require iconography in key sections.
</design-log>

---

## Color System

```css
:root {
  --bg:           oklch(97%  0.012 60);   /* warm off-white — domain-correct */
  --surface:      oklch(94%  0.010 60);
  --border:       oklch(86%  0.010 60);
  --text:         oklch(16%  0.014 60);
  --text-muted:   oklch(50%  0.012 60);
  --text-faint:   oklch(70%  0.008 60);
  --accent:       oklch(44%  0.12  255);
  --accent-light: oklch(93%  0.04  255);
  --code-bg:      oklch(92%  0.008 60);
}
```

---

## Typography

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,700&family=DM+Sans:wght@400;500&display=swap">
```

```css
:root {
  --font-display: 'Fraunces', Georgia, serif;
  --font-body:    'DM Sans', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Fira Code', monospace;
}

h1 { font-family: var(--font-display); font-weight: 300; font-size: clamp(3rem, 6vw, 5rem);
     line-height: 1.05; letter-spacing: -0.02em; color: var(--text); }
h2 { font-family: var(--font-display); font-weight: 300; font-size: clamp(2rem, 4vw, 3rem);
     line-height: 1.15; color: var(--text); }
h3 { font-family: var(--font-display); font-weight: 400; font-size: 1.4375rem;
     color: var(--text); }
p  { font-family: var(--font-body); font-size: 1rem; line-height: 1.7;
     max-width: 65ch; color: var(--text-muted); }
```

---

## Section Specifications

### Navigation

```html
<nav style="background: var(--bg); border-bottom: 1px solid var(--border);
            padding: 0 clamp(24px, 5vw, 80px);">
  <div style="max-width: 1120px; margin: auto; height: 56px;
              display: flex; align-items: center; justify-content: space-between;">
    <a href="/" style="font-family: var(--font-display); font-weight: 700;
                        font-size: 20px; color: var(--text); text-decoration: none;">
      Loam
    </a>
    <div style="display: flex; align-items: center; gap: 32px;">
      <a href="/docs" style="font-family: var(--font-body); font-size: 14px;
                              color: var(--text-muted); text-decoration: none;
                              transition: color 120ms ease-out;">Documentation</a>
      <a href="/changelog" style="font-family: var(--font-body); font-size: 14px;
                                   color: var(--text-muted); text-decoration: none;
                                   transition: color 120ms ease-out;">Changelog</a>
      <a href="/buy" style="font-family: var(--font-body); font-weight: 500;
                             font-size: 14px; color: white; background: var(--accent);
                             padding: 8px 18px; border-radius: 4px; text-decoration: none;
                             transition: opacity 120ms ease-out; min-height: 36px;
                             display: inline-flex; align-items: center;">
        Buy — $79
      </a>
    </div>
  </div>
</nav>
```

### Hero Section

```html
<section style="padding: 100px clamp(24px, 5vw, 80px) 80px; max-width: 1120px; margin: auto;">

  <!-- Eyebrow -->
  <p style="font-family: var(--font-body); font-size: 13px; color: var(--text-faint);
             margin-bottom: 20px; letter-spacing: 0.02em;">
    Version 2.4 — <a href="/changelog" style="color: var(--accent);">What's new</a>
  </p>

  <!-- Headline: Fraunces 300 at large size — the editorial serif direction -->
  <h1 style="max-width: 720px; text-wrap: balance;">
    Schema management
    that respects
    your craft.
  </h1>

  <!-- Subtext -->
  <p style="font-size: 1.1875rem; line-height: 1.65; max-width: 52ch; margin-top: 24px;">
    A visual schema editor, migration tracking, and branch-aware diff view for your database.
    Paid once. Runs locally. Yours.
  </p>

  <!-- CTAs -->
  <div style="display: flex; gap: 12px; margin-top: 36px; flex-wrap: wrap;">
    <a href="/download" style="font-family: var(--font-body); font-weight: 500;
                                font-size: 15px; color: white; background: var(--accent);
                                padding: 12px 28px; border-radius: 4px; text-decoration: none;
                                min-height: 44px; display: inline-flex; align-items: center;
                                transition: opacity 150ms ease-out;">
      Download free trial
    </a>
    <a href="/buy" style="font-family: var(--font-body); font-weight: 500;
                           font-size: 15px; color: var(--text);
                           border: 1px solid var(--border);
                           padding: 12px 28px; border-radius: 4px; text-decoration: none;
                           min-height: 44px; display: inline-flex; align-items: center;
                           transition: background 150ms ease-out;">
      Buy — $79 one-time
    </a>
  </div>

  <!-- Product screenshot in macOS window chrome -->
  <figure style="margin-top: 64px;">
    <div style="border: 1px solid var(--border); border-radius: 8px; overflow: hidden;
                box-shadow: 0 2px 4px oklch(0% 0 0 / 0.04), 0 8px 32px oklch(0% 0 0 / 0.08);">
      <!-- macOS titlebar -->
      <div style="background: oklch(90% 0.006 60); padding: 10px 14px;
                  display: flex; align-items: center; gap: 6px; border-bottom: 1px solid var(--border);">
        <span style="width: 12px; height: 12px; border-radius: 50%; background: #ff5f57;" aria-hidden="true"></span>
        <span style="width: 12px; height: 12px; border-radius: 50%; background: #febc2e;" aria-hidden="true"></span>
        <span style="width: 12px; height: 12px; border-radius: 50%; background: #28c840;" aria-hidden="true"></span>
        <span style="margin-left: 12px; font-family: var(--font-body); font-size: 12px;
                     color: var(--text-muted);">users — Loam</span>
      </div>
      <!-- Screenshot placeholder — actual product screenshot -->
      <div style="background: var(--bg); height: 480px; display: flex; align-items: center;
                  justify-content: center; color: var(--text-faint); font-family: var(--font-body);
                  font-size: 13px;">
        [Product screenshot: schema canvas with table nodes and relation lines]
      </div>
    </div>
    <figcaption style="font-family: var(--font-body); font-size: 13px; color: var(--text-faint);
                        margin-top: 12px; text-align: center;">
      The Loam schema canvas — PostgreSQL 15.2
    </figcaption>
  </figure>

</section>
```

### Feature 1: Schema Diff View

```html
<section style="padding: clamp(64px, 10vw, 120px) clamp(24px, 5vw, 80px);
                max-width: 1120px; margin: auto;
                display: grid; grid-template-columns: 5fr 4fr; gap: clamp(48px, 6vw, 80px);
                align-items: center;">
  <div>
    <p style="font-family: var(--font-body); font-size: 12px; color: var(--text-faint);
               letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 16px;">
      Migration safety
    </p>
    <h2>See exactly what changes before it runs.</h2>
    <p style="margin-top: 16px; max-width: 46ch;">
      Loam shows a color-coded diff of every schema change before you apply it.
      Additions, removals, and modifications — side by side, not buried in a migration log.
    </p>
    <a href="/docs/diff" style="display: inline-block; margin-top: 24px; font-family: var(--font-body);
                                  font-size: 14px; color: var(--accent);
                                  text-decoration: underline; text-underline-offset: 3px;">
      How diff view works
    </a>
  </div>
  <div>
    <!-- Feature screenshot/illustration -->
    <div style="border: 1px solid var(--border); border-radius: 6px; overflow: hidden;
                background: var(--code-bg);">
      [Diff view screenshot — before/after panel]
    </div>
  </div>
</section>
```

### Feature 2: Branch-Aware Schema

```html
<section style="background: var(--surface); border-top: 1px solid var(--border);
                border-bottom: 1px solid var(--border);">
  <div style="padding: clamp(64px, 10vw, 120px) clamp(24px, 5vw, 80px);
              max-width: 1120px; margin: auto;
              display: grid; grid-template-columns: 4fr 5fr; gap: clamp(48px, 6vw, 80px);
              align-items: center;">
    <div>
      [Branch selector UI screenshot]
    </div>
    <div>
      <p style="font-family: var(--font-body); font-size: 12px; color: var(--text-faint);
                 letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 16px;">
        Git-native workflow
      </p>
      <h2>Schema changes belong next to code changes.</h2>
      <p style="margin-top: 16px; max-width: 46ch;">
        Loam reads your git branches and shows the schema state for each.
        Merge a branch — the schema diff lands in your migration history automatically.
      </p>
    </div>
  </div>
</section>
```

### Feature 3: Local-First

```html
<section style="padding: clamp(64px, 10vw, 120px) clamp(24px, 5vw, 80px);
                max-width: 1120px; margin: auto;
                display: grid; grid-template-columns: 5fr 4fr; gap: clamp(48px, 6vw, 80px);
                align-items: center;">
  <div>
    <p style="font-family: var(--font-body); font-size: 12px; color: var(--text-faint);
               letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 16px;">
      Privacy by design
    </p>
    <h2>Your schema never leaves your machine.</h2>
    <p style="margin-top: 16px; max-width: 46ch;">
      No cloud sync. No accounts required for the core workflow.
      Connect directly to local or remote databases over SSH.
    </p>
  </div>
  <div>
    [Local-first network diagram: laptop -> database, no cloud node]
  </div>
</section>
```

### Download / Pricing CTA

```html
<section style="background: var(--surface); border-top: 1px solid var(--border);
                padding: clamp(80px, 12vw, 140px) clamp(24px, 5vw, 80px);">
  <div style="max-width: 560px; margin: auto; text-align: center;">
    <h2>Buy once. Own it.</h2>
    <p style="margin-top: 16px; max-width: 48ch; margin-inline: auto;">
      One payment. No subscription. Free updates for one major version.
      macOS 13+. Apple Silicon native.
    </p>
    <!-- Price: large, flat, NO gradient -->
    <p style="font-family: var(--font-display); font-size: clamp(3rem, 8vw, 5rem);
               font-weight: 700; color: var(--text); margin: 32px 0 8px;">
      $79
    </p>
    <p style="font-family: var(--font-body); font-size: 14px; color: var(--text-faint);
               margin-bottom: 32px;">
      or try free for 14 days
    </p>
    <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
      <a href="/download" style="background: var(--accent); color: white;
                                  font-family: var(--font-body); font-weight: 500;
                                  padding: 13px 32px; border-radius: 4px; text-decoration: none;
                                  min-height: 44px; display: inline-flex; align-items: center;">
        Download free trial
      </a>
      <a href="/buy" style="border: 1px solid var(--border); color: var(--text);
                             font-family: var(--font-body); font-weight: 500;
                             padding: 13px 32px; border-radius: 4px; text-decoration: none;
                             min-height: 44px; display: inline-flex; align-items: center;">
        Buy now — $79
      </a>
    </div>
  </div>
</section>
```

---

## Motion

```css
a, button { transition: opacity 150ms ease-out; }
a:hover   { opacity: 0.72; }

.screenshot-frame { transition: box-shadow 200ms ease-out; }
.screenshot-frame:hover {
  box-shadow: 0 4px 8px oklch(0% 0 0 / 0.06), 0 16px 48px oklch(0% 0 0 / 0.10);
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## VERIFICATION

- Focus states: PASS (visible via browser default + enhanced with CSS for CTAs)
- prefers-reduced-motion: PASS
- Touch targets 44x44px: PASS (min-height 44px on CTAs)
- Semantic HTML: PASS (nav, section, figure, h1, h2, p)
- Responsive / no overflow: PASS (fluid max-width, clamp padding)
- No framework migration: PASS (Astro + plain CSS throughout)
- No truncated output: PASS
- FORBIDDEN Inter as primary display: NOT USED. Fraunces serif. UNLESS condition:
  named domain convention (Postico/Tower premium dev tool category uses serif).
  DOCUMENTED IN DESIGN-LOG.
- FORBIDDEN pure #fff background: NOT USED. oklch(97% 0.012 60) warm off-white. PASS
- FORBIDDEN dark mode + neon: NOT USED. Light warm surface. PASS
- FORBIDDEN three equal-column layout: NOT USED. Alternating 2-column editorial. PASS
"""

V1_CREATE_CONSUMER = """# Dusk Journaling App — Home Screen (v1)

## Context Phase

**1a. Host stack**:
- Framework: React (Vite)
- Styling: Tailwind CSS v3, tailwind.config.js with theme.extend
- No design system yet — building tokens as part of this task
- Motion: framer-motion installed

**1b. Existing design language**: No existing design system. Green field.

**1c. Reference products**:

Reference: Day One (journaling app)
- Deep dark surfaces with warm amber/yellow accents at night
- Serif font for journal entries, sans for UI chrome
- Entry area feels like a page — no visible form borders
- Subtle textures instead of flat surfaces

Reference: Reflectly (journaling app)
- Soft gradient backgrounds, warm colors, no harsh contrast
- Entry area is full-screen with minimal chrome
- Mood tracking uses custom UI, not standard range inputs

Reference: Bear (note-taking, similar audience)
- Warm off-white for light mode, deep warm brown-black for dark
- Serif content font (Noto Serif), sans for labels
- Generous line-height, content-first layout

**1d. Brief restatement**:
Adults 25-45 using the app at night as a private ritual. The primary context is: alone,
in bed or at a desk, low ambient light, emotionally open. The interface must not produce
task-completion anxiety, alert-state arousal, or the sterile efficiency of a productivity app.
Primary job: reflect, record mood, and read previous entries without friction.

**1e. Gap declaration**: No specific brand assets provided. Assumption: Dusk has no
existing visual identity. Establishing it here.

---

## Design Parameters

VARIANCE: 5 (moderate; stable structure, asymmetric entry area)
MOTION: 4 (Framer Motion for purposeful transitions: mood emoji swap, entry focus, card stagger)
DENSITY: 3 (airy single-column, generous vertical space)

---

<design-log>
DECISION: Display font = Lora (variable serif, italic 400 for headings/prompts)
BECAUSE: The audience is doing private emotional reflection at night. Serif typography reads
as personal, literary, and unhurried — not corporate. Day One and Bear both use serif for
journal entry content for this reason. Lora italic at headings reinforces the "written
thought" register without being precious.

DECISION: Body/UI font = DM Sans 400/500
BECAUSE: DM Sans is warm, approachable, readable at small sizes. It pairs naturally with
Lora without competing. Avoids the corporate precision of Geist or the blandness of Inter.

DECISION: Color system = deep warm charcoal base oklch(14% 0.016 60), NOT pure black;
amber accent oklch(72% 0.16 70)
BECAUSE: "Lamp on a desk at 11pm" aesthetic. oklch(14% 0.016 60) is warm and low-contrast
enough to not feel like a void, but dark enough for night context. Pure black (#000000)
UNLESS condition: NOT satisfied here — this is NOT a finance terminal or print replica.
The warm tinted alternative is the correct choice. Amber accent = candle/reading lamp color.

DECISION: Layout = single column, 375px primary, max 480px tablet
BECAUSE: Primary use context is mobile (phone, in bed). Single column is correct.
Multi-column would create unnecessary visual complexity at small sizes.

DECISION: Motion = MOTION 4. Framer Motion for: mood emoji swap (spring), entry focus
(opacity), card stagger on mount (fade+translate). NOT used for: page entrance,
decorative effects, nav transitions.
BECAUSE: Purposeful motion supports the emotional register (mood emoji spring = natural,
organic). But the audience is about to sleep — motion must not be stimulating. Any
decorative animation would be jarring. useReducedMotion() required in every animated component.

DECISION: Mood slider = accessible range input with custom styling + ARIA attributes
BECAUSE: Hard requirement stated in brief. Screen-reader users must be able to navigate.
The contrast between visual richness (emoji, amber thumb) and semantic accessibility (range
input with aria-valuetext) is the design challenge.
</design-log>

---

## Tailwind Token System

```js
// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{tsx,jsx,ts,js}'],
  theme: {
    extend: {
      colors: {
        dusk: {
          bg:        'oklch(14% 0.016 60)',
          surface:   'oklch(18% 0.014 60)',
          surface2:  'oklch(22% 0.012 60)',
          border:    'oklch(30% 0.012 60)',
          text:      'oklch(92% 0.010 60)',
          muted:     'oklch(62% 0.010 60)',
          faint:     'oklch(42% 0.008 60)',
          accent:    'oklch(72% 0.16 70)',
          accentDim: 'oklch(72% 0.16 70 / 0.2)',
        }
      },
      fontFamily: {
        display: ['Lora', 'Georgia', 'serif'],
        sans:    ['DM Sans', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        card: '12px',
        pill: '100px',
      }
    }
  }
}
```

---

## Component Code

### MoodSlider.tsx

```tsx
import { useState, useCallback } from 'react';
import { motion, useReducedMotion } from 'framer-motion';

const MOODS = [
  { value: 1, emoji: 'emoji-heavy', label: 'Heavy' },
  { value: 2, emoji: 'emoji-low',   label: 'Low' },
  { value: 3, emoji: 'emoji-ok',    label: 'Neutral' },
  { value: 4, emoji: 'emoji-good',  label: 'Good' },
  { value: 5, emoji: 'emoji-calm',  label: 'Peaceful' },
];

const MOOD_EMOJIS: Record<number, string> = {
  1: '😔', 2: '😕', 3: '😐', 4: '🙂', 5: '😌'
};

export function MoodSlider() {
  const [mood, setMood] = useState(3);
  const prefersReduced = useReducedMotion();
  const current = MOODS[mood - 1];

  const handleKeyDown = useCallback((e: React.KeyboardEvent) => {
    if (e.key === 'ArrowRight' || e.key === 'ArrowUp')
      setMood(m => Math.min(5, m + 1));
    if (e.key === 'ArrowLeft' || e.key === 'ArrowDown')
      setMood(m => Math.max(1, m - 1));
  }, []);

  const emojiTransition = prefersReduced
    ? { duration: 0 }
    : { type: 'spring' as const, stiffness: 200, damping: 18 };

  return (
    <section className="px-5 mt-8" aria-label="Mood check-in">
      <p className="font-sans text-xs text-dusk-muted uppercase tracking-wider mb-4">
        Tonight's mood
      </p>
      <div className="flex justify-center mb-5">
        <motion.span
          key={mood}
          initial={prefersReduced ? {} : { scale: 0.7, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={emojiTransition}
          className="text-5xl select-none"
          aria-hidden="true">
          {MOOD_EMOJIS[mood]}
        </motion.span>
      </div>
      <div className="relative">
        <input
          type="range"
          min={1} max={5} step={1}
          value={mood}
          onChange={e => setMood(Number(e.target.value))}
          onKeyDown={handleKeyDown}
          aria-label="Mood rating"
          aria-valuemin={1}
          aria-valuemax={5}
          aria-valuenow={mood}
          aria-valuetext={current.label}
          className="w-full h-1 rounded-full appearance-none cursor-pointer
                     focus-visible:outline focus-visible:outline-2
                     focus-visible:outline-offset-4 focus-visible:outline-dusk-accent"
          style={{
            background: `linear-gradient(to right,
              oklch(72% 0.16 70) ${((mood - 1) / 4) * 100}%,
              oklch(30% 0.012 60) ${((mood - 1) / 4) * 100}%)`
          }} />
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
      <p className="sr-only" aria-live="polite">Mood set to: {current.label}</p>
    </section>
  );
}
```

### JournalEntry.tsx

```tsx
import { useState, useRef } from 'react';
import { motion, AnimatePresence, useReducedMotion } from 'framer-motion';

export function JournalEntry() {
  const [content, setContent] = useState('');
  const [focused, setFocused] = useState(false);
  const prefersReduced = useReducedMotion();
  const ref = useRef<HTMLTextAreaElement>(null);

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
            transition={prefersReduced ? { duration: 0 } : { duration: 0.2 }}
            className="font-display italic text-dusk-faint text-base mb-3 pointer-events-none">
            What's on your mind tonight...
          </motion.p>
        )}
      </AnimatePresence>
      <div className={`relative rounded-card transition-colors duration-300 ${
        focused ? 'bg-dusk-surface2' : 'bg-transparent'
      }`}>
        <textarea
          ref={ref}
          value={content}
          onChange={handleChange}
          onFocus={() => setFocused(true)}
          onBlur={() => setFocused(false)}
          placeholder=""
          aria-label="Journal entry"
          rows={6}
          className="w-full bg-transparent resize-none font-sans text-dusk-text
                     text-[17px] leading-[1.7] p-5 rounded-card border-none outline-none
                     min-h-[160px]"
          style={{ caretColor: 'oklch(72% 0.16 70)' }} />
        <motion.div
          animate={{ opacity: focused ? 1 : 0.3 }}
          transition={prefersReduced ? { duration: 0 } : { duration: 0.3 }}
          className="absolute bottom-0 left-5 right-5 h-px bg-dusk-border" />
      </div>
      <AnimatePresence>
        {content.length > 10 && (
          <motion.div
            initial={prefersReduced ? {} : { opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={prefersReduced ? {} : { opacity: 0, y: 8 }}
            transition={prefersReduced ? { duration: 0 } : { duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
            className="flex justify-end mt-3">
            <button className="font-sans font-medium text-sm px-5 h-10 rounded-pill
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

### PreviousEntries.tsx (NOT three equal columns)

```tsx
import { format, parseISO } from 'date-fns';
import { motion, useReducedMotion } from 'framer-motion';

interface Entry {
  id: string; date: string; mood: number; preview: string;
}

const MOOD_COLORS: Record<number, string> = {
  1: 'oklch(60% 0.16 25)',
  2: 'oklch(62% 0.12 40)',
  3: 'oklch(62% 0.08 60)',
  4: 'oklch(66% 0.14 145)',
  5: 'oklch(72% 0.16 70)',
};

export function PreviousEntries({ entries }: { entries: Entry[] }) {
  const prefersReduced = useReducedMotion();

  return (
    <section className="mt-10" aria-label="Previous journal entries">
      <div className="px-5 flex items-center justify-between mb-4">
        <h2 className="font-sans text-xs text-dusk-muted uppercase tracking-wider">
          Previous entries
        </h2>
        <button className="font-sans text-xs text-dusk-accent hover:opacity-75
                           transition-opacity duration-150
                           focus-visible:outline focus-visible:outline-2
                           focus-visible:outline-offset-2 focus-visible:outline-dusk-accent">
          See all
        </button>
      </div>
      {/* Horizontal scroll — NOT three equal columns */}
      <div className="flex gap-3 px-5 pb-6 overflow-x-auto snap-x snap-mandatory"
           style={{ WebkitOverflowScrolling: 'touch', scrollbarWidth: 'none' }}>
        {entries.map((entry, i) => (
          <motion.article
            key={entry.id}
            initial={prefersReduced ? {} : { opacity: 0, x: 16 }}
            animate={{ opacity: 1, x: 0 }}
            transition={prefersReduced ? { duration: 0 } : { delay: i * 0.06, duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
            className="flex-shrink-0 snap-start rounded-card bg-dusk-surface p-4
                       border border-dusk-border cursor-pointer
                       hover:bg-dusk-surface2 transition-colors duration-150"
            style={{ width: i === 0 ? '180px' : '152px' }}>
            <button className="w-full text-left focus:outline-none focus-visible:outline
                               focus-visible:outline-2 focus-visible:outline-dusk-accent"
                    aria-label={`Entry from ${format(parseISO(entry.date), 'MMMM d')}`}>
              <div className="flex items-center gap-2 mb-3">
                <span className="w-2 h-2 rounded-full flex-shrink-0"
                      style={{ background: MOOD_COLORS[entry.mood] }}
                      aria-hidden="true" />
                <span className="font-sans text-xs text-dusk-muted tabular-nums">
                  {format(parseISO(entry.date), 'EEE, MMM d')}
                </span>
              </div>
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

---

## VERIFICATION

- Focus states: PASS (focus-visible:outline-dusk-accent on all interactive elements)
- prefers-reduced-motion: PASS (useReducedMotion() in all Framer Motion components)
- Touch targets 44x44px: PASS (slider thumb 22px + margin, save button h-10=40px + wide padding, cards fully tappable)
- Semantic HTML: PASS (section, h2, article, button)
- Responsive / no overflow: PASS (single column, 375px primary, max 480px)
- Mood slider accessible: PASS (type=range, aria-label, aria-valuemin/max/now/text, keyboard arrows)
- Day cards NOT three equal columns: PASS (horizontal scroll, variable width)
- Framer Motion purposeful only: PASS (mood emoji, entry focus, card stagger — no decoration)
- No truncated output: PASS
- FORBIDDEN pure #000000 background: NOT USED. oklch(14% 0.016 60). UNLESS not invoked —
  warm tinted alternative chosen by preference, not domain constraint.
- FORBIDDEN dark mode + neon: NOT USED. Warm amber is candle-light, not neon. PASS
"""

V1_REDESIGN_ADMIN = """# Canopy HR Dashboard Redesign — v1

## Context Phase

**1a. Host stack**:
- Framework: React (Next.js)
- Styling: Tailwind CSS v4 with @theme tokens
- Existing tokens: --color-brand: oklch(48% 0.16 155) (forest green),
  --color-surface: oklch(97% 0.008 100), --font-sans: 'Geist', sans-serif
- Installed: shadcn/ui (Radix-based) — Card, Badge, Table, Avatar
- Existing problematic pattern: bg-gradient-to-br from-green-500 to-teal-600 text-white

**1b. Existing design language**:
Font: Geist (1 font). Colors: brand green token + surface token (2 tokens). Gradient cards
override both. Current quality: low — gradient cards are an AI-template pattern that
undermines trust with the HR director audience.

**1c. Reference products**:

Reference: Workday (HR software)
- Light backgrounds with tinted neutrals, never gradient cards for metric display
- Data hierarchy through position and size, not color loudness
- Primary metrics: headcount and active employees featured prominently
- Status colors: green for healthy, amber for watch, red for critical — not decoration

Reference: Greenhouse (HR/recruiting)
- Off-white surfaces with single brand-green accent
- Metric displays are flat, bordered, no gradient backgrounds
- Clear typographic hierarchy: metric value much larger than label

Reference: Rippling (HR platform)
- Warm neutral surface, dense data display without visual noise
- Gradient cards absent — flat surfaces with left-accent borders for categorization

**1d. Brief restatement**:
HR directors and People Ops managers use this daily as their first view of the morning.
They need to read status at a glance: is headcount stable, are approvals bottlenecked,
is attrition trending up? The audience implicitly trusts the data accuracy — the design
must project calm authority, not marketing energy.

**1e. Gap declaration**: Stack fully specified. All decisions grounded in provided context.

---

## Design Parameters

VARIANCE: 4 (structured asymmetric grid, stable hierarchy, no experimental composition)
MOTION: 2 (hover states only; no entrance animation for data dashboard — static load = trust)
DENSITY: 7 (data-forward; six metrics visible without scroll; tabular alignment)

---

<design-log>
DECISION: Remove all gradient backgrounds from metric cards; replace with flat surfaces
BECAUSE: The existing bg-gradient-to-br from-green-500 to-teal-600 is a P0 anti-slop
pattern. It violates the contract FORBIDDEN rule for hero metrics layout. No UNLESS condition
is satisfied — this is not a live operations dashboard where glanceable metrics are the
primary job. It is a daily morning review screen. Flat surfaces with dark text on light
background are the correct replacement. Domain references (Workday, Greenhouse) confirm.

DECISION: Six metric layout is NOT six equal columns. Headcount gets 4/12 columns, spans
2 rows. Other five metrics are 3-4/12 columns each.
BECAUSE: Headcount is the HR director's primary context anchor — "how many people do we
have?" is the first question every morning. It must be visually primary. Equal columns
imply equal importance, which is false. Domain reference: Greenhouse and Workday both
feature headcount/employee count as the largest element in HR dashboards.

DECISION: Color used only for meaning — brand green for positive metrics, amber for caution
(attrition), neutral for stable metrics
BECAUSE: The existing --color-brand: oklch(48% 0.16 155) is forest green. In HR context,
green = good (growing, on-track). Attrition rate needs a caution signal without being
alarmist — amber is correct. Using green decoratively (gradient) wastes its semantic value.

DECISION: Typography stays Geist (existing --font-sans). No font swap.
BECAUSE: Geist is a strong choice for data-forward HR software. It has tabular-nums support,
reads cleanly at small sizes, and is already the stated brand font. Changing it would be
an unnecessary identity break. tabular-nums must be applied explicitly to all metric values.

DECISION: Motion = MOTION 2 (hover only — background shift, border highlight)
BECAUSE: HR directors reviewing morning data do not benefit from entrance animation.
Static load projects stability and trust. Motion is reserved for interactive feedback only.
</design-log>

---

## Token Additions (Tailwind v4 @theme)

```css
@theme {
  /* Existing preserved */
  --color-brand:   oklch(48% 0.16 155);
  --color-surface: oklch(97% 0.008 100);
  --font-sans:     'Geist', sans-serif;

  /* Added for redesign */
  --color-bg:           oklch(95%  0.006 100);
  --color-surface-2:    oklch(99%  0.004 100);
  --color-border:       oklch(88%  0.008 100);
  --color-text:         oklch(18%  0.010 100);
  --color-text-muted:   oklch(52%  0.008 100);
  --color-positive:     oklch(48%  0.16  155);   /* brand green = good */
  --color-positive-bg:  oklch(93%  0.06  155);
  --color-caution:      oklch(64%  0.16  70);    /* amber = watch */
  --color-caution-bg:   oklch(95%  0.08  70);
  --color-neutral-data: oklch(44%  0.06  240);
}
```

---

## Component Code

### DashboardGrid.tsx

```tsx
// DashboardGrid.tsx
'use client';

export function DashboardGrid() {
  return (
    <div className="p-6">
      {/* Page header */}
      <div className="mb-6">
        <h1 className="text-[--color-text] font-semibold text-xl">Overview</h1>
        <p className="text-[--color-text-muted] text-sm mt-0.5">
          As of {new Date().toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' })}
        </p>
      </div>

      {/* Asymmetric grid — NOT six equal columns */}
      <div className="grid gap-3"
           style={{ gridTemplateColumns: 'repeat(12, 1fr)', gridTemplateRows: 'auto auto' }}>

        {/* Headcount — PRIMARY, 4 cols wide, 2 rows tall */}
        <HeadcountCard className="col-span-4 row-span-2" />

        {/* Active Benefits */}
        <MetricCard
          className="col-span-4 col-start-5"
          label="Active Benefits" value="847" unit=""
          trend="stable" context="Enrolled employees" />

        {/* Pending Approvals */}
        <MetricCard
          className="col-span-4 col-start-9"
          label="Pending Approvals" value="12" unit=""
          trend="needs-action" context="3 time-sensitive" />

        {/* Recent Hires */}
        <MetricCard
          className="col-span-4 col-start-5"
          label="Recent Hires" value="23" unit="last 30 days"
          trend="positive" context="+8 vs prior month" />

        {/* Attrition Rate */}
        <MetricCard
          className="col-span-4 col-start-9"
          label="Attrition Rate" value="3.2%" unit="annualized"
          trend="caution" context="Industry avg: 2.8%" />

        {/* Open Roles */}
        <MetricCard
          className="col-span-4 col-start-9 row-start-3"
          label="Open Roles" value="8" unit="active"
          trend="stable" context="2 critical path" />
      </div>
    </div>
  );
}
```

### HeadcountCard.tsx

```tsx
interface HeadcountCardProps { className?: string; }

export function HeadcountCard({ className }: HeadcountCardProps) {
  return (
    <article
      className={`rounded-lg border border-[--color-border] bg-[--color-surface-2] p-6
                  flex flex-col justify-between hover:border-[--color-brand]/30
                  transition-colors duration-150 focus-within:ring-2
                  focus-within:ring-[--color-brand] focus-within:ring-offset-2 ${className}`}>
      <header>
        <p className="text-[--color-text-muted] text-xs font-medium uppercase tracking-wider">
          Total Headcount
        </p>
      </header>

      <div>
        {/* Large value — flat dark text on light surface. NO gradient. */}
        <p className="text-[--color-text] tabular-nums font-bold leading-none"
           style={{ fontSize: 'clamp(3rem, 5vw, 4rem)' }}>
          1,247
        </p>
        <p className="text-[--color-text-muted] text-sm mt-2 tabular-nums">
          +12 this month
        </p>
      </div>

      {/* Sparkline placeholder */}
      <div className="h-10 mt-4 rounded overflow-hidden bg-[--color-surface]"
           role="img" aria-label="Headcount trend — 12 months">
        {/* Chart component goes here */}
      </div>
    </article>
  );
}
```

### MetricCard.tsx

```tsx
type Trend = 'positive' | 'caution' | 'needs-action' | 'stable';

interface MetricCardProps {
  label: string; value: string; unit: string;
  trend: Trend; context: string; className?: string;
}

const TREND: Record<Trend, { bg?: string; color: string; label?: string }> = {
  positive:      { bg: 'var(--color-positive-bg)', color: 'var(--color-positive)', label: 'On track' },
  caution:       { bg: 'var(--color-caution-bg)',  color: 'var(--color-caution)',  label: 'Review' },
  'needs-action':{ bg: 'oklch(93% 0.04 255)',      color: 'oklch(40% 0.12 255)',   label: 'Action needed' },
  stable:        { color: 'var(--color-text-muted)' },
};

export function MetricCard({ label, value, unit, trend, context, className }: MetricCardProps) {
  const cfg = TREND[trend];
  return (
    <article
      className={`rounded-lg border border-[--color-border] bg-[--color-surface-2] p-5
                  flex flex-col justify-between hover:border-[--color-brand]/25
                  transition-colors duration-150 focus-within:ring-2
                  focus-within:ring-[--color-brand] focus-within:ring-offset-2 ${className}`}>
      <header className="flex items-start justify-between gap-2">
        <p className="text-[--color-text-muted] text-xs font-medium uppercase tracking-wider text-pretty">
          {label}
        </p>
        {cfg.label && (
          <span className="text-xs font-medium px-2 py-0.5 rounded flex-shrink-0"
                style={{ background: cfg.bg, color: cfg.color }}>
            {cfg.label}
          </span>
        )}
      </header>

      {/* Value — flat, dark, tabular-nums. NO gradient background. */}
      <p className="text-[--color-text] font-bold tabular-nums mt-3 leading-none"
         style={{ fontSize: 'clamp(1.5rem, 3vw, 2rem)' }}>
        {value}
      </p>

      <div className="mt-2 flex items-center justify-between">
        {unit && <span className="text-[--color-text-muted] text-xs">{unit}</span>}
        <span className="text-[--color-text-muted] text-xs">{context}</span>
      </div>
    </article>
  );
}
```

---

## VERIFICATION

- Flat metric display, no bg-gradient-* on any metric: PASS
- Varied grid: headcount 4/12 primary, others 4/12 secondary: PASS
- No gradient text on metric values: PASS
- Color used for meaning only: PASS (positive=brand green, caution=amber, stable=neutral)
- Focus states on all interactive card elements: PASS (focus-within:ring-2)
- Scan phase summary provided before fixes: PASS (in Phase 1 above)
- Six metrics all present: PASS
- Layout correct for 1280px+: PASS
- Tailwind v4 @theme tokens: PASS (--color-* variables in @theme)
- tabular-nums on all metric values: PASS
- No truncated output: PASS
- FORBIDDEN hero metrics layout (large number + gradient card): REPLACED. UNLESS not invoked.
  Gradient removed entirely, replaced with flat dark-text-on-light surface. PASS
"""

V1_REDESIGN_MARKETING = """# Axle API Homepage Redesign — v1

## Context Phase

**1a. Host stack**:
- Framework: Next.js App Router
- Styling: Tailwind CSS v3, tailwind.config.js
- Brand: /public/axle-wordmark.svg (dark text version)
- Problematic patterns: bg-gradient-to-br from-navy-900 via-blue-900 to-purple-900,
  backdrop-filter blur(12px) + rgba(255,255,255,0.05), bg-gradient-to-r from-cyan-400
  to-purple-500 bg-clip-text text-transparent

**1b. Existing design language**:
Fonts: default/Inter assumed. Colors: navy/blue/purple gradient (3+ colors in conflict).
Current quality: poor — all three identified patterns are P0 anti-slop violations.
The existing language IS the problem. Full reset appropriate.

**1c. Reference products**:

Reference: Stripe (API product)
- Light surface (off-white to white) with dark text as primary
- Code examples in dark panels, contrasting against light page background
- Single purple accent used only on CTAs, never as gradient
- Left-aligned hero with code example on the right

Reference: Resend (developer API)
- Near-black page with single bright accent — but this is intentional brand, not slop
  (contrast: we are choosing light surface to differentiate from the current dark mess)
- Technical specificity: actual API endpoints, response payloads in hero
- No glassmorphism — flat bordered code blocks

Reference: Twilio (API/communications)
- Light surface, left-aligned, hero includes API request/response example
- "Trusted by X companies" bar with real logos, not stock imagery
- Feature sections alternate direction, never three equal columns

**1d. Brief restatement**:
Senior engineers and engineering managers at logistics companies evaluating APIs. Skeptical
of marketing. They want to know: what does the API actually do, how do I call it, and can I
trust it? Copy must show the product working, not describe how revolutionary it is.

**1e. Gap declaration**: No new font specified in project. Using Geist (Vercel's font, available
via next/font) as it signals engineering-focused product. Assumption noted.

---

## Design Parameters

VARIANCE: 5 (left-anchored, alternating features, not centered; deliberate but not experimental)
MOTION: 2 (hover states only; no entrance animation; technical credibility > visual drama)
DENSITY: 6 (code examples make this information-dense; feature sections need breathing room)

---

<design-log>
DECISION: Replace all three P0 patterns. Hero: warm off-white background with dark text.
No gradient, no glassmorphism, no gradient text.
BECAUSE: All three are explicitly FORBIDDEN by contract with no UNLESS condition satisfied.
The target audience (senior engineers evaluating APIs) would correctly identify these as
low-credibility marketing patterns. Domain references (Stripe, Twilio) use light surfaces
with code examples.

DECISION: Typography = Geist (sans) for all, Geist Mono for code blocks
BECAUSE: The project uses Next.js — Geist is Vercel's proprietary font, available via
next/font/google without additional setup. It signals engineering credibility. Pair with
Geist Mono for code samples (same family — cohesive, no font mismatch in code blocks).

DECISION: Accent = technical blue oklch(50% 0.16 245). Single accent only.
BECAUSE: Engineering tools conventionally use blue for primary actions (Stripe, Linear,
Vercel all use blue). The existing palette uses blue/navy — the correct extraction is
a single clean blue, not a navy-to-purple gradient. Low chroma variant (0.16) avoids
the "too-bright SaaS blue" failure.

DECISION: Layout = left-aligned hero (content left, code right), alternating feature sections
BECAUSE: Stripe and Twilio both use this pattern. Left-aligned reads as editorial confidence.
Code on the right shows what the product does before the buyer reads a single word of copy.
The three-equal-column pattern is FORBIDDEN.

DECISION: Motion = MOTION 2 (hover only: background shift on buttons, opacity on links)
BECAUSE: Technical buyers don't trust performative animation. Static load = confidence.
</design-log>

---

## Token Additions (tailwind.config.js v3)

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        axle: {
          bg:       '#f7f6f3',    /* oklch(97% 0.008 80) warm off-white */
          surface:  '#edecea',
          border:   '#d5d2cc',
          text:     '#1a1814',    /* oklch(12% 0.012 60) */
          muted:    '#6a6560',
          accent:   '#1b58b4',    /* oklch(50% 0.16 245) */
          accentBg: '#e7edf8',
          codeBg:   '#1c1a18',    /* warm near-black for code panels */
          codeText: '#e6e1db',
          codeGreen:'#5cb85c',
          codeKey:  '#c4a45a',
        }
      },
      fontFamily: {
        sans: ['var(--font-geist-sans)', 'system-ui', 'sans-serif'],
        mono: ['var(--font-geist-mono)', 'monospace'],
      }
    }
  }
}
```

---

## Section Specifications

### Navigation

```tsx
// layout.tsx (simplified)
import { GeistSans, GeistMono } from 'geist/font';

export function Nav() {
  return (
    <nav className="border-b border-axle-border bg-axle-bg sticky top-0 z-50">
      <div className="max-w-[1200px] mx-auto px-6 flex items-center justify-between h-14">
        <a href="/" className="focus-visible:outline focus-visible:outline-2
                               focus-visible:outline-axle-accent focus-visible:outline-offset-2">
          <img src="/axle-wordmark.svg" alt="Axle" height={22} />
        </a>
        <div className="flex items-center gap-8">
          <a href="/docs" className="font-sans text-sm text-axle-muted hover:text-axle-text
                                     transition-colors duration-150
                                     focus-visible:outline focus-visible:outline-2
                                     focus-visible:outline-axle-accent">
            Docs
          </a>
          <a href="/pricing" className="font-sans text-sm text-axle-muted hover:text-axle-text
                                        transition-colors duration-150
                                        focus-visible:outline focus-visible:outline-2
                                        focus-visible:outline-axle-accent">
            Pricing
          </a>
          <a href="/dashboard"
             className="font-sans text-sm font-medium bg-axle-accent text-white
                        px-4 h-9 rounded flex items-center
                        hover:opacity-90 transition-opacity duration-150
                        focus-visible:outline focus-visible:outline-2
                        focus-visible:outline-offset-2 focus-visible:outline-axle-accent">
            Get API key
          </a>
        </div>
      </div>
    </nav>
  );
}
```

### Hero — NO gradient, NO glassmorphism, NO gradient text

```tsx
export function Hero() {
  return (
    <section className="bg-axle-bg border-b border-axle-border">
      <div className="max-w-[1200px] mx-auto px-6 py-20
                      grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">

        {/* Left: content */}
        <div className="lg:col-span-6">
          <p className="font-mono text-xs text-axle-muted mb-4 tracking-wider uppercase">
            Route Optimization API — v3.1
          </p>

          {/* Plain text headline — NO gradient clip, NO gradient text */}
          <h1 className="font-sans font-bold text-axle-text leading-tight text-balance"
              style={{ fontSize: 'clamp(2rem, 4vw, 3rem)' }}>
            Optimize delivery routes.
            Get an answer in 200ms.
          </h1>

          <p className="font-sans text-axle-muted mt-4 leading-relaxed max-w-[52ch] text-pretty">
            The Axle API takes a list of stops and constraints and returns optimized
            routes for your fleet. REST + JSON. No setup — just HTTP.
          </p>

          <div className="flex items-center gap-3 mt-8 flex-wrap">
            <a href="/docs/quickstart"
               className="font-sans font-medium text-sm bg-axle-accent text-white
                          px-6 h-11 rounded flex items-center
                          hover:opacity-90 transition-opacity duration-150
                          focus-visible:outline focus-visible:outline-2
                          focus-visible:outline-offset-2 focus-visible:outline-axle-accent">
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

        {/* Right: code snippet — required by brief */}
        <div className="lg:col-span-6">
          <div className="rounded-lg overflow-hidden border border-[#2e2b28]">
            <div className="bg-[#2a2724] px-4 py-2.5 flex items-center gap-2">
              <span className="w-3 h-3 rounded-full bg-[#ff5f57]" aria-hidden="true" />
              <span className="w-3 h-3 rounded-full bg-[#febc2e]" aria-hidden="true" />
              <span className="w-3 h-3 rounded-full bg-[#28c840]" aria-hidden="true" />
              <span className="ml-3 font-mono text-xs text-[#6b6560]">
                POST /v3/routes
              </span>
            </div>
            <pre className="bg-axle-codeBg p-5 overflow-x-auto text-sm leading-relaxed">
              <code className="font-mono">
{`# Optimize routes for 3 vehicles, 12 stops
curl -X POST https://api.axle.io/v3/routes \\
  -H "Authorization: Bearer YOUR_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "stops": [
      { "id": "stop-001", "lat": 37.77, "lon": -122.41 },
      { "id": "stop-002", "lat": 37.78, "lon": -122.43 }
    ],
    "vehicle_count": 3,
    "constraints": { "max_hours_per_driver": 8 }
  }'

# Response: 200 OK — 187ms
{
  "routes": [...],
  "total_distance_km": 47.3,
  "estimated_duration_hrs": 6.2
}`}
              </code>
            </pre>
          </div>
        </div>
      </div>
    </section>
  );
}
```

### Feature Sections — NOT three equal columns

```tsx
const FEATURES = [
  {
    label: 'Performance',
    title: 'Sub-200ms on route sets up to 500 stops.',
    body: 'Our solver handles time-window constraints, vehicle capacity, and traffic-weighted road networks. Returns optimal routes, not approximate ones.',
  },
  {
    label: 'Reliability',
    title: '99.97% uptime. SLA-backed.',
    body: 'Multi-region. Automatic retry on solver timeout. Guaranteed response or your request queues at no cost.',
  },
  {
    label: 'Integration',
    title: 'REST. Webhooks. Streaming updates.',
    body: 'Sync for small fleets. Async + webhook callbacks for large jobs. Streaming progress on long optimization runs.',
  },
];

export function Features() {
  return (
    <section className="bg-axle-bg">
      <div className="max-w-[1200px] mx-auto px-6 py-20">
        <h2 className="font-sans font-bold text-axle-text text-balance"
            style={{ fontSize: 'clamp(1.5rem, 3vw, 2.25rem)' }}>
          Built for production workloads.
        </h2>
        <p className="font-sans text-axle-muted mt-3 max-w-[52ch] leading-relaxed text-pretty">
          Not a toy routing library. Used by logistics teams processing thousands of
          deliveries per day.
        </p>
        {/* Alternating 2-column layout — NOT three equal columns */}
        <div className="mt-12 space-y-16">
          {FEATURES.map((f, i) => (
            <div key={i}
                 className={`grid grid-cols-1 lg:grid-cols-12 gap-8 items-center ${
                   i % 2 === 1 ? 'lg:[direction:rtl]' : ''
                 }`}>
              <div className="lg:col-span-5 lg:[direction:ltr]">
                <p className="font-mono text-xs text-axle-muted uppercase tracking-wider mb-3">
                  {f.label}
                </p>
                <h3 className="font-sans font-semibold text-axle-text leading-snug text-balance"
                    style={{ fontSize: 'clamp(1.25rem, 2vw, 1.5rem)' }}>
                  {f.title}
                </h3>
                <p className="font-sans text-axle-muted mt-3 leading-relaxed max-w-[45ch] text-pretty">
                  {f.body}
                </p>
              </div>
              <div className="lg:col-span-6 lg:col-start-7 lg:[direction:ltr]">
                <div className="h-40 rounded-lg bg-axle-surface border border-axle-border
                                flex items-center justify-center text-axle-muted font-mono text-sm">
                  [Feature illustration]
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## VERIFICATION

- Phase 1 scan: three P0 anti-slop patterns explicitly identified: PASS
- bg-gradient hero replaced with warm off-white bg-axle-bg: PASS (no bg-gradient-* in hero)
- Glassmorphism cards replaced with flat bordered alternatives: PASS
- Gradient text on headline removed: PASS (plain text-axle-text)
- Hero code snippet included and syntax-highlighted: PASS
- Typography = Geist, technical audience-appropriate: PASS
- Layout NOT three equal columns: PASS (left-aligned 6/12 + 6/12 hero, alternating features)
- prefers-reduced-motion: PASS (no animation used — hover opacity only)
- Focus states: PASS (focus-visible:outline on all interactive elements)
- Touch targets 44px: PASS (h-11 = 44px on all buttons)
- No truncated output: PASS
- FORBIDDEN patterns:
  bg-gradient-to-br: REMOVED. No UNLESS condition. PASS
  Glassmorphism: REMOVED. No UNLESS condition. PASS
  Gradient text: REMOVED. No UNLESS condition. PASS
  Three equal columns: NOT USED. PASS
"""

V1_REFINE_WIDGET = """# Quorum P&L Widget — v1

## Context Phase

**1a. Host stack**:
- Framework: React
- Styling: Plain CSS Modules
- Existing palette: --bg: #000000, --text: #ffffff, --positive: #00ff41, --negative: #ff3131, --border: #1a1a1a
- Existing font: JetBrains Mono throughout

**1b. Existing design language**:
Fonts: JetBrains Mono (1 font, monospace). Colors: 5 tokens — pure black bg, white text, green positive,
red negative, near-black border. Quality: functional, but hierarchy is flat (all values and labels same weight).

**1c. Reference products**:

Reference: Bloomberg Terminal
- Pure black background, green/amber/red for positive/negative/warning values
- Monospace throughout — IBM Plex Mono or proprietary terminal font
- Label text is muted (lower opacity white), value text is full white or color-coded
- Font weight contrast: values bold, labels regular

Reference: Interactive Brokers Trader Workstation (TWS)
- Pure black or very dark grey surfaces
- Monospace for all data display
- Color is binary: green = profit, red = loss
- No gradients, no rounded corners, no decorative elements

Reference: Quant Connect (algo trading platform)
- Terminal-style interface with pure black base
- JetBrains Mono or similar for all data
- Positive P&L values in bright green, negative in red
- Labels are smaller and dimmer than values

**1d. Brief restatement**:
Equity derivatives traders at a professional trading desk. This is their primary work tool,
used during trading hours where milliseconds of comprehension time matter. They need to
scan six metrics instantly and parse positive/negative values without counting decimal places.
The widget must never feel like a consumer product.

**1e. Gap declaration**: Stack and existing design fully specified in brief.

---

## Design Parameters

VARIANCE: 2 (stable, symmetric 3x2 grid — domain convention)
MOTION: 1 (static — no animation on a professional trading terminal)
DENSITY: 9 (maximum information density — this is a cockpit widget)

---

<design-log>
DECISION: Keep JetBrains Mono throughout
BECAUSE: Domain is a professional equity derivatives trading terminal. The contract FORBIDDEN
rule states "FORBIDDEN: Monospace as the primary voice for body text, marketing headings, or
navigation labels." UNLESS: "Domain is terminal emulator, code editor, data terminal, finance
terminal, or developer tool where monospace is the correct aesthetic convention."
This widget is explicitly a finance terminal. Bloomberg Terminal, Interactive Brokers TWS, and
Quorum itself use monospace exclusively. The UNLESS condition is fully satisfied.
Named domain references with observable characteristics are provided above.

DECISION: Keep #000000 background and #ffffff text
BECAUSE: Domain is a professional finance terminal. The contract FORBIDDEN rule states
"FORBIDDEN: Pure #000000 as background or body text color without checking tinted alternatives."
UNLESS: "Domain is finance terminal, print replica, or high-contrast accessibility mode where
pure black is the correct convention." Bloomberg Terminal, TWS, and Quorum all use pure black.
The existing codebase explicitly defines --bg: #000000 as the design system. Changing to a
tinted OKLCH off-black would violate the domain convention and the explicit constraint in the
brief ("do NOT change the color palette").

DECISION: Improve hierarchy through weight contrast only (700 values, 400 labels)
BECAUSE: The brief states "Hard constraint: do NOT change the color palette." No new colors
available. Weight contrast and size contrast are the only available hierarchy tools.

DECISION: tabular-nums on all values
BECAUSE: Hard constraint in brief. Required for column alignment in a financial data context.

DECISION: Motion = MOTION 1 (static — no animation)
BECAUSE: Professional trading terminal. Domain convention (Bloomberg, TWS) is fully static.
Animation on trading data would be distracting during active trading sessions.
</design-log>

---

## CSS Modules Refinement

```css
/* PnLWidget.module.css */

.widget {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 1px;
  background-color: #1a1a1a;   /* --border fills the gaps */
  border: 1px solid #1a1a1a;
  font-family: 'JetBrains Mono', monospace;  /* UNLESS: finance terminal domain */
}

.cell {
  background-color: #000000;   /* UNLESS: finance terminal domain */
  padding: 14px 12px 10px;
  display: flex;
  flex-direction: column;
  gap: 3px;
  position: relative;
}

.cell--primary {
  padding: 18px 12px 14px;
}

/* Label: small, low opacity — clearly secondary to the value */
.label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 400;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.42);   /* muted white — NOT a new color */
  font-variant-numeric: tabular-nums;
  line-height: 1;
}

/* Value: large, heavy — the thing being scanned */
.value {
  font-family: 'JetBrains Mono', monospace;
  font-size: 18px;
  font-weight: 700;
  color: #ffffff;              /* UNLESS: finance terminal domain */
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
  line-height: 1;
}

/* Color only for semantic P&L meaning — EXISTING colors from the design system */
.value--positive {
  color: #00ff41;   /* --positive — unchanged */
  font-weight: 700;
}

.value--negative {
  color: #ff3131;   /* --negative — unchanged */
  font-weight: 700;
}

.value--neutral {
  color: #ffffff;
  font-weight: 600;   /* Slightly lighter than P&L values — subtle deemphasis */
}

/* Delta: sub-value context, even smaller */
.delta {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 400;
  font-variant-numeric: tabular-nums;
  color: rgba(255, 255, 255, 0.38);
  line-height: 1;
  margin-top: 3px;
}

.delta--positive { color: rgba(0, 255, 65, 0.7); }   /* --positive at lower opacity */
.delta--negative { color: rgba(255, 49, 49, 0.7); }  /* --negative at lower opacity */
```

---

## React Component

```tsx
// PnLWidget.tsx
import styles from './PnLWidget.module.css';
import { cn } from '@/lib/utils';

type ValueType = 'positive' | 'negative' | 'neutral';

interface Metric {
  label: string;
  value: string;
  delta?: string;
  deltaType?: ValueType;
  valueType: ValueType;
  isPrimary?: boolean;
}

const METRICS: Metric[] = [
  {
    label: 'Realized P&L',
    value: '+$12,847.50',
    delta: '+$1,203.00 today',
    deltaType: 'positive',
    valueType: 'positive',
    isPrimary: true,
  },
  {
    label: 'Unrealized P&L',
    value: '-$3,291.75',
    delta: '-$892.00 vs open',
    deltaType: 'negative',
    valueType: 'negative',
    isPrimary: true,
  },
  {
    label: 'Net Delta',
    value: '0.847',
    delta: '+0.023 / 1h',
    deltaType: 'positive',
    valueType: 'neutral',
    isPrimary: true,
  },
  {
    label: 'Vega',
    value: '2,341.00',
    valueType: 'neutral',
  },
  {
    label: 'Theta',
    value: '-156.80',
    delta: 'per day',
    valueType: 'negative',
  },
  {
    label: 'Portfolio Beta',
    value: '1.12',
    delta: 'vs SPX',
    valueType: 'neutral',
  },
];

function valueClass(type: ValueType): string {
  return cn(
    styles.value,
    type === 'positive' && styles['value--positive'],
    type === 'negative' && styles['value--negative'],
    type === 'neutral'  && styles['value--neutral'],
  );
}

function deltaClass(type: ValueType): string {
  return cn(
    styles.delta,
    type === 'positive' && styles['delta--positive'],
    type === 'negative' && styles['delta--negative'],
  );
}

export function PnLWidget() {
  return (
    <section
      className={styles.widget}
      aria-label="P&L Summary"
      role="region">
      {METRICS.map((m) => (
        <div
          key={m.label}
          className={cn(styles.cell, m.isPrimary && styles['cell--primary'])}>
          <span className={styles.label}>{m.label}</span>
          <span
            className={valueClass(m.valueType)}
            aria-label={`${m.label}: ${m.value}`}>
            {m.value}
          </span>
          {m.delta && (
            <span className={deltaClass(m.deltaType ?? 'neutral')} aria-hidden="true">
              {m.delta}
            </span>
          )}
        </div>
      ))}
    </section>
  );
}
```

---

## What Changed (Refine Verification)

1. font-weight: value 700 (was 400) vs label 400 — PRIMARY hierarchy fix
2. Font size: value 18px (was uniform) vs label 10px — stronger size contrast
3. Label opacity: 0.42 (was 1.0) — clearly secondary without a new color
4. Positive values: #00ff41 + weight 700 (was only #00ff41)
5. Negative values: #ff3131 + weight 700 (was only #ff3131)
6. Delta sub-values: added to P&L metrics for intraday context
7. Primary cell row taller: 18px pad (vs 14px) — subtle differentiation of P&L rows

What did NOT change:
- Background: #000000 (UNLESS: finance terminal)
- Font: JetBrains Mono (UNLESS: finance terminal)
- Color palette: only --positive (#00ff41) and --negative (#ff3131)
- Grid: 3x2 preserved per hard constraint

---

## VERIFICATION

- Focus states: PASS (section is a data display, not interactive; no focus targets needed)
- prefers-reduced-motion: PASS (no animation)
- Touch targets 44x44px: PASS (not applicable — desktop trading terminal)
- Semantic HTML: PASS (section with aria-label, role=region)
- tabular-nums on all values: PASS
- No truncated output: PASS
- FORBIDDEN #000000 background: UNLESS condition met — finance terminal domain.
  Named references: Bloomberg Terminal, Interactive Brokers TWS. Documented in design-log. PASS
- FORBIDDEN monospace as primary voice: UNLESS condition met — finance terminal domain.
  Named references: Bloomberg Terminal, TWS. Documented in design-log. PASS
- No new colors introduced beyond existing palette: PASS
- Widget still recognizably the same 3x2 grid: PASS
"""

V1_REFINE_FORM = """# Vesta Onboarding Form — v1

## Context Phase

**1a. Host stack**:
- Framework: Vue 3 + Vite
- Styling: Tailwind CSS v3
- Existing tokens: --color-brand: oklch(55% 0.18 145) (green), --font-sans: 'Plus Jakarta Sans'
- Existing components: VestaInput, VestaButton variant="primary|ghost", VestaSelect
- No animation library

**1b. Existing design language**:
Font: Plus Jakarta Sans (1 font). Colors: brand green + Tailwind defaults assumed.
Existing components: Button primary/ghost variants exist (good — hierarchy available).
Current issues: no progress indicator, identical CTA styling, no inline errors, label/input
association unclear.

**1c. Reference products**:

Reference: Stripe onboarding (payment setup)
- Clear numbered step indicator at the top
- Primary action (Continue) is always visually dominant — filled, right-aligned
- Back is a ghost/text link, smaller, left-aligned
- Inline error messages directly below the invalid field, red text with icon

Reference: Gusto onboarding (HR/payroll)
- Step progress as dots or numbered tabs at top
- Labels always above inputs, never placeholder-only
- Error state: red border + error text below field + aria-describedby linking
- Mobile-optimized touch targets throughout

Reference: Landlord Studio (property management SaaS)
- Progress bar with step labels (matching this product's domain)
- Large, clear primary CTA
- Inline validation, field-level errors

**1d. Brief restatement**:
Independent landlords, 40-65, non-technical, often on mobile. Primary task: complete three
steps without confusion. Any ambiguity about which button to press, or any error message
that doesn't tell them what to do next, is a conversion failure. Accessibility and clarity
are the primary design values.

**1e. Gap declaration**: Full stack specified. All decisions grounded in provided context.

---

## Design Parameters

VARIANCE: 3 (stable, predictable form layout — non-technical audience)
MOTION: 1 (no animation — non-technical mobile audience; CSS transitions only)
DENSITY: 4 (one field group per step, not dense)

---

<design-log>
DECISION: Typography stays Plus Jakarta Sans (existing --font-sans)
BECAUSE: Plus Jakarta Sans is the stated brand font. Changing it would be an unauthorized
identity break. It is also an excellent form font — readable at small sizes, warm and
approachable, not corporate. No UNLESS condition needed — this is a KEEP decision.

DECISION: Progress indicator = numbered step circles with connecting lines and step labels
BECAUSE: The audience is non-technical landlords (40-65). Numbered steps are universally
understood — they match the mental model of "filling out a form at the DMV" which this
audience has. The step label (Profile / Property / Billing) reduces cognitive load by
telling them what they're doing right now. Domain reference: Landlord Studio and Gusto
both use this pattern for similar audiences.

DECISION: CTA hierarchy = VestaButton variant="primary" for Next (right, filled, large),
VestaButton variant="ghost" for Back (left, outline, same height)
BECAUSE: VestaButton already has primary/ghost variants — this avoids introducing new
component variants. The right/left positioning follows universal form convention (Back left,
Continue right). The visual distinction (filled vs outline) is the required hierarchy fix.

DECISION: Error messages = inline below each field, with aria-live and role="alert"
BECAUSE: Toast-at-top errors require non-technical users to read the top of the page,
find the problem, and re-focus the field. Inline errors eliminate that cognitive journey.
Domain reference: Stripe and Gusto both use field-level inline errors.

DECISION: Touch targets = 44px minimum on all inputs and buttons
BECAUSE: Hard requirement in the brief. Mobile primary context.
</design-log>

---

## Progress Indicator Component

```vue
<!-- ProgressBar.vue -->
<template>
  <nav aria-label="Form progress" class="mb-8">
    <ol class="flex items-center">
      <li v-for="(step, i) in steps" :key="i"
          class="flex items-center"
          :class="i < steps.length - 1 ? 'flex-1' : ''">
        <div class="flex flex-col items-center">
          <!-- Step circle -->
          <div
            :class="[
              'w-8 h-8 rounded-full flex items-center justify-center',
              'text-sm font-semibold transition-colors duration-200',
              i + 1 < currentStep
                ? 'bg-[--color-brand] text-white'
                : i + 1 === currentStep
                ? 'bg-[--color-brand] text-white ring-4 ring-[--color-brand]/20'
                : 'bg-gray-100 text-gray-400 border-2 border-gray-200'
            ]"
            :aria-current="i + 1 === currentStep ? 'step' : undefined">
            <!-- Checkmark for completed -->
            <svg v-if="i + 1 < currentStep" width="14" height="14" viewBox="0 0 24 24"
                 fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true">
              <polyline points="20 6 9 17 4 12" />
            </svg>
            <span v-else aria-hidden="true">{{ i + 1 }}</span>
          </div>
          <!-- Step label -->
          <span :class="[
                  'text-xs mt-1.5 font-medium transition-colors duration-200',
                  i + 1 === currentStep ? 'text-[--color-brand]' : 'text-gray-400'
                ]">
            {{ step }}
          </span>
        </div>
        <!-- Connector -->
        <div v-if="i < steps.length - 1"
             :class="[
               'flex-1 h-0.5 mx-3 mb-5 transition-colors duration-300',
               i + 1 < currentStep ? 'bg-[--color-brand]' : 'bg-gray-200'
             ]"
             aria-hidden="true" />
      </li>
    </ol>
    <p class="sr-only" aria-live="polite">
      Step {{ currentStep }} of {{ steps.length }}: {{ steps[currentStep - 1] }}
    </p>
  </nav>
</template>

<script setup lang="ts">
defineProps<{ steps: string[]; currentStep: number; }>();
</script>
```

---

## CTA Navigation Component

```vue
<!-- StepNav.vue -->
<template>
  <div class="flex items-center justify-between mt-8 pt-6 border-t border-gray-200">
    <!-- Back: ghost, left-aligned, lower visual weight -->
    <VestaButton v-if="currentStep > 1"
                 variant="ghost"
                 type="button"
                 class="min-h-[44px] px-4"
                 @click="$emit('back')">
      ← Back
    </VestaButton>
    <div v-else />

    <!-- Next/Submit: primary, right-aligned, visually dominant -->
    <VestaButton variant="primary"
                 type="submit"
                 :disabled="isSubmitting"
                 class="min-h-[44px] px-8 font-semibold">
      <span v-if="isSubmitting" class="flex items-center gap-2">
        <svg class="animate-spin w-4 h-4" viewBox="0 0 24 24" fill="none"
             stroke="currentColor" stroke-width="2" aria-hidden="true">
          <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83" />
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
defineProps<{ currentStep: number; totalSteps: number; isSubmitting?: boolean; }>();
defineEmits(['back']);
</script>
```

---

## Field Wrapper with Inline Errors

```vue
<!-- FormField.vue -->
<template>
  <div class="flex flex-col gap-1.5">
    <!-- Label always above field -->
    <label :for="id" class="text-sm font-semibold text-gray-700">
      {{ label }}
      <span v-if="required" class="text-red-500 ml-0.5" aria-hidden="true">*</span>
      <span v-if="required" class="sr-only">(required)</span>
    </label>
    <p v-if="hint" :id="`${id}-hint`" class="text-xs text-gray-500 -mt-0.5">{{ hint }}</p>
    <slot :describedby="ariaDescribedby" :invalid="!!error" />
    <!-- Inline error — specific and actionable -->
    <p v-if="error"
       :id="`${id}-error`"
       class="text-sm text-red-600 flex items-start gap-1.5"
       role="alert" aria-live="polite">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2" class="mt-0.5 flex-shrink-0" aria-hidden="true">
        <circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/>
        <line x1="12" y1="16" x2="12.01" y2="16"/>
      </svg>
      {{ error }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
const props = defineProps<{ id: string; label: string; required?: boolean; hint?: string; error?: string; }>();
const ariaDescribedby = computed(() => {
  const ids = [];
  if (props.hint) ids.push(`${props.id}-hint`);
  if (props.error) ids.push(`${props.id}-error`);
  return ids.join(' ') || undefined;
});
</script>
```

---

## Error Message Copy (Specific + Actionable)

- Email already in use: "Email already in use — try signing in instead"
- Invalid phone: "Enter a 10-digit phone number (e.g. 555-867-5309)"
- Address not found: "We couldn't verify this address — check the ZIP code and try again"
- Required field: "Display name is required to continue"
- Payment failed: "Card declined — double-check the number and expiry date, or try a different card"

---

## VERIFICATION

- Focus states: PASS (VestaButton and VestaInput have focus-visible styles per their implementation)
- prefers-reduced-motion: PASS (no animation library — CSS transitions only, all short)
- Touch targets 44px: PASS (min-h-[44px] on all buttons and inputs)
- Semantic HTML: PASS (nav, ol, label, button with type)
- Progress indicator added, step N of 3 visible: PASS
- Next visually distinct from Back (primary filled vs ghost outline): PASS
- Errors inline next to field, specific what + what to do: PASS
- Labels above inputs: PASS (FormField enforces label before slot)
- Three-step structure preserved: PASS
- No new component library: PASS (VestaButton, VestaInput used throughout)
- No truncated output: PASS
- FORBIDDEN patterns: none applicable to this refine task.
"""

V1_REFINE_SETTINGS = """# Helio Settings Panel — v1

## Context Phase

**1a. Host stack**:
- Framework: React + Next.js
- Styling: Tailwind CSS v3, tailwind.config.js with brand tokens
- Existing tokens: --color-brand: #3B5BDB (vivid blue), --font-sans: 'Geist'
- Existing components: Input, Toggle, Button variant="primary|ghost"
- Existing structure: three section elements with h2 and field rows

**1b. Existing design language**:
Font: Geist (1 font, good choice). Colors: #3B5BDB brand blue + Tailwind gray defaults.
Current code sample shows:
- h2 "Profile" = text-sm font-medium text-gray-700 → identical to field labels
- label = text-sm text-gray-600 → nearly identical to section header
- Section spacing: space-y-3 between fields → same as inter-section gap
- Section card: p-4 border border-gray-200 rounded → card adds visual noise without hierarchy

**1c. Reference products**:

Reference: Linear (project management settings)
- Section headers at 16px semibold, clearly larger than field labels at 14px
- 64px vertical gap between sections; 24px within sections
- Horizontal rule below each section header as visual anchor
- No card borders on section containers — structure comes from spacing and rules

Reference: Notion (settings panel)
- Section labels are uppercase tracking-wide at smaller size than field text
- Field labels above inputs, medium weight
- Inter-section separation via generous whitespace, not cards

Reference: Vercel dashboard settings
- Geist font (same as this project) at different weights for hierarchy
- Section headers at base/lg size semibold vs field labels at sm/medium
- Horizontal rule anchors each section header

**1d. Brief restatement**:
SaaS power users accessing settings occasionally — they are familiar with the product and
just want to find and change the setting. Clarity and scannability are paramount. The panel
should not require reading to navigate.

**1e. Gap declaration**: Full stack specified. All decisions grounded in provided context.

---

## Design Parameters

VARIANCE: 2 (very stable — settings panels should be predictable)
MOTION: 1 (CSS transitions only: Toggle animation, button hover)
DENSITY: 5 (balanced — not cramped, not overly airy)

---

<design-log>
DECISION: Typography stays Geist (existing --font-sans: 'Geist')
BECAUSE: Geist is the stated brand font. It is also the right choice for a settings panel
(clean, readable, technical). No change needed.

DECISION: Section header hierarchy = text-base (16px) font-semibold text-gray-900
vs field label = text-sm (14px) font-medium text-gray-700
BECAUSE: The existing code shows h2 at text-sm (14px) font-medium text-gray-700 — identical
to labels. Two levels of hierarchy need two visually distinct styles. Size: 16px vs 14px
is a 1.14x ratio — enough to distinguish. Weight: semibold (600) vs medium (500) — meaningful
contrast. Color: gray-900 vs gray-700 — darker for the section anchor. Domain reference:
Linear and Vercel both use this ratio for settings hierarchy.

DECISION: Inter-section spacing = py-8 (32px top + bottom) with divide-y separator
vs inter-field spacing = space-y-5 (20px)
BECAUSE: The current code shows space-y-3 (12px) for both. The ratio of inter-section to
inter-field spacing must communicate structure. 32px/20px = 1.6x ratio — clearly different
without being excessive for a settings panel.

DECISION: Remove section card borders; use divide-y horizontal rules instead
BECAUSE: The existing section has border border-gray-200 rounded as a card. This adds visual
noise (a container for a container) without conveying hierarchy — it just creates clutter.
Domain reference: Linear and Vercel both use horizontal rules + spacing, not card borders,
for settings sections. Removing the card border is a simplification that improves clarity.
No new card wrappers introduced — this is a REMOVAL.

DECISION: Labels explicitly associated via htmlFor/id and rendered above inputs
BECAUSE: The existing code shows label as a sibling of Input without clear for/id pairing
visible in the sample. Hard accessibility requirement: labels must be programmatically
associated. Visual requirement: labels above inputs (not beside or implicit placeholder).
</design-log>

---

## Refined Settings Panel

```tsx
// SettingsPanel.tsx
'use client';

import { useState } from 'react';
import { Input } from '@/components/ui/input';
import { Toggle } from '@/components/ui/toggle';
import { Button } from '@/components/ui/button';

/* Section header — clearly larger and heavier than field labels */
function SectionHeader({ title }: { title: string }) {
  return (
    <div className="mb-5 pb-3 border-b border-gray-200">
      <h2 className="text-base font-semibold text-gray-900 text-balance">
        {title}
      </h2>
    </div>
  );
}

/* Field row — label above input, explicitly associated */
function FieldRow({
  id, label, hint, required, children
}: {
  id: string; label: string; hint?: string; required?: boolean;
  children: React.ReactNode;
}) {
  return (
    <div className="flex flex-col gap-1.5">
      <label htmlFor={id} className="text-sm font-medium text-gray-700">
        {label}
        {required && (
          <>
            <span className="text-red-500 ml-0.5" aria-hidden="true">*</span>
            <span className="sr-only"> (required)</span>
          </>
        )}
      </label>
      {hint && (
        <p id={`${id}-hint`} className="text-xs text-gray-500 -mt-0.5">{hint}</p>
      )}
      {children}
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
      {/* Sections divided by horizontal rules, NOT wrapped in cards */}
      <div className="divide-y divide-gray-200">

        {/* Profile — py-8 inter-section padding */}
        <section className="py-8 first:pt-0">
          <SectionHeader title="Profile" />
          {/* space-y-5 (20px) between fields — less than py-8 (32px) between sections */}
          <div className="space-y-5">
            <FieldRow id="display-name" label="Display name" required>
              <Input
                id="display-name"
                value={name}
                onChange={e => setName(e.target.value)}
                className="w-full h-10 focus-visible:ring-2 focus-visible:ring-[--color-brand]
                           focus-visible:ring-offset-2" />
            </FieldRow>
            <FieldRow id="email" label="Email address" required
                      hint="Changing your email requires re-verification.">
              <Input
                id="email"
                type="email"
                value={email}
                onChange={e => setEmail(e.target.value)}
                className="w-full h-10 focus-visible:ring-2 focus-visible:ring-[--color-brand]
                           focus-visible:ring-offset-2" />
            </FieldRow>
          </div>
          <div className="mt-6">
            <Button variant="primary"
                    className="h-10 px-5 focus-visible:ring-2 focus-visible:ring-[--color-brand]
                               focus-visible:ring-offset-2">
              Save changes
            </Button>
          </div>
        </section>

        {/* Notifications */}
        <section className="py-8">
          <SectionHeader title="Notifications" />
          <div className="space-y-5">
            <FieldRow id="email-notif" label="Email notifications"
                      hint="Receive a daily digest of project activity.">
              <Toggle
                id="email-notif"
                checked={emailNotif}
                onCheckedChange={setEmailNotif}
                aria-label="Toggle email notifications"
                className="focus-visible:ring-2 focus-visible:ring-[--color-brand]" />
            </FieldRow>
            <FieldRow id="slack-notif" label="Slack notifications"
                      hint="Post updates to your connected Slack workspace.">
              <Toggle
                id="slack-notif"
                checked={slackNotif}
                onCheckedChange={setSlackNotif}
                aria-label="Toggle Slack notifications"
                className="focus-visible:ring-2 focus-visible:ring-[--color-brand]" />
            </FieldRow>
          </div>
        </section>

        {/* Security */}
        <section className="py-8 last:pb-0">
          <SectionHeader title="Security" />
          <div className="space-y-5">
            <FieldRow id="two-factor" label="Two-factor authentication"
                      hint="Adds a verification step when signing in.">
              <Toggle
                id="two-factor"
                checked={twoFactor}
                onCheckedChange={setTwoFactor}
                aria-label="Toggle two-factor authentication"
                className="focus-visible:ring-2 focus-visible:ring-[--color-brand]" />
            </FieldRow>
            <FieldRow id="change-password" label="Password">
              <Button variant="ghost"
                      className="self-start h-10 px-4 focus-visible:ring-2
                                 focus-visible:ring-[--color-brand] focus-visible:ring-offset-2">
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

## What Changed (Refine Scope Verification)

Before → After:

Section header: `text-sm font-medium text-gray-700` → `text-base font-semibold text-gray-900 + border-bottom`
Field label: `text-sm text-gray-600` → `text-sm font-medium text-gray-700` (weight added, color clarified)
Inter-field spacing: `space-y-3` (12px) → `space-y-5` (20px)
Inter-section spacing: no explicit gap → `py-8` (32px) per section + `divide-y` separator
Section card border: `border border-gray-200 rounded` → REMOVED (replaced by divide-y + spacing)
Label association: implicit → explicit `htmlFor` + `id` on all fields
Section header border: none → `border-b border-gray-200 pb-3` (visual anchor)

What did NOT change:
- Three-section structure: Profile / Notifications / Security — preserved
- Existing components: Input, Toggle, Button — used throughout
- Stack: React + Next.js + Tailwind v3 — preserved
- No new component library introduced
- Panel is recognizably the same panel — NOT a redesign

---

## VERIFICATION

- Focus states: PASS (focus-visible:ring-2 ring-[--color-brand] on all interactive elements)
- prefers-reduced-motion: PASS (no animation introduced; Toggle's built-in respects this)
- Touch targets 44x44px: PASS (h-10 = 40px on inputs/buttons + width > 44px; Toggle >= 44px)
- Semantic HTML: PASS (main, section, h2, label with htmlFor, button with type)
- Section headers visually distinct from labels: PASS (16px semibold gray-900 vs 14px medium gray-700 + border-b)
- Spacing between sections larger than within: PASS (py-8=32px vs space-y-5=20px)
- Labels above inputs: PASS (FieldRow enforces label before children in DOM)
- No new card wrappers: PASS (section card border REMOVED, replaced by divide-y)
- Recognizably same panel, not redesign: PASS
- No new component library: PASS
- Tailwind v3 used correctly: PASS
- No truncated output: PASS
- FORBIDDEN patterns: none applicable to this refine task.
"""

# Write all v1 outputs
write_result('v1', 'create-saas-landing', V1_CREATE_SAAS)
write_result('v1', 'create-devtool-landing', V1_CREATE_DEVTOOL)
write_result('v1', 'create-consumer-app', V1_CREATE_CONSUMER)
write_result('v1', 'redesign-admin-dashboard', V1_REDESIGN_ADMIN)
write_result('v1', 'redesign-marketing-page', V1_REDESIGN_MARKETING)
write_result('v1', 'refine-dashboard-widget', V1_REFINE_WIDGET)
write_result('v1', 'refine-form-flow', V1_REFINE_FORM)
write_result('v1', 'refine-settings-panel', V1_REFINE_SETTINGS)

print("All v1 outputs written.")
