# v0.2.0 conceptual self-test

This is a process self-test, not a claim that a historical product run was re-executed.

## Benchmark prompt

Assume the v0.2.0 skill receives an existing product redesign where engineering fixes made the interface usable, but the result still resembles a generic enterprise application.

## Expected additional behavior

Before substantial implementation, the agent must:

1. state REDESIGN mode and inspect the whole product;
2. capture BEFORE evidence and record the existing visual language without rewriting history;
3. produce a Design Director direction with personality, visual thesis, hierarchy, composition, typography, density, surfaces, interaction character, deliberate exclusions, design rationale, and rendered acceptance criteria;
4. choose problem-relevant reference categories, including at least a visual/art-direction or typography category when the generic-language problem is real;
5. synthesize principles from multiple references into a new product-specific system rather than list admired products;
6. implement a representative slice from that direction;
7. run the real application and capture matched AFTER evidence;
8. switch to Visual Critic mode and run the anti-generic gate;
9. run the BEFORE → AFTER transformation matrix across visual language, composition, hierarchy, density, interaction, and personality;
10. return to Design Director if the result is still generic, merely tidier, or weak/acceptable on identity, composition, typography, distinctiveness, or intentionality;
11. run the Engineering Gate and preserve browser, responsive, accessibility, content-stress, overflow, and regression evidence;
12. record the case’s candidate lessons and skill_gap: which v0.1 rule existed but failed to prevent generic UI.

## Self-test conclusion

v0.2.0 contains operational routing and gates for these additional actions. This is a conceptual check against a maintainer-provided benchmark summary. It is not a visual re-run because the historical case artifacts and application were not part of this skill-only task.

