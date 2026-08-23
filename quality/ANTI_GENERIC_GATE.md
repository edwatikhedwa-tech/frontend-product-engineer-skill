# Anti-generic UI gate

Run this gate on the rendered result after the first implementation and after material fixes. It is mandatory for CREATE and REDESIGN, and applies to EXTEND when the new screen could drift from the product language.

## Fail conditions

Fail and return to the Design Director stage when one or more of these is true without a documented product reason:

- removing the logo/brand name leaves a generic SaaS/admin dashboard;
- the interface could be swapped with dozens of AI-generated dashboards without changing the user job;
- cards, borders, pills, badges, blue buttons, and standard gaps are the whole visual language;
- card nesting replaces meaningful composition;
- semantic levels receive the same visual treatment;
- spacing is a list of defaults rather than a composition tied to hierarchy and content;
- hierarchy is only font-size + bold + color with no spatial or structural logic;
- component-library defaults determine the design direction;
- the result is a token restyle with no meaningful change in composition, information emphasis, or interaction character.

## Review questions

1. What makes this product visually recognizable?
2. What feels template-derived?
3. Where does it feel like an AI-generated SaaS dashboard?
4. Which visual decisions feel accidental?
5. Which decisions are supported by product/user/task rationale?
6. What would a senior designer criticize immediately?
7. Does the identity survive a state change and a narrow viewport?
8. Is there unnecessary decoration or ornamental complexity?

## Evidence and disposition

Record the answer, screenshot or rendered state, failed signal, product reason if a conventional treatment is intentional, and the next Design Director decision. “Looks distinctive” without a paragraph, rationale, and rendered evidence does not pass. A qualitative result of WEAK or ACCEPTABLE on identity, composition, typography, distinctiveness, or intentionality requires another iteration.

## Do not overcorrect

The gate does not require unusual colors, animation, gradients, glass, oversized typography, or anti-pattern novelty. A quiet, dense operational interface can pass when its language is coherent, purposeful, and recognizable through structure, type, rhythm, navigation, and data treatment.
