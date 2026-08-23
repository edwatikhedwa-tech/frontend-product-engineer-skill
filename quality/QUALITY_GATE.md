# Quality gate

The quality gate is mandatory after implementation and before DONE. Engineering quality and design quality are separate acceptance conditions; passing one does not compensate for failing the other.

## Engineering Gate

- [ ] The real application was run.
- [ ] Important screens were opened in a real browser when possible.
- [ ] Screenshots cover relevant widths: 1920, 1440, 1280, 1024, tablet, and 390 where applicable.
- [ ] Intermediate desktop behavior was inspected.
- [ ] Realistic content and stress content were tested.
- [ ] DOM/browser overflow, clipping, overlap, and intentional scroll regions were checked where tooling permits.
- [ ] Keyboard, focus, semantics, labels, contrast, and reduced-motion behavior were reviewed.
- [ ] Automated accessibility checks were run when justified and available.
- [ ] Interaction, loading, empty, error, permission, and recovery states were checked.
- [ ] Regression checks cover changed and neighboring flows.

Defect gate:

- P0: 0
- P1: 0
- P2: fixed or explicitly accepted with reason
- P3: may remain with a documented tradeoff

## UX Gate

- [ ] Navigation and entry points support the product job.
- [ ] Information hierarchy and scanability are clear.
- [ ] Density is appropriate for the job and viewport.
- [ ] Affordances and interaction feedback are understandable.
- [ ] States preserve hierarchy and provide recovery.
- [ ] Responsive behavior has an intentional strategy, not desktop shrinkage.
- [ ] Content robustness covers long, missing, multiline, and expanded values.

## Visual Gate

- [ ] A Design Director direction exists before substantial CREATE/REDESIGN implementation.
- [ ] The direction contains a visual identity paragraph and product/user/task rationale.
- [ ] Reference categories were deliberately selected and synthesized into a new product-specific system.
- [ ] Visual identity is recognizable without relying on the logo or brand name.
- [ ] Distinctiveness comes from intentional language, not decoration or novelty.
- [ ] Composition, typography, hierarchy, surfaces, navigation, and data presentation are coherent.
- [ ] The result does not fail the anti-generic UI gate.
- [ ] The Visual Critic reviewed the rendered result independently.
- [ ] No critical visual dimension is WEAK or ACCEPTABLE after the final iteration.
- [ ] Design ambition was answered: is this the best interface the product could reasonably have within constraints?

## Transformation Gate

Required for REDESIGN and for EXTEND when visual drift is a risk:

- [ ] Matched BEFORE and AFTER evidence exists, or missing evidence is explicitly recorded.
- [ ] The comparison covers job, hierarchy, composition, visual language, typography, density, interaction, responsive behavior, accessibility/states, and product personality.
- [ ] The AFTER result demonstrates meaningful improvement where the original was weak.
- [ ] If change is intentionally restrained because the original was already strong, the reason is documented.
- [ ] A token restyle or component swap is not being presented as systemic redesign.

## Evidence and handoff

If a checkbox cannot be checked, say not verified in the handoff. Never replace missing evidence with a confidence score. Use qualitative labels WEAK, ACCEPTABLE, STRONG, or EXCEPTIONAL only as summaries; a label is not evidence. Keep the final report separated into Engineering, UX, Visual, and Transformation results.

