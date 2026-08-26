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
    parser.add_argument("title", help="Short case title, for example 'Customer directory redesign'.")
    parser.add_argument("--root", type=Path, help="Override the cases directory for testing or a separate dataset.")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = (args.root or (REPO_ROOT / "dataset" / "cases")).resolve()
    if not args.dry_run:
        root.mkdir(parents=True, exist_ok=True)
    number = next_number(root)
    case = root / f"CASE-{number:04d}-{slugify(args.title)}"
    display_case = case.relative_to(REPO_ROOT) if case.is_relative_to(REPO_ROOT) else case
    print(f"Case: {display_case}")
    if case.exists():
        print(f"[ERROR] Case already exists: {case}")
        return 2
    if args.dry_run:
        print("[PLAN] Would create context, design-direction, references, implementation, review, accepted, lessons, and skill-gap templates.")
        return 0

    case.mkdir(parents=True)
    (case / "README.md").write_text(
        f"# {case.name}\n\n"
        "Context, product job, users, constraints, scope, success criteria, and evidence links. Keep private project data out of this repository.\n",
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
        "# Review\n\nRecord Visual Critic and Engineering QA findings, viewport/state evidence, P0/P1/P2/P3 severity, fixes, and re-check results.\n",
        encoding="utf-8",
    )
    (case / "design-direction.md").write_text(
        "# Design direction\n\nRecord product personality, visual identity paragraph, visual thesis, hierarchy, composition, typography, density, surfaces, interaction, motion, rationale, reference synthesis, deliberate exclusions, and rendered acceptance criteria.\n",
        encoding="utf-8",
    )
    (case / "references.md").write_text(
        "# References\n\nRecord selected categories, problem solved, transferable principle, adaptation, and deliberate non-copy. End with a product-specific synthesis.\n",
        encoding="utf-8",
    )
    (case / "lessons.md").write_text(
        "# Lessons\n\nRecord candidate lessons only. Extract framework-agnostic, evidence-backed rules and deduplicate against knowledge/LESSONS.md and knowledge/ANTI_PATTERNS.md.\n",
        encoding="utf-8",
    )
    (case / "skill-gaps.md").write_text(
        "# Skill gaps\n\nWhich rule existed but failed to produce the desired result? Which rule was too abstract, missing, or contradicted by another rule? Record evidence and a proposed vNext change.\n",
        encoding="utf-8",
    )
    print(f"[OK] Created {case}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
