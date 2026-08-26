# CREATE workflow

Use when the product or screen is new.

Follow [`quality/AUDIT_PROTOCOL.md`](../quality/AUDIT_PROTOCOL.md) throughout. CREATE has no BEFORE state, but it still requires rendered browser evidence and a second audit after fixes.

1. **Product Thinker** — define user, job, constraints, success criteria, information architecture, and important states.
2. **Design Director** — write `DESIGN_DIRECTION.md` before substantial implementation: visual identity, visual thesis, hierarchy, composition, typography, density, surfaces, interaction character, motion philosophy, design rationale, reference categories, synthesis, deliberate exclusions, and rendered acceptance criteria.
3. **Reference Researcher** — select only the product/UX, information architecture, visual/art direction, typography, interaction, data-dense, and motion references relevant to the job. Synthesize principles; do not copy a product.
4. **Frontend Engineer** — build a coherent first slice from the direction with real content and non-happy-path states. Use existing primitives or a justified library; do not let defaults become the design direction.
5. **Run and browser audit** — start the actual application, exercise critical flows, capture the viewport matrix and relevant states, and collect DOM/runtime/accessibility evidence where available.
6. **Independent review** — review identity, distinctiveness, composition, typography, art direction, restraint, product personality, anti-generic signals, responsive behavior, accessibility, content stress, overflow, interaction, states, and regression.
7. **Objective findings** — record findings with severity, location, actual, problem, expected, constraints, acceptance criteria, and evidence.
8. **Fix, verify, and re-audit** — resolve P0/P1/P2 defects and any WEAK/ACCEPTABLE critical design dimension, then repeat the browser and project checks.
9. **Dataset** — if this work becomes a case, preserve direction, references, implementation, review, AFTER evidence, candidate lessons, and skill gaps.
10. **Done** — both Engineering/UX and Visual gates pass. Report evidence, remaining P3 items, and anything NOT VERIFIED.

Do not start by generating random cards or a decorative dashboard with no user job. Do not “make it prettier” after a generic implementation; establish the direction first.

