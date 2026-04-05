---
name: presto-gsap
description: Best practices for combining GSAP skills (gsap-core, gsap-timeline, gsap-react, gsap-frameworks, gsap-scrolltrigger, gsap-plugins, gsap-utils, gsap-performance) with the presto-design harness. Use this skill when the user has GSAP installed AND is working on design tasks — building a UI with animation, making a landing page that wows, refining motion on an existing interface, or asking which GSAP plugin fits their design intent. Triggers on: any combination of GSAP + design/UI work.
---

# Presto × GSAP Integration

This skill bridges the presto-design harness and the GSAP skill suite. Read it when you're doing design work AND have access to GSAP skills. It tells you which GSAP skill to invoke for which design intent, and how to keep GSAP animations aligned with the presto-design aesthetic system.

---

## Decision: CSS Animation vs GSAP

The presto-design `contract.md` and `motion.md` cover CSS-native animation. Load GSAP when:

| Situation | Use CSS | Use GSAP |
|-----------|---------|----------|
| Simple fade/slide entrance | ✓ | |
| Hover micro-interaction | ✓ | |
| State toggle (on/off) | ✓ | |
| Sequenced multi-step timeline | | ✓ gsap-timeline |
| Scroll-driven reveal with scrub | | ✓ gsap-scrolltrigger |
| Element morphs from one position to another (layout → layout) | | ✓ gsap-plugins (Flip) |
| Text split into characters/words for animation | | ✓ gsap-plugins (SplitText) |
| SVG path morphing | | ✓ gsap-plugins (MorphSVG) |
| Draggable with inertia/throw | | ✓ gsap-plugins (Draggable + Inertia) |
| 60fps mouse-tracking / cursor effect | | ✓ gsap-core (quickTo) |
| React component with complex animation lifecycle | | ✓ gsap-react |
| Vue/Svelte component animation | | ✓ gsap-frameworks |

**Rule of thumb**: if you find yourself writing `setTimeout` chains or fighting CSS `transition` conflicts — switch to GSAP.

---

## Mapping: Presto Cluster → GSAP Skills

### create.md + GSAP

When building from scratch, GSAP adds production-quality entrance choreography:

1. Load `gsap-core` for tween fundamentals.
2. Sequenced entrance → `gsap-timeline` (position parameter controls overlap: `'-=0.2'`).
3. React → `gsap-react` (`useGSAP` with `scope: container`). **Never `useEffect` for GSAP.**
4. `contract.md` still applies: only animate `transform` + `opacity` even in GSAP.

For API details → see `gsap-react` + `gsap-timeline` skills.

### refine.md + GSAP

When adding motion to existing UI:

- Micro-interactions → `gsap-core` `quickTo` for 60fps mouse tracking / value changes.
- Delight moments → `gsap-timeline` for brief celebration sequences (checkmark → message).
- Staggered list entrances → `gsap-core` stagger parameter.

For API details → see `gsap-core` skill.

### overdrive.md + GSAP

For technically ambitious effects — load the relevant plugin skill, not this file:

| Intent | Load |
|--------|------|
| Scroll-pinned sections, scrub, horizontal scroll | `gsap-scrolltrigger` |
| Element morphs between DOM positions (layout transition) | `gsap-plugins` (Flip) |
| Text split into chars/words/lines | `gsap-plugins` (SplitText) |
| SVG path morphing | `gsap-plugins` (MorphSVG) |
| Draggable cards with throw/inertia | `gsap-plugins` (Draggable + Inertia) |

This file only tells you *which* skill to load. The API details live in the GSAP skills themselves.

### fix.md + GSAP

When auditing motion for performance issues:

1. Check `gsap-performance`: verify `will-change` is removed after animation ends, no layout thrashing.
2. For `fixing-motion-performance` findings (animating non-compositor props): replace with GSAP `transform`-only approach.
3. For large scroll-linked animations: check `gsap-scrolltrigger` batch() for performance.

```js
// Fix: was animating height (layout property) — replace with clip-path
// BEFORE (bad):
gsap.to('.drawer', { height: '300px', duration: 0.4 }); // forces layout recalc

// AFTER (good): clip-path runs on compositor
gsap.from('.drawer', {
  clipPath: 'inset(0 0 100% 0)',
  duration: 0.4,
  ease: 'power2.out'
});
```

---

## Aesthetic Alignment: GSAP + Presto Contract

The presto `contract.md` rules apply to ALL animation — CSS and GSAP alike. The most common violations with GSAP:

### Easing alignment

```js
// WRONG: GSAP defaults that conflict with presto aesthetic
gsap.to('.el', { ease: 'bounce.out' });    // banned — reads dated
gsap.to('.el', { ease: 'elastic.out' });   // banned — reads dated

// RIGHT: presto-aligned easing in GSAP terms
gsap.to('.el', { ease: 'power2.out' });    // ≈ ease-out-quart
gsap.to('.el', { ease: 'power3.out' });    // ≈ ease-out-quint
gsap.to('.el', { ease: 'expo.out' });      // ≈ ease-out-expo

// CustomEase for exact presto values
import { CustomEase } from 'gsap/CustomEase';
gsap.registerPlugin(CustomEase);
CustomEase.create('presto-out', 'M0,0 C0.25,1 0.5,1 1,1'); // ease-out-quart
```

### Duration alignment

Map presto timing table to GSAP durations:

| Presto | GSAP `duration` |
|--------|----------------|
| 100–150ms instant feedback | `0.1–0.15` |
| 200–300ms state change | `0.2–0.3` |
| 300–500ms layout change | `0.3–0.5` |
| 500–800ms entrance | `0.5–0.8` |

### `prefers-reduced-motion` in GSAP

```js
// Always check — wrap all non-essential animations
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!prefersReduced) {
  gsap.from('.card', { opacity: 0, y: 20, duration: 0.5, stagger: 0.08 });
} else {
  gsap.set('.card', { opacity: 1 }); // instant, no motion
}

// Or globally set GSAP to minimal motion
if (prefersReduced) {
  gsap.globalTimeline.timeScale(0);  // stop all animations
  gsap.set('*', { clearProps: 'all' });
}
```

---

## GSAP Skill Load Guide

| You need... | Load this GSAP skill |
|-------------|---------------------|
| Basic tweens, easing, stagger | `gsap-core` |
| Multi-step sequences, position parameter | `gsap-timeline` |
| Scroll-driven reveals, pinning, scrub | `gsap-scrolltrigger` |
| Flip, SplitText, MorphSVG, Draggable | `gsap-plugins` |
| React + GSAP (`useGSAP`) | `gsap-react` |
| Vue/Svelte + GSAP lifecycle | `gsap-frameworks` |
| Mouse tracking, will-change, batching | `gsap-performance` |
| `clamp`, `mapRange`, `wrap`, `pipe` | `gsap-utils` |

**Minimum useful set** for a designed UI with quality motion:
`gsap-core` + `gsap-react` (if React) + `gsap-timeline` ≈ ~6,500 tokens.

**Full overdrive set** for landing pages / extraordinary effects:
All 8 GSAP skills ≈ ~22,400 tokens — only load when building something technically ambitious.
