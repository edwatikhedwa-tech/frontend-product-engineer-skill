# CANDIDATE LESSONS FOR REVIEW

These are observations from CASE-0001 only. They are not universal skill rules.

1. For data-heavy routes, reduce card nesting before changing color or typography; divider-led lists make primary content easier to scan.
2. Treat external synchronization as a bounded side effect. Render cached/local content first and expose a retryable status instead of blocking the entire route.
3. Medium desktop widths need their own hierarchy rule. Moving supporting context above the primary list can be more useful than squeezing a two-column layout.
4. Mobile bulk actions should be composed as an intentional action grid, not a desktop flex row that happens to wrap.
5. A visual acceptance gate needs both route-level screenshots and state-level screenshots for dialogs, loading, and error behavior.
