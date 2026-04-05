# Tailwind Integration

Use this file whenever the target project already uses Tailwind CSS. It sharpens implementation choices; it does not replace the selected cluster.

---

## 1. Detect The Tailwind Shape First

Before editing code, confirm:

- version: v3 or v4
- token source: `tailwind.config.*` or CSS `@theme`
- shared utilities: `cn`, `cva`, `tailwind-merge`, variant helpers
- app framework: React / Next.js / Vite / plain HTML

Do not guess the Tailwind version. The setup changes what "good" output looks like.

---

## 2. Default Tailwind Strategy

Use Tailwind for:
- layout, spacing, sizing, responsive rules
- typography hierarchy
- surface styling, borders, radius, shadows
- state styles: `hover:`, `focus-visible:`, `disabled:`, `data-[state=...]`

Use CSS variables or theme tokens for:
- brand colors
- font families
- spacing scales reused across features
- semantic surface roles such as background, border, muted text, accent

Use plain CSS only when Tailwind becomes less readable:
- complex keyframes
- long pseudo-element treatments
- reusable noise/texture overlays
- very complex mask/clip-path effects

---

## 3. Output Rules For Tailwind Code

- Prefer semantic wrappers with utility classes over anonymous `div` soup.
- Prefer `h-dvh` or `min-h-dvh`; never introduce `h-screen`.
- Prefer `max-w-*`, `mx-auto`, `px-*`, `gap-*`, `space-y-*` over ad-hoc pixel math.
- Prefer design tokens over arbitrary values. `gap-6` beats `gap-[22px]`.
- Arbitrary values are allowed only for one-off art direction or exact optical fixes.
- Keep class lists readable: structure -> typography -> color -> effects -> state modifiers.
- If a class string becomes hard to scan, extract with `cn(...)` or a variant helper already used by the project.
- Respect existing conventions. If the codebase uses `cva`, keep using it. If it does not, do not introduce it casually.

Example ordering:

```tsx
className={cn(
  "grid gap-6 rounded-2xl border border-border/60 bg-background/95 p-6",
  "text-foreground shadow-[0_8px_30px_oklch(0%_0_0_/_0.06)]",
  "transition-transform duration-200 ease-out hover:-translate-y-0.5",
)}
```

---

## 4. Version-Specific Guidance

### Tailwind v4

- Put reusable tokens in CSS with `@theme`.
- Favor modern CSS variables and semantic color names.
- Avoid pretending `tailwind.config.js` is the primary extension point if the project does not use one.

### Tailwind v3

- Extend `theme` in `tailwind.config.*` for reusable colors, fonts, spacing, radii, and shadows.
- Do not pollute `theme.extend` with one-off experiment values.

---

## 5. Tailwind Quality Bar

Every Tailwind output should also satisfy these checks:

- responsive behavior is explicit, not accidental
- focus styles are visible with `focus-visible:`
- numeric data uses `tabular-nums`
- headings use `text-balance`, body copy uses `text-pretty` where available
- motion is limited to `transform` and `opacity`
- repeated visual patterns are extracted before class strings become unmaintainable
- no giant wrapper full of utilities around every section unless containment is doing real work
