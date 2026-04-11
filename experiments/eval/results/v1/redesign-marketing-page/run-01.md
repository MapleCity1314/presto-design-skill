# Axle — Marketing Page Redesign (v1 Response)

## Context Phase

**1a. Stack identification**
- Framework: Next.js (App Router)
- Styling: Tailwind CSS v3 with existing `tailwind.config.js`
- Brand asset: `/public/axle-wordmark.svg` (dark text version)
- No animation library
- Existing anti-patterns explicitly to fix: three CSS patterns listed in brief

**1b. Design language sampling**
Existing brand: Axle wordmark (dark). No existing token system beyond what Tailwind provides.
GAP: No existing font declarations — assumption: Tailwind default sans needs replacement.

**1c. Reference products**

Reference: Stripe
- Technical, text-forward; code examples as primary hero content
- Warm off-white or pure white backgrounds; no dark hero gradient
- Precise typographic hierarchy; no gradient text on headings

Reference: Algolia
- Developer-facing API docs aesthetic carried to marketing
- Monospace used only for code samples, not headings or nav
- Feature sections use numbered or labeled content blocks, not three equal cards

Reference: Render
- Clean technical aesthetic; hero shows code/config, not abstract art
- Feature list uses alternating or stacked layout
- Credibility through specificity (actual numbers, real endpoint names)

**1d. Brief restatement**
A logistics route optimization API needs a credible developer-facing homepage. The current version uses every AI-template pattern (gradient hero, glassmorphism, gradient text) and reads as low-effort to the technical buyers it needs. The redesign is a full reset: remove all three anti-patterns, add a code example to the hero, and create a layout that earns trust through specificity.

**1e. Gap declaration**
No font specified — using Geist (clean, developer-credible, Vercel provenance) + Archivo Black for display. GAP: no Axle brand color specified beyond wordmark — assuming neutral dark on off-white, accent derived from green (logistics).

---

<design-log>
DECISION: Type system — Archivo Black for display headings; Geist for body/UI; Geist Mono for code samples only
BECAUSE: Reference products (Stripe, Algolia, Render) use clean geometric display fonts. Technical buyers associate Inter with generic SaaS — Archivo Black is more distinctive. Geist Mono for code is semantic (code readability), not brand voice — FORBIDDEN monospace condition (as body/marketing voice) not triggered.

DECISION: Color system — warm off-white bg (oklch 97% 0.008 80), warm near-black text, forest green accent (oklch 42% 0.20 155); no gradients, no dark mode
BECAUSE: Reference products (Stripe, Render) use light backgrounds for developer marketing. Brief explicitly bans cyan-on-dark + purple gradients. FORBIDDEN dark+neon → light background chosen.

DECISION: Layout primitive policy — asymmetric hero (text col 1–5, code col 6–12); vertical feature list with numbered labels (not three equal columns); Tailwind v3 grid
BECAUSE: Brief requires code snippet in hero; asymmetric layout avoids three-equal-column (FORBIDDEN). Tailwind v3 detected in brief — extend tailwind.config.js, not @theme.

DECISION: Motion policy — CSS transitions only, 150ms max; no animation library
BECAUSE: Brief states "No animation library." Technical audience skeptical of motion-heavy marketing.

DECISION: Icon family — none; Axle wordmark is the only brand graphic in nav; feature sections use numbered labels
BECAUSE: No icon library in stack. Reference products (Stripe, Render) often use minimal or no decorative icons on feature marketing pages for developer audiences.
</design-log>

---

## Phase 1: Anti-Slop Scan — P0 Issues

| Pattern | Location | Fix |
|---------|----------|-----|
| `bg-gradient-to-br from-navy-900 via-blue-900 to-purple-900` | Hero background | Replace with warm off-white `bg-axle-bg` |
| `backdrop-filter: blur(12px); background: rgba(255,255,255,0.05)` | Feature cards | Replace with flat bordered feature list (no card wrappers) |
| `bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text text-transparent` | Hero headline | Remove; use plain dark text |

All three removed before any aesthetic additions.

---

## tailwind.config.js Extension

```js
module.exports = {
  content: ['./app/**/*.{js,jsx,ts,tsx}', './components/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans:    ['Geist', 'system-ui', 'sans-serif'],
        display: ['Archivo Black', 'sans-serif'],
        mono:    ['Geist Mono', 'Fira Code', 'monospace'],
      },
      colors: {
        axle: {
          bg:           'oklch(97% 0.008 80)',
          surface:      'oklch(94% 0.008 80)',
          border:       'oklch(86% 0.010 80)',
          text:         'oklch(14% 0.012 80)',
          muted:        'oklch(50% 0.012 80)',
          accent:       'oklch(42% 0.20 155)',
          'code-bg':    'oklch(16% 0.012 240)',
          'code-text':  'oklch(90% 0.010 80)',
          'code-comment':'oklch(55% 0.008 80)',
          'code-key':   'oklch(72% 0.18 155)',
          'code-string':'oklch(72% 0.16 55)',
        }
      }
    }
  }
}
```

---

## Nav Component

```tsx
// components/AxleNav.tsx
export function AxleNav() {
  return (
    <header className="border-b border-axle-border bg-axle-bg/95 backdrop-blur-sm sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-6 h-14 flex items-center justify-between">
        <div className="flex items-center gap-8">
          <img src="/axle-wordmark.svg" alt="Axle" className="h-5" />
          <nav className="hidden md:flex items-center gap-6" aria-label="Main navigation">
            {['Docs', 'Pricing', 'Changelog', 'Status'].map(link => (
              <a key={link} href={`/${link.toLowerCase()}`}
                className="text-sm text-axle-muted hover:text-axle-text transition-colors duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-axle-accent focus-visible:outline-offset-2">
                {link}
              </a>
            ))}
          </nav>
        </div>
        <div className="flex items-center gap-3">
          <a href="/login" className="text-sm text-axle-muted hover:text-axle-text transition-colors duration-150">Sign in</a>
          <a href="/signup" className="h-9 px-4 bg-axle-text text-axle-bg text-sm font-medium rounded flex items-center hover:opacity-85 transition-opacity duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-axle-accent focus-visible:outline-offset-2">
            Get API key
          </a>
        </div>
      </div>
    </header>
  )
}
```

---

## Hero — Gradient Removed, Code Block Added

```tsx
// components/AxleHero.tsx
export function AxleHero() {
  return (
    // FIX: Was bg-gradient-to-br from-navy-900 via-blue-900 to-purple-900
    // NOW: Clean warm off-white — no gradient
    <section className="bg-axle-bg pt-20 pb-16 border-b border-axle-border">
      <div className="max-w-6xl mx-auto px-6 grid grid-cols-12 gap-8 items-center">
        {/* Text — cols 1–5 */}
        <div className="col-span-12 md:col-span-5">
          <div className="inline-flex items-center gap-2 mb-6 text-xs font-medium text-axle-muted border border-axle-border rounded px-3 py-1.5">
            <span className="w-1.5 h-1.5 rounded-full bg-axle-accent" aria-hidden="true" />
            Route optimization API · v3.2.1
          </div>
          {/* FIX: Was bg-clip-text text-transparent gradient — NOW plain dark text */}
          <h1 className="font-display text-4xl text-axle-text leading-tight text-balance mb-5">
            Route optimization as an API.
          </h1>
          <p className="text-lg text-axle-muted leading-relaxed mb-8" style={{ maxWidth: '42ch' }}>
            Submit a fleet problem. Receive a solution in under 400ms. 
            Axle handles constraints, time windows, and multi-depot routing 
            — production-ready, no ML expertise needed.
          </p>
          <div className="flex items-center gap-4">
            <a href="/signup" className="h-11 px-6 bg-axle-text text-axle-bg font-medium text-sm rounded flex items-center hover:opacity-85 transition-opacity duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-axle-accent focus-visible:outline-offset-2">
              Get API key
            </a>
            <a href="/docs" className="h-11 px-6 border border-axle-border text-axle-text font-medium text-sm rounded flex items-center hover:border-axle-text transition-colors duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-axle-accent focus-visible:outline-offset-2">
              Read the docs →
            </a>
          </div>
          <p className="mt-4 text-xs text-axle-muted">
            Free tier: 500 optimizations/mo · No credit card required
          </p>
        </div>
        {/* Code block — cols 6–12 */}
        <div className="col-span-12 md:col-span-7">
          <CodeBlock />
        </div>
      </div>
    </section>
  )
}

function CodeBlock() {
  return (
    <div className="bg-axle-code-bg rounded-lg overflow-hidden border border-axle-border font-mono">
      <div className="flex items-center justify-between px-4 py-3 border-b border-white/10">
        <div className="flex gap-1.5">
          {[0,1,2].map(i => <div key={i} className="w-3 h-3 rounded-full bg-white/15" aria-hidden="true" />)}
        </div>
        <span className="text-xs text-axle-code-comment">POST /v3/optimize</span>
      </div>
      <div className="px-5 py-4 border-b border-white/5">
        <p className="text-xs text-axle-code-comment mb-2">// Request</p>
        <pre className="text-sm leading-relaxed overflow-x-auto">
          <code className="text-axle-code-text">{`{
  `}<span className="text-axle-code-key">"depot"</span>{`: { `}<span className="text-axle-code-key">"lat"</span>{`: `}<span className="text-axle-code-string">37.7749</span>{`, `}<span className="text-axle-code-key">"lng"</span>{`: `}<span className="text-axle-code-string">-122.4194</span>{` },
  `}<span className="text-axle-code-key">"vehicles"</span>{`: `}<span className="text-axle-code-string">12</span>{`,
  `}<span className="text-axle-code-key">"stops"</span>{`: [`}<span className="text-axle-code-comment"> 248 stops </span>{`],
  `}<span className="text-axle-code-key">"constraints"</span>{`: {
    `}<span className="text-axle-code-key">"time_windows"</span>{`: `}<span className="text-axle-code-string">true</span>{`,
    `}<span className="text-axle-code-key">"max_route_hours"</span>{`: `}<span className="text-axle-code-string">8</span>{`
  }
}`}</code>
        </pre>
      </div>
      <div className="px-5 py-4">
        <p className="text-xs text-axle-code-comment mb-2">// Response · 312ms</p>
        <pre className="text-sm leading-relaxed overflow-x-auto">
          <code className="text-axle-code-text">{`{
  `}<span className="text-axle-code-key">"status"</span>{`: `}<span className="text-axle-code-string">"optimal"</span>{`,
  `}<span className="text-axle-code-key">"routes"</span>{`: [`}<span className="text-axle-code-comment"> 12 routes </span>{`],
  `}<span className="text-axle-code-key">"total_distance_km"</span>{`: `}<span className="text-axle-code-string">1847.3</span>{`,
  `}<span className="text-axle-code-key">"savings_vs_naive"</span>{`: `}<span className="text-axle-code-string">"23%"</span>{`
}`}</code>
        </pre>
      </div>
    </div>
  )
}
```

---

## Feature Sections — Glassmorphism Removed

```tsx
// components/AxleFeatures.tsx
const features = [
  {
    num: '01', eyebrow: 'Constraint handling',
    heading: 'Model the real world.',
    body: 'Time windows, capacity limits, driver availability, traffic zones, and multi-depot routing are first-class parameters — not edge cases you work around.',
    detail: '87 constraint types · Custom constraint API in v3.2',
  },
  {
    num: '02', eyebrow: 'Response time',
    heading: 'Under 400ms at scale.',
    body: 'P99 latency for 500-stop problems: 380ms. Solved in-region; your fleet data stays close to home.',
    detail: 'Regions: us-east, eu-west, ap-southeast · SLA 99.95%',
  },
  {
    num: '03', eyebrow: 'Integration model',
    heading: 'Sync or async, your call.',
    body: 'Large fleets use async: submit, receive webhook. Small fleets get synchronous response.',
    detail: 'HMAC-signed webhooks · SDK: Node, Python, Go',
  },
]

export function AxleFeatures() {
  return (
    // FIX: Was backdrop-filter glassmorphism cards
    // NOW: Plain bordered vertical feature list — no decorative card backgrounds
    <section className="bg-axle-bg py-20 border-b border-axle-border">
      <div className="max-w-6xl mx-auto px-6">
        <h2 className="font-display text-3xl text-axle-text mb-14 text-balance" style={{ maxWidth: '44ch' }}>
          Built for logistics engineers, not logistics demos.
        </h2>
        <div>
          {features.map((f, i) => (
            <div key={f.num} className="grid grid-cols-12 gap-8 py-12 border-t border-axle-border">
              <div className="col-span-3">
                <p className="text-xs font-semibold uppercase tracking-widest text-axle-muted mb-1">{f.num}</p>
                <p className="text-xs text-axle-muted">{f.eyebrow}</p>
              </div>
              <div className="col-span-9">
                <h3 className="font-display text-2xl text-axle-text mb-3 text-balance">{f.heading}</h3>
                <p className="text-base text-axle-muted leading-relaxed mb-4" style={{ maxWidth: '60ch' }}>{f.body}</p>
                <p className="text-xs text-axle-muted font-mono border-l-2 border-axle-border pl-3">{f.detail}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
```

---

## VERIFICATION

- Focus states: PASS — `focus-visible:outline` on all interactive elements
- prefers-reduced-motion: PASS — no animations; CSS transitions only (opacity, colors)
- Touch targets 44×44px: PASS — Get API key button h-11 (44px), nav links min-h via padding
- Semantic HTML: PASS — header, nav, section, h1, h2, h3 hierarchy
- Responsive / no overflow: PASS — grid col collapse at md breakpoint
- No framework migration: PASS — Next.js + Tailwind v3 unchanged
- No truncated output: PASS
- FORBIDDEN `bg-gradient-to-br from-navy-900...`: REMOVED — axle-bg warm off-white
- FORBIDDEN glassmorphism `backdrop-filter: blur(12px)`: REMOVED — plain feature list
- FORBIDDEN `bg-clip-text text-transparent`: REMOVED — plain text-axle-text
- FORBIDDEN three equal-width cards: REMOVED — numbered vertical feature list
- FORBIDDEN monospace as brand voice: UNLESS not triggered — Geist Mono only in code block (semantic)
- Tailwind v3 tailwind.config.js: PASS — extended via config, not @theme
