# Cluster: Overdrive

Push interfaces past conventional limits. Synthesizes: `overdrive`, `industrial-brutalist-ui`.

---

```
──────────── ⚡ OVERDRIVE ─────────────
》》》 Entering overdrive mode...
```

---

## MANDATORY: Propose Before Building

This cluster has the highest risk of misfiring. Do NOT jump straight into implementation.

1. **Think through 2–3 directions** — what would each feel like? What's the trade-off?
2. **Present the directions** and ask the user to choose. Include browser support, performance cost, and complexity notes.
3. **Only build what the user confirms**.

Skipping this step risks building something that gets thrown away.

---

## What "Extraordinary" Means by Context

| Surface | What impresses |
|---------|---------------|
| Landing pages / hero sections / portfolios | Sensory: scroll-driven reveals, shader backgrounds, generative art responding to cursor |
| Functional UI (tables, forms, dialogs) | Feel: morphing dialog from its trigger button, 100k-row table at 60fps, streaming form validation |
| Performance-critical UI | Invisible excellence: search through 50k items without flicker, image processing in real-time |
| Data-heavy dashboards | Fluidity: GPU-accelerated canvas charts, animated data state transitions |

**Rule**: something about the implementation exceeds what users expect from a web interface. The technique must serve the experience — not decorate it.

---

## The Toolkit

### Scroll-driven

```css
/* CSS-only scroll progress */
@property --scroll-progress {
  syntax: '<number>';
  initial-value: 0;
  inherits: false;
}

.hero {
  animation: scroll-reveal linear;
  animation-timeline: scroll();
  animation-range: 0% 50%;
}
```

Or GSAP ScrollTrigger for complex sequences (see `clusters/motion.md`).

### Shaders & WebGL

Use Three.js + custom GLSL or React Three Fiber for:
- Animated gradient meshes (no CSS gradient slop)
- Particle systems reacting to interaction
- Post-processing effects (bloom, chromatic aberration — sparingly)
- Procedurally generated backgrounds

```glsl
// Example: noise-based animated gradient
uniform float u_time;
varying vec2 v_uv;

float noise(vec2 st) { /* ... simplex or perlin */ }

void main() {
  float n = noise(v_uv * 3.0 + u_time * 0.2);
  vec3 color = mix(vec3(0.05, 0.05, 0.08), vec3(0.2, 0.15, 0.3), n);
  gl_FragColor = vec4(color, 1.0);
}
```

### Spring Physics

For drag, throw, and natural-feeling interactions:

```js
// Via GSAP + InertiaPlugin
import { InertiaPlugin } from 'gsap/InertiaPlugin';
gsap.registerPlugin(Draggable, InertiaPlugin);

Draggable.create('.card', {
  type: 'x,y',
  inertia: true,
  bounds: '.container',
});
```

Or via React Spring / Framer Motion spring configs:
```js
// Framer Motion spring
animate={{ x: 0 }}
transition={{ type: 'spring', stiffness: 100, damping: 20 }}
```

### View Transitions API

For morphing page transitions:

```js
document.startViewTransition(() => {
  // update DOM here — browser captures before + after and animates
  updateContent();
});
```

```css
/* Give shared elements a matching view-transition-name */
.product-card { view-transition-name: product-detail; }
```

### High-Performance Data

For 100k+ row tables: virtual scrolling (TanStack Virtual).
For real-time charts: Canvas or WebGL (Chart.js canvas renderer, or D3 + canvas).
For heavy computation: offload to Web Workers.

```js
// Web Worker example
const worker = new Worker(new URL('./heavy-compute.worker.js', import.meta.url));
worker.postMessage({ data: largeDataset });
worker.onmessage = ({ data }) => updateUI(data);
```

---

## Industrial Brutalist Mode

Use when the aesthetic direction is raw, mechanical, and unapologetic.

### Palette
- Background: `oklch(8% 0.01 240)` (near-black, cool-tinted)
- Primary text: `oklch(92% 0.005 60)` (off-white, warm)
- Accent: `oklch(72% 0.19 85)` (amber/industrial yellow)
- Secondary accent: `oklch(55% 0.22 30)` (rust/oxide red)
- No gradients. No glassmorphism. No rounded rectangles as decorative elements.

### Typography
- Monospace for data, labels, and UI chrome: `JetBrains Mono`, `Geist Mono`, `IBM Plex Mono`.
- Wide-tracking caps for headings: `letter-spacing: 0.12em; text-transform: uppercase;`
- No serif. Body in a condensed grotesque if available.

### Layout
- Rigid grid. Explicit columns. No auto-fit. Hard borders, not drop shadows.
- Expose the structure: grid lines, dividers, borders as design elements — not decorations to hide.
- No cards with rounded corners as the primary surface. Use sharp edges or ruled lines.
- High information density. Dense, not cramped.

### Motion
- No easing — or very minimal. Mechanical snapping.
- Or: high-spring-stiffness physics that settles sharply (stiffness: 400, damping: 30).
- Cursor effects: position tracking with raw rAF, no spring smoothing.
- Scan lines, noise overlays (very subtle), terminal-cursor blink: all valid.

### Components
```css
/* Industrial button */
.btn-industrial {
  background: transparent;
  border: 1px solid oklch(92% 0.005 60);
  color: oklch(92% 0.005 60);
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 10px 24px;
  cursor: pointer;
  transition: background 80ms, color 80ms;
}

.btn-industrial:hover {
  background: oklch(92% 0.005 60);
  color: oklch(8% 0.01 240);
}
```

---

## Quality Bar for Overdrive

Before declaring done, verify visually (use browser automation / screenshot):

- [ ] Does the effect actually look extraordinary, or just technically complex?
- [ ] Does it feel like it belongs to this product, or was it copy-pasted from a portfolio?
- [ ] Does it work at 60fps? (Check with Chrome DevTools Performance panel)
- [ ] Does it degrade gracefully? (Test with `prefers-reduced-motion: reduce`)
- [ ] Does it break on mobile? (Test at 375px width)
- [ ] Is the fallback for unsupported browsers acceptable?

Technically ambitious effects rarely work on the first try. Expect multiple visual iterations. The gap between "technically works" and "looks extraordinary" is closed through iteration, not code alone.
