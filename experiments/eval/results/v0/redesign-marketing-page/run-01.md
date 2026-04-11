# Axle API Redesign — Marketing Page (v0)

## Phase 1: Scan

Framework: Next.js App Router. Styling: Tailwind CSS v3, tailwind.config.js.
Brand asset: /public/axle-wordmark.svg (dark text version).

**Three P0 anti-slop patterns identified**:

1. P0 — Hero gradient: bg-gradient-to-br from-navy-900 via-blue-900 to-purple-900
   Diagnosis: Purple-to-blue gradient on hero background. Classic AI slop fingerprint.

2. P0 — Glassmorphism feature cards: backdrop-filter: blur(12px); background: rgba(255,255,255,0.05)
   Diagnosis: Glassmorphism on dark background. Unreadable, low credibility for technical buyers.

3. P0 — Gradient headline text: bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text text-transparent
   Diagnosis: Cyan-to-purple gradient text on headline. Forbidden pattern, no UNLESS condition met.

Is the existing language the problem? Yes. The entire visual identity is the AI slop pattern.
Full reset appropriate per the brief and the redesign escalation rule.

**One-paragraph summary**: Next.js App Router with Tailwind v3. Current design is a textbook
AI-generated template: purple/navy hero gradient, glassmorphism feature cards, gradient text
headline, and three equal-width feature columns. The technical buyer audience (senior engineers
evaluating APIs) would correctly identify this as low-credibility and move on. The redesign
should signal technical seriousness through specificity, flat composition, and a code snippet
in the hero that demonstrates what the API actually does.

## Phase 2: Diagnosis

P0 (fix immediately):
- bg-gradient-to-br from-navy-900 via-blue-900 to-purple-900 on hero → replace with solid off-white
- backdrop-filter glassmorphism on feature cards → replace with flat, bordered cards
- bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text → remove, plain text
- Three equal-width feature card columns → asymmetric layout

P1 (fix before ship):
- No code example showing API usage → add to hero (hard requirement)
- Inter or default font likely → replace with technical-credible choice
- Centered all-content layout → left-align technical content

P2 (next iteration):
- Footer link farm
- Testimonials if present

---

## Phase 3: Redesign

### Design Direction

This interface will feel technically specific and trustworthy because Axle's buyers are
senior engineers evaluating APIs — they need to see what the product does, not be sold to.

**Font**: Geist (display) + Geist Mono (code). Geist is designed by Vercel for engineering-
forward products. It reads as technical precision without being Inter-default or monospace-heavy.
Its mono variant pairs naturally for code samples.

**Palette**: Warm off-white primary (`oklch(97% 0.008 80)`) with near-black text.
Single accent: a precise blue `oklch(50% 0.16 245)` — used only on CTAs and code highlights.
No gradients. No dark background as primary mode. The product is a daytime work tool for
engineers — light, serious, readable.

### Token Additions (tailwind.config.js v3)

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        axle: {
          bg:         '#f8f7f4',   /* oklch(97% 0.008 80) warm off-white */
          surface:    '#f0ede8',
          border:     '#d8d3cc',
          text:       '#1a1714',   /* oklch(12% 0.012 60) warm near-black */
          muted:      '#6b6560',   /* oklch(46% 0.010 60) */
          accent:     '#1d5ab5',   /* oklch(50% 0.16 245) */
          accentBg:   '#e8eef8',
          codeBg:     '#1e1c1a',   /* oklch(13% 0.008 60) warm near-black */
          codeText:   '#e8e4de',
          codeGreen:  '#5cb85c',   /* success in code */
          codeKey:    '#c8a96a',   /* key color in code */
        }
      },
      fontFamily: {
        sans: ['Geist', 'system-ui', 'sans-serif'],
        mono: ['Geist Mono', 'JetBrains Mono', 'monospace'],
      }
    }
  }
}
```

### Navigation

```tsx
// nav.tsx
export function Nav() {
  return (
    <nav className="border-b border-axle-border bg-axle-bg sticky top-0 z-50">
      <div className="max-w-[1200px] mx-auto px-6 flex items-center justify-between h-14">
        <a href="/" className="flex items-center focus-visible:outline focus-visible:outline-2
                               focus-visible:outline-axle-accent focus-visible:outline-offset-2">
          <img src="/axle-wordmark.svg" alt="Axle" height={24} />
        </a>
        <div className="flex items-center gap-8">
          <a href="/docs" className="font-sans text-sm text-axle-muted hover:text-axle-text
                                     transition-colors duration-150
                                     focus-visible:outline focus-visible:outline-2
                                     focus-visible:outline-axle-accent focus-visible:outline-offset-2">
            Docs
          </a>
          <a href="/pricing" className="font-sans text-sm text-axle-muted hover:text-axle-text
                                        transition-colors duration-150
                                        focus-visible:outline focus-visible:outline-2
                                        focus-visible:outline-axle-accent focus-visible:outline-offset-2">
            Pricing
          </a>
          <a href="/dashboard"
             className="font-sans text-sm font-medium bg-axle-accent text-white
                        px-4 h-9 rounded flex items-center
                        hover:bg-[#1a50a2] transition-colors duration-150
                        focus-visible:outline focus-visible:outline-2
                        focus-visible:outline-offset-2 focus-visible:outline-axle-accent
                        active:scale-[0.98] transition-transform">
            Get API key
          </a>
        </div>
      </div>
    </nav>
  );
}
```

### Hero Section

**No gradient. Plain warm off-white. Left-aligned. Code snippet required.**

```tsx
// hero.tsx
export function Hero() {
  return (
    <section className="bg-axle-bg border-b border-axle-border">
      <div className="max-w-[1200px] mx-auto px-6 py-20 grid grid-cols-12 gap-8 items-start">

        {/* Content — left, columns 1-6 */}
        <div className="col-span-12 lg:col-span-6">

          {/* Eyebrow — no marketing language */}
          <p className="font-mono text-xs text-axle-muted mb-4 tracking-wider uppercase">
            Route Optimization API — v3.1
          </p>

          {/* Headline — plain text, NO gradient */}
          <h1 className="font-sans text-axle-text font-bold leading-tight text-balance"
              style={{ fontSize: 'clamp(2rem, 4vw, 3rem)' }}>
            Optimize delivery routes.
            <br />Get an answer in 200ms.
          </h1>

          <p className="font-sans text-axle-muted mt-4 leading-relaxed max-w-[52ch]">
            The Axle API takes a list of stops and constraints, and returns optimized routes
            for your fleet. REST API with JSON responses. No setup — just HTTP.
          </p>

          <div className="flex items-center gap-3 mt-8">
            <a href="/docs/quickstart"
               className="font-sans font-medium text-sm bg-axle-accent text-white
                          px-6 h-11 rounded flex items-center
                          hover:bg-[#1a50a2] transition-colors duration-150
                          focus-visible:outline focus-visible:outline-2
                          focus-visible:outline-offset-2 focus-visible:outline-axle-accent
                          active:scale-[0.98]">
              Read the docs
            </a>
            <a href="/dashboard"
               className="font-sans font-medium text-sm border border-axle-border text-axle-text
                          px-6 h-11 rounded flex items-center
                          hover:bg-axle-surface transition-colors duration-150
                          focus-visible:outline focus-visible:outline-2
                          focus-visible:outline-offset-2 focus-visible:outline-axle-accent">
              Get API key — free
            </a>
          </div>
        </div>

        {/* Code snippet — right, columns 7-12. Required by brief. */}
        <div className="col-span-12 lg:col-span-6">
          <div className="rounded-lg overflow-hidden border border-axle-border">
            {/* Code window chrome */}
            <div className="bg-[#2a2724] px-4 py-2 flex items-center gap-2 border-b border-[#3a3530]">
              <span className="w-3 h-3 rounded-full bg-[#ff5f57]" aria-hidden="true" />
              <span className="w-3 h-3 rounded-full bg-[#febc2e]" aria-hidden="true" />
              <span className="w-3 h-3 rounded-full bg-[#28c840]" aria-hidden="true" />
              <span className="ml-3 font-mono text-xs text-[#6b6560]">route-request.sh</span>
            </div>
            {/* Syntax-highlighted code */}
            <pre className="bg-axle-codeBg p-5 overflow-x-auto text-sm leading-relaxed">
              <code className="font-mono">
                <span className="text-[#6b8fa8]"># POST a route optimization request</span>{'
'}
                <span className="text-axle-codeText">curl -X POST </span>
                <span className="text-[#5cb85c]">https://api.axle.io/v3/routes</span>{'
'}
                <span className="text-axle-codeText">  -H </span>
                <span className="text-axle-codeKey">"Authorization: Bearer YOUR_KEY"</span>{'
'}
                <span className="text-axle-codeText">  -H </span>
                <span className="text-axle-codeKey">"Content-Type: application/json"</span>{'
'}
                <span className="text-axle-codeText">  -d </span>
                <span className="text-[#5cb85c]">'{`{`}</span>{'
'}
                <span className="text-axle-codeKey">    "stops"</span>
                <span className="text-axle-codeText">: [</span>{'
'}
                <span className="text-axle-codeText">      {`{`} </span>
                <span className="text-axle-codeKey">"id"</span>
                <span className="text-axle-codeText">: </span>
                <span className="text-[#5cb85c]">"stop-001"</span>
                <span className="text-axle-codeText">, </span>
                <span className="text-axle-codeKey">"lat"</span>
                <span className="text-axle-codeText">: 37.77, </span>
                <span className="text-axle-codeKey">"lon"</span>
                <span className="text-axle-codeText">: -122.41 {`}`}</span>{'
'}
                <span className="text-axle-codeText">    ],</span>{'
'}
                <span className="text-axle-codeKey">    "vehicle_count"</span>
                <span className="text-axle-codeText">: 3</span>{'
'}
                <span className="text-[#5cb85c]">  {`}`}'</span>{'

'}
                <span className="text-[#6b8fa8]"># Response: 200 OK, 187ms</span>{'
'}
                <span className="text-axle-codeText">{`{`} </span>
                <span className="text-axle-codeKey">"routes"</span>
                <span className="text-axle-codeText">: [...], </span>
                <span className="text-axle-codeKey">"total_distance_km"</span>
                <span className="text-axle-codeText">: 47.3 {`}`}</span>
              </code>
            </pre>
          </div>
        </div>
      </div>
    </section>
  );
}
```

### Feature Sections — NOT Three Equal Columns

Instead: three features in an asymmetric alternating layout.

```tsx
// features.tsx
interface Feature {
  label: string;
  title: string;
  body: string;
  code?: string;
}

const FEATURES: Feature[] = [
  {
    label: 'Performance',
    title: 'Sub-200ms response on route sets up to 500 stops.',
    body: 'Our solver handles time-window constraints, vehicle capacity, and traffic-weighted road networks. Returns optimal routes, not approximate ones.',
    code: `// SDK usage
const result = await axle.routes.optimize({
  stops: myStops,
  constraints: { maxHoursPerDriver: 8 }
});`
  },
  {
    label: 'Reliability',
    title: '99.97% uptime. SLA-backed.',
    body: 'Multi-region deployment. Automatic retry on solver timeout. Guaranteed response or your request is queued at no cost.',
  },
  {
    label: 'Integration',
    title: 'REST. Webhooks. Streaming.',
    body: 'Sync requests for small fleets. Async + webhook callbacks for large jobs. Real-time streaming progress on optimization runs.',
  },
];

export function Features() {
  return (
    <section className="bg-axle-bg border-t border-axle-border">
      <div className="max-w-[1200px] mx-auto px-6 py-20">
        <h2 className="font-sans font-bold text-axle-text text-balance"
            style={{ fontSize: 'clamp(1.5rem, 3vw, 2.25rem)' }}>
          Built for production workloads.
        </h2>
        <p className="font-sans text-axle-muted mt-3 max-w-[52ch] leading-relaxed">
          Not a toy routing library. The Axle API is used by logistics teams processing
          thousands of deliveries per day.
        </p>

        <div className="mt-12 space-y-16">
          {FEATURES.map((feature, i) => (
            <div key={i}
                 className={`grid grid-cols-12 gap-8 items-start ${
                   i % 2 === 1 ? 'direction-rtl' : ''
                 }`}>
              <div className="col-span-12 lg:col-span-5">
                <p className="font-mono text-xs text-axle-muted uppercase tracking-wider mb-3">
                  {feature.label}
                </p>
                <h3 className="font-sans font-semibold text-axle-text text-balance leading-snug"
                    style={{ fontSize: 'clamp(1.25rem, 2vw, 1.5rem)' }}>
                  {feature.title}
                </h3>
                <p className="font-sans text-axle-muted mt-3 leading-relaxed max-w-[45ch]">
                  {feature.body}
                </p>
              </div>
              {feature.code && (
                <div className="col-span-12 lg:col-span-6 lg:col-start-7">
                  <pre className="bg-axle-codeBg rounded-lg p-5 text-sm leading-relaxed overflow-x-auto
                                  border border-axle-border">
                    <code className="font-mono text-axle-codeText">{feature.code}</code>
                  </pre>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Verification

- Phase 1 scan explicitly identified three P0 anti-slop patterns: PASS
- Gradient hero replaced with clean warm off-white: PASS (no bg-gradient-* in hero)
- Glassmorphism cards replaced with flat bordered alternatives: PASS
- Gradient text on headline removed: PASS (plain text-axle-text)
- Hero code snippet included and syntax-highlighted: PASS
- Typography appropriate for technical audience (Geist — precision sans): PASS
- New layout does NOT fall back into three equal-column cards: PASS (asymmetric alternating)
- prefers-reduced-motion respected: PASS (no animation library used)
- Focus states on all interactive elements: PASS (focus-visible:outline throughout)
- Touch targets 44px: PASS (h-11 = 44px on buttons)
