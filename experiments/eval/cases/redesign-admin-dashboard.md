# Eval Case: Redesign Admin Dashboard

## Task description

Redesign the admin overview dashboard for Canopy, a HR software product. The current dashboard is a grid of six equal metric cards (headcount, active benefits, pending approvals, recent hires, attrition rate, open roles), each with a gradient background and a large white number. It looks like an AI-generated template. HR admins use this daily as their first view of the morning. Redesign it to feel like a serious, trustworthy product.

## Stack context

- Framework: React (Next.js)
- Styling: Tailwind CSS v4 with `@theme` tokens
- Existing tokens:
  - `--color-brand: oklch(48% 0.16 155)` (forest green)
  - `--color-surface: oklch(97% 0.008 100)`
  - `--font-sans: 'Geist', sans-serif`
- Installed components: shadcn/ui (Radix-based) — Card, Badge, Table, Avatar
- Existing gradient cards: `bg-gradient-to-br from-green-500 to-teal-600 text-white` (this is the pattern to replace)

## Constraints

- Audience: HR directors and People Ops managers at companies of 100–1000 employees; data accuracy is trusted implicitly
- Tone: professional, calm, information-forward — no marketing language
- The six metrics are non-negotiable content — all must appear
- The redesign should work at 1280px+ desktop viewport as the primary context
- The redesigned layout must NOT be six equal-width cards

## Adversarial signal

None. Standard case.

## What a good output demonstrates

- Flat, data-forward design replacing the gradient cards (verifiable: no `bg-gradient-*` on metric display)
- Varied grid layout that creates hierarchy between metrics (e.g., headcount prominently sized, others secondary)
- No gradient text on metric values
- Color used for meaning only (attrition = caution color, positive metrics neutral)
- Focus states on interactive elements (sort, filter)
- Scan-phase summary provided before fixes are made
