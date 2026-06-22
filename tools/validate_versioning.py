#!/usr/bin/env python3
"""
Validate versioning consistency: VERSION ↔ CHANGELOG ↔ SKILL.md.

Checks:
  1. VERSION matches a CHANGELOG section header
  2. CHANGELOG entry for current version has actual content (not empty)
  3. SKILL.md has ≥3 trigger phrase groups
"""

import re
import sys

VERSION_FILE = "VERSION"
CHANGELOG_FILE = "CHANGELOG.md"
SKILL_FILE = "SKILL.md"


def read_version() -> str:
    with open(VERSION_FILE) as f:
        return f.read().strip()


def check_changelog_header(version: str) -> None:
    with open(CHANGELOG_FILE) as f:
        content = f.read()
    pattern = rf"^## \[{re.escape(version)}\]"
    if not re.search(pattern, content, re.MULTILINE):
        print(f"FAIL: CHANGELOG missing [{version}] section — run 'make bump-*' first")
        sys.exit(1)
    print(f"  CHANGELOG has [{version}] section")


def check_changelog_content(version: str) -> None:
    with open(CHANGELOG_FILE) as f:
        content = f.read()
    # Split into sections by ## headers
    parts = re.split(r"^## ", content, flags=re.MULTILINE)
    body = ""
    for part in parts[1:]:  # skip first element (before first ##)
        if part.startswith(f"[{version}]"):
            # Extract everything after the version line up to the next ## or end
            lines = part.split("\n")[1:]  # skip the [ver] — date line
            body = "\n".join(lines)
            break
    if not body:
        print("FAIL: Could not find CHANGELOG section")
        sys.exit(1)
    # Remove section markers (### Added etc.) and list markers (- )
    cleaned = re.sub(r"^### \w+\s*$|^- ", "", body, flags=re.MULTILINE).strip()
    if not cleaned:
        print(f"FAIL: CHANGELOG entry for [{version}] is empty — add entries before releasing")
        sys.exit(1)
    print(f"  CHANGELOG entry has content")


def check_skill_phrases() -> None:
    with open(SKILL_FILE) as f:
        content = f.read()
    phrases = [
        p.strip() for p in re.findall(r"(?:when|phrases?)[:\s]+([^\n]+)", content, re.I)
    ]
    print(f"  SKILL.md has {len(phrases)} trigger phrase groups")
    if len(phrases) < 3:
        print(f"  WARNING: SKILL.md should have ≥3 trigger phrase groups")


def main() -> None:
    print("Versioning checks:")

    version = read_version()
    print(f"  VERSION = {version}")

    check_changelog_header(version)
    check_changelog_content(version)
    check_skill_phrases()

    print("")
    print("All versioning checks passed")


if __name__ == "__main__":
    main()
