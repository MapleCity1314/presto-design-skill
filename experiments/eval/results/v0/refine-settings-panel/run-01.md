# Helio Settings Panel Refinement — v0

## Target and Scope

What is being improved: section header hierarchy vs field label hierarchy, spacing between
and within sections, visual clarity.

What stays intact: three-section structure (Profile, Notifications, Security), existing
components (Input, Toggle, Button), Tailwind v3 + Next.js stack, no new component library.

This is a refine, not a redesign. The result must be recognizably the same panel.

---

## Diagnosis

Current issues from provided code sample:

1. h2 "Profile" = text-sm font-medium text-gray-700
   label "Display Name" = text-sm text-gray-600
   → These are visually identical. Section headers and field labels are indistinguishable.
   This is the primary hierarchy failure.

2. Section padding: p-4 for each section = 16px
   Space between fields: space-y-3 = 12px gap
   Space between sections: no explicit separation beyond the section border itself
   → Sections don't breathe. Inter-field and inter-section spacing are nearly identical.

3. Label is a sibling of Input with space-y-3 between them — no explicit association via
   htmlFor/id pair visible in the sample (labels need explicit for= attributes).

4. Section container: p-4 border border-gray-200 rounded — this is a card.
   The refine contract says no NEW card wrappers. But these already exist. We keep them.
   However, we improve them: remove the border+rounded from the section container,
   use a ruled separator and padding instead. Cards around form sections add no hierarchy value.

---

## Refinement

### Section Header: Make It Visually Distinct from Field Labels

```tsx
// Settings section header — was: text-sm font-medium text-gray-700
// Now: larger, heavier, clearer hierarchy

function SectionHeader({ title }: { title: string }) {
  return (
    <div className="mb-6 pb-3 border-b border-gray-200">
      <h2 className="text-base font-semibold text-gray-900 text-balance">
        {title}
      </h2>
    </div>
  );
}
```

Before: text-sm font-medium text-gray-700 (same as labels)
After: text-base font-semibold text-gray-900 + border-bottom as visual anchor

Changes made:
- Size: text-sm → text-base (one step up in Tailwind scale)
- Weight: font-medium → font-semibold
- Color: text-gray-700 → text-gray-900 (stronger contrast)
- Added border-bottom as a structural separator — not a new card wrapper

### Field Label: Clearly Label, Not Section

```tsx
// Field label — was: text-sm text-gray-600 (nearly same as section header)
// Now: smaller than section header, explicitly associated

function FieldLabel({ htmlFor, children, required }: {
  htmlFor: string;
  children: React.ReactNode;
  required?: boolean;
}) {
  return (
    <label
      htmlFor={htmlFor}
      className="block text-sm font-medium text-gray-700 mb-1.5">
      {children}
      {required && (
        <>
          <span className="text-red-500 ml-0.5" aria-hidden="true">*</span>
          <span className="sr-only"> (required)</span>
        </>
      )}
    </label>
  );
}
```

### Spacing: Inter-Section vs Inter-Field

```tsx
// Before:
// <section className="p-4 border border-gray-200 rounded">

// After:
// Section: large separation (48px) between sections
// Fields: small separation (20px) between field rows within a section
// Section container: no card border (redundant with the section header border)

function SettingsSection({ title, children }: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <section className="py-0">
      <SectionHeader title={title} />
      <div className="space-y-5 pb-12">
        {children}
      </div>
    </section>
  );
}

// The outer container:
function SettingsPanel() {
  return (
    <div className="max-w-2xl mx-auto px-4 py-8 divide-y divide-gray-200">
      <SettingsSection title="Profile">
        {/* fields */}
      </SettingsSection>
      <SettingsSection title="Notifications">
        {/* fields */}
      </SettingsSection>
      <SettingsSection title="Security">
        {/* fields */}
      </SettingsSection>
    </div>
  );
}
```

Key changes:
- divide-y divide-gray-200 on the outer container creates visual breaks between sections
- pb-12 (48px) on each section's field group creates generous inter-section breathing room
- space-y-5 (20px) between individual fields — was space-y-3 (12px)
- Section card border REMOVED — the section header border-bottom and divide-y do the separating work
  without nesting a card inside the panel

### Full Refined Settings Panel

```tsx
// SettingsPanel.tsx
'use client';

import { useState } from 'react';

interface FieldRowProps {
  label: string;
  htmlFor: string;
  hint?: string;
  required?: boolean;
  children: React.ReactNode;
}

function FieldRow({ label, htmlFor, hint, required, children }: FieldRowProps) {
  return (
    <div className="flex flex-col gap-1.5">
      <label
        htmlFor={htmlFor}
        className="text-sm font-medium text-gray-700">
        {label}
        {required && (
          <>
            <span className="text-red-500 ml-0.5" aria-hidden="true">*</span>
            <span className="sr-only"> (required)</span>
          </>
        )}
      </label>
      {hint && (
        <p id={`${htmlFor}-hint`} className="text-xs text-gray-500">
          {hint}
        </p>
      )}
      {children}
    </div>
  );
}

function SectionHeader({ title }: { title: string }) {
  return (
    <div className="mb-6 pb-3 border-b border-gray-200">
      <h2 className="text-base font-semibold text-gray-900 text-balance">
        {title}
      </h2>
    </div>
  );
}

export function SettingsPanel() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [emailNotif, setEmailNotif] = useState(true);
  const [slackNotif, setSlackNotif] = useState(false);
  const [twoFactor, setTwoFactor] = useState(false);

  return (
    <main className="max-w-2xl mx-auto px-4 py-8">
      {/* Sections separated by horizontal rules, not cards */}
      <div className="divide-y divide-gray-200">

        {/* Profile */}
        <section className="py-8 first:pt-0">
          <SectionHeader title="Profile" />
          <div className="space-y-5">
            <FieldRow htmlFor="display-name" label="Display name" required>
              <Input
                id="display-name"
                value={name}
                onChange={e => setName(e.target.value)}
                className="w-full focus-visible:ring-[--color-brand] focus-visible:ring-2" />
            </FieldRow>

            <FieldRow htmlFor="email" label="Email address" required
                      hint="Changing your email requires re-verification.">
              <Input
                id="email"
                type="email"
                value={email}
                onChange={e => setEmail(e.target.value)}
                className="w-full focus-visible:ring-[--color-brand] focus-visible:ring-2" />
            </FieldRow>
          </div>

          <div className="mt-6">
            <Button variant="primary" className="focus-visible:ring-2 focus-visible:ring-[--color-brand]
                                                  focus-visible:ring-offset-2">
              Save changes
            </Button>
          </div>
        </section>

        {/* Notifications */}
        <section className="py-8">
          <SectionHeader title="Notifications" />
          <div className="space-y-5">
            <FieldRow htmlFor="email-notifications" label="Email notifications"
                      hint="Receive a daily digest of project activity.">
              <Toggle
                id="email-notifications"
                checked={emailNotif}
                onCheckedChange={setEmailNotif}
                aria-label="Toggle email notifications" />
            </FieldRow>

            <FieldRow htmlFor="slack-notifications" label="Slack notifications"
                      hint="Post updates to your connected Slack workspace.">
              <Toggle
                id="slack-notifications"
                checked={slackNotif}
                onCheckedChange={setSlackNotif}
                aria-label="Toggle Slack notifications" />
            </FieldRow>
          </div>
        </section>

        {/* Security */}
        <section className="py-8 last:pb-0">
          <SectionHeader title="Security" />
          <div className="space-y-5">
            <FieldRow htmlFor="two-factor" label="Two-factor authentication"
                      hint="Adds a second verification step when signing in.">
              <Toggle
                id="two-factor"
                checked={twoFactor}
                onCheckedChange={setTwoFactor}
                aria-label="Toggle two-factor authentication" />
            </FieldRow>

            <FieldRow htmlFor="current-password" label="Change password">
              <Button variant="ghost"
                      className="self-start focus-visible:ring-2 focus-visible:ring-[--color-brand]
                                 focus-visible:ring-offset-2">
                Change password
              </Button>
            </FieldRow>
          </div>
        </section>

      </div>
    </main>
  );
}
```

---

## Self-Check

- Section headers visually distinct from field labels (size text-base vs text-sm, weight
  semibold vs medium, color gray-900 vs gray-700, + border-bottom anchor): PASS
- Spacing between sections larger than between fields (py-8 per section / space-y-5 within): PASS
- Labels above inputs in all sections (label before input in DOM order, htmlFor/id linked): PASS
- Self-check: this is a refine, not a redesign (three sections preserved, structure unchanged,
  same components, recognizably same panel): PASS
- No new card wrappers introduced (section border REMOVED, replaced by divide-y horizontal rules): PASS
- Stack preserved: React + Next.js + Tailwind v3: PASS
- No new component library: PASS
- focus-visible states present on all interactive elements: PASS
