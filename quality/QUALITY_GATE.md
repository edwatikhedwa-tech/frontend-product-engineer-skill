# Quality gate

The quality gate is mandatory after implementation and before DONE.

## Evidence checklist

- [ ] The real application was run.
- [ ] Important screens were opened in a real browser when possible.
- [ ] Screenshots cover relevant widths: 1920, 1440, 1280, 1024, tablet, and 390 where applicable.
- [ ] Intermediate desktop behavior was inspected.
- [ ] Realistic content and stress content were tested.
- [ ] DOM/browser overflow and clipping were checked where tooling permits.
- [ ] Keyboard, focus, semantics, labels, and contrast were reviewed.
- [ ] Automated accessibility checks were run when justified and available.
- [ ] The rendered result was reviewed independently after implementation.
- [ ] A second screenshot/recheck cycle followed fixes.

## Defect gate

- P0: 0
- P1: 0
- P2: fixed or explicitly accepted with reason
- P3: may remain with a documented tradeoff

If a checkbox cannot be checked, say “not verified” in the handoff. Never replace missing evidence with a confidence score.
