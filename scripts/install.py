"""Install the portable skill into Codex and/or Claude Code skill locations."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path

from _common import REPO_ROOT, SKILL_NAME, display_path, home_path, iter_bundle_files, read_version, sha256


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install frontend-product-engineer for Codex and/or Claude Code.")
    parser.add_argument("--agent", choices=("codex", "claude", "all"), default="all")
    parser.add_argument("--scope", choices=("global", "project"), default="global")
    parser.add_argument("--project", type=Path, help="Existing project directory for --scope project.")
    parser.add_argument("--dry-run", action="store_true", help="Show planned actions without writing files.")
    return parser.parse_args()


def destinations(agent: str, scope: str, project: Path | None) -> list[tuple[str, Path]]:
    if scope == "project":
        assert project is not None
        base = project.resolve()
        return [
            ("Codex", base / ".agents" / "skills" / SKILL_NAME),
            ("Claude Code", base / ".claude" / "skills" / SKILL_NAME),
        ] if agent == "all" else [
            ("Codex", base / ".agents" / "skills" / SKILL_NAME)
            if agent == "codex"
            else ("Claude Code", base / ".claude" / "skills" / SKILL_NAME)
        ]
    return [
        ("Codex", home_path(".agents", "skills", SKILL_NAME)),
        ("Claude Code", home_path(".claude", "skills", SKILL_NAME)),
    ] if agent == "all" else [
        ("Codex", home_path(".agents", "skills", SKILL_NAME))
        if agent == "codex"
        else ("Claude Code", home_path(".claude", "skills", SKILL_NAME))
    ]


def backup_existing(target: Path, dry_run: bool) -> Path | None:
    if not target.exists():
        return None
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = target.parent / f".{SKILL_NAME}-backup-{timestamp}"
    if dry_run:
        return backup
    shutil.copytree(target, backup)
    return backup


def install_one(target: Path, dry_run: bool) -> None:
    backup = backup_existing(target, dry_run)
    if target.exists() and not dry_run:
        print(f"[OK] Backup created: {display_path(backup)}")
    elif target.exists() and dry_run:
        print(f"[PLAN] Existing installation would be backed up to: {display_path(backup)}")

    if dry_run:
        for source in iter_bundle_files(REPO_ROOT):
            print(f"[PLAN] Copy {source.relative_to(REPO_ROOT)} -> {display_path(target / source.relative_to(REPO_ROOT))}")
        return

    target.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, str] = {}
    for source in iter_bundle_files(REPO_ROOT):
        relative = source.relative_to(REPO_ROOT)
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        manifest[str(relative).replace("\\", "/")] = sha256(source)
    (target / ".install-manifest.json").write_text(
        json.dumps({"skill": SKILL_NAME, "version": read_version(), "files": manifest}, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    if args.scope == "project":
        if not args.project:
            print("[ERROR] --project PATH is required for --scope project.")
            return 2
        if not args.project.exists() or not args.project.is_dir():
            print(f"[ERROR] Project directory does not exist: {args.project}")
            return 2

    print(f"frontend-product-engineer {read_version()} from {display_path(REPO_ROOT)}")
    print(f"Mode: agent={args.agent}, scope={args.scope}, dry-run={args.dry_run}")
    for label, target in destinations(args.agent, args.scope, args.project):
        print(f"[{label}] destination: {display_path(target)}")
        install_one(target, args.dry_run)
    print("[OK] Installation plan completed." if args.dry_run else "[OK] Skill installation completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
