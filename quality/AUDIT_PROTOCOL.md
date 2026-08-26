# Browser-first audit protocol

This protocol is the mandatory quality loop for CREATE, REDESIGN, and EXTEND. REVIEW uses the same audit and reporting rules but does not implement fixes unless the user changes the request.

## Project context before the audit

Record the known context before choosing fixes:

- product, users, primary jobs, and critical flows;
- existing design language, tokens, components, and protected areas;
- business, technical, accessibility, and compatibility constraints;
- stack, installed versions, start command, test command, and project-specific acceptance criteria.

Unknowns stay marked as unknown or assumption. Do not invent product rules to make an audit look complete.

## Required loop

```text
INSPECT → PLAN → IMPLEMENT → RUN → BROWSER AUDIT → FIX → VERIFY → RE-AUDIT → DONE
```

For existing products, use this expanded sequence:

```text
INSPECT → RUN → BROWSER → AUDIT → OBJECTIVE FINDINGS
→ FIX P0/P1/P2 → RUN → BROWSER → VERIFY
→ INDEPENDENT REVIEW → RE-AUDIT → DONE
```

CREATE has no BEFORE state. REDESIGN requires matched BEFORE and AFTER evidence when the surface can be captured. EXTEND compares the affected neighboring surface when visual drift is a risk. REVIEW stops after findings and recommendations.

## Tool strategy and fallback

Use available project and browser tooling; never make the skill depend on one vendor:

- start the real app with its documented command;
- prefer Playwright for repeatable browser flows, screenshots, DOM inspection, and viewport changes;
- if Playwright is unavailable, use the available in-app or system browser tool;
- inspect DOM geometry, `scrollWidth`, clipping, overlap, focus targets, and intentional scroll containers when the browser permits;
- collect console errors, uncaught runtime errors, failed requests, and relevant network responses when the browser permits;
- run axe-core or another accessibility tool when available, then interpret findings with manual semantic and keyboard review;
- run the project’s tests, lint, typecheck, and build when present and relevant;
- consult current official technology documentation after checking the project’s installed versions; use Context7 when actually available.

If a tool or environment is unavailable, record the exact scope as `NOT VERIFIED`. Do not infer success from source code, a static screenshot, a passing build, or a self-score.

## Minimum audit checklist

### Visual hierarchy

- primary action and secondary actions;
- visual weight and information hierarchy;
- first, second, and third scan stops;
- scanability, focus, and visual noise.

### Layout

- alignment, spacing, padding, margins, grid, and container widths;
- consistency of meaningful edges and rhythm;
- overflow, clipping, unexpected scroll, overlap, and broken positioning;
- intentional scroll regions and whether their affordance is clear.

### Typography

- hierarchy, font size, line height, weight, contrast, and readable line length;
- numerals, labels, long text, multiline content, and localization expansion;
- truncation and wrapping behavior with a recoverable way to read hidden content.

### Component consistency

- buttons, links, inputs, forms, tables, cards, badges, dialogs, dropdowns, and icons;
- control heights, borders, radius, shadows, states, and semantic roles;
- repeated components that should share behavior or tokens.

### Responsive behavior

- desktop, tablet, mobile, and intermediate breakpoint transitions;
- navigation, toolbars, filters, tables, panels, and primary actions;
- horizontal overflow, clipped content, inaccessible controls, broken tables, and disappearing actions.

Default viewport matrix:

| Viewport | Purpose |
| --- | --- |
| 1920×1080 | wide composition and max-width behavior |
| 1440×900 | common desktop baseline |
| 1280×800 | dense desktop and breakpoint pressure |
| 1024×768 | medium-width workflow safety |
| ~768px | tablet transition |
| 390×844 | narrow mobile flow |

Adapt the matrix to the product and add intermediate widths where the layout changes.

### Interaction and states

Check the relevant hover, focus, active/pressed, selected, disabled, loading, empty, error, success, confirmation, permission, recovery, and destructive-action states. Verify trigger, feedback, result, cancellation, and recovery, not only the resting state.

### Accessibility

- semantic HTML, headings, landmarks, lists, tables, buttons, and links;
- accessible names and labels for every control;
- keyboard order, activation, escape behavior, focus return, and visible focus;
- text, control, focus, and status contrast;
- field errors associated and announced appropriately;
- no information conveyed by color alone;
- reduced-motion, zoom, and reflow behavior;
- automated results plus manual review where possible.

### Content robustness

Stress the real UI with long names, long emails, long URLs, large numbers, multiline text, missing values, many tags, long roles/titles, and supported locale expansion. Record whether values wrap, truncate, overflow, or preserve an accessible recovery path.

### Runtime and regression

Verify the critical user flow after launch and again after fixes. Record console/runtime errors, failed network requests, data-loading failures, and visible recovery. Repeat relevant tests, lint, typecheck, build, and neighboring-flow checks. A clean source diff is not runtime evidence.

## Objective finding format

Every material finding must be actionable and evidence-backed:

```text
ID: FE-014
Title: Inconsistent card spacing
Severity: P2
Location: route, state, viewport, and component/region
Actual: Three instances use different internal padding.
Problem: The same component creates an inconsistent visual rhythm and slows scanning.
Expected: Instances use the existing spacing system consistently.
Constraints: Preserve business behavior and the project’s established component API.
Acceptance Criteria:
- all instances use the agreed spacing token;
- no overflow or visual regression at required viewports;
- no new console/runtime/network errors.
Evidence: screenshot path, browser/DOM measurement, or test output
```

Do not create findings such as “make cards look better.” Convert them into observable actual behavior, user impact, expected behavior, constraints, acceptance criteria, and evidence.

## Release disposition

- P0 — broken or unusable; zero before DONE.
- P1 — serious usability, accessibility, layout, runtime, or product defect; zero before DONE.
- P2 — noticeable quality defect; fix before DONE unless an explicit trade-off is accepted and documented.
- P3 — minor polish opportunity; may remain only when documented.

Evidence must match the claim: screenshots for visual and responsive claims, browser/DOM evidence for layout claims, console/network evidence for runtime claims, automated plus manual evidence for accessibility claims, and explicit stress cases for content robustness.

The final report must include Mode, Scope, Changed, Evidence, Viewport coverage, Findings, Fixed, Remaining, Not verified, and Regression. Never write “everything looks good” without evidence.
