# Eval Case: Refine Multi-Step Form Flow

## Task description

Refine a three-step onboarding form for Vesta, a property management SaaS. The form collects: Step 1 - landlord profile (name, email, phone); Step 2 - first property (address, unit count, property type); Step 3 - billing (plan selection + payment). The current flow has no progress indicator, unclear error states, and the "Next" and "Back" buttons are identically styled. Improve the form UX without changing the three-step structure.

## Stack context

- Framework: Vue 3 + Vite
- Styling: Tailwind CSS v3
- Existing tokens: `--color-brand: oklch(55% 0.18 145)` (green), `--font-sans: 'Plus Jakarta Sans', sans-serif`
- Existing component: `<VestaInput>`, `<VestaButton variant="primary|ghost">`, `<VestaSelect>`
- No animation library

## Constraints

- Audience: independent landlords (non-technical), often 40-65 years old, managing 1-20 properties; mobile device likely
- Primary task: get from signup to first property listed without confusion
- Hard requirement: all form fields must have visible labels (not placeholder-only)
- Hard requirement: error messages must specify what was wrong AND what to do ("Email already in use - try signing in instead")
- Touch targets 44x44px minimum
- Do not change the three-step structure

## Adversarial signal

None. Standard case.

## What a good output demonstrates

- Progress indicator added (step 1 of 3, visually clear)
- Primary "Next" button is visually distinct from "Back" (filled vs. ghost or size difference)
- Error states are inline, next to the field, not a toast at the top of the page
- Labels are above inputs in all steps
- Touch targets verified in the self-check
- Form completion flow has no dead ends (Back always works, no accidental submit)
