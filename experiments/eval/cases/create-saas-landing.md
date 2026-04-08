# Eval Case: Create SaaS Landing Page

## Task description

Build a landing page from scratch for Meridian, a B2B workflow automation SaaS. The product helps operations teams at mid-market companies (50–500 employees) reduce manual handoffs between internal tools. The team has a brief design system in CSS variables but no existing landing page. Start from scratch.

## Stack context

- Framework: Next.js 14 (App Router)
- Styling: Tailwind CSS v4 with `@theme` tokens in `globals.css`
- Existing tokens: `--color-brand: oklch(52% 0.18 240)` (slate blue), `--font-sans: 'Inter', sans-serif`
- No existing landing page — green field
- No animation library installed

## Constraints

- Audience: VP Ops and Head of RevOps at mid-market SaaS companies, evaluating tools on behalf of their team
- Tone: confident, trustworthy, technically competent — not playful, not enterprise-formal
- Required sections: hero, 3 core features, 1 social proof row (logos or quote), pricing CTA
- Hard requirement: no full-page dark mode — light mode primary
- Hard requirement: must work without JavaScript for initial render

## Adversarial signal

None. Standard case.

## What a good output demonstrates

- Committed aesthetic direction with grounded BECAUSE rationale
- Typography choice that is NOT Inter (the existing token) as the display font
- Layout that escapes the three-equal-column feature grid
- Pricing CTA with clear hierarchy between tiers
- Full production baseline (focus states, reduced-motion, responsive, semantic HTML)
