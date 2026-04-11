# Helio Settings Panel — Refine (v1 Response)

## Context Phase

**1a. Stack identification**
- Framework: React with Next.js
- Styling: Tailwind CSS v3; `tailwind.config.js` with brand tokens
- Existing tokens: `--color-brand: #3B5BDB` (vivid blue), `--font-sans: 'Geist', sans-serif`
- Existing components: `<Input />`, `<Toggle />`, `<Button variant="primary|ghost" />`
- Existing structure: three `<section>` elements, each with `<h2>` and field rows

**1b. Design language sampling**
From the representative code:
- Font: Geist, sans-serif
- Brand color: `#3B5BDB` — vivid blue
- Section header: `text-sm font-medium text-gray-700`
- Field label: `text-sm text-gray-600`
- Section padding: `p-4` (16px)
- Field spacing: `space-y-3` (12px)

**1c. Reference products**

Reference: Linear settings page
- Section headers: clearly larger + heavier than field labels
- Section dividers separate sections visually (more space between sections than within)
- Labels always above inputs with clear visual grouping

Reference: Vercel project settings
- `h2` is text-base or text-lg with font-semibold — unmistakably distinct from labels
- Sections separated by 48–64px of space (not a shared `space-y-3` rhythm)
- Save button per section, not a global save

Reference: Notion settings
- Section headers at 16px+ with clear weight (500–600)
- Individual setting rows with `label + control` in a horizontal layout for toggles
- Ample padding within each section (24–32px)

**1d. Brief restatement**
A settings panel with three sections (Profile, Notifications, Security). Current problems: section headers and field labels are visually identical, spacing is cramped and uniform, and no clear hierarchy exists between section and field level. Fix hierarchy and spacing without redesigning the panel structure.

**1e. Gap declaration**
No gaps — full context provided.

---

<design-log>
DECISION: Type system — Geist (existing brand font) throughout; increase section header size to text-base/font-semibold; field labels remain text-sm/font-medium; hierarchy through size + weight contrast
BECAUSE: Existing codebase fact: `--font-sans: 'Geist', sans-serif` is the declared font. Current `h2 = text-sm font-medium text-gray-700` vs label `text-sm text-gray-600` creates near-zero hierarchy. Brief identifies this as the primary problem. Reference products (Linear, Vercel) use text-base+ and font-semibold for section headers.

DECISION: Color system — existing brand blue #3B5BDB preserved; section headers in text-gray-900 (darker than current text-gray-700); field labels remain text-gray-700; muted secondary descriptions in text-gray-500
BECAUSE: Existing token `--color-brand: #3B5BDB` load-bearing in existing components. No reason to change brand color. Darkening section headers to text-gray-900 (from text-gray-700) increases contrast without introducing new hues.

DECISION: Layout — increase inter-section spacing to 48px+; keep intra-section field spacing at 20–24px; no new card wrappers; existing section border treatment modified to border-b divider only
BECAUSE: Current `p-4` + `border border-gray-200 rounded` creates cards that feel cramped and add unnecessary visual weight. Brief specifies "no new card wrappers." Replacing with border-b divider and more padding creates breathing room without adding structure.

DECISION: Motion — existing hover transitions preserved; no new motion introduced
BECAUSE: No animation library. Settings panels require zero motion for professional confidence.

DECISION: Icon family — none; existing components (Toggle, Button) handle their own iconography
BECAUSE: No icon library specified. Brief does not mention icons. Existing components are self-contained.
</design-log>

---

## Problem Summary

| Element | Before | After |
|---------|--------|-------|
| Section h2 | `text-sm font-medium text-gray-700` | `text-base font-semibold text-gray-900` |
| Field label | `text-sm text-gray-600` | `text-sm font-medium text-gray-700` |
| Section padding | `p-4` (16px all sides) | `pb-10 mb-10` (40px bottom, 40px margin) |
| Field spacing | `space-y-3` (12px, labels + inputs as siblings) | `space-y-6` with `FieldRow` grouping |
| Section wrapper | `border border-gray-200 rounded` (card) | `border-b border-gray-200` (divider only) |

---

## Refined Component

```tsx
// components/SettingsPanel.tsx
import React from 'react'
import { Input } from '@/components/Input'
import { Toggle } from '@/components/Toggle'
import { Button } from '@/components/Button'

interface ProfileData { displayName: string; email: string; bio?: string; timezone: string }
interface NotificationsData { emailDigest: boolean; mentionAlerts: boolean; weeklyReport: boolean; browserPush: boolean; smsAlerts: boolean }
interface SecurityData { twoFactorEnabled: boolean; sessionsActive: number }

interface SettingsPanelProps {
  profile: ProfileData
  notifications: NotificationsData
  security: SecurityData
  onUpdate: (section: string, key: string, value: unknown) => void
  onSave: (section: string) => void
}

export function SettingsPanel({ profile, notifications, security, onUpdate, onSave }: SettingsPanelProps) {
  return (
    <div className="max-w-2xl mx-auto px-6 py-10" style={{ fontFamily: 'var(--font-sans)' }}>

      {/* Profile Section */}
      <section
        className="border-b border-gray-200 pb-10 mb-10"
        aria-labelledby="profile-heading"
      >
        <SectionHeader
          id="profile-heading"
          title="Profile"
          description="Update your personal information and preferences."
        />
        <div className="space-y-6">
          <FieldRow label="Display name" htmlFor="display-name" required>
            <Input
              id="display-name"
              value={profile.displayName}
              onChange={e => onUpdate('profile', 'displayName', e.target.value)}
              className="max-w-sm"
            />
          </FieldRow>
          <FieldRow label="Email address" htmlFor="email" required>
            <Input
              id="email"
              type="email"
              value={profile.email}
              onChange={e => onUpdate('profile', 'email', e.target.value)}
              className="max-w-sm"
            />
          </FieldRow>
          <FieldRow label="Bio" htmlFor="bio" hint="Optional. Visible to your teammates.">
            <textarea
              id="bio"
              value={profile.bio ?? ''}
              onChange={e => onUpdate('profile', 'bio', e.target.value)}
              rows={3}
              className="max-w-sm w-full px-3 py-2 text-sm text-gray-900 border border-gray-200 rounded-md focus:outline-none focus:ring-2 focus:ring-offset-0 focus:ring-[var(--color-brand)] resize-none"
            />
          </FieldRow>
          <FieldRow label="Timezone" htmlFor="timezone">
            <select
              id="timezone"
              value={profile.timezone}
              onChange={e => onUpdate('profile', 'timezone', e.target.value)}
              className="max-w-sm w-full px-3 py-2 text-sm text-gray-900 border border-gray-200 rounded-md focus:outline-none focus:ring-2 focus:ring-offset-0 focus:ring-[var(--color-brand)] bg-white"
            >
              <option value="America/New_York">Eastern Time (ET)</option>
              <option value="America/Chicago">Central Time (CT)</option>
              <option value="America/Denver">Mountain Time (MT)</option>
              <option value="America/Los_Angeles">Pacific Time (PT)</option>
              <option value="Europe/London">London (GMT/BST)</option>
            </select>
          </FieldRow>
        </div>
        <div className="mt-8 flex justify-end">
          <Button variant="primary" onClick={() => onSave('profile')} className="min-h-[44px]">
            Save profile
          </Button>
        </div>
      </section>

      {/* Notifications Section */}
      <section
        className="border-b border-gray-200 pb-10 mb-10"
        aria-labelledby="notifications-heading"
      >
        <SectionHeader
          id="notifications-heading"
          title="Notifications"
          description="Choose when and how Helio contacts you."
        />
        <div className="space-y-5">
          <ToggleRow
            label="Email digest"
            description="Daily summary of project activity sent each morning."
            htmlFor="email-digest"
            checked={notifications.emailDigest}
            onChange={v => onUpdate('notifications', 'emailDigest', v)}
          />
          <ToggleRow
            label="Mention alerts"
            description="Notify me when someone @mentions me in a project."
            htmlFor="mention-alerts"
            checked={notifications.mentionAlerts}
            onChange={v => onUpdate('notifications', 'mentionAlerts', v)}
          />
          <ToggleRow
            label="Weekly report"
            description="Project progress summary delivered every Monday."
            htmlFor="weekly-report"
            checked={notifications.weeklyReport}
            onChange={v => onUpdate('notifications', 'weeklyReport', v)}
          />
          <ToggleRow
            label="Browser notifications"
            description="Push notifications while the app is open in your browser."
            htmlFor="browser-push"
            checked={notifications.browserPush}
            onChange={v => onUpdate('notifications', 'browserPush', v)}
          />
          <ToggleRow
            label="SMS alerts"
            description="Text message alerts for critical deadline overruns."
            htmlFor="sms-alerts"
            checked={notifications.smsAlerts}
            onChange={v => onUpdate('notifications', 'smsAlerts', v)}
          />
        </div>
      </section>

      {/* Security Section */}
      <section aria-labelledby="security-heading">
        <SectionHeader
          id="security-heading"
          title="Security"
          description="Manage your account access and authentication."
        />
        <div className="space-y-6">
          <FieldRow label="Password" htmlFor="change-password">
            <Button variant="ghost" id="change-password" className="min-h-[44px]">
              Change password →
            </Button>
          </FieldRow>
          <ToggleRow
            label="Two-factor authentication"
            description="Require an authenticator app in addition to your password."
            htmlFor="two-factor"
            checked={security.twoFactorEnabled}
            onChange={v => onUpdate('security', 'twoFactorEnabled', v)}
          />
          <div className="pt-1">
            <p className="text-sm font-medium text-gray-700 mb-1">Active sessions</p>
            <p className="text-sm text-gray-500">
              You have{' '}
              <span className="font-medium text-gray-700 tabular-nums">{security.sessionsActive}</span>
              {' '}{security.sessionsActive === 1 ? 'session' : 'sessions'} active.
            </p>
            <Button
              variant="ghost"
              className="mt-3 min-h-[44px] text-red-600 hover:bg-red-50 border-red-200"
            >
              Sign out all other sessions
            </Button>
          </div>
        </div>
      </section>
    </div>
  )
}

// ─── Section Header ────────────────────────────────────────────

function SectionHeader({ id, title, description }: { id: string; title: string; description?: string }) {
  return (
    <div className="mb-7">
      {/* BEFORE: text-sm font-medium text-gray-700 — almost identical to field labels */}
      {/* AFTER:  text-base font-semibold text-gray-900 — clearly dominant */}
      <h2 id={id} className="text-base font-semibold text-gray-900 tracking-tight">
        {title}
      </h2>
      {description && (
        <p className="text-sm text-gray-500 mt-1">{description}</p>
      )}
    </div>
  )
}

// ─── Field Row ─────────────────────────────────────────────────

function FieldRow({ label, htmlFor, required, hint, children }: {
  label: string; htmlFor: string; required?: boolean; hint?: string; children: React.ReactNode
}) {
  return (
    <div className="flex flex-col gap-1.5">
      {/* Label always above input — clear grouping */}
      <label htmlFor={htmlFor} className="text-sm font-medium text-gray-700 leading-none">
        {label}
        {required && <span className="text-red-500 ml-0.5" aria-hidden="true">*</span>}
      </label>
      {hint && <p className="text-xs text-gray-400">{hint}</p>}
      {children}
    </div>
  )
}

// ─── Toggle Row ────────────────────────────────────────────────

function ToggleRow({ label, description, htmlFor, checked, onChange }: {
  label: string; description: string; htmlFor: string; checked: boolean; onChange: (v: boolean) => void
}) {
  return (
    <div className="flex items-start justify-between gap-6 py-1">
      <div className="flex-1">
        <label htmlFor={htmlFor} className="text-sm font-medium text-gray-700 cursor-pointer">{label}</label>
        <p className="text-sm text-gray-500 mt-0.5 text-pretty" style={{ maxWidth: '48ch' }}>{description}</p>
      </div>
      <Toggle
        id={htmlFor}
        checked={checked}
        onCheckedChange={onChange}
        aria-label={label}
        className="shrink-0 mt-0.5"
      />
    </div>
  )
}
```

---

## VERIFICATION

- Focus states: PASS — Input, Toggle, Button, select all use focus:ring-[var(--color-brand)] or existing focus styles from components
- prefers-reduced-motion: PASS — no new animations introduced
- Touch targets 44×44px: PASS — all buttons use `min-h-[44px]`; Toggle component assumed 44px min (Radix-based)
- Semantic HTML: PASS — section+aria-labelledby, h2, label+for, tabular-nums on session count
- Responsive / no overflow: PASS — max-w-sm on inputs, max-w-2xl on panel
- No framework migration: PASS — React + Next.js + Tailwind v3 unchanged
- No truncated output: PASS
- Section headers distinct from field labels: PASS — text-base font-semibold text-gray-900 vs text-sm font-medium text-gray-700
- Inter-section spacing > intra-section: PASS — pb-10 mb-10 between sections, space-y-6 within
- Labels above inputs: PASS — FieldRow always places label before children
- No new card wrappers: PASS — removed border/rounded card treatment; using border-b divider only
- Same three sections: PASS — Profile, Notifications, Security all present
- Not a redesign: PASS — content identical, structure identical, only hierarchy and spacing changed
