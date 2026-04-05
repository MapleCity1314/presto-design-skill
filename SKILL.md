---
name: "presto-design"
description: "Unified frontend design harness that routes create, refine, redesign, motion, fix, and overdrive requests to the right cluster, enforces the contract, and applies aesthetic presets. Use this skill whenever the user wants to build UI, improve a design, redesign an existing project, add animation, audit quality, or push an interface further."
---

# Presto Design Harness

A thin router. Detect intent, load one cluster and one optional preset, then apply the contract. Never load more than one cluster at a time.

---

## 1. Context Check

Before doing any design work, confirm you have:
- **Audience**: who uses this, and in what context?
- **Brand personality / tone**: how should it feel?
- **Use cases**: what jobs are they trying to get done?

Check in order:
1. Current conversation already contains this context: proceed.
2. `.impeccable.md` exists in project root with a `## Design Context` section: read it and proceed.
3. Neither exists: load `context/teach-impeccable.md` and run that workflow first.

---

## 2. Design Parameters

These three parameters shape all design decisions. Defaults apply unless the user specifies otherwise. Adjust them based on user signals in the conversation.

| Parameter | Default | Range | What it controls |
|-----------|---------|-------|------------------|
| `VARIANCE` | **8** | 1-10 | 1 = perfectly symmetric and predictable; 10 = asymmetric and experimental |
| `MOTION` | **6** | 1-10 | 1 = static; 10 = cinematic, spring-heavy motion |
| `DENSITY` | **4** | 1-10 | 1 = airy gallery; 10 = compact cockpit |

How to apply them:

- `VARIANCE 1-3`: symmetric layouts, centered content, stable grid, no surprises
- `VARIANCE 4-7`: offset asymmetry, varied spacing, deliberate breaks from the grid
- `VARIANCE 8-10`: bleeding edges, overlap, rotated text, unexpected composition

- `MOTION 1-3`: CSS transitions only, `150ms` max, no entrance animation
- `MOTION 4-7`: entrance animations, stagger, micro-interactions, spring on key elements
- `MOTION 8-10`: scroll-driven motion, spring physics, page transitions, GSAP timeline choreography

- `DENSITY 1-3`: generous whitespace, single-column layouts, max `65ch` text, few elements per screen
- `DENSITY 4-7`: balanced information density with breathing room
- `DENSITY 8-10`: dense tables, side navigation, multi-panel dashboards

User override signals:

| User says | Parameter adjustment |
|-----------|----------------------|
| "more minimal", "cleaner", "simpler" | `VARIANCE -> 2-3`, `DENSITY -> 2-3` |
| "more dramatic", "bold", "impactful" | `VARIANCE -> 8-9`, `MOTION -> 7-8` |
| "less animation", "more subtle" | `MOTION -> 2-3` |
| "data-heavy", "dashboard", "dense" | `DENSITY -> 7-8` |
| "premium", "editorial", "luxury" | `VARIANCE -> 7`, `MOTION -> 5`, `DENSITY -> 3` |
| "brutalist", "raw", "industrial" | `VARIANCE -> 9`, `MOTION -> 3`, `DENSITY -> 6` |

---

## 3. Intent To Cluster Routing

Load exactly one cluster:

| Signal | Cluster |
|--------|---------|
| Build, create, make, or design from scratch | `clusters/create.md` |
| Improve, refine, polish, or simplify specific elements | `clusters/refine.md` |
| Redesign, upgrade, or overhaul an existing project | `clusters/redesign.md` |
| Animate, motion, transition, hover, GSAP, or scroll effects | `clusters/motion.md` |
| Audit, review, critique, check, fix, debug, accessibility, or performance | `clusters/fix.md` |
| Overdrive, wow, extreme, go all out, or push limits | `clusters/overdrive.md` |

Disambiguate refine vs redesign:
- If the user points at a whole existing project, use `clusters/redesign.md`.
- If the user points at a specific element, use `clusters/refine.md`.

---

## 4. Aesthetic To Preset Routing

After selecting a cluster, check for an aesthetic signal and load a preset if one applies:

| Signal | Preset |
|--------|--------|
| Minimal, clean, simple, quiet | `presets/minimalist.md` |
| Editorial, magazine, high-end, premium, luxury | `presets/editorial.md` |
| Brutalist, raw, industrial, mechanical, terminal | Use the industrial section in `clusters/overdrive.md` |
| No strong signal | No preset; rely on the cluster defaults and current parameters |

---

## 5. Contract

Every output from every cluster must satisfy `contract.md`. Read it before writing code.

---

## 6. GSAP Integration

If GSAP skills are available and the task involves animation, load `gsap-integration.md` alongside the selected cluster.

Quick signal: `gsap` in `package.json` plus a motion-related task means you should load it.

---

## 7. Execution

Follow the selected cluster's workflow. This file is only the router. Do not improvise routing rules mid-task.
