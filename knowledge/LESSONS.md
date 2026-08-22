# Lessons

This is the condensed, reusable experience memory for the skill. Add a lesson only after a case or review provides evidence. Keep it framework-agnostic and remove project-specific names.

## Maintainer format

```text
### L-XXXX — Short rule
Context: what kind of task exposed it.
Evidence: case/review and the observed signal.
Rule: the reusable instruction.
Avoid: the tempting but weaker alternative.
```

## Initial lessons

### L-0001 — Rendered evidence closes the loop
Context: any frontend implementation.
Evidence: source inspection cannot reveal responsive clipping, interaction feedback, or visual noise reliably.
Rule: run the real app and capture the relevant browser states before calling the work complete.
Avoid: treating a passing build or a high self-score as acceptance.

### L-0002 — Intermediate widths expose systemic layout mistakes
Context: responsive product screens.
Evidence: layouts can look acceptable at 1440px and 390px while failing at 1024px or 1280px.
Rule: include intermediate desktop widths in the viewport matrix.
Avoid: checking only one desktop and one mobile screenshot.

### L-0003 — Curate the rule, not the anecdote
Context: adding experience from a project case.
Evidence: project-specific implementation details do not generalize safely.
Rule: deduplicate each lesson into a short, framework-agnostic rule before adding it here.
Avoid: copying a one-off workaround into universal guidance.
