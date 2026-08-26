# Changelog

## 0.3.0 — 2026-08-26

- Added browser-first verification as a mandatory `INSPECT → PLAN → IMPLEMENT → RUN → BROWSER AUDIT → FIX → VERIFY → RE-AUDIT → DONE` workflow.
- Added evidence-driven UI audit guidance for visual hierarchy, layout, typography, component consistency, responsive behavior, interaction states, accessibility, content robustness, and runtime/console/network checks.
- Strengthened the independent reviewer mode and added objective audit findings with severity, actual, problem, expected behavior, constraints, acceptance criteria, and evidence.
- Added the audit → fix → verify loop, explicit re-audit, and separate NOT VERIFIED handling when tools or surfaces are unavailable.
- Expanded accessibility, runtime, responsive, and long-content checks and kept the P0/P1/P2/P3 quality gate.
- Added anti-AI-slop guidance for unjustified cards, gradients, shadows, radii, icons, badges, colors, animation, chrome, and generic patterns without banning contextually valid choices.
- Made the skill project-agnostic and changed the runtime invocation name to `front` (`/front` in Claude Code and `$front` in Codex); the repository remains `frontend-product-engineer-skill`.

## 0.2.0 — 2026-08-23

- Added an explicit Design Director stage between product thinking and reference research/implementation.
- Added visual identity, design rationale, anti-generic, transformation, and design ambition gates.
- Split quality acceptance into Engineering, UX, Visual, and Transformation gates.
- Expanded reference research into category selection and synthesis instead of a list of admired products.
- Expanded dataset case schema with design direction, BEFORE/AFTER evidence, candidate lessons, and skill gaps.
- Added a gap analysis that preserves the historical CASE-0001 boundary without rewriting or recreating missing evidence.

The v0.1.0 process could detect many engineering and usability defects but could still accept a generic-looking interface. v0.2.0 addresses that gap by requiring a defensible visual thesis before substantial implementation and evidence of identity and transformation after rendering.

## 0.1.0 — 2026-08-22

- Initial portable frontend product engineer skill.
- Added CREATE, REDESIGN, EXTEND, and REVIEW workflows.
- Added browser-first evidence rules, viewport matrix, content stress tests, accessibility guidance, and P0–P3 quality gates.
- Added curated knowledge, reference research, capability map, technology radar, dataset case mechanism, installer, sync, and doctor scripts.
- Added Codex and Claude Code installation documentation based on current official documentation.
