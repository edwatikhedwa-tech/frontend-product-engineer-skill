# EXTEND workflow

Use when a good existing product gains a screen or feature.

1. Inspect existing visual language, tokens, components, control heights, spacing, density, and interaction patterns.
2. Identify the user job, entry points, affected navigation, data states, and compatibility constraints.
3. Reuse existing primitives where they carry the right semantics.
4. Research references for the new product problem, not as a reason to change the entire style.
5. Define the smallest extension that feels native to the product.
6. Implement loading, empty, error, permission, success, and long-content states relevant to the feature.
7. Run the real app and verify the new flow plus neighboring regression surfaces.
8. Capture desktop, intermediate, tablet/mobile, focus, and stress-content evidence where relevant.
9. Review independently and fix P0/P1/P2 defects.

Do not introduce a new visual language or dependency without a concrete problem and compatibility evidence.
