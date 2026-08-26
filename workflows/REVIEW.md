# REVIEW workflow

Use when the user asks for an independent audit and has not asked for implementation.

Follow [`quality/AUDIT_PROTOCOL.md`](../quality/AUDIT_PROTOCOL.md). REVIEW is evidence collection and reporting only; do not modify code unless the user changes the request.

1. Establish the review scope, product job, success criteria, and whether a BEFORE comparison is required.
2. Run the real app if possible; do not review source code alone. Record console/runtime/network limitations.
3. Capture representative screens, relevant viewports/states, and matched BEFORE evidence when reviewing a redesign.
4. Reconstruct the current visual identity and design direction; mark assumptions as assumptions.
5. Test realistic and stress content.
6. Inspect DOM overflow, clipping, scroll containers, focus, semantics, and accessibility evidence when tooling allows.
7. **Visual Critic** — ask what makes the product recognizable, what feels template-derived, what feels accidental, what a senior designer would criticize, and whether the visual language serves the job.
8. Run UX/Engineering review and the anti-generic gate. Run the transformation gate when BEFORE/AFTER evidence exists or the scope is a REDESIGN review.
9. Record each finding with ID, title, severity, location, actual, problem, expected, constraints, acceptance criteria, and evidence.
10. Summarize Engineering, UX, Visual, and Transformation results, P0/P1/P2/P3 counts, strengths, limitations, NOT VERIFIED checks, and next actions.

Do not modify code unless the user explicitly changes the request from review to implementation.

