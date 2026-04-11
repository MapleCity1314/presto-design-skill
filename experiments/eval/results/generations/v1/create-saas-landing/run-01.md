# SignalForge Landing Page Design Direction

## Design Rationale

This interface should feel operational, credible, and fast because SignalForge is for engineering leaders evaluating an observability product they will trust during incidents, not a marketing toy.

Typography should signal technical authority without falling into generic AI-SaaS defaults. The palette should feel calm and precise, with color used for meaning rather than spectacle. The page should establish a full design system because this is a green-field landing page, not a refinement of an existing brand surface.

## Parameters

- VARIANCE: 7
- MOTION: 4
- DENSITY: 5

## Typography

- Display: `Cabinet Grotesk`
- Body: `Geist`
- Mono: `JetBrains Mono`

```css
:root {
  --font-display: "Cabinet Grotesk", sans-serif;
  --font-body: "Geist", "DM Sans", sans-serif;
  --font-mono: "JetBrains Mono", monospace;

  --text-xs: clamp(0.75rem, 0.72rem + 0.1vw, 0.8125rem);
  --text-sm: clamp(0.875rem, 0.84rem + 0.15vw, 0.9375rem);
  --text-base: clamp(1rem, 0.96rem + 0.2vw, 1.0625rem);
  --text-lg: clamp(1.125rem, 1.05rem + 0.35vw, 1.25rem);
  --text-xl: clamp(1.375rem, 1.2rem + 0.8vw, 1.75rem);
  --text-2xl: clamp(1.75rem, 1.35rem + 1.8vw, 2.5rem);
  --text-3xl: clamp(2.25rem, 1.7rem + 2.8vw, 3.75rem);
  --text-4xl: clamp(3rem, 2.1rem + 4vw, 5rem);
}
```

Why this works:
- `Cabinet Grotesk` has enough edge and compression to feel product-grade rather than template-grade.
- `Geist` is readable and technical without looking corporate.
- `JetBrains Mono` is reserved for product UI snippets and incident data, not used as the brand voice.

## Color System

Warm neutrals with a restrained amber accent. No cyan-on-dark, no purple gradient, no neon.

```css
:root {
  --bg:            oklch(97% 0.010 85);
  --surface:       oklch(94% 0.008 85);
  --surface-2:     oklch(90% 0.010 85);
  --border:        oklch(84% 0.010 85);

  --text:          oklch(18% 0.015 240);
  --text-muted:    oklch(45% 0.010 240);
  --text-soft:     oklch(60% 0.008 240);

  --panel:         oklch(14% 0.012 240);
  --panel-2:       oklch(18% 0.010 240);
  --panel-border:  oklch(28% 0.010 240);
  --panel-text:    oklch(94% 0.008 85);
  --panel-muted:   oklch(70% 0.008 85);

  --accent:        oklch(67% 0.17 62);
  --accent-hover:  oklch(72% 0.17 62);
  --success:       oklch(64% 0.14 145);
  --warning:       oklch(74% 0.15 82);
}
```

Color logic:
- Light surfaces build trust and readability for technical buyers.
- Dark product panels let the observability UI feel real without turning the whole marketing page into a dark-mode clich��.
- Amber highlights urgency and navigation without inheriting AI-brand tropes.

## Layout Architecture

- Max width: `1280px`
- Base container padding: `clamp(24px, 5vw, 72px)`
- 12-column grid on desktop
- Hero split: content `1 / 7`, product panel `8 / 13`
- Feature sections alternate text/visual alignment
- No full-page three-card layout anywhere

```css
.container {
  width: min(100% - clamp(24px, 5vw, 72px), 1280px);
  margin-inline: auto;
}

.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: clamp(16px, 2vw, 24px);
}
```

## Page Structure

### 1. Header

Left:
- SignalForge wordmark in `Cabinet Grotesk 700`

Center:
- Product
- Integrations
- Docs
- Pricing

Right:
- `Sign in`
- Primary CTA: `Start free trial`

Behavior:
- Sticky header with subtle background blur
- Border-bottom appears after scroll
- Mobile collapses into drawer with 44px tap targets

### 2. Hero

Left column:
- Eyebrow: `OBSERVABILITY / INCIDENT RESPONSE`
- Headline:
  `From alert to resolution, without the dashboard sprawl.`
- Supporting copy:
  `SignalForge unifies logs, traces, anomaly detection, and incident timelines into one operational workflow for engineering teams that need speed without enterprise drag.`
- CTAs:
  - Primary: `Start free trial`
  - Secondary: `See product walkthrough`
- Trust line:
  `SOC 2 Type II �� 5-minute setup �� No credit card`

Right column:
- Product visualization concept: a dark incident timeline panel
- Top row: incident title, severity badge, current owner
- Main body:
  - latency spike chart
  - trace waterfall
  - timeline events
  - anomaly callout
- Bottom row: resolution summary with highlighted root cause

This visual should feel like a believable product surface, not an abstract illustration.

### 3. Trust Bar

Directly below hero.

- `Trusted by platform and infrastructure teams at`
- 5-6 monochrome customer marks
- Low contrast by default, clearer on hover
- Presented as a simple horizontal row, not cards

### 4. Feature Sections

Four sections, alternating light and dark emphasis.

#### Feature 1: One timeline for the whole incident
Copy focus:
- Logs, traces, alerts, and deploy markers unified chronologically
Visual:
- Shared horizontal time axis with event density

#### Feature 2: Find the cause, not just the symptom
Copy focus:
- Correlates downstream failures to the triggering service event
Visual:
- Dependency flow with highlighted causal path

#### Feature 3: Built for responders, not dashboard tourists
Copy focus:
- Assignments, status, and next actions stay in the same workflow
Visual:
- Incident owner handoff panel with SLA countdown

#### Feature 4: Add signal without adding noise
Copy focus:
- Teams outgrowing basic monitoring but rejecting enterprise bloat
Visual:
- Settings/config panel showing fast onboarding and source connections

Each section should have:
- strong headline
- 1 short paragraph
- 2-3 support bullets
- product-shaped visual
- no equal-width feature-card trio

### 5. Workflow Section

Section title:
`Alert to resolution`

Format:
- horizontal 4-step sequence on desktop
- vertical stack on mobile

Steps:
1. Detect
2. Correlate
3. Assign
4. Resolve

Each step includes:
- large numeric marker
- short title
- concise explanation
- thin connecting rule between steps

This section should read like operational flow, not marketing storytelling.

### 6. Pricing Teaser

Two-column asymmetrical section.

Left:
- headline
- explanation of pricing posture
- link to full pricing

Right:
- compact comparison table

Plans:
- Starter
- Team
- Growth

Table style:
- ruled lines
- one highlighted recommended tier
- no floating pricing cards

### 7. Final CTA

Headline:
`See the full incident path before the next outage spreads.`

Support copy:
`Spin up SignalForge, connect your sources, and get a working incident timeline in minutes.`

Actions:
- `Start free trial`
- `Book a demo`

Background treatment:
- very subtle radial accent wash behind the CTA block
- restrained, not luminous

## Motion

Keep motion useful and quiet.

- Header transition: `150ms ease-out`
- Hero content reveal: fade + `translateY(12px)` over `350-450ms`
- Feature visuals: intersection-based reveal only
- Button feedback: `120ms`
- No bouncing, no elastic motion
- Full `prefers-reduced-motion` fallback

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

## Component Guidance

### Buttons
- 44px minimum height
- Primary uses amber fill
- Secondary is text or light outline
- Strong focus-visible ring

### Product Panel
- Use real data shapes
- Monospace only inside the panel
- High contrast inside dark surfaces
- Avoid fake glass or glowing chrome

### Code / Data Labels
- `JetBrains Mono`
- `tabular-nums`
- Small caps or uppercase only where operationally useful

## Responsive Behavior

### Mobile (375px)
- Hero becomes single-column
- Product panel stacks below CTAs
- Trust row becomes horizontally scrollable
- Workflow steps stack vertically
- Pricing table scrolls or simplifies to rows

### Tablet
- Hero remains split if space allows
- Feature sections keep alternating structure with reduced offsets

### Desktop
- Full 12-column composition
- Larger product panel presence
- More asymmetry in spacing and section rhythm

## Content Tone

Avoid:
- revolutionary
- next-gen
- unlock
- transform your workflow
- AI-powered future

Prefer:
- direct
- technical
- specific
- operationally credible

Examples:
- `Unify traces, logs, and incidents in one timeline.`
- `See what changed before the alert hit.`
- `Resolve incidents faster without adding another enterprise system.`

## Practical Execution Notes

A frontend designer or engineer should be able to build this from the output because it defines:
- font families
- color tokens
- layout system
- section order
- component behavior
- responsive intent
- motion constraints

## Self-Check

- Distinct typography direction chosen: yes
- Clear color logic without neon AI clich��s: yes
- Hero includes product visualization concept: yes
- Social proof included near top: yes
- 3-5 feature sections included: yes
- Workflow section included: yes
- Pricing teaser included: yes
- Final CTA included: yes
- Mobile-responsive thinking included: yes
- Output stays at design-spec level, not implementation code: yes
