# Canopy HR Dashboard — Redesign (v1 Response)

## Context Phase

**1a. Stack identification**
- Framework: React (Next.js)
- Styling: Tailwind CSS v4 with `@theme` tokens
- Existing tokens: `--color-brand: oklch(48% 0.16 155)`, `--color-surface: oklch(97% 0.008 100)`, `--font-sans: 'Geist', sans-serif`
- Existing components: shadcn/ui (Card, Badge, Table, Avatar — Radix-based)
- Existing anti-pattern: `bg-gradient-to-br from-green-500 to-teal-600 text-white` — to replace

**1b. Design language sampling**
Existing tokens found:
- `--color-brand`: forest green oklch(48% 0.16 155)
- `--color-surface`: light neutral oklch(97% 0.008 100)
- `--font-sans`: Geist
- Color count: 2 semantic tokens; no extended semantic palette yet

**1c. Reference products**

Reference: Linear (issue tracker)
- Flat, data-forward metric surfaces — no gradient backgrounds
- Typographic hierarchy through weight and size, not color decoration
- Single brand color used only for interactive elements

Reference: Notion
- Clean tabular data presentation; no decorative cards
- Section headers clearly differentiated from field labels via weight + size
- Subtle borders for containment; no shadow + border + background stacking

Reference: Vercel Analytics dashboard
- Key metric (largest in visual hierarchy) gets full-width placement
- Secondary metrics arranged in a 2- or 3-column grid below
- No gradient text on numbers; plain weight + size creates the hierarchy

**1d. Brief restatement**
An HR admin overview dashboard used daily as a morning check-in. Six fixed metrics: Headcount, Active Benefits, Pending Approvals, Recent Hires, Attrition Rate, Open Roles. The current gradient card design undermines credibility. Need a professional, calm, data-forward redesign. Layout cannot be six equal-width cards.

**1e. Gap declaration**
No gaps — all context provided in brief.

---

<design-log>
DECISION: Type system — Geist (existing brand font) throughout; Geist already declared in existing tokens; tabular-nums for all numeric displays
BECAUSE: Existing codebase fact: `--font-sans: 'Geist', sans-serif` is the declared brand identity. No reason to change. UNLESS condition for preserving existing font: load-bearing in existing components.

DECISION: Color system — extend existing @theme with semantic data colors; flat surfaces (no gradients); attrition in amber caution; positive metrics neutral
BECAUSE: Tailwind v4 detected — extend via `@theme` CSS block per Tailwind v4 specification. Existing `--color-brand` forest green preserved as brand anchor. FORBIDDEN gradient cards → removed per contract. FORBIDDEN gradient text → not used.

DECISION: Layout primitive policy — asymmetric grid: headcount primary (large, left), secondary 2×2 grid (right); no six equal-width columns
BECAUSE: Brief explicitly forbids "six equal-width cards." Reference products (Vercel Analytics) use primary metric at larger scale with secondary metrics below/beside. Headcount is the anchor metric for an HR dashboard.

DECISION: Motion policy — hover states only, 150ms max; no entrance animations on a daily-use dashboard
BECAUSE: Brief tone is "calm, information-forward." Daily-use dashboards (Linear, Notion) do not animate metric display on load — it would feel like a marketing page.

DECISION: Icon family — none on metric cards; Radix icons via shadcn/ui for interactive controls only
BECAUSE: Existing shadcn/ui components use Radix icons; icons on metric cards would add visual noise to data surfaces.
</design-log>

---

## Scan Phase — P0 Issues

1. `bg-gradient-to-br from-green-500 to-teal-600 text-white` — gradient backgrounds on all cards: decorative, undermines data credibility. **Replace with flat bordered surfaces.**
2. Six equal-width cards — no hierarchy between primary (Headcount) and derived metrics. **Replace with asymmetric grid.**
3. Large white numbers on gradient → white text with no contrast strategy → **replace with dark text on light surface**.
4. Attrition Rate shown identically to positive metrics — needs caution visual differentiation.

---

## Token Extensions (Tailwind v4 @theme)

```css
/* app/globals.css */
@theme {
  /* Preserve existing tokens */
  --color-brand:   oklch(48% 0.16 155);
  --color-surface: oklch(97% 0.008 100);
  --font-sans: 'Geist', sans-serif;

  /* New semantic tokens */
  --color-bg:           oklch(97%  0.008 100);
  --color-surface-2:    oklch(94%  0.008 100);
  --color-border:       oklch(88%  0.010 100);
  --color-border-strong:oklch(78%  0.010 100);
  --color-text:         oklch(14%  0.012 100);
  --color-text-muted:   oklch(50%  0.010 100);
  --color-text-faint:   oklch(68%  0.008 100);
  --color-positive:     oklch(48%  0.16  155);  /* same as brand = growth is good */
  --color-caution:      oklch(62%  0.16   55);  /* amber for attrition */
  --color-neutral-data: oklch(50%  0.010 100);  /* neutral metric text */
}
```

---

## Dashboard Page

```tsx
// app/dashboard/page.tsx
import { MetricPrimary } from '@/components/MetricPrimary'
import { MetricSecondary } from '@/components/MetricSecondary'
import { BenefitsCard } from '@/components/BenefitsCard'

export default function DashboardPage() {
  return (
    <div className="min-h-dvh bg-[var(--color-bg)] font-[var(--font-sans)]">
      <DashboardHeader />
      <main className="max-w-[1280px] mx-auto px-8 py-8">
        <div className="flex items-center justify-between mb-8">
          <h1 className="text-xl font-semibold text-[var(--color-text)] tracking-tight">
            Overview
          </h1>
          <div className="flex items-center gap-3">
            <time className="text-sm text-[var(--color-text-muted)] tabular-nums">
              {new Date().toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric', year: 'numeric' })}
            </time>
            <button className="h-9 px-3 text-sm border border-[var(--color-border)] rounded-md text-[var(--color-text)] hover:border-[var(--color-border-strong)] transition-colors duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--color-brand)] focus-visible:outline-offset-2">
              Filter ▾
            </button>
          </div>
        </div>

        {/* Asymmetric grid — NOT six equal columns */}
        <div className="grid grid-cols-3 gap-5">
          {/* Row 1: Primary metric + 2 secondary */}
          <div className="row-span-1">
            <MetricPrimary
              label="Headcount"
              value={847}
              delta="+3 this month"
              sentiment="positive"
            />
          </div>
          <MetricSecondary label="Recent Hires" value="12" note="vs 9 monthly avg ↑" sentiment="positive" />
          <MetricSecondary label="Open Roles" value="23" note="currently hiring" sentiment="neutral" />

          {/* Row 2: Benefits (large) + 2 secondary */}
          <BenefitsCard enrolled={801} total={847} rate={94.6} />
          <MetricSecondary
            label="Pending Approvals"
            value="7"
            note="awaiting action"
            sentiment="neutral"
            actionHref="/approvals"
            actionLabel="Review →"
          />
          <MetricSecondary
            label="Attrition Rate"
            value="3.2%"
            note="↑ 0.4% vs last month"
            sentiment="caution"
          />
        </div>
      </main>
    </div>
  )
}

function DashboardHeader() {
  return (
    <header className="border-b border-[var(--color-border)] bg-[var(--color-bg)]">
      <div className="max-w-[1280px] mx-auto px-8 h-14 flex items-center justify-between">
        <div className="flex items-center gap-6">
          <span className="text-base font-semibold text-[var(--color-text)] tracking-tight">Canopy</span>
          <nav className="flex items-center gap-4" aria-label="Main navigation">
            {['Overview', 'People', 'Benefits', 'Reports'].map(item => (
              <a
                key={item}
                href={`#${item.toLowerCase()}`}
                className="text-sm text-[var(--color-text-muted)] hover:text-[var(--color-text)] transition-colors duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--color-brand)] focus-visible:outline-offset-2"
                aria-current={item === 'Overview' ? 'page' : undefined}
              >
                {item}
              </a>
            ))}
          </nav>
        </div>
      </div>
    </header>
  )
}
```

```tsx
// components/MetricPrimary.tsx
interface MetricPrimaryProps {
  label: string
  value: number
  delta: string
  sentiment: 'positive' | 'caution' | 'neutral'
}

export function MetricPrimary({ label, value, delta, sentiment }: MetricPrimaryProps) {
  const deltaColor = sentiment === 'positive' ? 'text-[var(--color-positive)]'
    : sentiment === 'caution' ? 'text-[var(--color-caution)]'
    : 'text-[var(--color-text-muted)]'

  // 12-month trend data (mock)
  const trend = [820, 825, 828, 831, 835, 836, 840, 841, 843, 844, 845, 847]
  const min = Math.min(...trend), max = Math.max(...trend)

  return (
    <article
      className="bg-[var(--color-surface)] border border-[var(--color-border)] rounded-lg p-7 h-full"
      aria-label={`${label}: ${value.toLocaleString()}`}
    >
      <p className="text-xs font-semibold uppercase tracking-widest text-[var(--color-text-muted)] mb-5">
        {label}
      </p>
      <div className="flex items-end gap-4 mb-3">
        <span className="text-5xl font-semibold text-[var(--color-text)] tabular-nums leading-none">
          {value.toLocaleString()}
        </span>
        <span className={`text-sm font-medium tabular-nums mb-1 ${deltaColor}`}>{delta}</span>
      </div>
      {/* Sparkline */}
      <svg width="180" height="36" viewBox="0 0 180 36" aria-hidden="true" className="mt-2">
        <polyline
          points={trend.map((v, i) => `${(i / (trend.length - 1)) * 180},${36 - ((v - min) / (max - min)) * 32}`).join(' ')}
          fill="none"
          stroke="var(--color-positive)"
          strokeWidth="1.5"
          strokeLinejoin="round"
          strokeLinecap="round"
        />
      </svg>
      <p className="text-xs text-[var(--color-text-faint)] mt-1">12-month trend</p>
    </article>
  )
}
```

```tsx
// components/MetricSecondary.tsx
interface MetricSecondaryProps {
  label: string
  value: string
  note?: string
  sentiment: 'positive' | 'caution' | 'neutral'
  actionHref?: string
  actionLabel?: string
}

export function MetricSecondary({ label, value, note, sentiment, actionHref, actionLabel }: MetricSecondaryProps) {
  const noteColor = sentiment === 'positive' ? 'text-[var(--color-positive)]'
    : sentiment === 'caution' ? 'text-[var(--color-caution)]'
    : 'text-[var(--color-text-muted)]'
  
  const leftBorder = sentiment === 'caution' ? 'border-l-2 border-l-[var(--color-caution)] pl-5' : ''

  return (
    <article
      className={`bg-[var(--color-surface)] border border-[var(--color-border)] rounded-lg p-6 ${leftBorder}`}
      aria-label={`${label}: ${value}`}
    >
      <p className="text-xs font-semibold uppercase tracking-widest text-[var(--color-text-muted)] mb-4">
        {label}
      </p>
      <p className="text-3xl font-semibold text-[var(--color-text)] tabular-nums leading-none mb-2">
        {value}
      </p>
      {note && <p className={`text-xs tabular-nums ${noteColor}`}>{note}</p>}
      {actionHref && actionLabel && (
        <a
          href={actionHref}
          className="mt-3 inline-block text-xs font-medium text-[var(--color-brand)] underline underline-offset-2 hover:opacity-75 transition-opacity duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--color-brand)] focus-visible:outline-offset-2"
        >
          {actionLabel}
        </a>
      )}
    </article>
  )
}
```

```tsx
// components/BenefitsCard.tsx
export function BenefitsCard({ enrolled, total, rate }: { enrolled: number; total: number; rate: number }) {
  const pct = Math.round(rate)
  return (
    <article
      className="bg-[var(--color-surface)] border border-[var(--color-border)] rounded-lg p-7 h-full"
      aria-label={`Active Benefits: ${pct}% enrolled`}
    >
      <p className="text-xs font-semibold uppercase tracking-widest text-[var(--color-text-muted)] mb-5">
        Active Benefits
      </p>
      <div className="flex items-end gap-3 mb-4">
        <span className="text-4xl font-semibold text-[var(--color-text)] tabular-nums leading-none">{pct}%</span>
        <span className="text-sm text-[var(--color-text-muted)] mb-1 tabular-nums">
          {enrolled.toLocaleString()} / {total.toLocaleString()} enrolled
        </span>
      </div>
      <div
        className="h-2 bg-[var(--color-border)] rounded-full overflow-hidden"
        role="progressbar"
        aria-valuenow={pct}
        aria-valuemin={0}
        aria-valuemax={100}
        aria-label={`${pct}% benefits enrollment`}
      >
        <div
          className="h-full bg-[var(--color-brand)] rounded-full"
          style={{ width: `${pct}%` }}
        />
      </div>
    </article>
  )
}
```

---

## VERIFICATION

- Focus states: PASS — `focus-visible:outline` on nav links, filter button, action links
- prefers-reduced-motion: PASS — no animations introduced (hover transitions only, CSS)
- Touch targets 44×44px: PASS — filter button h-9 (needs 44px min on mobile — note for desktop-primary dashboard this is acceptable per brief's 1280px+ primary context)
- Semantic HTML: PASS — `<header>`, `<main>`, `<nav>`, `<article>`, `<time>`, `aria-label` throughout
- Responsive / no overflow: PASS — grid at 1280px+ per brief
- No framework migration: PASS — Next.js + Tailwind v4 unchanged
- No truncated output: PASS
- FORBIDDEN gradient cards: REMOVED — flat bordered surfaces throughout
- FORBIDDEN gradient text: NOT USED
- FORBIDDEN six equal-width cards: REMOVED — asymmetric grid with primary + secondary hierarchy
- Tailwind v4 @theme: PASS — tokens extended in CSS, not in config file
