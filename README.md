# frontend-product-engineer

Portable Agent Skill for product-minded frontend work across Codex and Claude Code.

It provides a repeatable process for:

- **CREATE** — build a product or screen from zero.
- **REDESIGN** — understand and improve an existing interface systemically.
- **EXTEND** — add a feature while preserving a good existing visual language.
- **REVIEW** — independently audit the rendered product without changing it.

The canonical source is GitHub. A local installation is a runtime copy, so the skill remains usable offline after synchronization.

## Install

From a clone of this repository:

```powershell
python scripts/install.py --agent all --scope global
```

```bash
python3 scripts/install.py --agent all --scope global
```

Install only one agent with `--agent codex` or `--agent claude`. Use `--dry-run` first to preview destinations. Project-level installation uses `--scope project --project PATH` and writes the agent-specific skill folder inside that project.

The installer uses the current local skill locations documented by Codex and Claude Code:

- Codex global: `~/.agents/skills/frontend-product-engineer/`
- Codex project: `<project>/.agents/skills/frontend-product-engineer/`
- Claude global: `~/.claude/skills/frontend-product-engineer/`
- Claude project: `<project>/.claude/skills/frontend-product-engineer/`

It never removes other skills. When an existing installation is updated, it creates a timestamped backup before merging the new files.

## Use the skill

In Codex CLI or the IDE extension, run `/skills` to see it or mention `$frontend-product-engineer`. In Claude Code, use `/frontend-product-engineer` or describe a frontend CREATE, REDESIGN, EXTEND, or REVIEW task. Explicit invocation is recommended for an important workflow.

Examples:

```text
$frontend-product-engineer Create a responsive customer directory from this product brief. Use CREATE mode and do not stop before browser screenshots and the quality gate.
```

```text
/frontend-product-engineer Review the rendered settings screen independently. Do not change code; report P0/P1/P2/P3 findings with evidence.
```

## Update and diagnose

```powershell
python scripts/sync.py --check
python scripts/sync.py --update
python scripts/doctor.py
```

```bash
python3 scripts/sync.py --check
python3 scripts/sync.py --update
python3 scripts/doctor.py
```

`sync --check` does not alter the working tree. `sync --update` refuses to overwrite a dirty Git worktree and uses fast-forward-only updates. If GitHub is unavailable, the installed skill and local copy remain usable.

## Knowledge model

Curated repository knowledge contains durable principles, workflows, references, anti-patterns, lessons, benchmark cases, and a technology radar. Live external knowledge contains current package APIs, versions, browser behavior, and deprecations. The skill consults the latter only when needed and never treats this repository as a versioned API manual.

## Dataset cases and lessons

Create a new experience-memory case without copying a product into this repository:

```powershell
python scripts/new_case.py "Supplydesk redesign"
```

The script creates a `CASE-XXXX-short-name` skeleton under `dataset/cases/`. Cases are evidence and benchmarks, not ML training data. After reviewing a useful case, condense only reusable rules into `knowledge/LESSONS.md` or `knowledge/ANTI_PATTERNS.md`.

## Technology radar

`tech-radar/TECH_RADAR.md` is a recommendation map, not a dependency manifest. Categories are ADOPT, TRIAL, ASSESS, WATCH, and HOLD. Add a source and a dated rationale when changing a recommendation; never invent a current version number from memory.

## Live documentation and Context7 fallback

For React, Next.js, Tailwind, shadcn/ui, Base UI, React Aria, Motion, TanStack, Storybook, Playwright, browser APIs, or other version-sensitive tools:

1. inspect the project’s installed version;
2. consult Context7 if it is actually available;
3. otherwise consult current official documentation;
4. check compatibility and deprecations;
5. only then implement.

Absence of Context7 is not an error and must not block the workflow.

## Repository layout

`SKILL.md` is deliberately short and routes into `workflows/`, `knowledge/`, and `quality/` through progressive disclosure. `scripts/` contains deterministic portable installation, synchronization, diagnosis, and case scaffolding. `docs/SOURCES.md` records the official documentation checked when this repository was bootstrapped.

## Scope boundary

This repository is framework-agnostic and contains no Supplydesk code or private project data. It is a reusable frontend process, not a replacement for the project’s own architecture, tests, security rules, or design decisions.
