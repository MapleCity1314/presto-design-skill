---
name: "presto-design"
description: "Unified frontend design harness that routes create, refine, redesign, motion, fix, and overdrive requests to the right cluster, enforces the contract, and applies aesthetic presets. Use this skill whenever the user wants to build UI, improve a design, redesign an existing project, add animation, audit quality, or push an interface further."
---

# Presto Design Harness

A route-driven design workflow. Detect intent, load one cluster and one optional preset, then apply the contract. Never load more than one cluster at a time.

---

## 1. Context Phase (mandatory — run before any design work)

Before routing to a cluster, complete these steps in order. Declare any gap you cannot fill — do not skip silently.

**1a. Identify host stack**
- Grep `package.json` for framework, styling libraries, icon packages, animation libraries
- Check for `tailwind.config.*` or `@theme` in CSS (detect Tailwind version)
- Check for `@font-face` declarations and existing CSS variables / design tokens
- Report what you find as a short factual list

**1b. Sample existing design language**
- List all `font-family` values found in the codebase (exact values, not guesses)
- List color values defined in tokens or CSS variables (count them)
- List spacing scale values if a system exists
- If no codebase is provided: state "no codebase — working from brief only"

**1c. Name reference products**
Name ≥3 products in the target domain. For each, list ≥3 distinguishing characteristics:

```
Reference: [Product name]
- [Observable characteristic 1]
- [Observable characteristic 2]
- [Observable characteristic 3]
```

These characteristics must be specific (e.g., "single accent blue, generous whitespace, monospace for code samples") — not generic ("clean", "minimal").

**1d. Restate the brief**
In your own words (do not copy from the user message):
- Who is the audience and what context do they use this in?
- What is the primary job-to-be-done?
- What tone or register should the interface project?

**1e. Gap declaration**
If any of 1a–1d cannot be completed, state: "GAP: [what is missing] — [what assumption I am making instead]"

---

## 2. Design Parameters

These three parameters shape all design decisions. Defaults apply unless the user specifies otherwise. Adjust them based on user signals in the conversation.

| Parameter | Default | Range | What it controls |
|-----------|---------|-------|------------------|
| `VARIANCE` | **8** | 1-10 | 1 = perfectly symmetric and predictable; 10 = asymmetric and experimental |
| `MOTION` | **6** | 1-10 | 1 = static; 10 = cinematic, spring-heavy motion |
| `DENSITY` | **4** | 1-10 | 1 = airy gallery; 10 = compact cockpit |

Calibration rule:

- If you set a parameter, it must produce visible downstream decisions in layout, typography, spacing, or motion.
- Do not mention a parameter value unless you can point to what it changed.
- When the task is ambiguous, reason in coarse bands (`low`, `medium`, `high`) first, then map to the numeric range.

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

## 2.5 Decision Log Phase (mandatory — emit before writing code)

After the Context phase and parameter calibration, emit a `<design-log>` block. This block is the implementation contract. Every downstream decision traces back to it.

```
<design-log>
DECISION: [type system — font family/families and scale approach]
BECAUSE: [grounded in audience, domain, or Context phase finding]

DECISION: [color system — palette approach, mode, token strategy]
BECAUSE: [grounded in audience, domain, or Context phase finding]

DECISION: [layout primitive policy — grid approach, max-width, column strategy]
BECAUSE: [grounded in audience, domain, or Context phase finding]

DECISION: [motion policy — level, key interactions, library if any]
BECAUSE: [grounded in audience, domain, or Context phase finding]

DECISION: [icon family — which library, why this one]
BECAUSE: [grounded in existing project deps or domain convention]
</design-log>
```

Rules:
- Every BECAUSE must reference a fact from the Context phase, a user-stated requirement, or a named domain convention — never aesthetic preference alone ("it looks good" is not a BECAUSE).
- If a BECAUSE cannot be grounded, state "UNDECIDED: [category] — [what information would resolve it]" and do not proceed to code until resolved.
- Required categories: type system, color system, layout primitive policy, motion policy, icon family.

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

The contract now includes FORBIDDEN UNLESS rules (replacing the old adjective-level anti-slop rules). If a forbidden pattern appears in your output, document which UNLESS condition was satisfied.

After implementation, run the Verification phase from `contract.md` and report every item as PASS or FAIL.

---

## 6. GSAP Integration

If GSAP skills are available and the task involves animation, load `gsap-integration.md` alongside the selected cluster.

Quick signal: `gsap` in `package.json` plus a motion-related task means you should load it.

---

## 7. Tailwind Integration

If the project uses Tailwind CSS, load `tailwind-integration.md` alongside the selected cluster before writing code.

Quick signals:
- `tailwindcss` in `package.json`
- `globals.css` with `@tailwind` or `@import "tailwindcss"`
- `tailwind.config.*` exists
- existing code already uses utility-heavy `className` strings

Treat Tailwind support as version-sensitive:
- **Tailwind v4**: prefer tokens in CSS via `@theme`, keep styling close to the stylesheet, and do not invent a config-first workflow if no config exists.
- **Tailwind v3**: use `tailwind.config.*` theme extension when adding reusable tokens or new scales.

Do not force a CSS-module or styled-components refactor in a Tailwind project unless the user explicitly asks for it.

---

## 8. Execution

Follow the selected cluster's workflow. This file is only the router. Do not improvise routing rules mid-task.

**Deviation rule**: if implementation diverges from any DECISION in the `<design-log>`, emit inline:

```
DEVIATION: [what changed from the logged decision]
BECAUSE: [reason — must reference a discovered project fact or user request, not a new aesthetic preference]
```

Silent drift from a logged decision is a contract violation.

Respect-the-stack rule:

- Always preserve the host stack and working architecture.
- Preserve the existing design language when it is coherent and product-appropriate.
- Escalate to stronger visual change only when the current language is generic, inconsistent, or actively harming clarity or credibility.
