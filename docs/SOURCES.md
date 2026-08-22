# Official sources checked

Access date: 2026-08-22.

## Agent Skill formats and locations

- OpenAI / Codex — Build skills: https://developers.openai.com/codex/skills/ (redirects to the current ChatGPT Learn documentation at `https://learn.chatgpt.com/docs/build-skills`). Confirmed `SKILL.md` with `name` and `description`, optional scripts/references/assets, progressive disclosure, explicit `$skill` invocation, repository `.agents/skills`, user `~/.agents/skills`, and optional `agents/openai.yaml`.
- Anthropic / Claude Code — Extend Claude with skills: https://docs.anthropic.com/en/docs/claude-code/skills (current page at `https://code.claude.com/docs/en/skills`). Confirmed `SKILL.md` with YAML frontmatter, supporting files, progressive loading, personal `~/.claude/skills/<name>/`, project `.claude/skills/<name>/`, `/skill-name` invocation, and the portable Agent Skills standard.
- Agent Skills open standard: https://agentskills.io/specification

## Frontend technology sources

- React: https://react.dev/reference/react
- Next.js: https://nextjs.org/docs
- Tailwind CSS: https://tailwindcss.com/docs
- shadcn/ui: https://ui.shadcn.com/docs
- Base UI: https://base-ui.com/react/overview/quick-start
- React Aria: https://react-aria.adobe.com/
- Motion: https://motion.dev/docs
- TanStack Table: https://tanstack.com/table/latest/docs/introduction
- Storybook: https://storybook.js.org/docs
- Playwright: https://playwright.dev/docs/intro
- axe-core: https://www.deque.com/axe/core-documentation/
- Context7: https://context7.com/docs/overview

## Implementation implications

The repository keeps one portable root `SKILL.md`. Codex and Claude both support that shape, while each agent has its own local discovery directory. The installer copies the full bundle into the correct agent folder and includes Codex’s optional `agents/openai.yaml` metadata. No vendor-specific runtime dependency is required.
