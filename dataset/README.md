# Dataset / experience memory

This dataset is evidence, benchmark material, and accumulated experience—not ML training data. Cases should be small enough to review and useful enough to generalize.

## Case format

Each case should capture the chain that produced the result:

dataset/cases/CASE-XXXX-short-name/

- README.md — context, product job, users, constraints, scope, and success criteria.
- before/ — selected BEFORE screenshots or safe links; optional for CREATE.
- design-direction.md — visual identity, thesis, rationale, chosen references, synthesis, and acceptance criteria.
- references.md — reference categories, analysis, adaptation, and deliberate non-copy.
- attempt/ — selected implementation evidence or notes.
- review.md — Visual Critic and Engineering QA findings, severity, evidence, and fixes.
- accepted/ — final AFTER screenshots or safe links.
- lessons.md — candidate lessons, deduplicated before promotion.
- skill-gaps.md — which rule existed but failed, was too abstract, or was missing.

The before/attempt/accepted folders may contain a short README instead of large assets. Keep only the most useful evidence; optimize large files or use Git LFS when there is a real need. Never add secrets or private project data.

## Case questions

Every useful case should answer:

- What was the product job and context?
- What did BEFORE evidence show?
- What was the Design Director direction and rationale?
- Which reference categories were chosen, and how were they synthesized?
- What was implemented and why?
- What did the Visual Critic reject?
- What did Engineering QA verify?
- What changed from BEFORE to AFTER?
- What was accepted and what remained P3?
- What universal lesson is a candidate?
- Which skill rule existed but failed to produce the desired result? Record this as skill_gap.

## Learning loop

case → analyze → extract general lesson → deduplicate → update LESSONS/ANTI_PATTERNS → record skill gap

Do not turn a project-specific workaround into a universal rule without evidence and a clear boundary. Do not rewrite historical case evidence to make a later version look better.

