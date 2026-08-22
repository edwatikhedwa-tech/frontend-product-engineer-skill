# Technology radar

This radar is a recommendation map, not a dependency manifest. Status means how deliberately the skill should consider a capability, not that every project should install it.

| Area | Technology/capability | Status | Decision rule |
| --- | --- | --- | --- |
| UI foundation | React | ADOPT | Use when the project’s architecture calls for component-based UI; verify the installed version. |
| Full-stack React | Next.js | ASSESS | Consider for routing, server/client boundaries, and full-stack needs; do not migrate casually. |
| Styling | Tailwind CSS | ASSESS | Use existing project conventions or a real token/composition need. |
| UI source components | shadcn/ui | ASSESS | Consider source-owned primitives when they fit the project’s accessibility and ownership model. |
| UI primitives | Base UI | ASSESS | Consider for complex accessible primitives after checking compatibility. |
| Accessibility behavior | React Aria | ASSESS | Consider when accessible interaction behavior is the main problem. |
| Animation | Motion | ASSESS | Use for gestures, springs, shared layout, or complex sequencing; use CSS for simple transitions. |
| Tables | TanStack Table | ASSESS | Consider for complex sorting, filtering, selection, pagination, or state. |
| Component lab | Storybook | TRIAL | Add when the component/state surface benefits from isolation and repeatable review. |
| Browser QA | Playwright | ADOPT | Prefer when a real browser flow, screenshot, or visual regression needs automation. |
| Accessibility automation | axe-core | TRIAL | Use as a signal alongside manual semantics, keyboard, and focus review. |
| Live documentation | Context7 | ASSESS | Use when the integration is available; otherwise use official docs. |
| Visual research | product/UX references | ADOPT | Search by product problem and record reasoning; never pixel-copy. |
| Agent skills | Agent Skills standard | ADOPT | Keep `SKILL.md` portable and progressive; use agent-specific metadata only when supported. |
| Browser QA integrations | browser automation tools | WATCH | Use what is actually available in the environment; record missing evidence. |
| Design-to-code | project-approved tooling | WATCH | Assess based on fidelity, ownership, accessibility, and maintainability—not novelty. |
| MCP | project-approved documentation/tools | WATCH | Connect only with explicit scope, official source, and least privilege. |

## Update protocol

When changing a status, add the source URL, access date, observed capability, and a short reason. Do not add “latest” versions from memory. Version-specific implementation still follows the live-docs protocol in `knowledge/LIBRARY_SELECTION.md`.
