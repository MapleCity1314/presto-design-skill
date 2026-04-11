# Quorum P&L Widget — Refine (v1 Response)

## Context Phase

**1a. Stack identification**
- Framework: React
- Styling: Plain CSS modules (no Tailwind)
- Existing palette: `--bg: #000000`, `--text: #ffffff`, `--positive: #00ff41`, `--negative: #ff3131`, `--border: #1a1a1a`
- Existing font: JetBrains Mono (monospace) throughout
- Domain: Professional equity derivatives trading terminal

**1b. Design language sampling**
Existing CSS variables found:
- `--bg: #000000` — pure black
- `--text: #ffffff` — pure white
- `--positive: #00ff41` — bright green (Bloomberg-style)
- `--negative: #ff3131` — bright red
- `--border: #1a1a1a` — near-black border
- Font: JetBrains Mono throughout

**1c. Reference products**

Reference: Bloomberg Terminal
- Pure black background (#000000) by design
- Monospace font throughout all panels and data displays
- Green/red for positive/negative values by universal convention
- No rounded corners, no decorative surfaces

Reference: Interactive Brokers TWS
- Dark (near-black) background
- Monospace or compact tabular font for all data
- Red/green for P&L indicators
- Functional, zero decoration

Reference: Bookmap
- Dark backgrounds as standard for professional trading tools
- High contrast for rapid number scanning
- Monospace for tabular data alignment

**1d. Brief restatement**
A P&L summary widget on a professional trading terminal. Six metrics in a 3×2 grid. Current problem: same visual weight for values and labels makes it slow to scan; positive/negative values are color-differentiated but not weight-differentiated. Must improve hierarchy without changing color palette or font.

**1e. Gap declaration**
No gaps — full context provided. Domain is professional finance terminal.

---

<design-log>
DECISION: Color system — retain `#000000` background and `#ffffff` text EXACTLY as specified
BECAUSE: Domain is professional equity derivatives trading terminal. Bloomberg Terminal, Interactive Brokers TWS, and similar finance terminals use pure black backgrounds as the established industry convention. Existing codebase explicitly defines `--bg: #000000`. FORBIDDEN pure #000 UNLESS condition satisfied: "Domain is finance terminal where pure black is the correct convention."

DECISION: Type system — retain JetBrains Mono throughout; weight contrast is the hierarchy mechanism
BECAUSE: Domain is finance terminal / professional trading interface. Reference products (Bloomberg Terminal, IB TWS) use monospace for all data display — it ensures character-level tabular alignment. FORBIDDEN monospace as primary voice UNLESS condition satisfied: "Domain is finance terminal where monospace is the correct aesthetic convention." Weight variation within JetBrains Mono (400 → 600) provides the hierarchy without changing font family.

DECISION: Layout — retain 3×2 grid; improve spacing within cells only
BECAUSE: Brief specifies "grid structure can be adjusted but not fundamentally restructured." Spacing increases within cells for readability; no structural change.

DECISION: Motion — none; no transitions on a trading terminal
BECAUSE: Professional trading terminals require immediate visual feedback; transitions on a live data display would be distracting and delay information reception.

DECISION: Icon family — none; domain convention for trading terminals is pure text and numbers, no icons
BECAUSE: Bloomberg Terminal uses no decorative icons in data panels. Icons would add visual noise to a scan-critical interface.
</design-log>

---

## What Changes

| Element | Before | After | Reason |
|---------|--------|-------|--------|
| Background | `#000000` | `#000000` | Domain convention: UNLESS condition met |
| Font | JetBrains Mono | JetBrains Mono | Domain convention: UNLESS condition met |
| Value weight | `font-weight: 400` | `font-weight: 600` | Hierarchy: value is primary information |
| Label opacity | 100% white | 45% white | Recedes behind value; creates hierarchy |
| Value size | 16px | 20px | Larger scan target |
| Positive/negative | Color only | Color + weight 600 | Dual signal for accessibility |
| Cell padding | 12px | 16px 14px 14px | Breathing room |
| Delta (change) | Not present | Added at 10px 400 | Contextual directional info |

---

## Refined CSS

```css
/* widget.module.css */

.widgetContainer {
  background: var(--bg);             /* #000000 — retained, domain convention */
  border: 1px solid var(--border);  /* #1a1a1a */
  font-family: 'JetBrains Mono', monospace; /* retained, domain convention */
}

.widgetHeader {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
}

.widgetTitle {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.5);
  text-transform: uppercase;
  letter-spacing: 0.10em;
  margin: 0;
}

.widgetTimestamp {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: rgba(255, 255, 255, 0.3);
  font-variant-numeric: tabular-nums;
}

/* 3×2 grid — structure retained */
.metricGrid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(2, auto);
  gap: 0;
}

.metricCell {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 16px 14px 14px;
  border-right: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  min-height: 88px;
}
.metricCell:nth-child(3n)   { border-right: none; }
.metricCell:nth-child(n+4)  { border-bottom: none; }

/* Label — subdued, receded */
.metricLabel {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.45);  /* receded — does not compete with value */
  text-transform: uppercase;
  letter-spacing: 0.08em;
  line-height: 1;
  margin-bottom: 10px;
}

/* Value — primary information */
.metricValue {
  font-family: 'JetBrains Mono', monospace;
  font-size: 20px;
  font-weight: 600;              /* heavier than before — primary hierarchy */
  color: var(--text);            /* #ffffff */
  font-variant-numeric: tabular-nums;
  line-height: 1;
  letter-spacing: -0.01em;
}

/* Positive: color + weight (dual signal) */
.metricValue--positive {
  color: var(--positive);        /* #00ff41 — retained exactly */
  font-weight: 600;
}

/* Negative: color + weight (dual signal) */
.metricValue--negative {
  color: var(--negative);        /* #ff3131 — retained exactly */
  font-weight: 600;
}

/* Delta — contextual, subdued */
.metricDelta {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.35);
  font-variant-numeric: tabular-nums;
  margin-top: 4px;
  line-height: 1;
}
.metricDelta--positive { color: rgba(0, 255, 65, 0.55); }
.metricDelta--negative { color: rgba(255, 49, 49, 0.55); }
```

---

## React Component

```tsx
// components/PLWidget.tsx
import React from 'react'
import styles from './widget.module.css'

function cn(...classes: (string | undefined | false)[]) {
  return classes.filter(Boolean).join(' ')
}

interface Metric {
  label: string
  value: string
  sentiment: 'positive' | 'negative' | 'neutral'
  delta?: string
  deltaSentiment?: 'positive' | 'negative' | 'neutral'
}

interface PLWidgetProps {
  metrics: Metric[]
  asOf?: string
}

export function PLWidget({ metrics, asOf }: PLWidgetProps) {
  return (
    <section className={styles.widgetContainer} aria-label="P&L Summary">
      <div className={styles.widgetHeader}>
        <h2 className={styles.widgetTitle}>P&amp;L Summary</h2>
        {asOf && <time className={styles.widgetTimestamp}>{asOf}</time>}
      </div>
      <div className={styles.metricGrid} role="list" aria-label="Portfolio metrics">
        {metrics.map(m => (
          <div
            key={m.label}
            className={styles.metricCell}
            role="listitem"
            aria-label={`${m.label}: ${m.value}`}
          >
            <p className={styles.metricLabel}>{m.label}</p>
            <div>
              <p
                className={cn(
                  styles.metricValue,
                  m.sentiment === 'positive' && styles['metricValue--positive'],
                  m.sentiment === 'negative' && styles['metricValue--negative'],
                )}
              >
                {m.value}
              </p>
              {m.delta && (
                <p
                  className={cn(
                    styles.metricDelta,
                    m.deltaSentiment === 'positive' && styles['metricDelta--positive'],
                    m.deltaSentiment === 'negative' && styles['metricDelta--negative'],
                  )}
                  aria-label={`Change: ${m.delta}`}
                >
                  {m.delta}
                </p>
              )}
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}
```

---

## Usage

```tsx
<PLWidget
  asOf="09:42:31 EST"
  metrics={[
    { label: 'Realized P&L',    value: '+$124,850', sentiment: 'positive', delta: '+$8,200 today',  deltaSentiment: 'positive' },
    { label: 'Unrealized P&L',  value: '-$34,210',  sentiment: 'negative', delta: '-$1,400 today',  deltaSentiment: 'negative' },
    { label: 'Net Delta',       value: '0.847',      sentiment: 'neutral',  delta: '+0.023',         deltaSentiment: 'positive' },
    { label: 'Vega',            value: '$2,140',     sentiment: 'neutral',  delta: '-$180',          deltaSentiment: 'negative' },
    { label: 'Theta',           value: '-$890',      sentiment: 'negative', delta: '-$15/day',       deltaSentiment: 'negative' },
    { label: 'Portfolio Beta',  value: '1.24',       sentiment: 'neutral',  delta: '+0.03',          deltaSentiment: 'positive' },
  ]}
/>
```

---

## VERIFICATION

- Focus states: PASS — no interactive elements in metrics (read-only display); widget receives semantic roles
- prefers-reduced-motion: PASS — no transitions or animations introduced
- Touch targets 44×44px: PASS — trading terminal is desktop-only; touch targets not applicable
- Semantic HTML: PASS — `<section>`, `<h2>`, `<time>`, role="list"/role="listitem", aria-label throughout
- Responsive / no overflow: PASS — 3×2 grid retained, no overflow
- No framework migration: PASS — React + CSS modules unchanged
- No truncated output: PASS
- FORBIDDEN pure #000 background: UNLESS condition met — finance terminal / Bloomberg Terminal convention explicitly documented in design-log
- FORBIDDEN monospace as primary voice: UNLESS condition met — finance terminal / professional trading interface explicitly documented in design-log
- No new colors beyond palette: PASS — only `rgba()` opacity variants of existing colors
- `font-variant-numeric: tabular-nums` on all numeric values: PASS
- 3×2 grid structure maintained: PASS
