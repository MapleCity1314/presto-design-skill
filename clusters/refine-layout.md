# Refine - Layout

Structural fixes: spacing, hierarchy, responsive design, simplification. Loaded by `refine.md` when symptoms are layout-related.

---

## Arrange (layout & spacing)

Establish visual rhythm through varied spacing, not uniform padding everywhere.

1. Audit spacing: are related elements grouped (8-12px), sections separated (48-96px)? Or is everything the same padding?
2. Flatten hierarchy: never nest cards inside cards. If you see a card with a card inside, remove the outer container first.
3. Break monotony: if every row is the same height and every column the same width, introduce variation with a feature row, an asymmetric two-column, or a full-bleed section.
4. Layout tool choice: Flex for 1D (row or column of items), Grid for 2D (two-dimensional placement). Don't default to Grid for a simple row.
5. Responsive grid: `repeat(auto-fit, minmax(280px, 1fr))` for card grids.
6. Forbidden pattern: `big number + small label + gradient background` hero metrics. Flatten them.
7. Escalate to redesign: if fixing the problem requires replacing most sections or rethinking the entire page composition, this is no longer refine work.

Mandatory check: if your layout solution is still "three equal cards in one row", you have not refined enough.

---

## Distill (remove complexity)

Simplification is not removing features; it's removing friction between the user and their goal.

1. Information architecture: cut every piece of content that doesn't move the user toward their next action.
2. Visual: reduce to 1-2 colors plus neutrals. One type family, max 3-4 sizes, 2-3 weights. Remove decorative borders, shadows, or backgrounds that don't serve hierarchy.
3. Layout: linear flow over complex grids. Remove sidebars unless navigation is a primary task.
4. Interaction: one clear primary action per screen. Remove confirmations of confirmations.
5. Code: reduce component variants; if two variants are nearly identical, merge them.

Card simplification rule: if a card has a background, border, and shadow simultaneously, remove at least one unless elevation is doing real hierarchy work.

---

## Normalize (align to design system)

1. Spacing tokens: replace arbitrary `px` values with design system tokens. `gap-3` not `gap-[11px]`.
2. Color tokens: replace hardcoded hex with CSS variables from the theme.
3. Typography tokens: use the scale, not ad-hoc `text-[17px]`.
4. Component variants: if you have `ButtonPrimary`, `ButtonSecondary`, `ButtonDanger` all separately implemented, consolidate to `Button` with a `variant` prop.
5. Inline styles: if the project is not email HTML and the value is not truly runtime-dynamic, move inline styles into CSS classes, tokens, or component variants.

---

## Adapt (responsive & cross-device)

Use when the design breaks on mobile, has fixed widths, or was designed desktop-first without mobile consideration.

Step 1 - Identify target contexts

| Context | Key constraints |
|---------|----------------|
| Mobile (320-767px) | Single column, touch targets >= 44px, 16px+ body text, no hover-only states |
| Tablet (768-1023px) | 1-2 columns, may have hover |
| Desktop (1024px+) | Multi-column, cursor interactions |
| Email | Max 600px, single column, inline styles only |

Step 2 - Fluid before breakpoints

```css
/* Scale continuously - add breakpoints only when content breaks */
font-size: clamp(1rem, 2.5vw, 1.25rem);
padding:   clamp(16px, 5vw, 64px);
gap:       clamp(12px, 3vw, 32px);

/* Container: fluid up to a max */
max-width: min(100% - 48px, 1200px);
margin-inline: auto;
```

Step 3 - Layout breakpoints

```css
.grid { display: grid; grid-template-columns: 1fr; }

@media (min-width: 640px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 960px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}
```

Step 4 - Touch and interaction rules

```css
/* Touch targets */
.btn, .link, .icon-btn { min-height: 44px; min-width: 44px; }

/* Remove hover-only states on touch devices */
@media (hover: none) { .card:hover { transform: none; } }

/* Focus only for keyboard */
.btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.btn:focus:not(:focus-visible) { outline: none; }
```

Step 5 - Mobile typography floor

```css
@media (max-width: 767px) {
  body { font-size: 16px; line-height: 1.6; }
  h1   { font-size: clamp(1.75rem, 7vw, 3rem); }
}
```

Step 6 - Content priority on small screens

Consciously decide what to hide or collapse; don't auto-hide things. Secondary nav -> hamburger or bottom bar. Data table with many columns -> horizontal scroll or card layout. Large decorative hero images that push content below fold -> reduce or remove.

```css
.secondary-nav { display: none; }
@media (min-width: 768px) { .secondary-nav { display: flex; } }
```

Email adaptation: 600px max width, single column, all styles inline, HTML tables for layout, always set `width` and `height` on images.

---

## Extract (consolidate patterns)

Only extract when a pattern appears 3+ times:

1. Identify the repeated pattern (a card, a label, an icon + text combo).
2. Extract to a component with the minimal required props.
3. Replace all instances.
4. Name by what it is semantically, not how it looks: `StatusBadge` not `GreenPill`.

## Layout Exit Checklist

- [ ] The layout is less repetitive than before
- [ ] Unnecessary wrappers or nested cards were removed
- [ ] Equal-width three-column layouts are gone when they were the main composition
- [ ] Inline styling was reduced or eliminated where structure work touched the code
