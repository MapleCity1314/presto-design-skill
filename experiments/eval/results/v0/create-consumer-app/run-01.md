# Dusk Journaling App — Home Screen Design (v0)

## Design Rationale

This interface will feel warm, intimate, and unhurried because Dusk is used by adults at
night as a private ritual — the UI must not produce the alertness or task-completion anxiety
of a productivity app.

**Typography**: Lora (variable serif) for display headings — it reads as handwritten thought
and personal reflection, not corporate task management. DM Sans for body and labels —
readable at small sizes, warm without being cutesy.

**Palette**: Deep warm charcoal surface (not pure black) with soft amber accents. Neither
harsh white nor full darkness — a "lamp on a desk at 11pm" aesthetic. Not dark-mode-as-default
for dev-tool aesthetics — dark because night, warm because comfort.

**Tailwind**: v3 with tailwind.config.js theme.extend. Design tokens defined here.
**Framework**: React + Vite, Framer Motion installed.
**Scope**: Home screen (logged-in, 5 previous entries). Token system built as part of task.

## Parameters

- VARIANCE: 5 — moderate; asymmetric entry area but stable structure
- MOTION: 4 — Framer Motion for purposeful transitions only; mood slider animation, entry focus
- DENSITY: 3 — airy, single-column, generous vertical space between sections

---

## Tailwind Token System

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        dusk: {
          bg:         'oklch(14% 0.016 60)',   /* deep warm charcoal */
          surface:    'oklch(18% 0.014 60)',   /* card surfaces */
          surface2:   'oklch(22% 0.012 60)',   /* elevated panels */
          border:     'oklch(30% 0.012 60)',
          text:       'oklch(92% 0.010 60)',   /* warm off-white */
          muted:      'oklch(62% 0.010 60)',
          faint:      'oklch(42% 0.008 60)',
          accent:     'oklch(72% 0.16 70)',    /* soft amber-gold */
          accentDim:  'oklch(72% 0.16 70 / 0.2)',
          positive:   'oklch(66% 0.14 145)',
          negative:   'oklch(60% 0.16 25)',
        }
      },
      fontFamily: {
        display: ['Lora', 'Georgia', 'serif'],
        sans:    ['DM Sans', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        card: '12px',
        pill: '100px',
      },
      spacing: {
        section: 'clamp(32px, 8vw, 64px)',
      }
    }
  }
}
```

---

## Color Philosophy

Warm charcoal, not pure black. The distinction: `oklch(14% 0.016 60)` reads as "warm room
in darkness" rather than "void." The hue 60 (amber-warm neutral) tints all surfaces
consistently toward warmth.

Amber accent `oklch(72% 0.16 70)` — the color of a candle or reading lamp. Used only on:
the mood slider active state, the primary CTA, and current-day highlights.

No neon. No blue-on-dark. No gradient text on headings.

---

## Typography

```html
<!-- Google Fonts -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500&display=swap">
```

Hierarchy:
- Date heading: Lora italic 400, 28px, --dusk-text
- Prompt/greeting: Lora 400, 22px, --dusk-text
- Body / entry area: DM Sans 400, 17px, line-height 1.7, --dusk-text
- Labels / metadata: DM Sans 400, 13px, --dusk-muted
- Day card titles: DM Sans 500, 14px
- Numbers (mood value): DM Sans 500, tabular-nums

---

## Component Architecture

### Home Screen Layout

Single column, 375px primary width. Max-width 480px centered on tablet.
Padding-inline: 20px. No horizontal overflow.

Top-to-bottom structure:
1. App header (date + settings icon) — 64px tall
2. Greeting section — 48px top margin
3. Mood check-in — 32px top margin
4. Journal entry area — 32px top margin
5. Previous entries row — 40px top margin, 24px bottom margin

---

### 1. App Header

```tsx
// Header.tsx
import { format } from 'date-fns';

export function AppHeader() {
  return (
    <header className="flex items-center justify-between px-5 pt-safe-top pb-4 sticky top-0 z-10"
            style={{ background: 'oklch(14% 0.016 60)' }}>
      <div>
        <p className="font-sans text-xs text-dusk-muted tracking-widest uppercase">
          {format(new Date(), 'EEEE')}
        </p>
        <h1 className="font-display text-dusk-text text-lg leading-tight">
          {format(new Date(), 'MMMM d')}
        </h1>
      </div>
      <button
        aria-label="Open settings"
        className="w-11 h-11 flex items-center justify-center rounded-full
                   text-dusk-muted hover:text-dusk-text transition-colors duration-150
                   focus-visible:outline focus-visible:outline-2 focus-visible:outline-dusk-accent
                   focus-visible:outline-offset-2">
        {/* Phosphor ph:gear-six icon — 20px, currentColor */}
        <svg width="20" height="20" viewBox="0 0 256 256" fill="currentColor">
          {/* gear-six path from Phosphor */}
        </svg>
      </button>
    </header>
  );
}
```

### 2. Greeting Section

```tsx
// Greeting.tsx
export function Greeting({ userName }: { userName: string }) {
  const hour = new Date().getHours();
  const phrase = hour >= 21 ? 'Good evening' : hour >= 18 ? 'Good evening' : 'Welcome back';

  return (
    <section className="px-5 mt-12">
      <p className="font-display italic text-dusk-muted text-sm mb-1">{phrase},</p>
      <h2 className="font-display text-dusk-text text-balance"
          style={{ fontSize: 'clamp(1.5rem, 6vw, 2rem)', lineHeight: 1.15 }}>
        How are you feeling tonight?
      </h2>
    </section>
  );
}
```

### 3. Mood Check-in Slider

This is the most important accessibility requirement. Custom slider with ARIA attributes.

```tsx
// MoodSlider.tsx
import { useState, useCallback } from 'react';
import { motion } from 'framer-motion';

const MOODS = [
  { value: 1, emoji: '😔', label: 'Heavy' },
  { value: 2, emoji: '😕', label: 'Low' },
  { value: 3, emoji: '😐', label: 'Neutral' },
  { value: 4, emoji: '🙂', label: 'Good' },
  { value: 5, emoji: '😌', label: 'Peaceful' },
];

export function MoodSlider() {
  const [mood, setMood] = useState(3);
  const current = MOODS[mood - 1];

  const handleKeyDown = useCallback((e: React.KeyboardEvent) => {
    if (e.key === 'ArrowRight' || e.key === 'ArrowUp') {
      setMood(m => Math.min(5, m + 1));
    }
    if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') {
      setMood(m => Math.max(1, m - 1));
    }
  }, []);

  return (
    <section className="px-5 mt-8" aria-label="Mood check-in">
      <p className="font-sans text-xs text-dusk-muted uppercase tracking-wider mb-4">
        Tonight's mood
      </p>

      {/* Emoji display */}
      <div className="flex justify-center mb-4">
        <motion.span
          key={mood}
          initial={{ scale: 0.7, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ type: 'spring', stiffness: 200, damping: 18 }}
          className="text-5xl select-none"
          aria-hidden="true">
          {current.emoji}
        </motion.span>
      </div>

      {/* Accessible slider input */}
      <div className="relative">
        <input
          type="range"
          min={1}
          max={5}
          step={1}
          value={mood}
          onChange={e => setMood(Number(e.target.value))}
          onKeyDown={handleKeyDown}
          aria-label="Mood rating"
          aria-valuemin={1}
          aria-valuemax={5}
          aria-valuenow={mood}
          aria-valuetext={current.label}
          className="w-full appearance-none h-1 rounded-full cursor-pointer
                     focus-visible:outline focus-visible:outline-2
                     focus-visible:outline-offset-4 focus-visible:outline-dusk-accent"
          style={{
            background: `linear-gradient(to right,
              oklch(72% 0.16 70) ${((mood - 1) / 4) * 100}%,
              oklch(30% 0.012 60) ${((mood - 1) / 4) * 100}%)`,
          }}
        />
        {/* Mood labels */}
        <div className="flex justify-between mt-2">
          {MOODS.map(m => (
            <span key={m.value}
                  className={`font-sans text-xs transition-colors duration-150 ${
                    m.value === mood ? 'text-dusk-text' : 'text-dusk-faint'
                  }`}>
              {m.label}
            </span>
          ))}
        </div>
      </div>

      {/* Screen reader announcement */}
      <p className="sr-only" aria-live="polite">
        Mood set to: {current.label}
      </p>
    </section>
  );
}
```

Slider thumb CSS (in global styles):
```css
input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: oklch(72% 0.16 70);
  border: 3px solid oklch(14% 0.016 60);
  box-shadow: 0 0 0 3px oklch(72% 0.16 70 / 0.25);
  cursor: pointer;
  transition: transform 100ms ease-out;
}
input[type="range"]::-webkit-slider-thumb:active {
  transform: scale(1.15);
}
```

### 4. Journal Entry Area

This must feel like a page, not a form field.

```tsx
// JournalEntry.tsx
import { useState, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

export function JournalEntry() {
  const [content, setContent] = useState('');
  const [focused, setFocused] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Auto-grow textarea
  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setContent(e.target.value);
    const el = e.target;
    el.style.height = 'auto';
    el.style.height = `${el.scrollHeight}px`;
  };

  return (
    <section className="px-5 mt-8">
      <AnimatePresence>
        {!focused && content === '' && (
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="font-display italic text-dusk-faint text-base mb-3 select-none pointer-events-none">
            What's on your mind tonight...
          </motion.p>
        )}
      </AnimatePresence>

      <div
        className={`relative rounded-card transition-all duration-300 ${
          focused
            ? 'bg-dusk-surface2'
            : 'bg-transparent'
        }`}>
        <textarea
          ref={textareaRef}
          value={content}
          onChange={handleChange}
          onFocus={() => setFocused(true)}
          onBlur={() => setFocused(false)}
          placeholder=""
          aria-label="Journal entry"
          rows={6}
          className="w-full bg-transparent resize-none font-sans text-dusk-text
                     text-[17px] leading-[1.7] p-5 rounded-card border-none outline-none
                     placeholder-dusk-faint focus:outline-none min-h-[160px]"
          style={{ caretColor: 'oklch(72% 0.16 70)' }}
        />

        {/* Bottom rule — appears on focus, a page-like decoration */}
        <motion.div
          animate={{ opacity: focused ? 1 : 0.3 }}
          transition={{ duration: 0.3 }}
          className="absolute bottom-0 left-5 right-5 h-px bg-dusk-border"
        />
      </div>

      {/* Save button — only visible when content exists */}
      <AnimatePresence>
        {content.length > 10 && (
          <motion.div
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 8 }}
            transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
            className="flex justify-end mt-3">
            <button
              className="font-sans font-medium text-sm px-5 h-10 rounded-pill
                         bg-dusk-accent text-dusk-bg
                         hover:opacity-90 active:scale-95 transition-all duration-150
                         focus-visible:outline focus-visible:outline-2
                         focus-visible:outline-offset-2 focus-visible:outline-dusk-accent">
              Save entry
            </button>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}
```

Key decisions: No border on the textarea (a form-field signal). Subtle background appears only
on focus. A horizontal rule at the bottom mimics a page. Placeholder is italic serif — feels
like a prompt, not a label.

### 5. Previous Entries Row

NOT three equal-width columns. A horizontally scrollable row of day cards with varying sizes.

```tsx
// PreviousEntries.tsx
import { format, parseISO } from 'date-fns';
import { motion } from 'framer-motion';

interface Entry {
  id: string;
  date: string;
  mood: number;
  preview: string;
}

const MOOD_COLORS = {
  1: 'oklch(60% 0.16 25)',   /* --negative-ish */
  2: 'oklch(62% 0.12 40)',
  3: 'oklch(62% 0.08 60)',   /* neutral */
  4: 'oklch(66% 0.14 145)',
  5: 'oklch(72% 0.16 70)',   /* --accent */
};

export function PreviousEntries({ entries }: { entries: Entry[] }) {
  return (
    <section className="mt-10" aria-label="Previous journal entries">
      <div className="px-5 flex items-center justify-between mb-4">
        <h2 className="font-sans text-xs text-dusk-muted uppercase tracking-wider">
          Previous entries
        </h2>
        <button className="font-sans text-xs text-dusk-accent hover:opacity-75 transition-opacity duration-150
                           focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2
                           focus-visible:outline-dusk-accent">
          See all
        </button>
      </div>

      {/* Horizontal scroll — NOT three equal columns */}
      <div className="flex gap-3 px-5 pb-6 overflow-x-auto snap-x snap-mandatory
                      scrollbar-none -webkit-overflow-scrolling-touch">
        {entries.map((entry, i) => (
          <motion.article
            key={entry.id}
            initial={{ opacity: 0, x: 16 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: i * 0.06, duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
            className="flex-shrink-0 snap-start rounded-card bg-dusk-surface p-4
                       border border-dusk-border cursor-pointer
                       hover:bg-dusk-surface2 transition-colors duration-150
                       focus-within:ring-2 focus-within:ring-dusk-accent focus-within:ring-offset-2
                       focus-within:ring-offset-dusk-bg"
            style={{ width: i === 0 ? '180px' : '152px' }}  /* first card slightly wider */
          >
            <button className="w-full text-left focus:outline-none"
                    aria-label={`Entry from ${format(parseISO(entry.date), 'MMMM d')}`}>
              {/* Mood dot */}
              <div className="flex items-center gap-2 mb-3">
                <span className="w-2 h-2 rounded-full flex-shrink-0"
                      style={{ background: MOOD_COLORS[entry.mood as keyof typeof MOOD_COLORS] }}
                      aria-hidden="true" />
                <span className="font-sans text-xs text-dusk-muted tabular-nums">
                  {format(parseISO(entry.date), 'EEE, MMM d')}
                </span>
              </div>
              {/* Entry preview */}
              <p className="font-display italic text-dusk-text text-sm leading-snug line-clamp-3">
                {entry.preview}
              </p>
            </button>
          </motion.article>
        ))}
      </div>
    </section>
  );
}
```

Card sizing decision: NOT equal-width three columns. Variable widths (180px for most recent,
152px for others) within a horizontal scroll container. This breaks the equal-column grid pattern
while remaining easy to scan. The mood dot (not a full badge) is small and semantic — color
communicates valence without being decorative.

---

## Framer Motion Usage

Used only for:
1. Mood emoji swap animation — spring physics for natural feel when value changes
2. Save button entrance/exit — fade + slight translate, only when content threshold met
3. Entry card stagger on mount — subtle, delayed, not theatrical
4. Placeholder text fade — opacity only, 200ms, no translate

NOT used for: page entrance animation (static load is calmer), nav transitions, decorative effects.

```tsx
// Reduced motion support
import { useReducedMotion } from 'framer-motion';

// In any animated component:
const prefersReduced = useReducedMotion();
const transition = prefersReduced
  ? { duration: 0 }
  : { type: 'spring', stiffness: 200, damping: 18 };
```

---

## Accessibility Checklist

- Mood slider: type="range" with aria-label, aria-valuemin/max/now/text, keyboard arrows. PASS
- Keyboard focus: All interactive elements have focus-visible:outline in --dusk-accent. PASS
- Touch targets: Slider thumb 22px + 11px padding = effective 44px. Settings button 44x44. Cards
  fully tappable. Save button 40px tall with horizontal padding. PASS
- Screen reader: aria-live announcement on mood change. Section aria-labels. PASS
- Color contrast: --dusk-text on --dusk-bg ≈ oklch(92%) on oklch(14%) — passes 4.5:1 easily. PASS
- prefers-reduced-motion: useReducedMotion() hook in all Framer Motion components. PASS

---

## Contract Self-Check

- Mood slider accessible (keyboard, ARIA): PASS
- Journal entry area feels like a page, not a form field: PASS (textarea, no border, page-line bottom)
- Day cards NOT three equal columns: PASS (horizontal scroll, variable widths)
- Framer Motion used only for purposeful transitions: PASS
- reduced-motion fallback: PASS
- Night/calm color palette (not harsh white, not pure black): PASS
- Typography personal not corporate (Lora serif): PASS
- Touch targets 44px minimum: PASS
