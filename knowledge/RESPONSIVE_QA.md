# Responsive QA

Responsive behavior is a content and interaction design problem, not desktop shrinkage.

For important screens inspect `1920x1080`, `1440x900`, `1280x800`, `1024x768`, relevant tablet width around `768`, and `390x844`, plus any intermediate width where the layout changes.

At each width verify:

- hierarchy and primary actions remain clear;
- navigation, toolbars, tables, filters, and detail panels have an intentional strategy;
- controls remain tappable and keyboard reachable;
- text wraps or truncates with a deliberate affordance;
- no accidental horizontal scroll, clipping, overlap, or off-screen focus target;
- intentional scroll containers are understandable;
- density adapts without hiding essential meaning.

Use browser evidence, not CSS inspection alone.
