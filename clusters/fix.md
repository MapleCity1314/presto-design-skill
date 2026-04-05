# Cluster: Fix

Diagnose and fix quality issues. Synthesizes: `audit`, `critique`, `fixing-accessibility`, `fixing-metadata`, `fixing-motion-performance`, `optimize`, `harden`.

## Workflow

Run these phases in order. Each phase generates a prioritized issue list and recommended actions. Don't fix in the middle of audit — complete diagnosis first.

---

## Phase 1: Technical Audit (from `audit`)

Score each dimension 0–4. Total /20.

### Accessibility (0–4)
- [ ] Color contrast: body text ≥ 4.5:1, large text (18pt+ or 14pt bold) ≥ 3:1, UI components ≥ 3:1
- [ ] All interactive elements reachable and operable by keyboard
- [ ] Focus styles visible — not removed with `outline: none` without replacement
- [ ] Semantic HTML: `<button>` for actions, `<a>` for navigation, `<h1>`-`<h6>` hierarchy intact
- [ ] Images have meaningful `alt` text (not filename, not empty unless decorative)
- [ ] Form inputs have associated `<label>` (not just placeholder)
- [ ] ARIA roles used correctly — `role="button"` only on non-button elements with keyboard handling
- [ ] `prefers-reduced-motion` respected

### Performance (0–4)
- [ ] No animations on layout properties (width/height/top/left) — use transform instead
- [ ] No `will-change` outside active animations
- [ ] No large `blur()` or `backdrop-filter` on large surfaces
- [ ] Images: lazy loading, appropriate formats (WebP/AVIF), responsive `srcset`
- [ ] No layout thrashing (reading then writing DOM in loops)
- [ ] Bundle: no unused dependencies imported
- [ ] No `useEffect` chains that could be derived render logic

### Theming & Consistency (0–4)
- [ ] Color tokens used consistently — no hardcoded hex that duplicates a token
- [ ] Spacing uses design system scale, not arbitrary values
- [ ] Typography tokens consistent — not mixing `text-sm` with `text-[13px]`
- [ ] Component variants consolidated (no duplicate implementations)
- [ ] Dark/light mode both work, no hard-coded colors that break one mode

### Responsive Design (0–4)
- [ ] No fixed widths that break at small viewports
- [ ] Touch targets ≥ 44×44px
- [ ] No horizontal scroll at any viewport size
- [ ] Text doesn't overflow containers on small screens
- [ ] Body text min 16px on mobile

### AI Anti-Patterns (0–4)
Check for these — each present = –1 point:
- Cyan-on-dark / neon accents / purple-to-blue gradients
- Gradient text on headings or metrics
- Hero metrics layout (big number + gradient card)
- Three equal-width cards as the entire content
- Glassmorphism as a primary design element
- Inter/Roboto/Arial as the display font with no customization
- Rounded icon above every heading

**Scoring**: 18–20 excellent · 14–17 good · 10–13 acceptable · 6–9 poor · 0–5 critical

---

## Phase 2: UX Review (from `critique`)

Evaluate with Nielsen's 10 heuristics, score 0–4 each.

Focus on the four highest-leverage heuristics for most UIs:

1. **Visibility of system status** — does the user always know what's happening? (Loading states, progress, success/error feedback)
2. **Match between system and real world** — does the language match the user's mental model? Avoid jargon.
3. **Error prevention** — does the design prevent errors before they happen? (Confirmation dialogs, input validation, destructive action warnings)
4. **Recognition over recall** — can users see their options without memorizing? Navigation, action labels, visible affordances.

Additional checks:
- **Cognitive load**: if a decision point has >4 visible options, consider reducing or grouping.
- **Emotional journey**: is there a moment where the user feels accomplished? Is there a moment where they feel anxious or frustrated?
- **AI Slop test**: does any copy sound like a generic AI assistant? ("Seamlessly", "robust", "leverage", "cutting-edge") — replace with specific, concrete language.

---

## Phase 3: Fix Routing

Based on audit results, route to the targeted fix:

| Issue type | Action |
|-----------|--------|
| Contrast failures | Fix color values — lighten/darken until ratio passes. Use OKLCH lightness adjustments. |
| Missing ARIA / keyboard | Add `role`, `aria-label`, `tabindex`, keyboard event handlers. Prefer using Base UI / Radix primitives. |
| Animating layout properties | Replace with `transform: translate()` + `clip-path` for height. |
| Performance — layout thrashing | Batch DOM reads, then writes. Use `requestAnimationFrame`. |
| Inconsistent tokens | Run normalize pass: replace arbitrary values with design system tokens. |
| Responsive breaks | Add breakpoint logic, `clamp()` for fluid values, touch target adjustments. |
| AI anti-patterns | Refactor: swap fonts, replace gradient cards, restructure hero layout. |
| Unhelpful UX copy | Rewrite per clarify rules: specific action + outcome, active voice, no jargon. |
| Missing error handling | Add error states, empty states, loading states for every async operation. |
| Missing metadata | Add title, description, canonical URL, og:image, twitter:card. |

---

## Accessibility Fix Priorities

### P0 (fix immediately — blocks users)
- Keyboard trap (user cannot navigate away)
- Interactive element with no accessible name
- Form submission with no error feedback

### P1 (fix before ship)
- Contrast ratio below 4.5:1 for body text
- Focus indicator invisible
- Images missing alt text
- Form inputs without labels

### P2 (fix soon)
- `prefers-reduced-motion` not respected
- Touch targets below 44×44px
- Semantic HTML violations (div soup instead of semantic elements)

### P3 (address in next iteration)
- ARIA enhancements (live regions, extended descriptions)
- Skip-to-content link missing
- Keyboard shortcut documentation

---

## Harden (resilience)

After fixing functional issues, check resilience:

**Error states**: every async operation needs three states — loading, success, error. Error state must tell the user what happened and what to do.

**Empty states**: every list/table/feed needs an empty state. Minimum: what's empty + one clear next action.

**Edge cases**: test with 0 items, 1 item, 1000 items. Test with long strings (50+ char usernames, 200-char titles). Test with missing optional data.

**i18n resilience**: text containers must handle 2× the English length (German, Finnish, etc. expand significantly). Use `text-balance`, `overflow: hidden`, `text-overflow: ellipsis` where needed.

**Motion accessibility**: wrap all animations in `@media (prefers-reduced-motion: no-preference) { ... }` or check in JS with `window.matchMedia('(prefers-reduced-motion: reduce)')`.

---

## Metadata (SEO & social)

Run this when: the page has no `<title>`, shares badly on Slack/Twitter, or has missing canonical/og tags.

### Required tags checklist

```html
<head>
  <!-- 1. Title: brand + page | 50–60 chars -->
  <title>Page Name | Brand Name</title>

  <!-- 2. Description: action-oriented, 150–160 chars -->
  <meta name="description" content="Specific benefit of this page. What can the user do here?">

  <!-- 3. Canonical: prevents duplicate content penalties -->
  <link rel="canonical" href="https://example.com/current-page/">

  <!-- 4. Open Graph (Facebook, Slack, LinkedIn previews) -->
  <meta property="og:title"       content="Page Name | Brand Name">
  <meta property="og:description" content="Same as meta description">
  <meta property="og:url"         content="https://example.com/current-page/">
  <meta property="og:image"       content="https://example.com/og-image.png">
  <!-- og:image: minimum 1200×630px, ideally exact. Max 8MB. -->
  <meta property="og:type"        content="website">  <!-- or "article" for blog posts -->
  <meta property="og:site_name"   content="Brand Name">

  <!-- 5. Twitter Card -->
  <meta name="twitter:card"        content="summary_large_image">
  <meta name="twitter:title"       content="Page Name | Brand Name">
  <meta name="twitter:description" content="Same as meta description">
  <meta name="twitter:image"       content="https://example.com/og-image.png">
  <!-- twitter:image: min 300×157px, max 4096×4096px, max 5MB -->

  <!-- 6. Viewport (mobile) -->
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- 7. Charset -->
  <meta charset="UTF-8">
</head>
```

### Title formula

```
[Primary Keyword / Page Purpose] | [Brand Name]
```

- Homepage: `Brand Name — Tagline` (reversed)
- Inner page: `Feature Name | Brand Name`
- Blog post: `Article Title | Blog Name`
- Max 60 chars — truncated in Google at ~55–60.

### Common mistakes to fix

| Problem | Fix |
|---------|-----|
| `<title>` is generic ("Home", "Untitled") | Rewrite with keyword + brand |
| No `og:image` | Create a 1200×630 branded card image |
| `og:image` is a relative path | Must be absolute URL |
| Description is >160 chars | Truncated in previews — shorten |
| Description is the same on all pages | Each page needs unique, specific copy |
| Missing canonical on paginated content | Add `?page=N` canonical pointing to page 1 |
| No `lang` attribute on `<html>` | `<html lang="en">` (or appropriate locale) |

### Structured data (optional but valuable)

For articles, products, events, and FAQs — add JSON-LD:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Page Title",
  "description": "Page description",
  "url": "https://example.com/page/",
  "publisher": {
    "@type": "Organization",
    "name": "Brand Name",
    "logo": { "@type": "ImageObject", "url": "https://example.com/logo.png" }
  }
}
</script>
```

Validate with: [Google Rich Results Test](https://search.google.com/test/rich-results) or Schema Markup Validator.

---

## Output Format

After running the audit, output:

```
## Audit Score: X/20

### P0 Issues (fix immediately)
- [issue]: [specific location] → [fix]

### P1 Issues (fix before ship)  
- [issue]: [specific location] → [fix]

### P2 Issues (next iteration)
- [issue]: [specific location] → [fix]

### Recommended Actions
1. /fix-accessibility → addresses N P0/P1 items
2. /optimize → addresses performance items  
3. /clarify → addresses UX copy items
```
