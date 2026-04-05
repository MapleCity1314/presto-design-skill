---
name: presto-design
description: Unified frontend design harness — routes create/refine/redesign/motion/fix/overdrive intents to the right cluster, enforces the contract, and applies aesthetic presets. Use this skill whenever the user wants to build UI, improve a design, redesign an existing project, add animation, audit quality, or push an interface to its limits. Triggers on: "build", "create", "make", "design", "improve", "polish", "redesign", "upgrade", "animate", "add motion", "review", "audit", "fix", "overdrive", "go all out", "wow", "make it look better", or any frontend/UI task.
---

# Presto Design Harness

A thin router. Detect intent, load one cluster + one optional preset, apply the contract. Never load more than one cluster at a time.

---

## 1. Context Check (always first)

Before doing any design work, confirm you have:
- **Audience** — who uses this, in what context?
- **Brand personality / tone** — how should it feel?
- **Use cases** — what jobs are they trying to get done?

**Check in order:**
1. Current conversation already contains this context → proceed.
2. `.impeccable.md` exists in project root with a `## Design Context` section → read it and proceed.
3. Neither → load `context/teach-impeccable.md` and run the gathering workflow before anything else.

---

## 2. Design Parameters

These three parameters shape all design decisions. Defaults apply unless the user specifies otherwise. Adjust dynamically based on user signals in the conversation.

| Parameter | Default | Range | What it controls |
|-----------|---------|-------|-----------------|
| `VARIANCE` | **8** | 1–10 | 1 = perfect symmetry, predictable; 10 = asymmetric, artsy chaos |
| `MOTION` | **6** | 1–10 | 1 = static, no animation; 10 = cinematic, spring physics everywhere |
| `DENSITY` | **4** | 1–10 | 1 = art gallery / airy; 10 = cockpit / packed data |

**How to apply parameters:**

- `VARIANCE 1–3`: symmetric layouts, centered content, consistent grid, no surprises
- `VARIANCE 4–7`: offset asymmetry, varied spacing, deliberate breaks from the grid
- `VARIANCE 8–10`: elements bleeding off-edge, overlapping, rotated text, unexpected composition

- `MOTION 1–3`: CSS transitions only, `150ms` max, no entrance animation
- `MOTION 4–7`: entrance animations, stagger, micro-interactions, spring on key elements
- `MOTION 8–10`: scroll-driven, spring physics everywhere, page transitions, GSAP timeline choreography

- `DENSITY 1–3`: very generous whitespace, single-column, max `65ch` text, few elements per screen
- `DENSITY 4–7`: balanced — sections breathe but pages are information-rich
- `DENSITY 8–10`: dense data tables, sidebar navigation, multi-panel layouts

**User override signals:**

| User says | Parameter adjustment |
|-----------|---------------------|
| "more minimal / cleaner / simpler" | VARIANCE → 3–4, DENSITY → 2–3 |
| "more dramatic / bold / impactful" | VARIANCE → 8–9, MOTION → 7–8 |
| "less animation / more subtle" | MOTION → 2–3 |
| "data-heavy / dashboard / dense" | DENSITY → 7–9 |
| "premium / editorial / luxury" | VARIANCE → 7, MOTION → 5, DENSITY → 3 |
| "brutalist / raw / industrial" | VARIANCE → 9, MOTION → 3, DENSITY → 6 |

---

## 3. Intent → Cluster Routing

Load exactly one cluster:

| Signal | Cluster |
|--------|---------|
| Build / create / make / design from scratch | `clusters/create.md` |
| Improve / refine / polish / simplify specific elements | `clusters/refine.md` |
| **Redesign / upgrade / overhaul an existing project** | **`clusters/redesign.md`** |
| Animate / motion / transition / hover / GSAP / scroll effect | `clusters/motion.md` |
| Audit / review / critique / check / fix / debug / a11y / performance | `clusters/fix.md` |
| Overdrive / wow / extreme / go all out / push limits / shader | `clusters/overdrive.md` |

**Disambiguate refine vs redesign**: If the user points at a whole existing project ("redesign my portfolio", "upgrade this app to look premium") → `redesign.md`. If they point at a specific element ("fix the typography", "improve this card") → `refine.md`.

---

## 4. Aesthetic → Preset Routing

After selecting a cluster, check for an aesthetic signal and load a preset if one applies:

| Signal | Preset |
|--------|--------|
| Minimal / clean / simple / quiet | `presets/minimalist.md` |
| Editorial / magazine / high-end / premium / luxury | `presets/editorial.md` |
| Brutalist / raw / industrial / mechanical / terminal | `clusters/overdrive.md` (industrial section) |
| No signal / default | No preset — rely on cluster's defaults and current parameters |

---

## 5. Contract

Every output from every cluster must satisfy `contract.md`. Read it before writing any code.

---

## 6. GSAP Integration

If GSAP skills are available AND the task involves animation, load `gsap-integration.md` alongside the relevant cluster.

Quick signal: `gsap` in `package.json` + task touches motion → load it.

---

## 7. Execution

Follow the loaded cluster's workflow. This file is only the router. Don't improvise routing rules mid-task.
