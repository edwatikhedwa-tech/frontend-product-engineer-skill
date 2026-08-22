"""Create a compact, non-destructive experience-memory case skeleton."""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

from _common import REPO_ROOT


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized.lower()).strip("-")
    return slug or "case"


def next_number(root: Path) -> int:
    numbers = []
    for path in root.iterdir() if root.exists() else []:
        match = re.match(r"CASE-(\d{4})-", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a dataset case skeleton.")
    parser.add_argument("title", help="Short case title, for example 'Supplydesk redesign'.")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = REPO_ROOT / "dataset" / "cases"
    number = next_number(root)
    case = root / f"CASE-{number:04d}-{slugify(args.title)}"
    print(f"Case: {case.relative_to(REPO_ROOT)}")
    if case.exists():
        print(f"[ERROR] Case already exists: {case}")
        return 2
    if args.dry_run:
        print("[PLAN] Would create README.md, review.md, lessons.md, and evidence directories.")
        return 0

    case.mkdir(parents=True)
    (case / "README.md").write_text(
        f"# {case.name}\n\n"
        "Purpose, scope, product context, and evidence links. Keep private project data out of this repository.\n",
        encoding="utf-8",
    )
    for directory in ("before", "attempt", "accepted"):
        path = case / directory
        path.mkdir()
        (path / "README.md").write_text(
            f"# {directory.title()} evidence\n\nAdd only selected, permission-safe evidence for this case.\n",
            encoding="utf-8",
        )
    (case / "review.md").write_text(
        "# Review\n\nRecord viewport, state, evidence, P0/P1/P2/P3 findings, and re-check results.\n",
        encoding="utf-8",
    )
    (case / "lessons.md").write_text(
        "# Lessons\n\nExtract only framework-agnostic, evidence-backed rules. Deduplicate against knowledge/LESSONS.md and knowledge/ANTI_PATTERNS.md.\n",
        encoding="utf-8",
    )
    print(f"[OK] Created {case}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
