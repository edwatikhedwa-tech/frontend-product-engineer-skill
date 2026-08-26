# REDESIGN workflow

Use when an existing interface needs meaningful improvement.

Follow [`quality/AUDIT_PROTOCOL.md`](../quality/AUDIT_PROTOCOL.md). A redesign is not complete at source-code change; it requires matched rendered evidence and a re-audit.

1. **Product Thinker** — map users, jobs, constraints, success criteria, and the full product surface.
2. **Discover the entire product** — map routes, important screens, shared navigation, design tokens, components, and data states.
3. **Run the current app** — use the real start command and record setup assumptions.
4. **BEFORE evidence** — screenshot important screens at matched desktop, intermediate, tablet/mobile, and state coverage. Record the current visual language and known limitations without rewriting history.
5. **Browser audit** — identify structural, product, hierarchy, responsive, interaction, accessibility, content, runtime, and generic-language problems from the rendered product and evidence.
6. **Design Director** — write the direction before implementation: what systemic change is needed, why it fits the product, what identity should emerge, what will remain, and which choices have rationale.
7. **Reference Researcher** — choose relevant reference categories and synthesize principles into a new product-specific system. Do not end with a list of admired products.
8. **Frontend Engineer** — update shared tokens/components and representative flows before polishing isolated screens. Preserve working behavior unless scope explicitly changes it.
9. **Run and browser audit** — cover the same evidence set plus changed states, console/runtime/network behavior, and content stress.
10. **Visual Critic** — assume you did not create the interface. Run the anti-generic gate for identity, distinctiveness, composition, typography, art direction, intentionality, and restraint.
11. **Transformation gate** — compare BEFORE → AFTER across job, hierarchy, composition, visual language, typography, density, interaction, responsive behavior, accessibility/states, and personality. If the original was already strong, justify restrained preservation.
12. **Objective findings, fix, verify, re-audit** — record evidence-backed findings, resolve P0/P1/P2, repeat browser and project checks, then re-run the independent review.
13. **Dataset** — record the case evidence, candidate lessons, and `skill_gap`: which rule existed but failed or was missing.
14. **Done** — both design and engineering gates pass; report unverified surfaces explicitly.

Do not redesign only the first screen shown by chance. Do not call a token restyle a redesign when the information architecture or visual language remains generic.

