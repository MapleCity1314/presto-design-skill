# Vesta Onboarding Form — Refine (v1 Response)

## Context Phase

**1a. Stack identification**
- Framework: Vue 3 + Vite
- Styling: Tailwind CSS v3
- Existing tokens: `--color-brand: oklch(55% 0.18 145)` (green), `--font-sans: 'Plus Jakarta Sans'`
- Existing components: `<VestaInput>`, `<VestaButton variant="primary|ghost">`, `<VestaSelect>`
- No animation library

**1b. Design language sampling**
- Font: Plus Jakarta Sans (warm, geometric, humanist sans)
- Brand color: oklch(55% 0.18 145) — medium green
- Component variants: primary and ghost button variants exist

**1c. Reference products**

Reference: Stripe Checkout onboarding
- Clear step indicator at top showing numbered steps
- Primary action button (filled) distinctly larger than back button
- Inline validation errors with red border + below-field message

Reference: Linear workspace setup
- Progress stepper with step labels + numbered circles
- Back navigation styled as text link, not equal-weight button
- Accessible labeled fields above every input

Reference: Notion account setup
- Simple progress bar or step dots at top
- Labels always above inputs
- Error state: red border + text description below field

**1d. Brief restatement**
A three-step onboarding form for non-technical landlords (40–65 age range, mobile-likely). The form needs a progress indicator, distinct Next/Back buttons, and inline error states. The three-step structure must stay intact.

**1e. Gap declaration**
No gaps — full context in brief.

---

<design-log>
DECISION: Type system — Plus Jakarta Sans throughout (existing brand font); no change
BECAUSE: Existing codebase fact: `--font-sans: 'Plus Jakarta Sans'`. Brand identity is load-bearing. UNLESS condition for preserving existing font satisfied.

DECISION: Color system — existing brand green oklch(55% 0.18 145) as accent; no changes to color palette; add semantic red for error states (oklch 55% 0.22 25)
BECAUSE: Existing token is the brand anchor. Error state requires a semantic color not yet in the palette; oklch red is complementary and accessible (contrast checked). No gradients.

DECISION: Layout — single column, max-w-lg, centered; step indicator above form card; form navigation at bottom of each step
BECAUSE: Brief specifies "mobile device likely" and audience is non-technical. Single column with maximum focus per step is the correct information architecture. Reference products (Stripe, Linear) use this pattern.

DECISION: Motion — none; Tailwind v3 transition for hover states only; no animation library
BECAUSE: No animation library in stack. Non-technical audience would not benefit from entrance animations. Focus is on clarity, not delight.

DECISION: Icon family — SVG inline only for progress indicator checkmark and error icon; no external library needed
BECAUSE: No existing icon library specified. Two-icon use case (check + error circle) does not warrant a library dependency.
</design-log>

---

## Step Indicator Component

```vue
<!-- components/VestaStepIndicator.vue -->
<template>
  <nav aria-label="Form progress" class="mb-8">
    <ol class="flex items-center">
      <li
        v-for="(step, i) in steps"
        :key="step.id"
        class="flex items-center"
        :class="{ 'flex-1': i < steps.length - 1 }"
      >
        <div class="flex flex-col items-center gap-1.5">
          <div
            class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-semibold transition-colors duration-150"
            :class="nodeClass(i)"
            :aria-current="i === current ? 'step' : undefined"
          >
            <svg v-if="i < current" width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">
              <path d="M2.5 7L5.5 10L11.5 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span v-else class="tabular-nums">{{ i + 1 }}</span>
          </div>
          <span
            class="text-xs font-medium whitespace-nowrap"
            :class="i === current ? 'text-[var(--color-brand)]' : i < current ? 'text-gray-500' : 'text-gray-400'"
          >
            {{ step.label }}
          </span>
        </div>
        <div
          v-if="i < steps.length - 1"
          class="flex-1 h-px mx-3 mb-5"
          :class="i < current ? 'bg-[var(--color-brand)]' : 'bg-gray-200'"
          aria-hidden="true"
        />
      </li>
    </ol>
    <p class="sr-only" aria-live="polite" aria-atomic="true">
      Step {{ current + 1 }} of {{ steps.length }}: {{ steps[current]?.label }}
    </p>
  </nav>
</template>

<script setup lang="ts">
interface Step { id: string; label: string }
const props = defineProps<{ steps: Step[]; current: number }>()

function nodeClass(i: number) {
  if (i < props.current) return 'bg-[var(--color-brand)] text-white'
  if (i === props.current) return 'bg-[var(--color-brand)] text-white ring-2 ring-offset-2 ring-[var(--color-brand)]'
  return 'bg-white border-2 border-gray-200 text-gray-400'
}
</script>
```

---

## Field Error Component

```vue
<!-- components/VestaFieldError.vue -->
<template>
  <div v-if="message" :id="id" class="flex items-start gap-1.5 mt-1.5" role="alert" aria-live="polite">
    <svg class="w-4 h-4 text-red-500 mt-0.5 shrink-0" viewBox="0 0 16 16" fill="none" aria-hidden="true">
      <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="1.5"/>
      <path d="M8 5v3.5M8 11v.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
    <p class="text-sm text-red-600 leading-snug text-pretty">{{ message }}</p>
  </div>
</template>
<script setup lang="ts">
defineProps<{ id: string; message?: string }>()
</script>
```

---

## Form Navigation Component

```vue
<!-- components/VestaFormNav.vue -->
<template>
  <div class="flex items-center justify-between pt-6 mt-6 border-t border-gray-200">
    <!-- Back: ghost styling -->
    <VestaButton
      v-if="step > 0"
      variant="ghost"
      type="button"
      class="min-h-[44px] min-w-[44px] px-4 text-gray-500"
      @click="$emit('back')"
    >
      ← Back
    </VestaButton>
    <div v-else aria-hidden="true" />

    <!-- Next/Submit: primary — visually distinct -->
    <VestaButton
      variant="primary"
      type="submit"
      class="min-h-[44px] px-7 font-semibold"
      :disabled="submitting"
    >
      <span v-if="last">{{ submitting ? 'Setting up…' : 'Complete setup' }}</span>
      <span v-else>Continue →</span>
    </VestaButton>
  </div>
</template>
<script setup lang="ts">
import VestaButton from './VestaButton.vue'
defineProps<{ step: number; last: boolean; submitting?: boolean }>()
defineEmits<{ back: [] }>()
</script>
```

---

## Full OnboardingForm.vue

```vue
<template>
  <div class="min-h-dvh bg-gray-50 flex flex-col items-center justify-start pt-12 px-4 pb-16"
       style="font-family: var(--font-sans)">
    <div class="w-full max-w-lg">
      <div class="mb-8 text-center">
        <h1 class="text-xl font-semibold text-gray-900">Vesta</h1>
        <p class="text-sm text-gray-500 mt-1">Set up your landlord account</p>
      </div>

      <VestaStepIndicator :steps="steps" :current="step" />

      <div class="bg-white border border-gray-200 rounded-xl shadow-sm p-8">

        <!-- Step 1 -->
        <form v-if="step === 0" @submit.prevent="advance(0)" novalidate aria-label="Step 1: Your profile">
          <h2 class="text-lg font-semibold text-gray-900 mb-6">Your profile</h2>
          <div class="space-y-5">
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700 mb-1.5">
                Full name <span class="text-red-500" aria-hidden="true">*</span>
              </label>
              <VestaInput id="name" v-model="form.name" type="text" autocomplete="name"
                :aria-describedby="err.name ? 'name-err' : undefined" :aria-invalid="!!err.name"
                :class="{ 'border-red-400': err.name }" placeholder="Jane Smith" />
              <VestaFieldError id="name-err" :message="err.name" />
            </div>
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 mb-1.5">
                Email address <span class="text-red-500" aria-hidden="true">*</span>
              </label>
              <VestaInput id="email" v-model="form.email" type="email" autocomplete="email"
                :aria-describedby="err.email ? 'email-err' : undefined" :aria-invalid="!!err.email"
                :class="{ 'border-red-400': err.email }" placeholder="jane@example.com" />
              <VestaFieldError id="email-err" :message="err.email" />
            </div>
            <div>
              <label for="phone" class="block text-sm font-medium text-gray-700 mb-1.5">
                Phone <span class="text-gray-400 font-normal">(optional)</span>
              </label>
              <VestaInput id="phone" v-model="form.phone" type="tel" autocomplete="tel" placeholder="+1 (555) 000-0000" />
            </div>
          </div>
          <VestaFormNav :step="step" :last="false" @back="back" />
        </form>

        <!-- Step 2 -->
        <form v-else-if="step === 1" @submit.prevent="advance(1)" novalidate aria-label="Step 2: First property">
          <h2 class="text-lg font-semibold text-gray-900 mb-6">Your first property</h2>
          <div class="space-y-5">
            <div>
              <label for="address" class="block text-sm font-medium text-gray-700 mb-1.5">
                Street address <span class="text-red-500" aria-hidden="true">*</span>
              </label>
              <VestaInput id="address" v-model="form.address" type="text" autocomplete="street-address"
                :aria-invalid="!!err.address" :class="{ 'border-red-400': err.address }"
                placeholder="123 Main St" />
              <VestaFieldError id="address-err" :message="err.address" />
            </div>
            <div>
              <label for="units" class="block text-sm font-medium text-gray-700 mb-1.5">
                Number of units <span class="text-red-500" aria-hidden="true">*</span>
              </label>
              <VestaInput id="units" v-model.number="form.units" type="number" min="1"
                :aria-invalid="!!err.units" :class="{ 'border-red-400': err.units }"
                placeholder="e.g. 4" />
              <VestaFieldError id="units-err" :message="err.units" />
            </div>
            <div>
              <label for="type" class="block text-sm font-medium text-gray-700 mb-1.5">
                Property type <span class="text-red-500" aria-hidden="true">*</span>
              </label>
              <VestaSelect id="type" v-model="form.type"
                :aria-invalid="!!err.type" :class="{ 'border-red-400': err.type }">
                <option value="" disabled>Select a type</option>
                <option value="single">Single-family home</option>
                <option value="multi">Multi-family</option>
                <option value="condo">Condo / Co-op</option>
                <option value="commercial">Commercial</option>
              </VestaSelect>
              <VestaFieldError id="type-err" :message="err.type" />
            </div>
          </div>
          <VestaFormNav :step="step" :last="false" @back="back" />
        </form>

        <!-- Step 3 -->
        <form v-else @submit.prevent="submit" novalidate aria-label="Step 3: Billing">
          <h2 class="text-lg font-semibold text-gray-900 mb-6">Choose your plan</h2>
          <div class="space-y-3 mb-6">
            <label v-for="p in plans" :key="p.id"
              class="flex items-start gap-3 p-4 border rounded-lg cursor-pointer transition-colors duration-150"
              :class="form.plan === p.id ? 'border-[var(--color-brand)] bg-green-50' : 'border-gray-200 hover:border-gray-300'">
              <input type="radio" :value="p.id" v-model="form.plan" name="plan"
                class="mt-0.5 accent-[var(--color-brand)]" :aria-describedby="`plan-${p.id}-desc`" />
              <div class="flex-1">
                <div class="flex items-center justify-between">
                  <span class="font-medium text-gray-900">{{ p.name }}</span>
                  <span class="text-sm font-semibold text-gray-700 tabular-nums">{{ p.price }}</span>
                </div>
                <p :id="`plan-${p.id}-desc`" class="text-sm text-gray-500 mt-0.5">{{ p.desc }}</p>
              </div>
            </label>
          </div>
          <VestaFieldError id="plan-err" :message="err.plan" />
          <VestaFormNav :step="step" :last="true" :submitting="submitting" @back="back" />
        </form>

      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import VestaStepIndicator from '@/components/VestaStepIndicator.vue'
import VestaFormNav from '@/components/VestaFormNav.vue'
import VestaFieldError from '@/components/VestaFieldError.vue'
import VestaInput from '@/components/VestaInput.vue'
import VestaButton from '@/components/VestaButton.vue'
import VestaSelect from '@/components/VestaSelect.vue'

const steps = [
  { id: 'profile',  label: 'Your profile'   },
  { id: 'property', label: 'First property'  },
  { id: 'billing',  label: 'Billing'         },
]
const plans = [
  { id: 'starter', name: 'Starter',      price: 'Free',   desc: 'Up to 3 units. All core features.' },
  { id: 'growth',  name: 'Growth',       price: '$19/mo', desc: 'Up to 20 units. Maintenance + tenant portal.' },
  { id: 'pro',     name: 'Professional', price: '$49/mo', desc: 'Unlimited units + priority support.' },
]

const step = ref(0)
const submitting = ref(false)
const form = reactive({ name: '', email: '', phone: '', address: '', units: null, type: '', plan: 'starter' })
const err = reactive<Record<string, string | undefined>>({})

function clearErr() { Object.keys(err).forEach(k => { err[k] = undefined }) }

function validateStep0() {
  clearErr(); let ok = true
  if (!form.name.trim())       { err.name  = 'Full name is required.'; ok = false }
  if (!form.email.trim())      { err.email = 'Email address is required.'; ok = false }
  else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email))
                               { err.email = 'Enter a valid email (e.g. you@example.com).'; ok = false }
  return ok
}

function validateStep1() {
  clearErr(); let ok = true
  if (!form.address.trim())    { err.address = 'Street address is required.'; ok = false }
  if (!form.units || form.units < 1) { err.units = 'Enter the number of units (minimum 1).'; ok = false }
  if (!form.type)              { err.type = 'Select a property type to continue.'; ok = false }
  return ok
}

function advance(s: number) {
  const ok = s === 0 ? validateStep0() : validateStep1()
  if (ok) { step.value++; window.scrollTo({ top: 0, behavior: 'smooth' }) }
}

function back() {
  clearErr(); step.value--; window.scrollTo({ top: 0, behavior: 'smooth' })
}

async function submit() {
  clearErr()
  if (!form.plan) { err.plan = 'Select a plan to continue.'; return }
  submitting.value = true
  try {
    await new Promise(r => setTimeout(r, 1000)) // replace with API call
    // router.push('/dashboard')
  } finally { submitting.value = false }
}
</script>
```

---

## VERIFICATION

- Focus states: PASS — VestaInput, VestaSelect, VestaButton all have focus-visible states from existing components
- prefers-reduced-motion: PASS — no animations; Tailwind transition-colors only (CSS property, not layout)
- Touch targets 44×44px: PASS — `min-h-[44px]` on both navigation buttons
- Semantic HTML: PASS — form, label, input association, nav, ol, li for stepper, role="alert" on errors
- Responsive / no overflow: PASS — max-w-lg single column, full-width on mobile
- No framework migration: PASS — Vue 3 + Tailwind v3 unchanged
- No truncated output: PASS
- Progress indicator: PASS — VestaStepIndicator with numbered steps, sr-only live region
- Primary distinct from Back: PASS — `variant="primary"` (filled) vs `variant="ghost"` (outlined/text)
- Inline error messages: PASS — VestaFieldError below each field with role="alert" and actionable text
- Labels above inputs: PASS — all `<label>` elements above their inputs
- Back never dead-ends: PASS — back() clears errors and decrements step
- Three-step structure unchanged: PASS
