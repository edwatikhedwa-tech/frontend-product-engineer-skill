# EXTEND workflow

Use when a good existing product gains a screen or feature.

Follow [`quality/AUDIT_PROTOCOL.md`](../quality/AUDIT_PROTOCOL.md), including neighboring-flow regression and a re-audit after fixes.

1. Inspect existing visual language, product personality, tokens, components, control heights, spacing, density, and interaction patterns.
2. Identify the user job, entry points, affected navigation, data states, and compatibility constraints.
3. **Design Director compatibility direction** — state what is inherited, what the new feature contributes, why any deviation is justified, and how the new screen remains recognizable as part of the product.
4. Research references for the new product problem, selecting only the categories that address the actual gap.
5. Reuse existing primitives where they carry the right semantics; do not introduce a new visual language or dependency without a concrete problem.
6. Implement loading, empty, error, permission, success, and long-content states relevant to the feature.
7. Run the real app and verify the new flow plus neighboring regression surfaces.
8. Capture desktop, intermediate, tablet/mobile, focus, stress-content, identity, DOM, runtime, and accessibility evidence where relevant.
9. **Visual Critic + Engineering QA** — check product personality, anti-generic drift, responsiveness, accessibility, content, overflow, interaction, states, runtime behavior, and regression.
10. Record objective findings, fix P0/P1/P2 and any critical WEAK/ACCEPTABLE design dimension, then verify and re-audit. If the existing product is weak, do not silently amplify its generic patterns.

Do not create an isolated AI-generated page inside a coherent product.

