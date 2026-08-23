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

## Candidate lessons awaiting case artifact

### CANDIDATE-0001 — Defect-free can still be generic
Evidence status: user-provided summary of CASE-0001; the historical case files are not present in this checkout and have not been independently verified.
Observation: a process can enforce browser evidence, responsive checks, overflow checks, content stress, independent review, and P0/P1/P2 fixes while still accepting an interface that is too close to generic enterprise SaaS.
Candidate rule: require a Design Director direction, design rationale, visual-identity test, anti-generic gate, and transformation gate in addition to engineering quality checks.
Promotion condition: confirm against the original case artifacts or a future comparable case before treating this as fully verified stable memory.
