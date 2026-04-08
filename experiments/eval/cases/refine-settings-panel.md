# Eval Case: Refine Settings Panel

## Task description

Refine an existing settings panel for Helio, a project management SaaS. The current panel has issues: it's cramped, uses inconsistent spacing, and the section headers look identical to the field labels. The panel has three sections (Profile, Notifications, Security) each with 4–6 form fields. Improve hierarchy, spacing, and visual clarity without redesigning the structure.

## Stack context

- Framework: React with Next.js
- Styling: Tailwind CSS v3; existing `tailwind.config.js` with brand tokens
- Existing tokens: `--color-brand: #3B5BDB` (vivid blue), `--font-sans: 'Geist', sans-serif`
- Existing component: `<Input />`, `<Toggle />`, `<Button variant="primary|ghost" />`
- Existing structure (do not change): three `<section>` elements stacked vertically, each with a `<h2>` and a set of field rows

## Existing code (representative)

```tsx
<section className="p-4 border border-gray-200 rounded">
  <h2 className="text-sm font-medium text-gray-700 mb-3">Profile</h2>
  <div className="space-y-3">
    <label className="text-sm text-gray-600">Display Name</label>
    <Input value={name} onChange={...} />
    <label className="text-sm text-gray-600">Email</label>
    <Input value={email} onChange={...} type="email" />
  </div>
</section>
```

## Constraints

- Audience: SaaS power users accessing settings occasionally; familiarity assumed
- Do not change the three-section structure
- Do not introduce a new component library
- The result must be recognizably the same panel — not a redesign

## Adversarial signal

None. Standard case.

## What a good output demonstrates

- Section headers visually distinct from field labels (size, weight, or color contrast)
- Spacing between sections larger than spacing between fields within a section
- Labels are above their inputs, not visually merged (accessible)
- Self-check confirms this is a refine, not a redesign
- No new card wrappers introduced around existing section containers
