# Cluster: Motion

Add purposeful animation and motion. Synthesizes: `animate`, `delight` (motion aspects), `gsap-core`, `gsap-timeline`, `gsap-react`, `gsap-frameworks`, `gsap-scrolltrigger`, `gsap-plugins`, `gsap-utils`, `gsap-performance`, `fixing-motion-performance`.

## Strategy First

Before writing any animation code, answer these questions:

1. **What information does this motion communicate?** Entrance = "this arrived". Exit = "this left". State change = "this is different now". Delight = "this is alive". If the answer is "nothing, it just looks cool" — reconsider.
2. **Does the motion direct attention or provide feedback?** If neither, it's decoration. Decoration has a low threshold for removal.
3. **What's the performance cost?** Any non-compositor property (width, height, top, left, background, margin) forces layout recalculation. Refuse to animate them.

---

## Timing Reference

| Context | Duration | Notes |
|---------|----------|-------|
| Instant feedback (button press) | 100–150ms | `scale(0.95)` on press |
| Hover / focus state | 150–200ms | `scale(1.02–1.05)`, color change |
| State change (toggle, tab) | 200–300ms | Opacity + small translate |
| Layout change (accordion, modal) | 300–500ms | Height change via clip-path, not `height` |
| Entrance animation | 300–600ms | Stagger if multiple items |
| Page transition | 400–700ms | Should feel cinematic, not slow |

Exit animations: use ~75% of the entrance duration.

## Easing Reference

```css
--ease-out-quart:  cubic-bezier(0.25, 1, 0.5, 1);   /* general purpose */
--ease-out-quint:  cubic-bezier(0.22, 1, 0.36, 1);   /* slightly more aggressive */
--ease-out-expo:   cubic-bezier(0.16, 1, 0.3, 1);    /* fast start, gentle end */
--ease-in-out:     cubic-bezier(0.45, 0, 0.55, 1);   /* for loops/pendulums */
```

**Never use**: `bounce: cubic-bezier(0.34, 1.56, 0.64, 1)` or `elastic: cubic-bezier(0.68, -0.6, 0.32, 1.6)`. They read as dated.

## Performance Rules

`contract.md` covers the compositor-only rule and `prefers-reduced-motion`. Two additional rules specific to motion work:

- `will-change: transform` only while an animation is active — set it just before the animation starts, remove it in the `onComplete` callback. Leaving it on permanently forces the element onto its own layer permanently, wasting GPU memory.
- Never animate `blur()` > 4px on a surface larger than ~200px — each frame requires a full repaint of the blurred area.

```css
/* prefers-reduced-motion — remove motion, preserve meaning */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

---

## CSS Animation (no library needed)

Use for simple entrance, hover, and state changes:

```css
/* Entrance: fade + rise */
@keyframes fade-up {
  from { opacity: 0; translate: 0 12px; }
  to   { opacity: 1; translate: 0 0; }
}

.card { animation: fade-up 400ms var(--ease-out-quart) both; }

/* Stagger via custom property */
.card:nth-child(2) { animation-delay: 80ms; }
.card:nth-child(3) { animation-delay: 160ms; }

/* Hover micro-interaction */
.button {
  transition: transform 150ms var(--ease-out-quart);
}
.button:hover  { transform: scale(1.03); }
.button:active { transform: scale(0.96); }

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## GSAP (when needed)

Use GSAP for: complex sequences, scroll-driven animation, morphing, split-text, draggable, or any animation that CSS can't express cleanly.

### Setup

```js
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);
```

### Core API

```js
// to() — animate FROM current values TO target
gsap.to('.card', { opacity: 1, y: 0, duration: 0.4, ease: 'power2.out' });

// from() — animate FROM target TO current values (good for entrances)
gsap.from('.card', { opacity: 0, y: 16, duration: 0.4, ease: 'power2.out' });

// fromTo() — explicit start and end
gsap.fromTo('.card', { opacity: 0 }, { opacity: 1, duration: 0.4 });

// stagger
gsap.from('.card', { opacity: 0, y: 16, stagger: 0.08, ease: 'power2.out' });
```

**Easing**: prefer `power2.out` / `power3.out` / `expo.out`. Avoid `bounce` and `elastic`.

### Timelines

For sequencing multiple animations:

```js
const tl = gsap.timeline({ defaults: { ease: 'power2.out', duration: 0.4 } });

tl.from('.hero-title', { opacity: 0, y: 20 })
  .from('.hero-subtitle', { opacity: 0, y: 12 }, '-=0.2')  // 0.2s overlap
  .from('.hero-cta', { opacity: 0, scale: 0.9 }, '-=0.15');
```

Position parameter:
- `'+=0.2'` — 0.2s after previous ends
- `'-=0.2'` — 0.2s before previous ends (overlap)
- `'<'` — same start time as previous
- `'<0.1'` — 0.1s after previous starts

### React integration

```jsx
import { useRef } from 'react';
import { useGSAP } from '@gsap/react';
import gsap from 'gsap';

gsap.registerPlugin(useGSAP);

function HeroSection() {
  const container = useRef(null);

  useGSAP(() => {
    // selectors scoped to container automatically
    gsap.from('.hero-title', { opacity: 0, y: 20, duration: 0.5, ease: 'power2.out' });
  }, { scope: container });  // cleanup is automatic

  return <div ref={container}><h1 className="hero-title">Hello</h1></div>;
}
```

Never use `useEffect` for GSAP. `useGSAP` handles registration and cleanup automatically.

### ScrollTrigger

```js
gsap.from('.section', {
  opacity: 0,
  y: 40,
  duration: 0.6,
  ease: 'power2.out',
  scrollTrigger: {
    trigger: '.section',
    start: 'top 80%',    // when top of element hits 80% viewport height
    end: 'top 30%',
    toggleActions: 'play none none reverse',
    // scrub: true,      // tie animation progress to scroll position
    // pin: true,        // pin element during scroll
  }
});
```

Cleanup in React: `useGSAP` handles it. In Vue: kill in `onUnmounted`. In vanilla: store the trigger instance and call `.kill()`.

### Useful GSAP Utils

```js
gsap.utils.clamp(0, 100, value)         // clamp to range
gsap.utils.mapRange(0, 1, 0, 100, t)    // map t from [0,1] to [0,100]
gsap.utils.interpolate(0, 500, 0.5)     // linear interpolation
gsap.utils.wrap(0, colors.length, i)    // wrap index
```

### Performance (GSAP-specific)

- Use `quickTo` for frequently updated values (mouse tracking, scroll position):
  ```js
  const xSetter = gsap.quickTo('.cursor', 'x', { duration: 0.3, ease: 'power3' });
  window.addEventListener('mousemove', e => xSetter(e.clientX));
  ```
- Batch DOM reads then writes: `gsap.ticker.add()` for rAF-synced work.
- `force3D: true` on elements that need hardware acceleration.
- Avoid animating too many elements simultaneously — virtualize if needed.

---

## Six Motion Categories

When animating a feature, consider which categories apply:

1. **Entrance**: how content appears (fade+rise, slide, scale).
2. **Micro-interactions**: button press, hover, toggle — immediate feedback.
3. **State transitions**: tab change, filter apply, mode switch.
4. **Navigation flow**: page transitions, step progression, drawer open/close.
5. **Feedback and guidance**: form validation, loading, success/error.
6. **Delight moments**: confetti, celebration, easter eggs — use sparingly (< 1s, skippable).
