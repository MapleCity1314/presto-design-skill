# Output Contract

Every output from every presto-design cluster must satisfy these rules. They are not suggestions — treat violations as bugs.

## Anti-AI-Slop (mandatory)

These patterns mark output as AI-generated garbage. Never produce them:

**Typography**
- Never use Inter, Roboto, Arial, Open Sans, or system-ui as the primary display font.
- Never use monospace as lazy "tech" vibes shorthand.
- Never place large rounded icons above every heading.

**Color**
- Never use `#000` or `#fff` — always tint neutrals.
- Never use: cyan-on-dark, purple-to-blue gradients, neon accents on dark backgrounds.
- Never use gradient text on metrics, headings, or hero numbers.
- Never default to dark mode + glowing accent as the primary design decision.

**Layout**
- Never wrap everything in cards. Not everything needs a container.
- Never nest cards inside cards.
- Never use the "hero metrics" layout: big number + small label + gradient background.
- Never use three equal-width cards as the entire layout.
- Never center-align all content — use alignment to create rhythm, not just symmetry.

**Motion**
- Never animate layout properties (width, height, top, left, margin, padding).
- Never exceed 200ms for interaction feedback.
- Never use bounce or elastic easing — they read as dated.
- Always use `ease-out` variants: `cubic-bezier(0.25, 1, 0.5, 1)` or similar.
- Always respect `prefers-reduced-motion`.

## Technical Baseline (Tailwind projects)

- Use `motion/react` (formerly framer-motion) for JS animation.
- Use `cn` (clsx + tailwind-merge) for conditional classes.
- Use accessible primitives (Base UI / Radix / React Aria) for keyboard/focus behavior.
- Never use `h-screen` — use `h-dvh`.
- Use `text-balance` on headings, `text-pretty` on body.
- Use `tabular-nums` for numeric data.
- Animate only compositor properties: `transform`, `opacity`.
- Pause looping animations when off-screen.

## Output Completeness

- Never truncate code. Output every file, every function, complete.
- No `// ... rest of implementation`, no `// TODO: add styles`, no ellipsis.
- If the output is long, keep going — do not summarize or stop early.
- Produce working, runnable code. Not stubs.
