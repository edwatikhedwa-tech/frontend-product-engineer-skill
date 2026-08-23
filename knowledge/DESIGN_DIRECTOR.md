# Design Director

The Design Director is a mandatory decision stage between product understanding and substantial frontend implementation. It turns product intent into a defensible visual system. It is not a moodboard, a component inventory, or a request to make the interface unusual.

## Role chain

```text
PRODUCT THINKER
  → user, job, constraints, success
DESIGN DIRECTOR
  → visual thesis, hierarchy, composition, rationale
REFERENCE RESEARCHER
  → evidence and synthesis from selected problems/patterns
FRONTEND ENGINEER
  → implementation, states, compatibility, maintainability
VISUAL CRITIC
  → rendered quality, identity, distinctiveness, defects
ENGINEERING QA
  → browser, responsive, accessibility, content, regression evidence
DATASET
  → accepted evidence, candidate lessons, skill gaps
```

## Required design direction

Before substantial implementation in CREATE or systemic REDESIGN, write a short design direction containing:

- product personality and emotional target;
- one-paragraph visual identity statement;
- visual thesis: why this language fits the product, user, and job;
- information hierarchy and reading order;
- spatial/compositional strategy, including where density is intentional;
- typography strategy and editorial/data roles;
- surface, border, radius, elevation, and color strategy;
- navigation and interaction character;
- motion philosophy, only when motion serves comprehension or feedback;
- what makes this product visually recognizable without its logo;
- references selected by problem/category and a synthesis into a new system;
- deliberate exclusions: generic patterns or decorative choices rejected;
- evidence-based acceptance criteria for the first rendered slice.

EXTEND uses a shorter compatibility direction: existing visual language, product personality to preserve, new feature’s meaningful contribution, and any justified deviation. REVIEW reconstructs the direction from the existing product and marks assumptions.

## Design rationale

Every major visual decision needs this chain:

```text
Product/user/task reason → design principle → concrete UI decision → expected behavior/evidence
```

Example:

```text
Frequent supplier comparison → rapid scanning matters → stable aligned result rows with restrained emphasis → faster comparison at 1024px and 390px screenshots.
```

Do not accept rationale such as “modern”, “clean”, “premium”, “looks good”, or “the library defaults”. Name the product reason and the observable consequence.

## Design ambition questions

Before implementation and again after the first rendered review, answer:

1. What makes this product visually recognizable?
2. Does the visual language support the actual product job?
3. Is this the best interface this product could reasonably have within its constraints?
4. Which decisions are intentional, and which are inherited accidentally?
5. Does the design have restraint as well as ambition?

If the answer to the third question is no, iterate. Do not chase novelty, gradients, glassmorphism, animation, or oversized type for their own sake. For B2B and data-heavy products, clarity, speed, density, hierarchy, and accessibility remain primary.

## Completion rule

No substantial CREATE or REDESIGN implementation is accepted without a direction artifact, rationale, reference synthesis, and first-render acceptance criteria. A tiny local fix may use a proportional note when creating a full direction would cost more than the change, but it must still preserve the existing visual language and pass the relevant gates.
