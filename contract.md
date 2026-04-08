# Output Contract

Every output from every presto-design cluster must satisfy these rules. They are not suggestions — treat violations as bugs.

---

## Design rationale (mandatory)

Before implementation, the agent must emit a `<design-log>` block (see SKILL.md §2.5). The log must contain grounded decisions for: type system, color system, layout primitive policy, motion policy, and icon family.

Each BECAUSE must reference one of:
- A fact extracted during the Context phase (stack, existing tokens, brand assets)
- A user-stated requirement from the current conversation
- A named domain convention with ≥1 observable characteristic

If a BECAUSE cannot be grounded in one of these, the decision is not locked. Do not proceed to code.

---

## Anti-AI-Slop (mandatory)

These are common failure modes, not timeless truths. Each rule below uses the form `FORBIDDEN … UNLESS`. If a forbidden pattern appears in your output, a UNLESS condition must be satisfied and documented. Write which condition was met.

If no UNLESS condition is satisfied, the pattern is a contract violation.

### Typography

**FORBIDDEN**: Inter, Roboto, Arial, Open Sans, or system-ui as the primary display font.
**UNLESS**:
- Existing codebase uses this font as stated brand identity (evidenced by `@font-face` declarations, explicit brand docs, or existing components that make it load-bearing), OR
- User has stated this font requirement in the current conversation, OR
- DECISION log contains: `DECISION: use [font] BECAUSE: [audience or domain reason]`

**FORBIDDEN**: Monospace as the primary voice for body text, marketing headings, or navigation labels.
**UNLESS**:
- Domain is terminal emulator, code editor, data terminal, finance terminal, or developer tool where monospace is the correct aesthetic convention for that domain, OR
- DECISION log contains: `DECISION: use monospace BECAUSE: [named domain reason]`

**FORBIDDEN**: Large rounded icons placed above every heading as a default layout pattern.
*(No UNLESS — this is always a structural laziness, not a domain choice.)*

---

### Color

**FORBIDDEN**: Pure `#000000` as background or body text color without checking tinted alternatives.
**UNLESS**:
- Domain is finance terminal, print replica, or high-contrast accessibility mode where pure black is the correct convention, OR
- Existing brand guidelines explicitly specify pure black, OR
- DECISION log contains: `DECISION: use pure black BECAUSE: [domain/brand reason]`

**FORBIDDEN**: Pure `#ffffff` as the page background without checking tinted alternatives.
**UNLESS**: Same conditions as pure black above.

**FORBIDDEN**: Cyan-on-dark, purple-to-blue gradients, or neon accents on dark backgrounds.
**UNLESS**:
- Target domain is gaming, entertainment, nightlife, or creative-dark where this color convention is established and expected, OR
- User has explicitly requested this aesthetic, OR
- DECISION log contains: `DECISION: use [color convention] BECAUSE: [domain reason]`

**FORBIDDEN**: Gradient text on metrics, headings, or hero numbers.
**UNLESS**:
- User has explicitly requested gradient text in the current conversation, OR
- DECISION log contains an explicit entry with domain justification.
*(Note: there is no domain where gradient text on data is the correct default. This UNLESS is narrow.)*

**FORBIDDEN**: Dark mode + glowing neon accent as the primary visual identity.
**UNLESS**:
- Target domain is gaming, entertainment, nightlife, or creative-dark where this is the established convention, OR
- User has explicitly requested it, OR
- DECISION log contains: `DECISION: dark + neon BECAUSE: [domain reason]`

---

### Layout

**FORBIDDEN**: Three equal-width columns as the entire page layout.
**UNLESS**:
- Content is genuinely three parallel items of equal weight with no hierarchy between them, AND
- DECISION log contains: `DECISION: three-column equal layout BECAUSE: [content reason]`

**FORBIDDEN**: Nested cards (a card containing another card as its primary content surface).
*(No UNLESS — nested containment always signals a structural problem, not a design choice.)*

**FORBIDDEN**: Hero metrics layout (large number + small label + gradient background card) as the primary page composition.
**UNLESS**:
- Domain is a live operations dashboard where glanceable metrics are the primary job-to-be-done, AND
- DECISION log contains: `DECISION: hero metrics BECAUSE: [specific operational use case]`

**FORBIDDEN**: Center-aligning more than 60% of content blocks on a single page.
**UNLESS**:
- Layout is a single-column centered editorial, a landing page with a known centered-hero convention, or a narrow prose document, OR
- DECISION log contains: `DECISION: centered layout BECAUSE: [reason grounded in content structure]`

---

### Motion

**FORBIDDEN**: Animating layout properties — `width`, `height`, `top`, `left`, `margin`, `padding`.
*(No UNLESS — these always cause layout recalculation. Use `transform` + `clip-path` instead.)*

**FORBIDDEN**: Interaction feedback duration exceeding `200ms`.
*(No UNLESS — human perception makes this a hard cap for responsiveness.)*

**FORBIDDEN**: Bounce (`cubic-bezier(0.34, 1.56, 0.64, 1)`) or elastic easing as the default interaction language.
**UNLESS**:
- Domain is a playful consumer app, toy-like interface, or children's product where spring-heavy motion is part of the brand personality, AND
- DECISION log contains: `DECISION: bounce/elastic easing BECAUSE: [brand/audience reason]`

**REQUIRED**: `ease-out` variants such as `cubic-bezier(0.25, 1, 0.5, 1)` as the default.

**REQUIRED**: `prefers-reduced-motion` support whenever motion is introduced.

---

## Change policy

- Respect the host stack and working architecture.
- Respect an existing design language when it is coherent, branded, and competently implemented.
- Escalate to stronger visual change only when the current design language is generic, inconsistent, low-signal, or harmful to clarity.
- When taste and continuity conflict, prefer continuity unless the user explicitly asks for a stronger reset or the current design is clearly the root problem.

---

## Production baseline

These are default expectations for production-minded work. Each is a pass/fail item — report them as such in the Verification phase.

- [ ] Visible focus states and keyboard-reachable interactions
- [ ] `prefers-reduced-motion` support when motion is introduced
- [ ] Touch targets at least `44×44px` on mobile
- [ ] Semantic HTML where applicable
- [ ] Responsive behavior without horizontal overflow
- [ ] No framework migrations unless explicitly requested
- [ ] Tailwind version awareness when Tailwind is present
- [ ] Metadata hygiene on page-level work when relevant
- [ ] Motion choices that stay inside reasonable performance bounds
- [ ] No truncated code output (no `// ... rest of implementation`, no stubs)

Project-specific requirements can be stricter than this baseline and should take precedence.

---

## Technical baseline (Tailwind projects)

- Detect Tailwind version before editing config or tokens (`v3` vs `v4`).
- Tailwind v4: prefer semantic tokens in CSS via `@theme`.
- Tailwind v3: extend `tailwind.config.*` only for reusable theme values.
- Prefer scale tokens over arbitrary values; use arbitrary values only for true one-offs or optical corrections.
- If utility strings become unreadable, extract composition with `cn(...)` or the project's existing variant pattern.
- Use `motion/react` for JS animation when JS motion is needed.
- Use `cn` (`clsx` + `tailwind-merge`) for conditional classes.
- Use accessible primitives (Base UI, Radix, React Aria) for keyboard and focus behavior where appropriate.
- Never use `h-screen`; use `h-dvh`.
- Use `text-balance` on headings and `text-pretty` on body.
- Use `tabular-nums` for numeric data.
- Animate only compositor properties: `transform`, `opacity`.
- Pause looping animations when off-screen.

---

## Verification phase (mandatory)

After implementation, self-check every Production baseline item. Report as:

```
VERIFICATION:
- Focus states: PASS / FAIL
- prefers-reduced-motion: PASS / FAIL
- Touch targets 44×44px: PASS / FAIL
- Semantic HTML: PASS / FAIL
- Responsive / no overflow: PASS / FAIL
- No framework migration: PASS / FAIL
- No truncated output: PASS / FAIL
- [Any FORBIDDEN pattern used]: UNLESS condition met — [which condition]
```

FAIL items must be fixed before the output is complete. A FAIL is not a note for later.

---

## Deviation rule

If implementation diverges from a DECISION logged in `<design-log>`, emit inline:

```
DEVIATION: [what changed from the logged decision]
BECAUSE: [reason — must reference a discovered project fact or user request, not a new aesthetic preference]
```

Silent drift from a logged decision is a contract violation.

---

## Output completeness

- Never truncate code. Output every file, every function, complete.
- No `// ... rest of implementation`, no `// TODO: add styles`, no ellipsis.
- If the output is long, keep going; do not summarize or stop early.
- Produce working, runnable code. Not stubs.
