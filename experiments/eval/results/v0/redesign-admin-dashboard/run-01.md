# Canopy HR Dashboard Redesign — v0

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
