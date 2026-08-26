"""Check or fast-forward the local canonical skill clone from GitHub."""

from __future__ import annotations

import argparse
import re
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from _common import REPO_ROOT, display_path, is_git_repo, load_config, read_version, run_command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Synchronize the canonical skill clone.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="Compare local VERSION with the canonical VERSION.")
    group.add_argument("--update", action="store_true", help="Fast-forward a clean Git worktree from origin/main.")
    return parser.parse_args()


def version_tuple(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", value.strip())
    if not match:
        return (0, 0, 0)
    return tuple(int(part) for part in match.groups())


def raw_version_url(repository: str) -> str:
    parsed = urlparse(repository.rstrip("/"))
    parts = [part for part in parsed.path.split("/") if part]
    if parsed.netloc != "github.com" or len(parts) < 2:
        raise ValueError("canonical_repository must be a GitHub repository URL")
    owner, name = parts[0], parts[1].removesuffix(".git")
    # Use the explicit ref path so a branch-level raw cache cannot report a stale VERSION.
    return f"https://raw.githubusercontent.com/{owner}/{name}/refs/heads/main/VERSION"


def remote_version(repository: str) -> str | None:
    url = raw_version_url(repository)
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode("utf-8").strip()
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as error:
        print(f"[WARN] Could not reach canonical VERSION: {error}")
        return None


def update() -> int:
    before = read_version()
    if not is_git_repo():
        print("[WARN] This copy is not a Git clone; local skill remains usable, but --update cannot modify it safely.")
        return 0

    status = run_command(["git", "status", "--porcelain"], cwd=REPO_ROOT)
    if status.returncode != 0:
        print(f"[WARN] Git status unavailable: {status.stderr.strip()}")
        return 0
    if status.stdout.strip():
        print("[ERROR] Refusing --update because the local worktree has changes.")
        print(status.stdout.rstrip())
        print("Commit or stash local changes, then retry. No files were changed.")
        return 2

    result = run_command(["git", "pull", "--ff-only", "origin", "main"], cwd=REPO_ROOT, timeout=60)
    if result.returncode != 0:
        print(f"[WARN] Canonical update unavailable: {(result.stderr or result.stdout).strip()}")
        print("[OK] Local skill remains usable offline; no files were changed.")
        return 0
    after = read_version()
    print(f"[OK] Version before: {before}")
    print(f"[OK] Version after:  {after}")
    print("[OK] Fast-forward update completed.")
    return 0


def check() -> int:
    config = load_config()
    local = read_version()
    remote = remote_version(config["canonical_repository"])
    print(f"Local VERSION: {local}")
    if remote is None:
        print("[WARN] Remote VERSION could not be checked; no local files were changed.")
        return 0
    print(f"Remote VERSION: {remote}")
    if remote == local:
        print("[OK] Local copy is up to date.")
    elif version_tuple(remote) > version_tuple(local):
        print("[UPDATE] A newer canonical version is available.")
    else:
        print("[INFO] Local version is newer or differs from the canonical version.")
    return 0


def main() -> int:
    args = parse_args()
    print(f"Canonical repository: {load_config()['canonical_repository']}")
    return update() if args.update else check()


if __name__ == "__main__":
    raise SystemExit(main())
