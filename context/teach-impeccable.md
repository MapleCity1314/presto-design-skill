# Context Gathering Workflow

Run this when no design context exists. Goal: write `.impeccable.md` to the project root before doing any design work.

## Step 1 — Scan the codebase first

Extract what you can before asking questions:

- `README` / docs → project purpose, stated goals, audience clues
- `package.json` / config → tech stack, installed design libraries
- Existing components → current design patterns, spacing, typography in use
- CSS variables / tokens → existing color palette, font stack, spacing scale
- Brand assets → logos, favicons, color values already defined

Note what you've learned and what remains unclear.

## Step 2 — Ask only what you couldn't infer

Focus on four areas. Skip questions where the codebase already answered them.

**Users & Purpose**
- Who uses this? What's their context when using it?
- What job are they trying to get done?
- What emotions should the interface evoke? (confidence, delight, calm, urgency…)

**Brand & Personality**
- How would you describe the brand personality in 3 words?
- Any reference sites / apps that capture the right feel? What specifically about them?
- What should this explicitly NOT look like? Anti-references?

**Aesthetic Preferences**
- Any strong direction? (minimal, bold, elegant, playful, technical, organic…)
- Light mode, dark mode, or both?
- Colors that must be used or avoided?

**Accessibility & Inclusion**
- Specific accessibility requirements? (WCAG level, known user needs)
- Any `prefers-reduced-motion` or color-blindness considerations?

## Step 3 — Write `.impeccable.md`

Synthesize codebase findings + user answers into this format and write to project root:

```markdown
## Design Context

### Users
[Who they are, their context, the job to be done]

### Brand Personality
[Voice, tone, 3-word personality, emotional goals]

### Aesthetic Direction
[Visual tone, references, anti-references, light/dark preference]

### Design Principles
[3–5 principles derived from the conversation that should guide all decisions]
```

If `.impeccable.md` already exists, update the Design Context section in place. Ask the user if they'd also like it appended to `.github/copilot-instructions.md`.

Confirm completion and summarize the key principles before continuing with the design task.
