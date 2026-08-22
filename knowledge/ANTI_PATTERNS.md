# AI Frontend Anti-Patterns

Use this as a detection and repair checklist. For each anti-pattern, identify **WHY BAD**, **HOW TO DETECT**, and **HOW TO FIX**.

| Anti-pattern | Why bad | How to detect | How to fix |
| --- | --- | --- | --- |
| Card soup | Every region becomes a container, so nothing is prioritized. | Count nested cards and ask whether each boundary carries meaning. | Use alignment, spacing, and only meaningful surfaces. |
| Badge soup | Status treatment becomes visual noise. | Many badges compete with titles and actions. | Reserve badges for compact, scannable states; use text or hierarchy elsewhere. |
| Border soup | Borders fragment the reading flow. | Repeated lines appear around every row, field, and section. | Remove low-value borders; use rhythm, grouping, and selective dividers. |
| Excessive rounded rectangles | Every element has the same shape and loses semantic distinction. | Inputs, buttons, cards, tags, and headings all share a pill/box silhouette. | Match radius and shape to interaction and hierarchy. |
| Everything inside containers | Layout mirrors DOM nesting instead of user mental models. | Large parts of the page are boxed without a task reason. | Let content share a plane when separation is not needed. |
| Weak hierarchy | The user cannot tell where to begin or what matters. | Blur/zoom the screenshot and all text still looks equal. | Establish primary action, title, content order, and secondary layers. |
| Same visual importance | Metadata and decisions compete with core content. | Scan test has no clear first, second, or third stop. | Tune scale, weight, contrast, position, and spacing. |
| Random shadows | Shadows imply false layering and add noise. | Shadows appear without a real elevation relationship. | Use elevation only for overlays, floating surfaces, or clear focus. |
| Excessive gradients | Decoration competes with product content and ages quickly. | Gradient is not communicating state, depth, or brand purpose. | Remove it or limit it to a deliberate focal region. |
| Tiny secondary text | Important context becomes inaccessible and unreadable. | Metadata fails at mobile width or zoom. | Increase size/contrast or reduce the information shown. |
| Giant unused whitespace | The user loses context and operational density. | Large empty areas do not support focus or breathing room. | Rebalance layout and content; keep purposeful whitespace. |
| Excessive whitespace in data-heavy tools | Frequent scanning requires unnecessary scrolling. | Key rows and controls cannot fit in a working viewport. | Tune density while protecting row clarity and hit targets. |
| Unnecessary uppercase | Long uppercase labels are slower to read. | Labels are all caps without a real convention reason. | Use sentence case; reserve uppercase for compact, short metadata. |
| Excessive pills | Every action looks like a tag or filter. | Many pill shapes have no semantic distinction. | Use buttons, links, text, or plain controls according to meaning. |
| Too many action buttons | Decision cost and misclick risk increase. | Toolbar has many equal-weight actions. | Keep the primary action; group, defer, or menu secondary actions. |
| Arbitrary accent colors | Color stops encoding consistent meaning. | Accents change by component with no token or semantic rule. | Define semantic tokens and use color sparingly. |
| Decorative icons without value | Icons add visual and cognitive noise. | Removing an icon loses no meaning or affordance. | Remove it or pair it with a clear accessible label. |
| Fake premium styling | Surface effects substitute for product quality. | Blur, glow, and gradients carry the design while workflow remains unclear. | Repair hierarchy, content, states, and interaction first. |
| Dribbble-first design | A static composition is mistaken for a usable product. | No realistic states, content, or interaction evidence. | Start from jobs and real flows; judge the browser result. |
| Landing-page patterns in operational SaaS | Marketing composition harms scanning and task completion. | Hero blocks, oversized claims, or decorative cards dominate a work tool. | Optimize for workflow, density, and repeat use. |
| Fixed narrow columns for unpredictable content | Long names and values clip or destroy alignment. | Stress content overflows or forces unreadable truncation. | Use flexible tracks, wrapping, min/max widths, and intentional truncation. |
| Clipping and overflow | Information or controls become unreachable. | DOM/browser checks show clipping or unexpected horizontal scroll. | Fix constraints; keep only intentional scroll containers. |
| Inconsistent spacing | The product feels accidental and scanning slows. | Same relationships use unrelated gaps. | Consolidate to a spacing scale and explicit exceptions. |
| Inconsistent control heights | Mixed controls make the interface feel broken. | Buttons, inputs, selects, and rows do not align. | Define control tokens and verify states. |
| Poor line lengths | Reading and comprehension suffer. | Prose spans the full desktop canvas or is too narrow. | Set readable max widths and responsive behavior. |
| Poor empty states | Users cannot tell whether the system is broken or what to do. | Empty screen has no explanation or next step. | Explain cause, value, and the useful next action. |
| Poor loading states | Layout shifts and users lose confidence. | Spinner replaces structure or content jumps. | Preserve geometry with skeletons or staged feedback. |
| Missing error states | Failure paths are invisible until production. | Network, validation, permission, and recovery are unhandled. | Define message, location, retry, and preserved user input. |
| Desktop merely shrunk to mobile | Controls and hierarchy fail on small screens. | Tiny columns, off-screen actions, or horizontal scroll appear. | Redesign the information and interaction strategy for the viewport. |
| Tables unusable at medium widths | Important workflows break before mobile. | 1024/1280 screenshots show clipping or impossible scanning. | Prioritize columns, allow responsive detail views, and test intermediate widths. |
| Overly dense B2B interface | Users miss meaning and actions. | Every pixel is occupied; grouping and focus disappear. | Reduce competition, improve rhythm, and keep useful density. |
| Overly sparse B2B interface | Routine work requires needless scrolling. | One small data point occupies a large canvas. | Consolidate related information and tune density to the job. |
| Visual polish without IA | Surface quality hides a weak workflow. | Beautiful components still do not support the user’s job. | Return to product thinking and information architecture. |
| Change colors/radius only | The same bad layout remains. | Restyle pass changes tokens but not task flow or hierarchy. | Fix structure, content priority, responsive strategy, and states. |
