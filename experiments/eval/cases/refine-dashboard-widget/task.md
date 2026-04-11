# Eval Case: Refine Dashboard Widget - ADVERSARIAL

## Task description

Refine a P&L summary widget in Quorum, a professional equity derivatives trading terminal. The widget currently shows six key metrics in a 3x2 grid: Realized P&L, Unrealized P&L, Net Delta, Vega, Theta, and Portfolio Beta. The display is functional but visually cluttered - values and labels use the same weight, and positive/negative values are hard to scan at a glance. Improve readability and visual hierarchy within the existing grid structure.

## Stack context

- Framework: React
- Styling: Plain CSS modules (no Tailwind)
- Existing palette: `--bg: #000000`, `--text: #ffffff`, `--positive: #00ff41`, `--negative: #ff3131`, `--border: #1a1a1a`
- Existing font: JetBrains Mono (monospace) throughout
- This is a professional trading terminal - the entire interface is black/white/green/red. No other colors exist.

## Constraints

- Audience: equity derivatives traders at a professional trading desk; this is their primary work tool
- Hard constraint: do NOT change the color palette. Pure `#000000` background and `#ffffff` text is CORRECT for this domain. Bloomberg Terminal, Interactive Brokers TWS, and similar professional terminals use pure black backgrounds by convention. This is not an AI slop default - it is a domain requirement.
- Hard constraint: do NOT change the monospace font. JetBrains Mono is correct for a terminal interface.
- Hard constraint: tabular number alignment is mandatory - all values must use `font-variant-numeric: tabular-nums`
- The 3x2 grid structure can be adjusted but not fundamentally restructured

## Adversarial signal - IMPORTANT

This is an adversarial case. The contract forbids:
- `FORBIDDEN: pure #000000 as background or body text color`
- `FORBIDDEN: Monospace as the primary voice for body text`

**Both forbidden patterns are CORRECT here.** The UNLESS conditions are satisfied:
- Domain is a finance terminal (professional trading terminal) where pure black background and monospace are the established convention
- The existing codebase explicitly uses these colors as the design system

A correct output will:
1. Keep `#000000` background and `#ffffff` text unchanged
2. Keep JetBrains Mono unchanged
3. Show in its `<design-log>` that it invoked the UNLESS branch for both forbidden patterns
4. Improve hierarchy through weight contrast and spacing only (not color changes)

An incorrect output will either:
- Swap `#000000` for a tinted OKLCH off-black (violating domain requirements)
- Replace JetBrains Mono with a sans-serif (violating domain requirements)
- Add color accents beyond the existing `--positive` and `--negative` values

## What a good output demonstrates

- UNLESS mechanism working correctly for BOTH forbidden patterns simultaneously
- Improvement through weight contrast (e.g., value at `font-weight: 600`, label at `400`)
- Positive/negative values use color (`--positive` / `--negative`) and weight, not just color alone
- Tabular alignment maintained
- `<design-log>` explicitly names "finance terminal / Bloomberg Terminal convention" as domain justification
