# Review

## Product and stack

Supplydesk is a static HTML interface backed by a Python ThreadingHTTPServer, SQLite-backed workspace data, and inline JavaScript. No frontend framework migration or runtime dependency was added.

## Routes discovered

- Dashboard
- Supplier search results for a request
- Requests list and request detail
- Supplier database
- Correspondence and incoming messages
- Blacklist
- Mail settings, login, request creation, mail composer, and message dialogs

## Before findings

- The content area read as a stack of equally weighted rounded cards.
- Search controls, result cards, contact details, and request context competed for attention.
- Mobile actions consumed the first viewport before the supplier list became useful.
- Correspondence could remain on a loading state while mail synchronization waited on a slow provider response.
- Intermediate widths needed an explicit hierarchy instead of a squeezed desktop arrangement.

## Design direction

Operations workbench: graphite navigation rail, quiet cool canvas, compact command bar, cobalt primary actions, restrained surfaces, divider-led lists, and request context available while reviewing suppliers.

## References

- https://knowledge.hubspot.com/records/view-and-filter-records-in-the-updated-index-page
- https://learn.microsoft.com/en-us/power-apps/user/modern-fluent-design
- https://help.salesforce.com/s/articleView?id=basics_understanding_list_views_lex.htm&language=en_US&type=5

## First implementation reviewer findings

- P1: correspondence still blocked the whole route behind a provider synchronization call.
- P2: mobile actions were too vertically stacked.
- P2: nested card treatment made search and workspace screens feel like generic admin UI.

## Second pass changes

- Added a bounded mail sync wait and a non-blocking sync banner; saved correspondence renders when sync is slow or fails.
- Reworked shared surfaces into a KPI strip, command band, divider-led lists, reduced elevation, and explicit request-context placement.
- Reworked mobile controls into a two-column action grid and moved request context above results at medium widths.
- Added aria-current navigation state and closes the mobile rail after navigation.

## QA evidence

- Browser smoke: local app loaded at HTTP 200; dashboard, requests, suppliers, correspondence, blacklist, and search navigation worked.
- Search flow: filtering reduced visible cards; select-all checked 7 filtered records and enabled export/send actions.
- Dialogs: request creation, mail settings, and composer opened with labelled fields and closed without submitting.
- Correspondence loaded without a persistent spinner, showed 2 thread cards, and showed a sync status banner with no console errors.
- Overflow: scrollWidth matched clientWidth at 1920, 1440, 1280, 1024, 768, and 390 viewports.
- Content stress: long Russian names, long emails, missing fields, and multiline message text stayed inside their containers.
- Accessibility review: no unlabeled inputs and no unnamed buttons were found in inspected states; visible focus was present.

## Defect gate

- P0: 0
- P1: 0
- P2: fixed
- P3: optional future work — consolidate legacy style layers and replace text-glyph icons with a formal SVG icon set.

## Not verified

Automated axe was not run because the repository has no axe dependency and pytest is not installed. Live Yandex OAuth and outbound email delivery were not exercised; no message was sent.
