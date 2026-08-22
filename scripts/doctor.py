"""Run repository and local installation health checks without third-party dependencies."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from _common import REPO_ROOT, SKILL_NAME, command_exists, display_path, home_path, is_git_repo, load_config, read_version, run_command


errors = 0
warnings = 0


def ok(message: str) -> None:
    print(f"[OK] {message}")


def warn(message: str) -> None:
    global warnings
    warnings += 1
    print(f"[WARN] {message}")


def error(message: str) -> None:
    global errors
    errors += 1
    print(f"[ERROR] {message}")


def check_structure() -> None:
    required = [
        "SKILL.md", "README.md", "VERSION", "CHANGELOG.md", "LICENSE", ".gitignore",
        "config/repository.json", "knowledge/PRINCIPLES.md", "knowledge/LESSONS.md",
        "knowledge/ANTI_PATTERNS.md", "workflows/CREATE.md", "workflows/REDESIGN.md",
        "workflows/EXTEND.md", "workflows/REVIEW.md", "quality/QUALITY_GATE.md",
        "scripts/install.py", "scripts/sync.py", "scripts/doctor.py", "scripts/new_case.py",
        "docs/SOURCES.md", "tech-radar/TECH_RADAR.md", "dataset/README.md",
    ]
    missing = [item for item in required if not (REPO_ROOT / item).exists()]
    if missing:
        for item in missing:
            error(f"Missing required path: {item}")
    else:
        ok("Required repository structure is present.")


def check_skill_metadata() -> None:
    path = REPO_ROOT / "SKILL.md"
    if not path.exists():
        return
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        error("SKILL.md does not start with YAML frontmatter.")
        return
    try:
        end = lines.index("---", 1)
    except ValueError:
        error("SKILL.md frontmatter is not closed.")
        return
    frontmatter = "\n".join(lines[1:end])
    for field in ("name", "description"):
        if not re.search(rf"^{field}:\s*.+$", frontmatter, re.MULTILINE):
            error(f"SKILL.md frontmatter is missing {field}.")
    if "CODE COMPLETE != TASK COMPLETE" not in path.read_text(encoding="utf-8"):
        error("SKILL.md is missing the core quality law.")
    else:
        ok("SKILL.md frontmatter and core quality law are present.")


def check_config() -> None:
    try:
        config = load_config()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        error(f"repository.json is invalid: {exc}")
        return
    required = ("name", "canonical_repository", "version", "update_strategy")
    missing = [key for key in required if not config.get(key)]
    if missing:
        error(f"repository.json is missing: {', '.join(missing)}")
    elif not str(config["canonical_repository"]).startswith("https://github.com/"):
        error("canonical_repository is not an HTTPS GitHub URL.")
    else:
        ok(f"Canonical repository: {config['canonical_repository']}")


def check_version() -> None:
    try:
        version = read_version()
    except OSError as exc:
        error(f"VERSION cannot be read: {exc}")
        return
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        error(f"VERSION is not SemVer: {version}")
    elif version != load_config().get("version"):
        error("VERSION does not match config/repository.json.")
    else:
        ok(f"VERSION is {version}.")


def check_links() -> None:
    broken: list[str] = []
    pattern = re.compile(r"\[[^]]*\]\(([^)]+)\)")
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        for raw_target in pattern.findall(path.read_text(encoding="utf-8")):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            candidate = (path.parent / target).resolve()
            if not candidate.exists():
                broken.append(f"{path.relative_to(REPO_ROOT)} -> {raw_target}")
    if broken:
        for item in broken:
            error(f"Broken relative link: {item}")
    else:
        ok("Relative Markdown links resolve.")


def check_secrets() -> None:
    suspicious = re.compile(r"(gho_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]+ PRIVATE KEY-----)")
    found: list[str] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".ico"}:
            continue
        try:
            if suspicious.search(path.read_text(encoding="utf-8")):
                found.append(str(path.relative_to(REPO_ROOT)))
        except (OSError, UnicodeDecodeError):
            continue
    if found:
        for item in found:
            error(f"Possible secret pattern found in {item}.")
    else:
        ok("No obvious secret patterns found.")


def check_tools() -> None:
    if command_exists("git"):
        ok("Git is available.")
    else:
        error("Git is not available.")
    for tool in ("codex", "claude", "node", "npm", "pnpm"):
        if command_exists(tool):
            ok(f"Optional tool available: {tool}")
        else:
            warn(f"Optional tool not found: {tool}")
    playwright = command_exists("playwright")
    if not playwright and command_exists("npx"):
        warn("Playwright CLI was not found on PATH; browser QA remains optional and project-specific.")
    elif playwright:
        ok("Optional Playwright CLI is available.")
    else:
        warn("Neither Playwright CLI nor npx was found; browser QA remains optional.")
    codex_config = home_path(".codex", "config.toml")
    context7_seen = False
    if codex_config.exists():
        try:
            context7_seen = "context7" in codex_config.read_text(encoding="utf-8").lower()
        except OSError:
            pass
    if context7_seen:
        ok("Context7 reference found in Codex configuration.")
    else:
        warn("Context7 integration not detected; official-documentation fallback is supported.")


def check_installations() -> None:
    paths = [
        home_path(".agents", "skills", SKILL_NAME),
        home_path(".claude", "skills", SKILL_NAME),
    ]
    for path in paths:
        if (path / "SKILL.md").exists():
            ok(f"Installed skill found: {display_path(path)}")
        else:
            warn(f"Skill installation not found: {display_path(path)}")


def check_git() -> None:
    if not is_git_repo():
        warn("Canonical source is not a Git repository yet.")
        return
    remote = run_command(["git", "remote", "get-url", "origin"], cwd=REPO_ROOT)
    if remote.returncode == 0 and remote.stdout.strip():
        ok(f"Git remote origin: {remote.stdout.strip()}")
    else:
        warn("Git remote origin is not configured yet.")
    status = run_command(["git", "status", "--short"], cwd=REPO_ROOT)
    if status.returncode == 0 and not status.stdout.strip():
        ok("Canonical source worktree is clean.")
    elif status.returncode == 0:
        warn("Canonical source worktree has uncommitted changes.")


def main() -> int:
    print(f"Doctor: {display_path(REPO_ROOT)}")
    check_structure()
    check_skill_metadata()
    check_version()
    check_config()
    check_links()
    check_secrets()
    check_tools()
    check_installations()
    check_git()
    print(f"Summary: errors={errors}, warnings={warnings}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
