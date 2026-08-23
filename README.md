# frontend-product-engineer

Portable Agent Skill for product-minded frontend work across Codex and Claude Code.

It provides a repeatable process for:

- **CREATE** — define a visual direction before building a product or screen from zero.
- **REDESIGN** — understand the whole product, transform weak structure and visual language, and prove the BEFORE → AFTER result.
- **EXTEND** — add a feature while preserving and extending a good existing product personality.
- **REVIEW** — independently audit the rendered product without changing it.

The canonical source is GitHub. A local installation is a runtime copy, so the skill remains usable offline after synchronization.

## v0.2 design quality

v0.1.0 was strong at preventing broken or low-quality UI but could still accept generic enterprise SaaS. v0.2.0 adds an explicit role chain:

PRODUCT THINKER → DESIGN DIRECTOR → REFERENCE RESEARCHER → FRONTEND ENGINEER → VISUAL CRITIC → ENGINEERING QA → DATASET

The new Design Director defines visual identity, visual thesis, composition, rationale, references, synthesis, deliberate exclusions, and rendered acceptance criteria. The Visual Critic runs the anti-generic gate and design-ambition review. REDESIGN also runs the transformation gate. Engineering quality and design quality are separate requirements.

## Install

From a clone of this repository:

powershell:
  python scripts/install.py --agent all --scope global

Unix shell:
  python3 scripts/install.py --agent all --scope global

Install only one agent with --agent codex or --agent claude. Use --dry-run first to preview destinations. Project-level installation uses --scope project --project PATH and writes the agent-specific skill folder inside that project.

The installer uses the current local skill locations documented by Codex and Claude Code:

- Codex global: ~/.agents/skills/frontend-product-engineer/
- Codex project: <project>/.agents/skills/frontend-product-engineer/
- Claude global: ~/.claude/skills/frontend-product-engineer/
- Claude project: <project>/.claude/skills/frontend-product-engineer/

It never removes other skills. When an existing installation is updated, it creates a timestamped backup before merging the new files.

## Use the skill

In Codex CLI or the IDE extension, run /skills to see it or mention $frontend-product-engineer. In Claude Code, use /frontend-product-engineer or describe a frontend CREATE, REDESIGN, EXTEND, or REVIEW task. Explicit invocation is recommended for an important workflow.

Example CREATE request:

$frontend-product-engineer Create a responsive customer directory. Use CREATE mode, establish a Design Director direction, synthesize problem-relevant references, and do not stop before browser evidence and all quality gates.

Example REVIEW request:

/frontend-product-engineer Review the rendered settings screen independently. Run the Visual Critic and anti-generic gate; do not change code. Report Engineering, UX, Visual, and Transformation findings with evidence.

## Update and diagnose

powershell:
  python scripts/sync.py --check
  python scripts/sync.py --update
  python scripts/install.py --agent all --scope global
  python scripts/doctor.py

Unix shell:
  python3 scripts/sync.py --check
  python3 scripts/sync.py --update
  python3 scripts/install.py --agent all --scope global
  python3 scripts/doctor.py

sync --check does not alter the working tree. sync --update refuses to overwrite a dirty Git worktree and uses fast-forward-only updates. If GitHub is unavailable, the installed skill and local copy remain usable.

## Knowledge model

Curated repository knowledge contains durable principles, workflows, references, anti-patterns, lessons, benchmark cases, and a technology radar. Live external knowledge contains current package APIs, versions, browser behavior, and deprecations. The skill consults the latter only when needed and never treats this repository as a versioned API manual.

## Dataset cases and skill gaps

Create a new experience-memory case without copying a product into this repository:

  python scripts/new_case.py "Supplydesk redesign"

The case schema now includes context, BEFORE evidence, design direction, references, implementation, reviewer findings, AFTER evidence, accepted state, candidate lessons, and a skill_gap describing which rule existed but failed or was missing. Cases are evidence and benchmarks, not ML training data. Do not rewrite historical evidence to make a later skill version look better.

## Technology radar and live docs

tech-radar/TECH_RADAR.md is a recommendation map, not a dependency manifest. Categories are ADOPT, TRIAL, ASSESS, WATCH, and HOLD. Add a source and dated rationale when changing a recommendation; never invent a current version number from memory.

For React, Next.js, Tailwind, shadcn/ui, Base UI, React Aria, Motion, TanStack, Storybook, Playwright, browser APIs, or other version-sensitive tools:

1. inspect the project’s installed version;
2. consult Context7 if it is actually available;
3. otherwise consult current official documentation;
4. check compatibility and deprecations;
5. only then implement.

Absence of Context7 is not an error and must not block the workflow.

## Repository layout

SKILL.md is deliberately short and routes into workflows/, knowledge/, and quality/ through progressive disclosure. The main v0.2 additions are knowledge/DESIGN_DIRECTOR.md, knowledge/VISUAL_IDENTITY.md, quality/ANTI_GENERIC_GATE.md, quality/TRANSFORMATION_GATE.md, and docs/CASE-0001-DESIGN-GAP.md.

## Scope boundary

This repository is framework-agnostic and contains no Supplydesk code or private project data. It is a reusable frontend process, not a replacement for the project’s own architecture, tests, security rules, or design decisions.

