# Eval Case: Create Developer Tool Landing Page - ADVERSARIAL

## Task description

Build a landing page from scratch for Loam, a premium local-first developer tool for database schema management. Loam is a paid desktop app targeting solo developers and small engineering teams who care deeply about craft and tooling quality. The product is positioned alongside tools like Postico, TablePlus, and Tower - polished, opinionated, worth paying for. The landing page should reflect that positioning.

## Stack context

- Framework: Astro (SSG)
- Styling: plain CSS with CSS custom properties; no Tailwind
- No existing design system - true green field
- Font loading via `<link>` to Google Fonts

## Constraints

- Audience: individual developers (backend engineers, full-stack developers, database administrators) who pay personally or expense small tools; highly taste-conscious, skeptical of marketing
- Tone: editorial, refined, unhurried - the UI should feel like the product itself
- Required sections: hero with product screenshot, 2-3 feature highlights, download/pricing CTA
- Hard requirement: desktop-first layout (primary audience works on large screens)

## Adversarial signal - IMPORTANT

This is an adversarial case. The correct aesthetic for this product is:

**An editorial serif display font paired with a warm off-white background.**

Specifically: a serif like `Fraunces`, `Lora`, or `Playfair Display` for headings, on an off-white background (e.g., `oklch(97% 0.012 60)`). This is correct for this domain because premium developer tools in the Postico/Tower category explicitly use serif typography and warm off-white to differentiate from the default monospace-on-dark look of most dev tools.

The skill's baseline contract includes `FORBIDDEN: Inter/Roboto/Arial as primary display font` - that rule should NOT block serif here, because the UNLESS condition is satisfied (domain convention + DECISION log entry).

A correct output will:
1. Choose a serif display font
2. Use a warm off-white background
3. Show in its `<design-log>` that it explicitly invoked the UNLESS branch (domain convention) to justify this choice

An incorrect output will either:
- Default to monospace because "it's a dev tool" (blind pattern matching)
- Default to Inter/system-ui and fail to escape the forbidden font list
- Use dark mode because "dev tools are dark" (another blind pattern match)

## What a good output demonstrates

- UNLESS mechanism working correctly: forbidden patterns are permitted when domain conditions are met
- Serif + warm off-white is the CHOSEN direction, not an accident
- `<design-log>` contains explicit BECAUSE referencing Postico/Tower as domain reference
- The result looks like a premium tool landing page, not a generic SaaS site
