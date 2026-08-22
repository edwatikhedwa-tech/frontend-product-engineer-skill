# Library Selection and Live-Docs Protocol

## Capability map

| Capability | Consider when | Default posture |
| --- | --- | --- |
| React | component-based web UI | use the project’s installed version |
| Next.js | full-stack React framework, routing, server/client boundaries | use only if the project already uses it or the requirement warrants it |
| Tailwind CSS | utility styling and tokenized composition | use existing project conventions; do not migrate casually |
| shadcn/ui | source-owned accessible component starting points | inspect generated code and project conventions |
| Base UI | accessible low-level primitives with controlled composition | consider for complex popovers, dialogs, menus, and comboboxes |
| React Aria | accessible behavior and interaction primitives | consider when semantics and interaction behavior are the hard problem |
| Motion | gestures, spring physics, shared layout, or meaningful sequencing | use CSS for simple transitions |
| TanStack Table | complex sorting, filtering, selection, pagination, or table state | use native/existing components for simple semantic tables |
| Storybook | component isolation, states, and component regression | add when the component surface merits a laboratory |
| Playwright | browser functional, visual, and responsive QA | prefer for real browser evidence when available |
| axe-core | automated accessibility signals | pair with manual semantic and keyboard review |
| Context7 | current library documentation through an available integration | use when actually available; never make it mandatory |

## Decision rule

USE A LIBRARY BECAUSE IT SOLVES A REAL PROBLEM, NOT BECAUSE IT EXISTS.

Before adding a dependency, state the problem, the native/project alternative, the accessibility and maintenance tradeoff, and why the dependency is justified. Do not create an npm zoo.

## Version-sensitive protocol

For React, Next.js, Tailwind, shadcn/ui, Base UI, React Aria, Motion, TanStack, Storybook, Playwright, axe-core, browser APIs, or any fast-moving tool:

1. inspect `package.json`, lockfile, and project configuration;
2. determine the installed version and supported runtime;
3. consult Context7 if the integration is available;
4. otherwise use current official documentation;
5. check compatibility and deprecations;
6. implement only after the evidence is sufficient;
7. record the official URL and date in the task evidence when the choice matters.

This repository does not pin or pretend to be the source of truth for package APIs.
