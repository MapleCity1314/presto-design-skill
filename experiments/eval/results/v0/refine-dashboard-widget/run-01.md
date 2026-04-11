# Quorum P&L Widget Refinement — v0

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
