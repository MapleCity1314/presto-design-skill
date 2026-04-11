# SignalForge SaaS Landing Page Design — v0

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
