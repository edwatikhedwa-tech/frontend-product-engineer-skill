# CASE-0001 design-system gap analysis

## Evidence boundary

The canonical v0.1.0 checkout available during the v0.2.0 update contains no `dataset/cases/CASE-0001-supplydesk-redesign/`, `review.md`, or `lessons.md`. The Supplydesk repository also contains no matching case artifact. Therefore the historical case cannot be independently inspected here and is not recreated from memory.

The maintainer supplied this benchmark summary: v0.1.0 successfully enforced real-app execution, browser evidence, responsive and overflow checks, content stress, independent review, P0/P1/P2 fixes, and dataset creation; the resulting redesign remained too close to generic enterprise SaaS/admin UI. The summary is recorded as user-provided evidence, not as a locally verified case file.

## Confirmed from v0.1.0 repository

- Browser, responsive, overflow, accessibility, content-stress, severity, and independent-review rules exist.
- `DESIGN_DIRECTION.md` asks for personality, hierarchy, density, typography, surfaces, responsive strategy, states, motion, and references.
- `QUALITY_GATE.md` requires rendered evidence and defect severity, but has no separate engineering/UX/visual/transformation gates.
- `REVIEW_SCORECARD.md` includes hierarchy, typography, spacing, density, polish, and content robustness, but not a distinct identity, art direction, distinctiveness, or transformation decision.
- CREATE and REDESIGN both mention design direction, but neither defines a Design Director decision artifact or a required rationale chain.
- Reference research asks for problem-based analysis, but does not require category selection or synthesis into a new visual system.

## Inference

The v0.1.0 process was strong at detecting broken or low-quality outcomes, but its acceptance language was largely defect-oriented. A defect-free interface could therefore pass without proving a visual thesis, a recognizable identity, a deliberate composition, or a meaningful redesign transformation.

## Candidate lesson

An engineering-quality gate cannot substitute for a design-quality gate. Before substantial implementation, require a Design Director artifact with rationale, reference synthesis, and identity criteria; after rendering, independently test whether the result is generic and whether a redesign materially transformed the relevant dimensions.

## v0.2.0 response

- `knowledge/DESIGN_DIRECTOR.md` makes the role and decision artifact explicit.
- `knowledge/VISUAL_IDENTITY.md` operationalizes identity without requiring novelty.
- `quality/ANTI_GENERIC_GATE.md` fails template-derived outcomes and routes them back to Design Director.
- `quality/TRANSFORMATION_GATE.md` requires matched BEFORE → AFTER reasoning for REDESIGN.
- `quality/QUALITY_GATE.md` separates Engineering, UX, Visual, and Transformation gates.
- CREATE now requires Design First before substantial implementation; REDESIGN must prove systemic transformation or justified preservation.
