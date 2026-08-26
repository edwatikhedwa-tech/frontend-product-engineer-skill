"""Small standard-library helpers shared by the portable skill scripts."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Iterable, Sequence


SKILL_NAME = "front"
REPO_ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = REPO_ROOT / "VERSION"
CONFIG_FILE = REPO_ROOT / "config" / "repository.json"


def read_version(root: Path = REPO_ROOT) -> str:
    return (root / "VERSION").read_text(encoding="utf-8").strip()


def load_config(root: Path = REPO_ROOT) -> dict:
    return json.loads((root / "config" / "repository.json").read_text(encoding="utf-8"))


def command_exists(name: str) -> bool:
    return shutil.which(name) is not None


def run_command(args: Sequence[str], cwd: Path | None = None, timeout: int = 30) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args),
        cwd=str(cwd) if cwd else None,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_bundle_files(root: Path = REPO_ROOT) -> Iterable[Path]:
    ignored_dirs = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".venv", "venv", "node_modules"}
    ignored_names = {".env", ".env.local", ".env.production", ".env.development"}
    secret_suffixes = {".pem", ".key", ".p12", ".pfx"}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored_dirs for part in path.relative_to(root).parts):
            continue
        if path.name in ignored_names or path.suffix.lower() in secret_suffixes:
            continue
        if re.search(r"(cookie|credential|secret|token)", path.name, re.IGNORECASE):
            continue
        yield path


def is_git_repo(root: Path = REPO_ROOT) -> bool:
    return (root / ".git").exists()


def display_path(path: Path) -> str:
    try:
        return str(path.resolve()).replace(str(Path.home()), "~")
    except OSError:
        return str(path)


def home_path(*parts: str) -> Path:
    return Path.home().joinpath(*parts)
