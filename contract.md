# Output Contract

Every output from every presto-design cluster must satisfy these rules. They are not suggestions - treat violations as bugs.

## Design rationale (mandatory)

Before implementation, the agent must be able to state:

- why this direction fits the audience and use case
- why the chosen typography, color, and composition fit the product
- why the amount of change is appropriate for the current project

If the agent cannot explain the decision, the design is not locked yet.

## Anti-AI-Slop (mandatory)

These are common failure modes, not timeless truths. Treat them as warning signs to interrogate, not a substitute for reasoning.

If a project-specific reason justifies one of these patterns, the reason must be explicit and stronger than "it looks modern."

**Typography**

- Never default to Inter, Roboto, Arial, Open Sans, or system-ui as the primary display font without a project-specific reason.
- Never use monospace as lazy "tech" vibes shorthand.
- Never place large rounded icons above every heading by default.

**Color**

- Never default to `#000` or `#fff` without checking whether tinted neutrals would improve the palette.
- Never default to cyan-on-dark, purple-to-blue gradients, or neon accents on dark backgrounds as a shortcut to visual interest.
- Never default to gradient text on metrics, headings, or hero numbers.
- Never default to dark mode plus glowing accent as the primary design decision.

**Layout**

- Never wrap everything in cards. Not everything needs a container.
- Never nest cards inside cards.
- Never default to the "hero metrics" layout: big number plus small label plus gradient background.
- Never default to three equal-width cards as the entire layout.
- Never center-align all content. Use alignment to create rhythm, not just symmetry.

**Motion**

- Never animate layout properties (`width`, `height`, `top`, `left`, `margin`, `padding`).
- Never exceed `200ms` for interaction feedback.
- Never use bounce or elastic easing as the default interaction language.
- Always prefer `ease-out` variants such as `cubic-bezier(0.25, 1, 0.5, 1)`.
- Always respect `prefers-reduced-motion`.

## Change policy

- Respect the host stack and working architecture.
- Respect an existing design language when it is coherent, branded, and competently implemented.
- Escalate to stronger visual change only when the current design language is generic, inconsistent, low-signal, or harmful to clarity.
- When taste and continuity conflict, prefer continuity unless the user explicitly asks for a stronger reset or the current design is clearly the root problem.

## Production baseline

These are default expectations for "production-minded" work:

- visible focus states and keyboard-reachable interactions
- `prefers-reduced-motion` support when motion is introduced
- touch targets at least `44x44px` on mobile
- semantic HTML where applicable
- responsive behavior without horizontal overflow
- no framework migrations unless explicitly requested
- Tailwind version awareness when Tailwind is present
- metadata hygiene on page-level work when relevant
- motion choices that stay inside reasonable performance bounds

Project-specific requirements can be stricter than this baseline and should take precedence.

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

## Output completeness

- Never truncate code. Output every file, every function, complete.
- No `// ... rest of implementation`, no `// TODO: add styles`, no ellipsis.
- If the output is long, keep going; do not summarize or stop early.
- Produce working, runnable code. Not stubs.
