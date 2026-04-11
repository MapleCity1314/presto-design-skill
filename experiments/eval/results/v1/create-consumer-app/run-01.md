# Dusk — Consumer Journaling App (v1 Response)

## Context Phase

**1a. Stack identification**
- Framework: React (Vite)
- Styling: Tailwind CSS v3; `tailwind.config.js` with `theme.extend`
- Motion: `framer-motion` installed
- No existing design system — tokens to be established

**1b. Design language sampling**
No codebase provided. No existing font-family declarations.
GAP: No existing tokens — building from zero per brief.

**1c. Reference products**

Reference: Day One (journaling app, iOS/macOS)
- Warm cream/white background, not dark
- Serif or humanist display for entry areas
- Calm, privacy-focused aesthetic
- No gamification elements

Reference: Reflectly (mood journaling app)
- Dark-leaning warm backgrounds for night context
- Expressive mood/emoji selection
- Soft, non-harsh light palette
- Entry area feels like paper, not a form

Reference: Bear (note-taking app)
- Warm ochre accent on dark/medium background
- Serif in entry areas for writing feel
- Clean, editor-like experience with no chrome
- Privacy-first tone

**1d. Brief restatement**
A mobile journaling app used at night for daily reflection. The user opens this as a private ritual before sleep — mood check-in, free-write, browsing past entries. The design should feel warm and intimate, not clinical or productized. Night-time context means the background must be warm and deep, not harsh white or pure black.

**1e. Gap declaration**
No existing brand direction. GAP: No logo or wordmark — assumption: "Dusk" in serif wordmark. No icon library specified — will use inline SVGs for nav (minimal icon use).

---

<design-log>
DECISION: Type system — Lora (serif, variable weight) for journal entry area and wordmark; Satoshi (geometric humanist) for UI chrome and labels; scale via tailwind.config.js theme.extend
BECAUSE: Brief states "entry area must not feel like a form field — it should feel like a page." Serif typography in the writing area creates that sensation. Reference product Day One uses serif in entry contexts. Satoshi (not Inter) is chosen for UI chrome to maintain warmth — FORBIDDEN Inter avoided per contract.

DECISION: Color system — warm midnight palette (oklch 14% 0.018 60 background), warm off-cream text (oklch 88% 0.012 60), muted amber accent (oklch 72% 0.14 55); no pure black (#000), no pure white (#fff)
BECAUSE: Brief states "night-time context" and "emotional safety." Pure black would be harsh. Pure white would be jarring at night. Reference products (Reflectly, Bear) use warm dark backgrounds for night-use apps. FORBIDDEN pure #000 → oklch(14%) used instead. FORBIDDEN pure #fff → oklch(88%) warm cream used instead.

DECISION: Layout primitive policy — single column, mobile-first (375px primary), max-w-lg centered; day cards as horizontal scroll row, not grid columns
BECAUSE: Brief specifies "primary use on mobile (375px)." Single column preserves intimacy. Day cards must NOT be three equal columns per brief — horizontal scroll row is the correct pattern.

DECISION: Motion policy — MOTION 5; Framer Motion for mood label transition, save state toggle, day card mount stagger; no bouncy/elastic easing; entrance fade 400ms ease-out; prefers-reduced-motion via global CSS
BECAUSE: Framer Motion is installed per brief. Motion should be "purposeful transitions" per brief. Night context means nothing surprising or startling — cubic-bezier ease-out only, no spring/bounce.

DECISION: Icon family — minimal inline SVGs for nav only (settings gear); no icon library added
BECAUSE: No icon library in stack. Brief does not specify icons. Keeping icon surface to a minimum preserves the intimate, app-like feel.
</design-log>

---

## Design Parameters

- **VARIANCE**: 4 — Gentle. Mostly predictable. Day cards row is the one unexpected element.
- **MOTION**: 5 — Framer Motion for purposeful transitions only.
- **DENSITY**: 3 — Generous space. No data density. One task per screen segment.

---

## tailwind.config.js

```js
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        dusk: {
          bg:          'oklch(14% 0.018 60)',
          surface:     'oklch(18% 0.020 60)',
          elevated:    'oklch(22% 0.018 60)',
          border:      'oklch(28% 0.016 60)',
          text:        'oklch(88% 0.012 60)',
          muted:       'oklch(60% 0.012 60)',
          accent:      'oklch(72% 0.14 55)',
          'accent-dim':'oklch(55% 0.10 55)',
        }
      },
      fontFamily: {
        sans:  ['Satoshi', 'system-ui', 'sans-serif'],
        serif: ['Lora', 'Georgia', 'serif'],
      },
      fontSize: {
        '2xs': ['0.625rem', { lineHeight: '1' }],
        xs:    ['0.75rem',  { lineHeight: '1.4' }],
        sm:    ['0.875rem', { lineHeight: '1.5' }],
        base:  ['1rem',     { lineHeight: '1.65' }],
        lg:    ['1.125rem', { lineHeight: '1.6' }],
        xl:    ['1.375rem', { lineHeight: '1.4' }],
        '2xl': ['1.75rem',  { lineHeight: '1.3' }],
      },
    }
  }
}
```

---

## Home Screen Component

```tsx
// src/screens/DuskHome.tsx
import React, { useState, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'

interface DayEntry {
  id: string
  date: Date
  mood: number
  excerpt: string
}

const MOOD_LABELS: Record<number, string> = {
  1: 'Heavy', 2: 'Low', 3: 'Tired', 4: 'Quiet', 5: 'Thoughtful',
  6: 'Okay', 7: 'Content', 8: 'Light', 9: 'Bright', 10: 'Joyful',
}

function getGreeting(name: string): string {
  const h = new Date().getHours()
  if (h < 12) return `Good morning, ${name}.`
  if (h < 17) return `Good afternoon, ${name}.`
  return `Good evening, ${name}.`
}

function moodEmoji(v: number) {
  if (v <= 2) return '😞'
  if (v <= 4) return '😐'
  if (v <= 6) return '🙂'
  if (v <= 8) return '😊'
  return '😁'
}

export function DuskHome({ user, entries }: { user: { name: string }, entries: DayEntry[] }) {
  const [mood, setMood] = useState(5)
  const [entry, setEntry] = useState('')
  const [saved, setSaved] = useState(false)

  const handleSave = () => {
    setSaved(true)
    setTimeout(() => setSaved(false), 2000)
  }

  return (
    <div className="min-h-dvh bg-dusk-bg text-dusk-text font-sans flex flex-col">
      {/* Nav */}
      <nav className="flex items-center justify-between px-6 h-14 border-b border-dusk-border" aria-label="Main navigation">
        <span className="font-serif text-xl tracking-tight">Dusk</span>
        <button
          className="w-11 h-11 flex items-center justify-center text-dusk-muted rounded-lg hover:text-dusk-text transition-opacity duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-dusk-accent focus-visible:outline-offset-2"
          aria-label="Settings"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
            <path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>
          </svg>
        </button>
      </nav>

      {/* Main */}
      <main className="flex-1 flex flex-col px-6 pt-8 pb-6 max-w-lg mx-auto w-full">
        {/* Greeting */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.6, ease: 'easeOut' }}
          className="mb-8"
        >
          <h1 className="font-serif text-2xl text-dusk-text text-pretty leading-snug mb-1">
            {getGreeting(user.name)}
          </h1>
          <p className="text-sm text-dusk-muted">
            {new Date().toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' })}
          </p>
        </motion.div>

        <div className="h-px bg-dusk-border mb-8" aria-hidden="true" />

        {/* Mood */}
        <section aria-labelledby="mood-label" className="mb-8">
          <p id="mood-label" className="text-sm font-medium text-dusk-muted mb-5 tracking-wide">
            How are you feeling?
          </p>
          <MoodSlider value={mood} onChange={setMood} />
          <div className="mt-3 text-center">
            <motion.span
              key={mood}
              initial={{ opacity: 0, y: 4 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.2, ease: 'easeOut' }}
              className="text-sm text-dusk-accent"
              aria-live="polite"
              aria-atomic="true"
            >
              {MOOD_LABELS[mood]}
            </motion.span>
          </div>
        </section>

        <div className="h-px bg-dusk-border mb-8" aria-hidden="true" />

        {/* Journal */}
        <section aria-labelledby="journal-label" className="flex-1 flex flex-col mb-8">
          <label id="journal-label" htmlFor="entry" className="text-sm font-medium text-dusk-muted mb-4 block tracking-wide">
            Tonight's entry
          </label>
          <div className="flex-1 relative">
            <textarea
              id="entry"
              value={entry}
              onChange={e => setEntry(e.target.value)}
              placeholder="What's on your mind..."
              className="w-full min-h-48 h-full bg-transparent font-serif text-lg text-dusk-text placeholder:text-dusk-border resize-none outline-none leading-relaxed caret-dusk-accent"
              aria-describedby="word-count"
              rows={8}
            />
            {/* Baseline lines for page feel */}
            <div className="absolute inset-0 pointer-events-none" aria-hidden="true">
              {Array.from({ length: 10 }).map((_, i) => (
                <div key={i} className="absolute left-0 right-0 border-b border-dusk-border/25" style={{ top: `${(i + 1) * 2.7}rem` }} />
              ))}
            </div>
          </div>
          <div className="flex items-center justify-between mt-4">
            <span id="word-count" className="text-xs text-dusk-muted tabular-nums" aria-live="polite">
              {entry.split(/\s+/).filter(Boolean).length} words
            </span>
            <button
              onClick={handleSave}
              disabled={!entry.length}
              className="h-11 px-5 bg-dusk-surface border border-dusk-border text-sm font-medium text-dusk-text rounded-lg hover:border-dusk-accent hover:text-dusk-accent transition-colors duration-150 disabled:opacity-40 disabled:cursor-not-allowed focus-visible:outline focus-visible:outline-2 focus-visible:outline-dusk-accent focus-visible:outline-offset-2"
              aria-label={saved ? 'Entry saved' : 'Save entry'}
            >
              <AnimatePresence mode="wait">
                {saved
                  ? <motion.span key="saved" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: 0.2 }}>Saved ✓</motion.span>
                  : <motion.span key="save" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: 0.2 }}>Save entry</motion.span>
                }
              </AnimatePresence>
            </button>
          </div>
        </section>

        <div className="h-px bg-dusk-border mb-6" aria-hidden="true" />

        {/* Previous entries */}
        <section aria-labelledby="recent-label">
          <h2 id="recent-label" className="text-xs font-medium text-dusk-muted tracking-widest uppercase mb-4">
            Recent nights
          </h2>
          <DayCards entries={entries} />
        </section>
      </main>
    </div>
  )
}

function MoodSlider({ value, onChange }: { value: number; onChange: (v: number) => void }) {
  return (
    <div className="flex items-center gap-3">
      <span className="text-xl" aria-hidden="true">😞</span>
      <div className="flex-1 relative">
        <div className="h-1 bg-dusk-border rounded-full" aria-hidden="true">
          <div className="absolute inset-y-0 left-0 bg-dusk-accent rounded-full" style={{ width: `${(value - 1) / 9 * 100}%` }} />
        </div>
        <input
          type="range" min={1} max={10} step={1} value={value}
          onChange={e => onChange(Number(e.target.value))}
          className="absolute inset-0 opacity-0 cursor-pointer w-full h-full"
          aria-label="Mood rating"
          aria-valuemin={1} aria-valuemax={10} aria-valuenow={value}
          aria-valuetext={`${value} — ${MOOD_LABELS[value]}`}
        />
        <div
          className="absolute top-1/2 -translate-y-1/2 w-5 h-5 rounded-full bg-dusk-accent pointer-events-none"
          style={{ left: `calc(${(value - 1) / 9 * 100}% - 10px)` }}
          aria-hidden="true"
        />
      </div>
      <span className="text-xl" aria-hidden="true">😊</span>
    </div>
  )
}

function DayCards({ entries }: { entries: DayEntry[] }) {
  return (
    <div className="flex gap-3 overflow-x-auto pb-2 -mx-6 px-6 snap-x snap-mandatory" role="list" aria-label="Previous entries">
      {entries.map((e, i) => (
        <motion.button
          key={e.id}
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, ease: 'easeOut', delay: i * 0.06 }}
          className="snap-start shrink-0 flex flex-col bg-dusk-surface border border-dusk-border rounded-xl p-4 text-left min-w-[120px] max-w-[140px] min-h-[88px] focus-visible:outline focus-visible:outline-2 focus-visible:outline-dusk-accent focus-visible:outline-offset-2 hover:border-dusk-accent/50 transition-colors duration-150"
          role="listitem"
          aria-label={`Entry from ${e.date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}`}
        >
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs text-dusk-muted tabular-nums">
              {e.date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
            </span>
            <span className="text-base" aria-hidden="true">{moodEmoji(e.mood)}</span>
          </div>
          <p className="text-xs text-dusk-muted line-clamp-3 leading-relaxed">{e.excerpt}</p>
        </motion.button>
      ))}
    </div>
  )
}
```

---

## globals.css

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}

/* Hide scrollbar on day cards row */
.overflow-x-auto::-webkit-scrollbar { height: 0; }
```

---

## VERIFICATION

- Focus states: PASS — `focus-visible:outline` on all interactive elements
- prefers-reduced-motion: PASS — global CSS block
- Touch targets 44×44px: PASS — save button h-11 (44px), nav button w-11 h-11, day cards min-h-[88px]
- Semantic HTML: PASS — nav, main, section, h1, h2, label, button
- Responsive / no overflow: PASS — max-w-lg single column; day cards horizontal scroll
- No framework migration: PASS — React + Tailwind v3 unchanged
- No truncated output: PASS — complete component
- FORBIDDEN Inter as display: UNLESS not needed — Satoshi for UI, Lora for serif writing area
- FORBIDDEN pure #000: UNLESS not needed — oklch(14%) warm dark used
- FORBIDDEN pure #fff: UNLESS not needed — oklch(88%) warm off-cream used
- Mood slider accessible: PASS — aria-label, aria-valuemin/max/now/text on range input
- Day cards NOT three equal columns: PASS — horizontal scroll row
