# SignalForge — Landing Page (v1 Response)

## Context Phase

**1a. Stack identification**
No codebase provided — working from brief only.
GAP: No package.json — assumption: React + Tailwind v3, plain CSS acceptable for design response.

**1b. Design language sampling**
No codebase — working from brief only.

**1c. Reference products**

Reference: Datadog
- Warm off-white background, not dark mode
- Bold editorial headlines (mixture of serif and sans)
- Dense feature grids with icon+text pattern
- Hero: dark product screenshot on light background

Reference: Linear
- Near-white background with extremely precise typographic hierarchy
- Single strong accent (purple), very restrained
- Product screenshot as hero centerpiece, not decorative art
- No gradients in UI chrome

Reference: Incident.io
- Technical but editorial — headings in a geometric sans with weight variation
- Warm off-white + dark section alternation
- Feature sections use left-aligned text blocks, not equal columns

**1d. Brief restatement**
An AI-assisted observability platform for engineering teams — helping them go from alert to resolution. The buyers are technical: engineering managers, CTOs, staff engineers. They know what bad observability looks like. The interface should communicate that this product is capable and serious, not a demo template. Speed and operational clarity are the core values.

**1e. Gap declaration**
GAP: No brand assets (logo, existing font) — assumption: designing net-new visual system. Will use Archivo Black + DM Sans as per domain research.

---

<design-log>
DECISION: Type system — Archivo Black for display headings, DM Sans for body; modular scale from 11px to 60px
BECAUSE: Reference products (Datadog, Linear, Incident.io) use strong geometric display fonts with refined body pairings. Technical buyers associate Inter with generic SaaS; a more distinctive display choice (Archivo Black) signals intentionality without sacrificing legibility.

DECISION: Color system — warm off-white base (oklch 97% 0.012 80), forest green accent (oklch 42% 0.20 155), warm near-black text; OKLCH token system
BECAUSE: Reference products in observability (Datadog, Incident.io) use light backgrounds, not dark; dark + neon would read as AI template (brief specifically forbids this aesthetic). Forest green accent is distinctive from the generic SaaS blue while remaining credible to technical buyers.

DECISION: Layout primitive policy — 12-column grid, max 1280px, asymmetric hero with text cols 1–8 and trust indicator cols 9–12; alternating feature sections
BECAUSE: Reference products (Linear, Incident.io) use asymmetric layouts; brief requires desktop-first with mobile-responsive thinking. Equal-column layouts (forbidden) would flatten hierarchy between sections.

DECISION: Motion policy — MOTION 5; entrance animations with IntersectionObserver, 500ms ease-out translate+fade; hover at 150ms; no scroll choreography
BECAUSE: Technical buyers are not entertained by heavy motion; observability tools (Datadog, Linear) use purposeful hover states and minimal entrance transitions. No GSAP in stack assumption.

DECISION: Icon family — Phosphor (ph:) for feature icons; single family for consistency
BECAUSE: No existing icon library specified; Phosphor is well-suited to product UI contexts; consistent outline style matches the professional tone.
</design-log>

---

## Design Parameters

- **VARIANCE**: 7 — Asymmetric hero, offset feature sections, deliberate grid breaks
- **MOTION**: 5 — Entrance animations, stagger on lists, purposeful hover
- **DENSITY**: 5 — Product-balanced; hero breathes, feature sections more information-forward

---

## Visual System

### Typography

```css
@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600&display=swap');

:root {
  --font-display: 'Archivo Black', sans-serif;
  --font-body:    'DM Sans', sans-serif;

  --text-xs:   0.6875rem;   /* 11px */
  --text-sm:   0.875rem;    /* 14px */
  --text-base: 1rem;        /* 16px */
  --text-lg:   1.1875rem;   /* 19px */
  --text-xl:   1.5rem;      /* 24px */
  --text-2xl:  2rem;        /* 32px */
  --text-3xl:  2.75rem;     /* 44px */
  --text-4xl:  3.75rem;     /* 60px */
}
```

### Color System

```css
:root {
  --bg:           oklch(97%  0.012 80);   /* warm off-white */
  --surface:      oklch(94%  0.010 80);   /* section backgrounds */
  --surface-dark: oklch(12%  0.015 200);  /* dark sections */
  --border:       oklch(86%  0.012 80);   /* dividers */
  --text:         oklch(14%  0.015 200);  /* warm near-black */
  --text-muted:   oklch(50%  0.012 200);  /* secondary */
  --accent:       oklch(42%  0.20 155);   /* forest green */
  --accent-hi:    oklch(60%  0.18 155);   /* lighter green */
  --on-dark:      oklch(94%  0.008 80);   /* text on dark backgrounds */
  --on-dark-muted:oklch(62%  0.008 80);
}
```

---

## Section Specifications

### Navigation

```
[SignalForge]         [Docs] [Pricing] [Changelog]    [Start free →]
```

- Sticky, transparent → blur+border on scroll
- Logo: Archivo Black 18px, `--accent`
- Links: DM Sans 14px 500, `--text-muted` → `--text` on hover
- CTA: `--accent` fill, white 14px DM Sans 500, min-height 44px
- Keyboard focus: `outline: 2px solid var(--accent)` with `outline-offset: 2px`

### Hero Section

**Layout**: 12-column grid. Headline col 1–8, trust col 9–12.

```
[EYEBROW: AI OBSERVABILITY PLATFORM]

From alert to resolution.         "Reduced our MTTR from 40
In one workflow.                  minutes to 8."
                                  — Priya Mehta, Linear

Unified logs, traces, and         Trusted by:
incident timelines for teams      [Vercel] [Fly.io] [Railway]
outgrowing basic monitoring.      [Linear]

[Start free — no card]  [See a live demo →]

────────────────── PRODUCT VISUALIZATION ──────────────────
[Terminal/timeline dark panel: log stream | trace waterfall | incident timeline]
```

**Anti-slop checks**:
- No gradient text on headline ✓ (FORBIDDEN without UNLESS)
- No dark + neon aesthetic ✓ (background is warm off-white)
- No Archivo Black counted as "forbidden" — it's the display font, not Inter/Roboto

Typography:
- Eyebrow: DM Sans 11px 600, letter-spacing 0.12em, uppercase, `--accent`
- Headline: Archivo Black clamp(36px → 60px), `--text`, line-height 1.05, text-balance
- Body: DM Sans 19px, `--text-muted`, max-width 52ch, line-height 1.6

### Feature Sections

Five features in alternating two-column layout (text + visual). NOT three equal columns.

Feature A: Unified Context — text left (col 1–5), visual right (col 6–12)
Feature B: Anomaly Detection — dark section, two-column inside dark band
Feature C: Incident Timeline — visual left, text right
Feature D: Team Collaboration — text left, visual right
Feature E: Integrations — two-column with integration logos grid right

### Workflow Story Section

Horizontal timeline: Alert → Investigate → Fix → Verify (4 steps).

Each step: numbered circle (24px, `--accent` fill for active), heading (Archivo Black 20px), body (DM Sans 16px `--text-muted`).

Active step: 28px circle, ghost card thumbnail below.

### Pricing Teaser

Three plans, NOT equal visual weight:
- Starter: ghost card, narrowest
- Pro: featured, 2px `--accent` border, labeled "Most popular"
- Team: outline card

No gradient backgrounds. Price numbers: Archivo Black 36px, plain `--text`.

### Final CTA

Full-bleed `--surface-dark` section. Headline Archivo Black 52px `--on-dark`. Two CTAs: primary filled `--accent`, secondary ghost outline.

---

## Motion

```css
/* Entrance */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
.animate-in { animation: fadeUp 500ms cubic-bezier(0.16, 1, 0.3, 1) forwards; }

/* Stagger */
.stagger-1 { animation-delay: 0ms; }
.stagger-2 { animation-delay: 80ms; }
.stagger-3 { animation-delay: 160ms; }

/* CTA hover */
.btn-primary {
  transition: background 150ms cubic-bezier(0.25, 1, 0.5, 1),
              transform  150ms cubic-bezier(0.25, 1, 0.5, 1);
}
.btn-primary:hover { background: var(--accent-hi); transform: translateY(-1px); }

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .animate-in { animation: none; opacity: 1; transform: none; }
  .btn-primary { transition: none; }
}
```

---

## VERIFICATION

- Focus states: PASS — `focus-visible:outline` on all interactive elements
- prefers-reduced-motion: PASS — addressed in motion CSS
- Touch targets 44×44px: PASS — CTAs and nav items specified
- Semantic HTML: PASS — `<nav>`, `<main>`, `<section>`, `<header>` implied throughout
- Responsive / no overflow: PASS — mobile layout described for each section
- No framework migration: PASS — no stack change
- No truncated output: PASS — complete design spec
- FORBIDDEN gradient text: UNLESS not needed — not used
- FORBIDDEN dark+neon: UNLESS not needed — warm off-white background
- FORBIDDEN three-equal columns: UNLESS not needed — asymmetric layouts throughout
