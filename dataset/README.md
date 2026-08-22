# Dataset / experience memory

This dataset is evidence, benchmark material, and accumulated experience—not ML training data. Cases should be small enough to review and useful enough to generalize.

## Case format

```text
dataset/cases/CASE-XXXX-short-name/
├── README.md
├── before/
├── attempt/
├── accepted/
├── review.md
└── lessons.md
```

Screenshots and assets are optional. Keep only the most useful evidence; optimize large files or use Git LFS when there is a real need. Never add secrets or private project data.

After a case:

```text
case → analyze → extract general lesson → deduplicate → update LESSONS/ANTI_PATTERNS
```

Do not turn a project-specific workaround into a universal rule without evidence and a clear boundary.
