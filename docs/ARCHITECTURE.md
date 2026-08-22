# Architecture

## Canonical source and runtime copies

GitHub is the canonical source of truth. A clone is the editable source bundle. A global or project installation is a copied runtime bundle for Codex or Claude Code. The skill does not download GitHub before every frontend task.

## Progressive disclosure

The host first sees the `SKILL.md` frontmatter and concise routing instructions. When the skill is selected, it reads the root instructions. The root then routes to one workflow and only the specialist knowledge and quality documents relevant to the task. Dataset cases and the full radar are not loaded by default.

## Cross-agent portability

The content uses the shared `SKILL.md` format. Codex-specific UI metadata is isolated in `agents/openai.yaml`; Claude ignores it as an ordinary supporting file. Installation paths are selected by `scripts/install.py` from the official agent documentation, not hard-coded into the skill’s operating rules.

## Knowledge split

- Curated: principles, workflow, anti-patterns, lessons, reference methods, radar, and benchmark cases.
- Live: installed versions, API details, browser behavior, deprecations, and external documentation.

This split prevents durable design knowledge from becoming stale API documentation.

## Safety boundaries

Scripts use the standard library, do not execute remote code, do not install frontend dependencies, do not delete other skills, and refuse unsafe Git updates when the working tree is dirty. No project code or secrets are part of this repository.
