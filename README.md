# front — Frontend Product Engineer

Portable Agent Skill for product-minded frontend work across Codex and Claude Code. The repository remains `frontend-product-engineer-skill`; the runtime skill name is `front`.

It provides a repeatable process for:

- **CREATE** — define a visual direction before building a product or screen from zero.
- **REDESIGN** — understand the whole product, transform weak structure and visual language, and prove the BEFORE → AFTER result.
- **EXTEND** — add a feature while preserving and extending a good existing product personality.
- **REVIEW** — independently audit the rendered product without changing it.

The canonical source is GitHub. A local installation is a runtime copy, so the skill remains usable offline after synchronization.

## v0.3 browser-first audit quality

v0.1.0 was strong at preventing broken or low-quality UI but could still accept generic enterprise SaaS. v0.2.0 added an explicit design-quality role chain. v0.3.0 makes the browser-first audit loop operational:

PRODUCT THINKER → DESIGN DIRECTOR → REFERENCE RESEARCHER → FRONTEND ENGINEER → VISUAL CRITIC → ENGINEERING QA → DATASET

The Design Director defines visual identity, visual thesis, composition, rationale, references, synthesis, deliberate exclusions, and rendered acceptance criteria. The Visual Critic runs the anti-generic gate and design-ambition review. The Audit Protocol adds project-context discovery, objective findings, runtime/console/network evidence, content stress, and an explicit audit → fix → verify → re-audit loop. Engineering quality and design quality are separate requirements.

## Install

From a clone of this repository:

powershell:
  python scripts/install.py --agent all --scope global --apply

Unix shell:
  python3 scripts/install.py --agent all --scope global --apply

Install only one agent with --agent codex or --agent claude. Use --plan (or the legacy alias --dry-run) first to preview destinations. --apply is required to write files. Project-level installation uses --scope project --project PATH and writes the agent-specific skill folder inside that project.

The installer uses the current local skill locations documented by Codex and Claude Code:

- Codex global: ~/.agents/skills/front/
- Codex project: <project>/.agents/skills/front/
- Claude global: ~/.claude/skills/front/
- Claude project: <project>/.claude/skills/front/

It never removes other skills or an older frontend-product-engineer installation. When the front installation already exists, it creates a timestamped backup before copying the new files.

## Use the skill

In Claude Code, invoke the skill with /front. In Codex CLI or the IDE extension, run /skills to see it or mention $front. You can also describe a frontend CREATE, REDESIGN, EXTEND, or REVIEW task when implicit invocation is enabled. Explicit invocation is recommended for an important workflow.

Example CREATE request:

$front Create a responsive customer directory. Use CREATE mode, establish a Design Director direction, synthesize problem-relevant references, and do not stop before browser evidence and all quality gates.

Example REVIEW request:

/front Review the rendered settings screen independently. Run the Visual Critic and anti-generic gate; do not change code. Report Engineering, UX, Visual, and Transformation findings with evidence.

## Update and diagnose

powershell:
  python scripts/sync.py --check
  python scripts/sync.py --update
  python scripts/install.py --agent all --scope global --apply
  python scripts/doctor.py

Unix shell:
  python3 scripts/sync.py --check
  python3 scripts/sync.py --update
  python3 scripts/install.py --agent all --scope global --apply
  python3 scripts/doctor.py

sync --check does not alter the working tree. sync --update refuses to overwrite a dirty Git worktree and uses fast-forward-only updates. If GitHub is unavailable, the installed skill and local copy remain usable.

## Knowledge model

Curated repository knowledge contains durable principles, workflows, references, anti-patterns, lessons, benchmark cases, and a technology radar. Live external knowledge contains current package APIs, versions, browser behavior, and deprecations. The skill consults the latter only when needed and never treats this repository as a versioned API manual.

## Dataset cases and skill gaps

Create a new experience-memory case without copying a product into this repository:

  python scripts/new_case.py "Customer directory redesign"

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

SKILL.md is deliberately short and routes into workflows/, knowledge/, and quality/ through progressive disclosure. The main v0.3 addition is quality/AUDIT_PROTOCOL.md, supported by project-context, runtime, content, objective-finding, and invocation updates.

## Scope boundary

This repository is framework-agnostic and contains no project code or private project data. It is a reusable frontend process, not a replacement for the project’s own architecture, tests, security rules, or design decisions.

