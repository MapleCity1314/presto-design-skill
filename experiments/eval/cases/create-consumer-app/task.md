# Eval Case: Create Consumer App UI

## Task description

Build the main screen of Dusk, a personal journaling app. Dusk is a mobile-web app (responsive, primarily phone-sized) for daily reflection journaling. Users open it at night before bed. The app has a mood check-in (emoji slider), a free-write journal entry area, and a "previous entries" row of day cards. Build the home screen for a logged-in user who has 5 previous entries.

## Stack context

- Framework: React (Vite)
- Styling: Tailwind CSS v3; `tailwind.config.js` with `theme.extend`
- No design system exists yet - build the tokens as part of this task
- Motion: `framer-motion` is installed

## Constraints

- Audience: adults 25-55 using this alone, at night, as a private ritual; emotional safety and calm are paramount
- Tone: warm, intimate, unhurried - NOT productivity-app energy, not clinical
- Hard requirement: the mood slider must be accessible (keyboard navigable, labeled)
- Hard requirement: the free-write area must not feel like a form field - it should feel like a page
- Screen context: primary use on mobile (375px), secondary on tablet

## Adversarial signal

None. Standard case.

## What a good output demonstrates

- Aesthetic direction clearly suited to night/calm context (not generic pastel SaaS)
- Typography that feels personal, not corporate
- Color palette that works at night (neither harsh white nor pure black)
- Mood slider is a custom component with proper ARIA attributes
- Day cards are NOT three equal columns
- Framer Motion used only for purposeful transitions, with reduced-motion fallback
