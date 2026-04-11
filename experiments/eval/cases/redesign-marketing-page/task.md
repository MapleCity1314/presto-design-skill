# Eval Case: Redesign Marketing Page

## Task description

Redesign the homepage of Axle, a logistics route optimization API. The current page has: a hero with centered text on a dark navy background with a cyan-to-purple gradient overlay, three equal feature cards below with glassmorphism styling, a "trusted by" logo row, and a footer. The page was clearly AI-generated and has low credibility with the technical buyers it needs to reach. Redesign it to feel like a serious, developer-facing API product.

## Stack context

- Framework: Next.js (App Router)
- Styling: Tailwind CSS v3 with existing `tailwind.config.js`
- Existing brand asset: Axle wordmark (dark text version available at `/public/axle-wordmark.svg`)
- Current problematic patterns (explicitly to fix):
  - `bg-gradient-to-br from-navy-900 via-blue-900 to-purple-900` on hero
  - `backdrop-filter: blur(12px); background: rgba(255,255,255,0.05)` glassmorphism cards
  - `bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text text-transparent` gradient text on headline
- No animation library

## Constraints

- Audience: senior engineers and engineering managers at logistics companies evaluating APIs; skeptical of marketing, trust earned through technical specificity
- Tone: technical, direct, no hype - copy should show what the API does, not describe how revolutionary it is
- Hard requirement: replace all three anti-slop patterns listed above
- Hard requirement: the hero must include a code snippet (showing example API request/response)
- The redesign can change layout, colors, and typography - full reset is appropriate here given how broken the current design is

## Adversarial signal

None. Standard case.

## What a good output demonstrates

- Phase 1 scan explicitly identifies the three anti-slop patterns as P0 issues
- Gradient hero is replaced with a clean, non-gradient approach
- Glassmorphism cards are replaced with a less visually busy alternative
- Gradient text on headline is removed
- Hero code snippet is syntax-highlighted and readable
- Typography choice is appropriate for a technical audience (not purely aesthetic)
- New layout does not fall back into three-equal-column cards as the main composition
