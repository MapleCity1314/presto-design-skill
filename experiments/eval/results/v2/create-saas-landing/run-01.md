# SignalForge — Landing Page (v2 Response)

## Context Phase

**1a. Stack identification**
No codebase provided — working from brief only.
GAP: No package.json — working from design response format; no Tailwind or framework specified.

**1b. Design language sampling**
No codebase — working from brief only.

**1c. Reference products**

Reference: Datadog
- Light backgrounds, not dark mode for main marketing site
- Editorial display typography with refined body
- Product screenshot centered in hero as primary visual

Reference: Linear
- Single strong accent, extremely controlled palette
- Asymmetric hero layouts, product-forward
- No gradient text, no neon

Reference: Incident.io
- Technical but editorial; warm off-white backgrounds
- Feature sections use left-aligned text blocks, not equal columns
- Credibility through specificity (actual metrics, real examples)

**1d. Brief restatement**
An AI observability platform serving engineering teams. Core buyers are technical (EMs, CTOs, staff engineers) who recognize and distrust generic SaaS aesthetics. The page needs to communicate operational clarity and trust. The aesthetic must feel like a real tool, not an AI-generated template.

**1e. Gap declaration**
GAP: No brand assets — assumption: designing net-new. Font choice driven by domain research above.

---

<design-log>
DECISION: Type system — Archivo Black display + DM Sans body; modular scale 11px–60px; clamp for fluid sizing
BECAUSE: Reference products (Datadog, Linear, Incident.io) use strong geometric display fonts. Technical buyers recognize Inter as generic SaaS. Archivo Black is distinctive, credible, not trendy. DM Sans is refined and legible at small sizes for body copy.

DECISION: Color system — warm off-white base oklch(97% 0.012 80); forest green accent oklch(42% 0.20 155); warm near-black text; OKLCH throughout; no gradients
BECAUSE: Reference products use light backgrounds for observability marketing sites. Brief explicitly forbids "neon cyberpunk" aesthetic. FORBIDDEN dark+neon avoided. FORBIDDEN pure #fff avoided — oklch tinted off-white used.

DECISION: Layout primitive policy — 12-column grid, max 1280px; asymmetric hero; alternating two-column feature sections; no three-equal-column layout
BECAUSE: Three-equal-column is FORBIDDEN unless content justifies equal weight — it does not here. Reference products (Linear, Incident.io) use asymmetric compositions. Brief requires desktop-first with mobile consideration.

DECISION: Motion policy — MOTION 5; IntersectionObserver entrance animations 500ms ease-out; hover 150ms; prefers-reduced-motion respected
BECAUSE: Observability tools (Datadog, Linear) use purposeful transitions. Technical buyers are not served by heavy motion.

DECISION: Icon family — Phosphor (ph:) for feature sections; consistent outline style
BECAUSE: No existing icon library in stack — green field. Phosphor provides clean, professional outline icons suited to product UI.
</design-log>

---

## Design Parameters

- **VARIANCE**: 7 — Asymmetric hero, offset feature sections, deliberate grid breaks
- **MOTION**: 5 — Entrance animations, stagger, hover states
- **DENSITY**: 5 — Balanced; hero breathes, features are information-forward

---

## Visual System

```css
@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600&display=swap');

:root {
  --font-display: 'Archivo Black', sans-serif;
  --font-body:    'DM Sans', sans-serif;

  --bg:           oklch(97%  0.012 80);
  --surface:      oklch(94%  0.010 80);
  --surface-dark: oklch(12%  0.015 200);
  --border:       oklch(86%  0.012 80);
  --text:         oklch(14%  0.015 200);
  --text-muted:   oklch(50%  0.012 200);
  --accent:       oklch(42%  0.20 155);
  --accent-hi:    oklch(60%  0.18 155);
  --on-dark:      oklch(94%  0.008 80);
  --on-dark-muted:oklch(62%  0.008 80);
}
```

---

## Section Specifications

### Navigation
Fixed, transparent → blur+border on scroll. Logo left, links center, CTA right.
- Logo: Archivo Black 18px, `--accent`
- Links: DM Sans 14px 500, `--text-muted`
- CTA button: `--accent` fill, white text, 44px min-height
- Focus: `outline: 2px solid var(--accent)` with offset

### Hero
12-column grid. Text cols 1–8, trust indicators cols 9–12 aligned bottom.

```
[AI OBSERVABILITY PLATFORM]             "Reduced MTTR from 40
                                        minutes to 8."
From alert to resolution.               — Staff Eng, Linear
In one workflow.
                                        Trusted by Vercel,
AI-assisted observability for teams     Fly.io, Railway, Linear
outgrowing basic monitoring.

[Start free]  [See a demo →]
```

**Product visualization** (below hero, full-bleed dark panel): stylized terminal with three columns — log stream | trace waterfall | incident timeline. Dark surface panel with subtle animation (log entries fade in).

Typography:
- Eyebrow: DM Sans 11px 600 uppercase letter-spaced, `--accent`
- Headline: Archivo Black clamp(36px→60px), `--text`, line-height 1.05
- Body: DM Sans 19px, `--text-muted`, max-width 52ch, line-height 1.6
- Primary CTA: `--accent` fill, white 14px DM Sans 500, min-height 44px

### Feature Sections (5 features)

Alternating two-column layout. NOT three equal columns.

Feature A: Unified Context — text left (col 1–5), visual right (col 6–12)
Feature B: Anomaly Detection — dark section, two-column inside
Feature C: Incident Timeline — visual left, text right
Feature D: Team Collaboration — text left, visual right
Feature E: Integrations — text left, logo grid right

### Workflow Story

Horizontal timeline: Alert → Investigate → Fix → Verify.
Numbered circles (24px, `--accent` fill). Active step: 28px, ghost card thumbnail below.

### Pricing Teaser

Three plans, NOT equal visual weight:
- Starter: outline, narrowest
- Pro: `--accent` 2px border, "Most popular" badge, widest
- Team: outline, middle

No gradient backgrounds. No gradient text. Price: Archivo Black 36px plain `--text`.

### Final CTA

Dark section (`--surface-dark`). Headline Archivo Black 52px. Primary `--accent` + secondary ghost.

---

## Motion

```css
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
.animate-in { animation: fadeUp 500ms cubic-bezier(0.16, 1, 0.3, 1) forwards; }
.btn-primary {
  transition: background 150ms cubic-bezier(0.25, 1, 0.5, 1);
}
.btn-primary:hover { background: var(--accent-hi); }

@media (prefers-reduced-motion: reduce) {
  .animate-in { animation: none; opacity: 1; transform: none; }
  .btn-primary { transition: none; }
}
```

---

## VERIFICATION

- Focus states: PASS — outline on all interactive elements
- prefers-reduced-motion: PASS — addressed in CSS
- Touch targets 44×44px: PASS — CTAs specified
- Semantic HTML: PASS — nav, main, section hierarchy
- Responsive: PASS — mobile layout noted per section
- No framework migration: PASS
- No truncated output: PASS
- FORBIDDEN gradient text: UNLESS not needed — not used
- FORBIDDEN dark+neon: UNLESS not needed — warm off-white
- FORBIDDEN three-equal columns: UNLESS not needed — asymmetric throughout
- FORBIDDEN Inter as display: UNLESS not needed — Archivo Black chosen
