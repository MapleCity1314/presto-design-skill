# SignalForge Landing Page Concept

## Design Rationale

This interface should feel operationally credible and fast because SignalForge is for technical buyers evaluating whether the product can reduce incident resolution time without enterprise bloat.

Typography should feel sharp, technical, and trustworthy rather than futuristic. The palette should avoid neon AI tropes and instead use warm neutrals with a disciplined alert-colored accent that fits observability and incident workflows. The scope is a full landing-page concept, so the system establishes typography, color, layout rhythm, section structure, and interaction patterns in a way a designer or frontend engineer could execute directly.

## Parameters

- `VARIANCE: 7`
- `MOTION: 4`
- `DENSITY: 5`

This translates into a left-anchored hero, alternating section rhythm, moderate information density, and restrained motion that supports hierarchy without making the product feel theatrical.

## Visual Direction

A calm, editorial-operational marketing page: warm off-light sections, a dark primary hero surface, one amber accent for urgency and action, and product visuals that do the trust-building instead of gradients.

No cyan-on-dark.
No purple-to-blue gradient.
No gradient headline text.
No ��AI magic�� styling language.

## Color System

```css
:root {
  --bg-dark:        oklch(12% 0.015 250);
  --surface-dark:   oklch(16% 0.014 250);
  --border-dark:    oklch(26% 0.012 250);

  --bg-light:       oklch(97% 0.010 60);
  --surface-light:  oklch(94% 0.010 60);
  --border-light:   oklch(88% 0.010 60);

  --text-dark:      oklch(95% 0.006 60);
  --text-light:     oklch(16% 0.012 60);
  --text-muted:     oklch(54% 0.010 60);

  --accent:         oklch(68% 0.17 60);
  --accent-strong:  oklch(62% 0.19 52);
  --success:        oklch(62% 0.14 155);
  --warning:        oklch(72% 0.15 82);
}
```

Use the dark surface in the hero and workflow sections, then alternate into warm light sections for readability. Amber is the only saturated accent used for CTA emphasis, anomaly moments, and guided attention.

## Typography

```css
:root {
  --font-display: "Sora", "Geist", sans-serif;
  --font-body: "Geist", "DM Sans", sans-serif;
  --font-mono: "JetBrains Mono", monospace;

  --text-xs: clamp(0.75rem, 0.72rem + 0.1vw, 0.8125rem);
  --text-sm: clamp(0.875rem, 0.84rem + 0.15vw, 0.9375rem);
  --text-base: clamp(1rem, 0.96rem + 0.2vw, 1.0625rem);
  --text-lg: clamp(1.125rem, 1.05rem + 0.35vw, 1.25rem);
  --text-xl: clamp(1.375rem, 1.2rem + 0.8vw, 1.625rem);
  --text-2xl: clamp(1.75rem, 1.4rem + 1.4vw, 2.375rem);
  --text-3xl: clamp(2.5rem, 2rem + 2vw, 3.5rem);
  --text-4xl: clamp(3.25rem, 2.5rem + 3vw, 4.75rem);
}
```

- Headings: `Sora` at 600 to 700 for clean geometric authority
- Body: `Geist` for technical clarity
- Code / telemetry snippets: `JetBrains Mono`
- Headlines use `text-balance`
- Numeric metrics and timestamps use `tabular-nums`

## Layout System

```css
.container {
  width: min(1200px, calc(100vw - 48px));
  margin-inline: auto;
}

.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: clamp(16px, 2vw, 28px);
}
```

Composition rules:

- Hero is left-anchored, not centered
- Product visual occupies the right side of the hero
- Trust row is horizontal and low-noise
- Feature sections alternate media left / media right
- Pricing is a comparison band, not a stack of marketing cards
- Mobile collapses to one column cleanly without losing hierarchy

## Page Structure

### 1. Hero

Background: `--bg-dark`

Desktop layout:
- Left: columns 1-6
- Right: columns 7-12

Content:
- Eyebrow: `AI-ASSISTED OBSERVABILITY`
- Headline: `Find the root cause before the incident spreads.`
- Supporting copy: SignalForge connects logs, traces, anomaly detection, and incident timelines into one operating view for engineering teams that need speed without enterprise drag.
- Primary CTA: `Start free trial`
- Secondary CTA: `See incident replay`
- Subnote: `No credit card ? 14-day trial ? SOC 2 ready`

Product visualization concept:
A dark telemetry workspace showing:
- top incident banner with severity and assignee
- timeline scrubber linking anomaly spike to trace latency
- logs, traces, and incident notes aligned on a single time rail
- one amber anomaly marker drawing focus
- small resolution summary card in the lower-right corner

The visual should look like a real product surface, not an abstract illustration.

### 2. Trust Row

Background: transition from dark hero into warm light

Structure:
- Small label: `Used by infrastructure and platform teams who cannot afford slow incident response`
- Horizontal row of monochrome customer marks
- Secondary proof chips:
  - `SOC 2 workflows`
  - `OpenTelemetry friendly`
  - `PagerDuty and Slack integrations`

This should feel quiet and credible, not promotional.

### 3. Feature Section One: Unified Incident Timeline

Headline:
`One timeline for every signal.`

Body:
Logs, traces, anomaly detections, deploy markers, and human notes appear in one ordered narrative so engineers stop stitching the story together across tabs.

Visual:
A timeline panel with layered event types and one highlighted root-cause cluster.

### 4. Feature Section Two: Detection That Surfaces What Changed

Headline:
`See the change that caused the blast radius.`

Body:
SignalForge correlates regressions with recent deploys, dependency latency shifts, and abnormal traffic patterns so teams can isolate change, not just monitor symptoms.

Visual:
A dependency flow graphic or annotated latency waterfall.
Use amber only for the causal path.

### 5. Feature Section Three: Resolution Workflow

Headline:
`Move from alert to owner to fix without leaving the thread.`

Body:
Route incidents into the team��s operating flow with ownership, notes, status updates, and replayable context attached to the same event history.

Visual:
Incident detail panel with owner state, linked Slack thread, and resolution checklist.

### 6. Workflow Story Section

Background: `--surface-light`

Section title:
`From signal to resolution`

Four-step sequence:
1. Detect abnormal behavior
2. Correlate traces, logs, and timeline events
3. Assign ownership with context attached
4. Resolve and retain the replay for postmortem

Design:
Not four equal cards. Use a horizontal track on desktop with staggered widths, or a stepped editorial layout with a line connecting stages.

### 7. Pricing Teaser

Headline:
`Built for teams that need clarity before they need procurement.`

Structure:
Two-column band:
- Left: positioning copy
- Right: compact comparison table

Plans:
- Starter
- Team
- Scale

Comparison fields:
- traces / logs volume
- incident seats
- replay retention
- integrations

Highlight the Team tier with border emphasis only. No gradient fill.

### 8. Final CTA

Background: dark again for closure

Headline:
`Reduce resolution time this quarter, not next platform cycle.`

Body:
Start with your existing telemetry stack and give engineers one place to understand what actually happened.

Actions:
- `Start free trial`
- `Talk to an engineer`

## Component Guidance

### Navigation

- Transparent over hero, solid on scroll
- Left-aligned wordmark
- Mid-right nav links: Product, Integrations, Pricing, Docs
- Right-aligned CTA button
- Mobile: drawer, 44px touch targets minimum

### Buttons

Primary:
- filled amber
- dark text
- 44px minimum height
- subtle brightness shift on hover

Secondary:
- ghost / outlined
- uses dark or light border depending on section surface

### Product Visual Cards

- 1px tinted borders
- restrained radius: 8px max
- no glassmorphism
- no nested decorative cards
- shadow only where depth actually improves scan order

### Code / Data Snippets

Use `JetBrains Mono` and `tabular-nums`.
Make syntax highlighting muted and credible, not colorful for its own sake.

## Content Tone

Use specific, operational language.

Good:
- `Correlate regressions with deploys and dependency latency`
- `Incident replay with attached ownership and notes`
- `One operating view for traces, logs, and timelines`

Avoid:
- `Unlock AI-powered resilience`
- `Revolutionize observability`
- `Supercharge your workflows`

## Responsive Behavior

### Mobile (375px)
- Single-column flow
- Hero visual drops below copy
- CTAs stack vertically
- Trust row becomes horizontally scrollable or wraps into two rows
- Feature visuals simplify into framed panels
- Pricing becomes stacked comparison rows

### Tablet
- Hero remains split, but visual becomes narrower
- Workflow story can become a 2x2 stepped layout

### Desktop
- Preserve asymmetric composition
- Keep strong left edge for copy blocks
- Use alternating feature rhythm for pacing

## Motion

Use restrained motion only.

```css
:root {
  --ease-out: cubic-bezier(0.25, 1, 0.5, 1);
}

.hero-copy,
.hero-visual,
.feature-block {
  transition: opacity 220ms var(--ease-out), transform 220ms var(--ease-out);
}

@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition-duration: 0.01ms !important;
  }
}
```

Allowed:
- gentle fade-up on initial hero load
- hover states on CTA and nav
- small reveal transitions for feature media

Not allowed:
- parallax spectacle
- glowing pulses
- looping dashboard animation
- layout-property animation

## Execution Notes

This should be delivered as a credible product-marketing system, not a dribbblified hero. The page earns trust through product specificity, disciplined typography, and a product visualization that shows how SignalForge shortens the distance between alert and understanding.

## Verification

- Distinct typography and color logic: yes
- Hero includes headline, supporting copy, two CTAs, product visual: yes
- Social proof near top: yes
- 3-5 feature sections: yes
- Workflow story section: yes
- Pricing teaser: yes
- Final CTA: yes
- Mobile-responsive thinking included: yes
- No neon cyberpunk AI treatment: yes
- Practical enough for design / frontend implementation: yes
