# Cluster: Redesign

Upgrade an existing project to premium quality without rebuilding from scratch. Synthesizes: `redesign-existing-projects`, `typeset`, `colorize`, `arrange`, `harden`, `clarify`, `better-icons`, `fixing-metadata`.

**Core rule**: work with the existing stack. Do not migrate frameworks or rewrite what's working. Improve what's there, in place.

Escalation rule: preserve the current design language when it is coherent and product-appropriate. Push for a stronger reset only when the existing language is generic, inconsistent, or actively undermining clarity or trust.

---

## Three-Phase Workflow

Tailwind note: when the project uses Tailwind CSS, load `tailwind-integration.md` before deciding how to add tokens, variants, or shared utilities.

### Phase 1 — Scan

Before diagnosing anything, read the codebase to understand what you're working with:

- `DESIGN.md` → if present, this is the target design authority. Diagnosis in Phase 2 should measure the current implementation against DESIGN.md, not against generic best practices.
- `package.json` / config files → framework, Tailwind version (v3 vs v4), installed libraries
- Main layout components → current grid, spacing patterns, component structure
- CSS variables / design tokens → existing color palette, font stack, spacing scale
- Brand assets → logo, favicon, existing color values
- README / docs → project purpose, stated audience

**Output a one-paragraph summary**: framework + styling method + current design quality level + the 2-3 most glaring problems you've already spotted.

Before moving on, answer this explicitly: is this project asking for refinement inside an existing language, or is the existing language itself the problem?

---

### Phase 2 — Diagnose

Run through every dimension below. Mark each problem found as **P0** (fix now), **P1** (fix before ship), or **P2** (next iteration). Don't fix yet — complete the full diagnosis first.

**Priority guide**: P0 = instant visual credibility killers, P1 = significant quality improvements, P2 = polish and content refinement.

Add this cross-check to every category:

- Can you explain why the proposed change better fits the audience, product, and current codebase than the existing choice?
- If not, you are still reacting to style symptoms rather than making a design decision.

#### Typography

- [ ] `P0` **Default or overused font.** Inter, Roboto, Arial, system defaults → `Geist`, `Outfit`, `Cabinet Grotesk`, `Satoshi`. Editorial: pair serif header with sans-serif body.
- [ ] `P0` **Headlines lack presence.** Too small/light/wide → increase size, tighten `letter-spacing` (`-0.02em` to `-0.04em`), `line-height: 1.0–1.15`.
- [ ] `P1` **Body text too wide.** Full container width → `max-width: 65ch`.
- [ ] `P1` **Only Regular + Bold.** Introduce Medium (500) and SemiBold (600).
- [ ] `P1` **Numbers in proportional font.** Changing numeric data → `font-variant-numeric: tabular-nums`.
- [ ] `P2` **All-caps subheaders everywhere.** Try lowercase italics or sentence case.
- [ ] `P2` **Orphaned words.** Single words on last heading line → `text-wrap: balance`.
- [ ] `P2` **Missing tracking adjustments.** Negative tracking on large display text; positive on small labels.

#### Color and Surfaces

- [ ] `P0` **Purple/blue "AI gradient" fingerprint.** Most identifiable AI slop marker → neutral base + single considered accent.
- [ ] `P0` **Pure `#000000` or `#ffffff`.** → off-black `oklch(8% 0.01 240)`, warm off-white `oklch(97.5% 0.01 60)`.
- [ ] `P0` **More than one accent color.** Pick one. Remove the rest.
- [ ] `P1` **Oversaturated accent.** Saturation above 80% → desaturate.
- [ ] `P1` **Warm and cool grays mixed.** Tint all grays consistently toward one hue.
- [ ] `P1` **Generic drop shadows.** `rgba(0,0,0,0.1)` everywhere → tint shadows to background hue.
- [ ] `P2` **Flat design with zero texture.** Add subtle noise/grain overlay.
- [ ] `P2` **Perfectly even linear gradients.** Replace with radial gradients or mesh.
- [ ] `P2` **Inconsistent light direction.** Audit and unify shadow direction.
- [ ] `P2` **Random dark section in light page.** Commit to one mode or use a palette-consistent dark variant.
- [ ] `P2` **Empty flat sections.** Add ambient radial gradient or very subtle pattern.

#### Layout

- [ ] `P0` **Three equal-width card columns.** Most generic AI layout → 2-column zig-zag, asymmetric grid, or masonry.
- [ ] `P0` **Dashboard hero metrics layout.** Big number + gradient card → data-forward flat design.
- [ ] `P1` **Everything centered and symmetrical.** Break with offset margins or left-aligned headers.
- [ ] `P1` **`height: 100vh`** → `min-height: 100dvh` (iOS Safari bug).
- [ ] `P1` **No max-width container.** → `max-width: 1200–1440px; margin: auto`.
- [ ] `P1` **No breathing room.** Double section padding on marketing pages.
- [ ] `P1` **Buttons not bottom-aligned in card groups.** Pin CTAs to card bottom.
- [ ] `P2` **Flexbox percentage math.** `w-[calc(33%-1rem)]` → CSS Grid.
- [ ] `P2` **Uniform border-radius on everything.** Vary: tighter inner, softer containers.
- [ ] `P2` **No overlap or depth.** Use negative margins and z-index for layering.
- [ ] `P2` **Equal top/bottom padding.** Bottom usually needs ~10–20% more than top.
- [ ] `P2` **Feature lists starting at different Y positions.** Equalize with fixed-height title blocks.
- [ ] `P2` **Misaligned baselines across columns.** Titles, prices, buttons should share a Y baseline.
- [ ] `P2` **Mathematical center that looks optically wrong.** 1–2px optical adjustments on icons/buttons.

#### Interactivity and States

- [ ] `P0` **No hover states on buttons.** Add background shift, `scale(1.02)`, or translate.
- [ ] `P0` **No error states.** Inline validation feedback on all forms.
- [ ] `P0` **Missing focus ring.** Visible `:focus-visible` — accessibility requirement.
- [ ] `P1` **No active/pressed feedback.** `scale(0.97)` or `translateY(1px)` on `:active`.
- [ ] `P1` **Instant transitions.** Add `150–200ms ease-out` to all interactive elements.
- [ ] `P1` **No empty states.** Design "getting started" or "add your first X" state.
- [ ] `P1` **Animations on layout properties.** → `transform` + `opacity` only.
- [ ] `P2` **Generic circular spinners.** → skeleton loaders matching layout shape.
- [ ] `P2` **Dead placeholder links.** Disable visually or link to real destination.
- [ ] `P2` **No current-page indicator in nav.** Style active item distinctly.
- [ ] `P2` **Anchor links jump without scroll.** `scroll-behavior: smooth`.

#### Content

- [ ] `P0` **AI copywriting clichés.** Never: "Elevate", "Seamless", "Unleash", "Next-Gen", "Game-changer", "Delve", "Leverage" → plain, specific language.
- [ ] `P1` **Lorem Ipsum anywhere.** Write real copy or clearly marked `[PLACEHOLDER]`.
- [ ] `P1` **"Oops!" error messages.** → "Connection failed. Please try again."
- [ ] `P1` **Exclamation marks in success messages.** Remove. Confident, not loud.
- [ ] `P2` **Generic placeholder names.** "John Doe" → diverse, believable names.
- [ ] `P2` **Round fake numbers.** `99.99%` → organic: `47.2%`.
- [ ] `P2` **Passive voice.** "We couldn't save" not "Mistakes were made."
- [ ] `P2` **Title Case On Every Header.** Use sentence case.
- [ ] `P2` **Identical dates, same avatars.** Randomize and diversify.

#### Component Patterns

- [ ] `P1` **Generic card: border + shadow + white background.** Remove one of the three. Cards only when elevation communicates hierarchy.
- [ ] `P1` **Pricing table with 3 equal towers.** Highlight recommended tier with color and emphasis.
- [ ] `P2` **Always one filled + one ghost button.** Add text links or tertiary styles.
- [ ] `P2` **3-card carousel testimonials with dots.** → masonry wall or single rotating quote.
- [ ] `P2` **Modals for simple actions.** → inline editing or slide-overs.
- [ ] `P2` **Pill "New"/"Beta" badges.** → square badges or plain text labels.
- [ ] `P2` **Footer with 4-column link farm.** Simplify to essential paths + legal links.

#### Iconography

Tooling fallback:

- inspect installed icon packages first
- prefer one existing family over introducing a guessed mix
- avoid hand-authored SVG paths from memory
- if no dependable icon source exists, keep icon updates minimal and document the constraint

- [ ] `P1` **Lucide or Feather as sole library.** → Phosphor, Solar, or Tabler. Use `better-icons search` to find alternatives.
- [ ] `P2` **Cliché metaphors.** Rocket for launch, shield for security → bolt, fingerprint, spark, vault.
- [ ] **Inconsistent stroke widths.** Audit all icons and standardize to one stroke weight.
- [ ] **Missing favicon.** Always include a branded `<link rel="icon">`.
- [ ] **Stock "diverse team" photos.** Use real photos, candid shots, or a consistent illustration style.

#### Code Quality

- [ ] **Div soup.** Use semantic HTML: `<nav>`, `<main>`, `<article>`, `<aside>`, `<section>`, `<header>`, `<footer>`.
- [ ] **Inline styles mixed with classes.** Move to the styling system.
- [ ] **Hardcoded pixel widths.** `width: 400px` → use `%`, `rem`, `max-width`, or container queries.
- [ ] **Missing alt text.** Every meaningful image needs a description. `alt=""` only for decorative images.
- [ ] **Arbitrary z-index values.** `z-999`, `z-9999` → establish a clean scale: 10 / 20 / 30 / 100 / 200 / modal: 500.
- [ ] **Commented-out dead code.** Remove before shipping.
- [ ] **Import hallucinations.** Verify every import exists in `package.json`.
- [ ] **Missing metadata.** Add `<title>`, `<meta name="description">`, `og:image`, twitter:card. (See `clusters/fix.md` Metadata section for full spec.)

#### Strategic Omissions

Things AI typically generates without:

- [ ] Legal links in footer (privacy policy, terms of service)
- [ ] Back navigation — no dead ends in user flows
- [ ] Custom 404 page
- [ ] Client-side form validation (email format, required fields)
- [ ] Skip-to-content link for keyboard users
- [ ] Cookie consent (if required by jurisdiction)

---

### Phase 3 — Fix Priority

Apply in this order — maximum visual impact, minimum risk:

First decide whether a style reset is necessary at all. If the current language is already coherent, start with hierarchy, states, spacing, and implementation quality before changing identity-level choices.

1. **Font swap** — biggest instant improvement, lowest risk. One line changes the feel entirely.
2. **Color palette cleanup** — remove clashing/oversaturated colors, fix pure black/white.
3. **Hover and active states** — makes the interface feel alive with minimal code.
4. **Layout and spacing** — grid, max-width, consistent padding, break the 3-column card layout.
5. **Replace generic components** — swap pricing towers, testimonial carousels, accordion FAQs.
6. **Add missing states** — loading skeletons, empty states, error states.
7. **Typography scale and content** — final typographic refinement, replace placeholder content.
8. **Metadata and accessibility** — `<title>`, og:image, focus states, alt text, skip links.

---

## Upgrade Techniques

When the basic fixes are done, pull from these for high visual impact:

### Typography
- **Variable font animation**: interpolate `font-weight` on scroll or hover for text that feels alive.
- **Text mask reveals**: large typography as a window to video or animated imagery.
- **Outlined-to-fill transitions**: text starts as stroke outline, fills on scroll entry.

### Layout
- **Broken grid / asymmetry**: elements that deliberately ignore columns — overlapping, bleeding off-screen, calculated offset.
- **Parallax card stacks**: sections that stick and stack over each other on scroll.
- **Split-screen scroll**: two halves sliding in opposite directions.
- **Whitespace maximization**: aggressive negative space to force focus on a single hero element.

### Motion
- **Staggered entry**: elements cascade in with `50–80ms` delays, Y-translate + opacity fade. Never mount everything simultaneously.
- **Spring physics**: replace linear easing with spring-based motion on interactive elements (`stiffness: 100, damping: 20`).
- **Scroll-driven reveals**: content entering through expanding masks, wipes, or SVG draw-on paths tied to scroll.

### Surface
- **Noise and grain overlay**: `position: fixed; pointer-events: none; opacity: 0.03–0.06` pseudo-element with SVG noise — breaks digital flatness without decoration.
- **Colored tinted shadows**: shadows carry the background hue rather than generic black.
- **Spotlight borders**: card borders that illuminate dynamically under cursor (CSS custom property + `@property` + mousemove tracking).

---

## Final Self-Check

Before finishing, verify:

- Inline styles were removed unless the target is email HTML or a truly runtime-driven one-off
- Generic card language was simplified: do not keep background + border + shadow everywhere
- The layout no longer depends on three equal-width columns as its main composition
- The redesign can explain why its typography, palette, and composition are better fits for the audience
- The redesign upgraded structure and hierarchy, not just fonts and accent colors
- The final output still satisfies `contract.md`

## Constraints

- In Tailwind projects, prefer semantic tokens and readable utility composition over arbitrary-value sprawl.

- Work with the existing tech stack. No framework migration.
- Check Tailwind version (`v3` vs `v4`) before touching config — syntax is different.
- Verify every new import exists in `package.json` before using it.
- Do not break existing functionality. Keep changes reviewable and focused.
- Use vanilla CSS if no framework.
