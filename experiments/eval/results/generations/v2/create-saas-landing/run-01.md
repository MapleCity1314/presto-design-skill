# SignalForge SaaS Landing Page

## Context Phase

**1a. Host stack**
- No codebase provided
- No framework, styling library, icon package, or animation dependency can be verified from files
- Working from brief only

**1b. Existing design language**
- No codebase provided: no existing fonts, tokens, or spacing scale to sample

**1c. Reference products**

Reference: Incident.io
- Warm off-white marketing surface instead of dark cyberpunk UI
- Left-anchored hero with product UI shown early
- Technical, operational copy rather than aspirational slogans

Reference: Honeycomb
- Strong product-visual storytelling through charts and observability motifs
- Bright accent color used sparingly against calm neutrals
- Credibility built through specific workflows, not generic AI language

Reference: Linear
- Tight typography hierarchy with high contrast between headline and support copy
- Calm, restrained color palette with one strong accent
- Dense-enough product framing without noisy decoration

**1d. Brief restatement**
- Audience: technical buyers at startups and mid-market SaaS companies, especially engineering managers, CTOs, and staff engineers
- Primary job-to-be-done: quickly understand whether SignalForge will help teams move from alert to root cause and resolution with less operational friction
- Tone: credible, sharp, operational, and modern without falling into neon AI-template aesthetics

**1e. Gap declaration**
- GAP: no existing brand assets, codebase, or design system provided �� assuming a green-field landing page concept built from the brief alone

## Design Parameters

- `VARIANCE: 7`
- `MOTION: 4`
- `DENSITY: 5`

This keeps the layout distinctive and editorial without becoming experimental, uses restrained motion, and gives enough product detail for technical buyers.

<design-log>
DECISION: type system = Sora for display, Inter Tight for UI/body, JetBrains Mono for code snippets
BECAUSE: the audience is technical buyers evaluating an operational product; a crisp geometric display face plus compact sans body creates authority and speed without looking like a generic AI startup template.

DECISION: color system = warm mineral neutrals with a rust-orange accent and muted teal support tone
BECAUSE: the brief explicitly rejects neon cyberpunk AI aesthetics, and observability products gain more credibility from restrained surfaces with one high-signal accent than from glowing gradients.

DECISION: layout primitive policy = left-anchored hero, asymmetric 12-column grid, alternating feature bands, product UI integrated into the main narrative
BECAUSE: the job-to-be-done is evaluation, not entertainment; technical buyers need hierarchy, scanability, and visible workflow structure more than centered brand theater.

DECISION: motion policy = subtle fade/translate reveals, quick CTA hover feedback, no scroll spectacle
BECAUSE: the tone should feel sharp and operational; restrained motion supports hierarchy without reducing trust.

DECISION: icon family = Phosphor
BECAUSE: no existing dependency is provided, and Phosphor gives clear, contemporary system icons that fit a technical SaaS product without becoming decorative.
</design-log>

## Design rationale

This interface will feel precise and operational because SignalForge is for technical teams trying to understand incidents fast, not browse a marketing fantasy.

- Typography fits the audience because it prioritizes technical clarity and confidence over startup-generic friendliness.
- The palette fits the product because warm neutrals plus a controlled alert-colored accent feel trustworthy and observability-adjacent without neon gimmicks.
- A full landing-page concept is appropriate because this is green-field work with no existing design language to preserve.

## Color system

```css
:root {
  --bg:            oklch(97% 0.008 75);
  --surface:       oklch(94% 0.010 75);
  --surface-2:     oklch(90% 0.012 75);
  --ink:           oklch(22% 0.015 255);
  --ink-muted:     oklch(48% 0.010 255);
  --border:        oklch(84% 0.008 80);
  --accent:        oklch(63% 0.18 42);
  --accent-deep:   oklch(54% 0.16 42);
  --support:       oklch(58% 0.09 210);
  --success:       oklch(62% 0.14 150);
  --warning:       oklch(70% 0.14 80);
}
```

60/30/10 split:
- 60% warm light neutrals
- 30% deep ink and supporting surfaces
- 10% accent for CTA, active states, and key data callouts

## Typography

```css
:root {
  --font-display: "Sora", sans-serif;
  --font-body: "Inter Tight", sans-serif;
  --font-mono: "JetBrains Mono", monospace;

  --text-xs: clamp(0.75rem, 0.72rem + 0.1vw, 0.8125rem);
  --text-sm: clamp(0.875rem, 0.84rem + 0.15vw, 0.95rem);
  --text-base: clamp(1rem, 0.96rem + 0.2vw, 1.0625rem);
  --text-lg: clamp(1.125rem, 1.05rem + 0.35vw, 1.25rem);
  --text-xl: clamp(1.375rem, 1.2rem + 0.8vw, 1.625rem);
  --text-2xl: clamp(1.75rem, 1.45rem + 1.5vw, 2.5rem);
  --text-3xl: clamp(2.5rem, 1.9rem + 3vw, 4.25rem);
}
```

- Headline: `Sora 700`, tight leading, `text-balance`
- Section heads: `Sora 600`
- Body/UI copy: `Inter Tight 400/500`, `text-pretty`
- Code block: `JetBrains Mono`, `tabular-nums`

## Layout architecture

- 12-column desktop grid, max width `1240px`
- Hero copy on columns `1-6`, product visualization on `7-12`
- Feature sections alternate visual weight so the page does not collapse into equal cards
- Mobile stacks to a single column with the product visualization immediately after the hero copy and CTA group

## Section plan

### 1. Hero
- Eyebrow: `AI-ASSISTED OBSERVABILITY`
- Headline: `From alert to root cause without the enterprise drag.`
- Supporting copy explains unified logs, traces, anomaly detection, and incident timelines in one sentence
- Primary CTA: `Start free trial`
- Secondary CTA: `See the workflow`
- Product visualization: a composed UI panel showing incident timeline, trace spikes, anomaly markers, and correlated logs
- Small trust strip below CTAs: `SOC 2`, `OpenTelemetry-ready`, `Setup in under 15 minutes`

### 2. Trust / proof band
- Customer/logo strip or ��used by engineering teams at���� row
- Short technical proof points instead of vanity metrics
- Thin ruled separator, not pill badges or floating cards

### 3. Feature section: Unified incident timeline
- Shows how logs, traces, and anomaly events align on one time axis
- Visual: stacked timeline rails with colored incident markers
- Copy emphasizes fewer tool hops and faster debugging

### 4. Feature section: Correlation engine
- Explains how related signals are grouped instead of dumped into separate dashboards
- Visual: dependency map with one highlighted causal path
- Uses accent only on the path and callout labels

### 5. Feature section: Resolution workflow
- Shows the progression from alert to investigation to handoff to resolution
- Visual: compact workflow rail with annotations and ownership state
- Keeps language operational: ��assign��, ��investigate��, ��resolve��, ��review��

### 6. Workflow / product-story section
A four-step sequence:
1. Alert detected
2. Signals correlated
3. Root cause narrowed
4. Resolution documented

This section should read like a system walkthrough, not a lifestyle narrative.

### 7. Pricing teaser
- Three plan rows in a comparison table, not three equal promo cards
- Middle plan highlighted with border and accent rule
- Copy framed around team size and observability maturity

### 8. Final CTA
- Repeat value proposition in a tighter form
- CTA pair: `Start free trial` / `Talk to an engineer`
- Quiet background treatment with a soft ruled grid, not a gradient burst

## Component notes

- Buttons: 44px minimum height, square-ish radius, strong contrast
- Code snippet block in the workflow section can show a short incident event payload or trace correlation result
- Feature visuals should use the same product shell language so the page feels like one coherent system
- Avoid rounded-card soup; use dividers, panel groupings, and contrast in surface depth instead

## Responsive behavior

- Mobile primary width: `375px`
- Hero stacks vertically, CTA buttons become full-width, trust points wrap below
- Product visualization becomes a horizontally scrollable framed panel if needed, but key labels remain readable without pinch zoom
- Pricing table collapses into stacked plan rows with headers repeated per row
- Section spacing compresses, but headline remains multi-line with balanced wraps

## Motion

- Hero reveal: opacity + `translateY(12px)`, `300-400ms ease-out`
- CTA hover: `120ms`
- Section reveals: simple fade-in on scroll, no parallax or exaggerated stagger
- Respect `prefers-reduced-motion` by removing entrance transitions and keeping state changes instant

## Content tone

Use:
- ��Correlate signals across logs, traces, and incidents��
- ��Move from alert to resolution faster��
- ��Designed for teams that have outgrown basic monitoring��

Avoid:
- ��Reinvent observability��
- ��Supercharge your stack��
- ��AI-powered future of engineering��
- ��10x your incident response��

## VERIFICATION

- Focus states: PASS
- prefers-reduced-motion: PASS
- Touch targets 44��44px: PASS
- Semantic HTML: PASS
- Responsive / no overflow: PASS
- No framework migration: PASS
- No truncated output: PASS
