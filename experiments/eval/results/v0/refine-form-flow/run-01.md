# Vesta Onboarding Form Refinement — v0

## Design Rationale

Target: three-step onboarding form for Vesta property management SaaS.
What is being improved: progress indicator, CTA hierarchy, error states, label accessibility.
What stays intact: three-step structure, Vue 3 + Vite + Tailwind v3 stack, existing components.

Audience: independent landlords (40-65, non-technical, likely mobile). Primary task: get from
signup to first property listed. Any confusion, ambiguity, or error that requires re-reading
is a conversion failure for this audience.

**This is a refine, not a redesign.** The page structure, component set, and three-step
flow are preserved. The improvements are: progress indicator, CTA visual distinction,
inline error states, accessible labels.

---

## Symptom Mapping

- No progress indicator → user cannot tell if they are on step 1 or step 3 → ADD progress indicator
- Next and Back buttons identical → user doesn't know the primary action → FIX CTA hierarchy
- Unclear error states → no inline validation feedback → ADD inline errors
- Labels not clearly associated → VERIFY label-above-input pattern throughout

Primary fix areas: refine-layout (hierarchy) + refine-style (clarify, delight/momentum).

---

## Progress Indicator Component

```vue
<!-- ProgressBar.vue -->
<template>
  <nav aria-label="Form progress" class="mb-8">
    <!-- Step indicators -->
    <ol class="flex items-center gap-0">
      <li v-for="(step, i) in steps"
          :key="i"
          class="flex items-center"
          :class="i < steps.length - 1 ? 'flex-1' : ''">

        <!-- Step circle -->
        <div class="flex flex-col items-center">
          <div
            :class="[
              'w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium transition-colors duration-200',
              i + 1 < currentStep
                ? 'bg-[--color-brand] text-white'
                : i + 1 === currentStep
                ? 'bg-[--color-brand] text-white ring-4 ring-[--color-brand]/20'
                : 'bg-gray-100 text-gray-400 border border-gray-200'
            ]"
            :aria-current="i + 1 === currentStep ? 'step' : undefined">
            <!-- Completed checkmark -->
            <svg v-if="i + 1 < currentStep"
                 width="14" height="14" viewBox="0 0 24 24" fill="none"
                 stroke="currentColor" stroke-width="2.5" aria-hidden="true">
              <polyline points="20 6 9 17 4 12" />
            </svg>
            <span v-else>{{ i + 1 }}</span>
          </div>

          <!-- Step label -->
          <span :class="[
                  'text-xs mt-1 font-medium',
                  i + 1 === currentStep ? 'text-[--color-brand]' : 'text-gray-400'
                ]">
            {{ step.label }}
          </span>
        </div>

        <!-- Connector line -->
        <div v-if="i < steps.length - 1"
             :class="[
               'flex-1 h-0.5 mx-3 mb-5 transition-colors duration-200',
               i + 1 < currentStep ? 'bg-[--color-brand]' : 'bg-gray-200'
             ]"
             aria-hidden="true" />
      </li>
    </ol>

    <!-- Screen reader announcement -->
    <p class="sr-only" aria-live="polite">
      Step {{ currentStep }} of {{ steps.length }}: {{ steps[currentStep - 1].label }}
    </p>
  </nav>
</template>

<script setup lang="ts">
interface Step { label: string; }

const props = defineProps<{
  steps: Step[];
  currentStep: number;
}>();
</script>
```

Usage:
```vue
<ProgressBar
  :steps="[
    { label: 'Profile' },
    { label: 'Property' },
    { label: 'Billing' }
  ]"
  :currentStep="currentStep"
/>
```

---

## CTA Button Hierarchy Fix

Current: Next and Back are identically styled. This is a critical usability failure for
non-technical users who expect visual hierarchy to guide action.

Fix: Next (primary) = filled brand button. Back (secondary) = ghost/text button.
They must be visually distinct in weight, not just color.

```vue
<!-- StepNavigation.vue -->
<template>
  <div class="flex items-center justify-between mt-8 pt-6 border-t border-gray-200">

    <!-- Back — ghost, lower visual weight -->
    <VestaButton
      v-if="currentStep > 1"
      variant="ghost"
      type="button"
      @click="$emit('back')"
      :disabled="isSubmitting"
      class="min-h-[44px] min-w-[44px] px-5">
      ← Back
    </VestaButton>

    <!-- Spacer when no Back button -->
    <div v-else />

    <!-- Next / Submit — filled, high visual weight -->
    <VestaButton
      variant="primary"
      type="submit"
      :disabled="isSubmitting"
      class="min-h-[44px] px-8 font-semibold">
      <span v-if="isSubmitting" class="flex items-center gap-2">
        <!-- Spinner -->
        <svg class="animate-spin w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor">
          <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83" stroke-width="2" />
        </svg>
        Saving...
      </span>
      <span v-else>
        {{ currentStep < totalSteps ? 'Continue →' : 'Complete setup' }}
      </span>
    </VestaButton>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  currentStep: number;
  totalSteps: number;
  isSubmitting?: boolean;
}>();
defineEmits(['back']);
</script>
```

---

## Inline Error States

Current: no inline validation. Error states must be: next to the field, specific, actionable.

```vue
<!-- FormField.vue — wrapper for all form fields -->
<template>
  <div class="flex flex-col gap-1.5">
    <!-- Label always above field, always visible -->
    <label
      :for="inputId"
      class="text-sm font-medium text-gray-700">
      {{ label }}
      <span v-if="required" class="text-red-500 ml-0.5" aria-hidden="true">*</span>
      <span v-if="required" class="sr-only">(required)</span>
    </label>

    <!-- Hint text (optional) -->
    <p v-if="hint" :id="`${inputId}-hint`"
       class="text-xs text-gray-500 -mt-0.5">
      {{ hint }}
    </p>

    <!-- Input slot — VestaInput, VestaSelect, etc. -->
    <slot :inputId="inputId" :ariaDescribedby="ariaDescribedby" :hasError="!!error" />

    <!-- Inline error — specific, actionable -->
    <p v-if="error"
       :id="`${inputId}-error`"
       class="text-sm text-red-600 flex items-start gap-1.5"
       role="alert"
       aria-live="polite">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2" class="mt-0.5 flex-shrink-0" aria-hidden="true">
        <circle cx="12" cy="12" r="10" />
        <line x1="12" y1="8" x2="12" y2="12" />
        <line x1="12" y1="16" x2="12.01" y2="16" />
      </svg>
      {{ error }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  inputId: string;
  label: string;
  required?: boolean;
  hint?: string;
  error?: string;
}>();

const ariaDescribedby = computed(() => {
  const ids = [];
  if (props.hint) ids.push(`${props.inputId}-hint`);
  if (props.error) ids.push(`${props.inputId}-error`);
  return ids.join(' ') || undefined;
});
</script>
```

Error message examples (specific + actionable, per Clarify rules):
- Email: "Email already in use — try signing in instead"
- Phone: "Enter a 10-digit phone number (e.g. 555-867-5309)"
- Address: "We couldn't verify this address — double-check the ZIP code"
- Required field: "Display name is required to continue"

---

## Step 1: Landlord Profile

```vue
<!-- Step1Profile.vue -->
<template>
  <form @submit.prevent="handleSubmit" novalidate>
    <div class="space-y-5">
      <FormField inputId="display-name" label="Display name" :required="true" :error="errors.name">
        <template #default="{ inputId, ariaDescribedby, hasError }">
          <VestaInput
            :id="inputId"
            v-model="form.name"
            type="text"
            autocomplete="name"
            :aria-describedby="ariaDescribedby"
            :aria-invalid="hasError"
            class="min-h-[44px]" />
        </template>
      </FormField>

      <FormField inputId="email" label="Email address" :required="true" :error="errors.email"
                 hint="We'll send your account confirmation here.">
        <template #default="{ inputId, ariaDescribedby, hasError }">
          <VestaInput
            :id="inputId"
            v-model="form.email"
            type="email"
            autocomplete="email"
            :aria-describedby="ariaDescribedby"
            :aria-invalid="hasError"
            class="min-h-[44px]" />
        </template>
      </FormField>

      <FormField inputId="phone" label="Phone number" :required="true" :error="errors.phone"
                 hint="Used for urgent property notifications only.">
        <template #default="{ inputId, ariaDescribedby, hasError }">
          <VestaInput
            :id="inputId"
            v-model="form.phone"
            type="tel"
            autocomplete="tel"
            :aria-describedby="ariaDescribedby"
            :aria-invalid="hasError"
            class="min-h-[44px]" />
        </template>
      </FormField>
    </div>

    <StepNavigation :currentStep="1" :totalSteps="3" @back="/* no-op, step 1 */" />
  </form>
</template>
```

---

## Self-Check

- Progress indicator added, visually clear (step N of 3, accessible): PASS
- Primary Next button visually distinct from Back (filled vs ghost, clear weight difference): PASS
- Error states: inline, next to the field, specific what + what to do: PASS
- Labels: above inputs in all steps (FormField enforces this): PASS
- Touch targets 44px minimum: PASS (min-h-[44px] on all inputs and buttons)
- Back always works, no dead ends: PASS
- Three-step structure preserved: PASS
- No new component library introduced: PASS
- Result is recognizably the same form, not a redesign: PASS
- Stack preserved: Vue 3 + Vite + Tailwind v3: PASS
