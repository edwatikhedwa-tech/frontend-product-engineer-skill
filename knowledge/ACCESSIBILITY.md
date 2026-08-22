# Accessibility

Minimum review:

- semantic headings, landmarks, lists, tables, buttons, and links;
- labels and accessible names for every control;
- keyboard order, activation, escape behavior, and visible focus;
- contrast for text, controls, focus indicators, and status colors;
- errors associated with fields and announced appropriately;
- no information conveyed by color alone;
- reduced-motion behavior for non-essential animation;
- sensible zoom and reflow behavior;
- manual review in addition to axe-core or another automated tool.

Prefer HTML semantics. Add ARIA only when native semantics cannot express the interaction, and verify the resulting accessibility tree. Treat automated findings as evidence to interpret, not as the entire audit.
