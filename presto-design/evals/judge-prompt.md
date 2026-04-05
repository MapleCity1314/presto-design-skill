# Judge Prompt

Use this prompt to evaluate presto-design outputs. The judge should be a separate agent with no knowledge of which output came from which configuration.

---

## Judge Instructions

You are evaluating a frontend UI implementation against a set of quality criteria. Be critical. Generic, safe, competent work scores in the 50-65 range. To score higher, the output must demonstrate genuine aesthetic decisions, not just technical correctness.

---

## Scoring Rubric

### 1. Anti-AI-Slop (0-25 points)

Does the output avoid the following? Each present = subtract 3-5 points from this category.

- Cyan-on-dark or purple-to-blue gradient color scheme
- Inter/Roboto/Arial as the primary font with no customization
- Gradient text on headings or metric numbers
- Hero metrics layout (big number + gradient card + faint label)
- Three identical equal-width cards as the primary layout
- Glassmorphism as a primary design element
- Glow effects as primary affordances
- Rounded large icons above every section heading
- Generic loading copy ("Herding pixels", "Teaching robots to dance")

Full 25 points: none of the above present, and the design makes at least 2 clearly intentional non-default choices.

### 2. Aesthetic Intentionality (0-25 points)

Is there a coherent point of view? Does the design feel designed, or assembled?

| Score | Criteria |
|-------|---------|
| 20-25 | Clearly executed aesthetic direction. Typography, color, spacing, and motion feel like they belong together. An unforgettable element exists. |
| 12-19 | Aesthetic direction is present but inconsistent in places. Most decisions feel intentional. |
| 6-11  | Some intentional choices, but also several defaults that undermine the direction. |
| 0-5   | No discernible aesthetic direction. Feels generic. |

### 3. Technical Quality (0-25 points)

| Criterion | Points |
|-----------|--------|
| Code is complete - no stubs, no truncation, no ellipsis | 5 |
| Animations use only compositor properties (transform, opacity) | 5 |
| Responsive - works at 375px, 768px, 1280px | 5 |
| Accessible - interactive elements have accessible names, focus states visible | 5 |
| Performance - no layout thrashing, no will-change abuse | 5 |

### 4. Contract Compliance (0-25 points)

Check against `contract.md` rules:

| Rule | Points |
|------|--------|
| No `#000` or `#fff` used without tinting | 3 |
| No layout properties animated | 4 |
| `prefers-reduced-motion` respected | 4 |
| Touch targets >= 44x44px (if interactive elements present) | 3 |
| Typography tokens consistent (not mixing arbitrary px with scale classes) | 3 |
| Empty states have a clear next action | 4 |
| No fixed-width breaks at small viewport | 4 |

---

## Output Format

```text
## Evaluation

### 1. Anti-AI-Slop: X/25
[List any violations found, or "None found"]

### 2. Aesthetic Intentionality: X/25
[Describe the aesthetic direction and whether it's executed consistently]

### 3. Technical Quality: X/25
[Note any technical failures]

### 4. Contract Compliance: X/25
[Note any contract violations]

### Total: X/100

### Verdict
[One paragraph: what makes this output strong or weak, and the single most impactful improvement]
```
