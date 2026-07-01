#!/usr/bin/env python3
"""
Validate versioning consistency: VERSION ↔ CHANGELOG ↔ SKILL.md.

Checks:
  1. VERSION matches a CHANGELOG section header
  2. VERSION is the LATEST (first) CHANGELOG entry — no drift
  3. CHANGELOG entry for current version has actual content (not empty)
  4. SKILL.md has ≥3 trigger phrase groups
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

    # Reverse check: VERSION must be the FIRST (latest) CHANGELOG entry
    all_headers = re.findall(r"^## \[([^\]]+)\]", content, re.MULTILINE)
    if not all_headers:
        print("FAIL: No version headers found in CHANGELOG")
        sys.exit(1)
    latest = all_headers[0]
    if latest != version:
        print(f"FAIL: VERSION={version} but CHANGELOG latest entry is [{latest}] — bump VERSION to match")
        sys.exit(1)
    print(f"  VERSION matches latest CHANGELOG entry [{latest}]")


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
    # Look for "## Trigger phrases" section and count its bullet points
    lines = content.split("\n")
    in_trigger = False
    bullet_count = 0
    for line in lines:
        if "## Trigger phrases" in line or "## Trigger Phrases" in line:
            in_trigger = True
            continue
        if in_trigger:
            if line.startswith("## "):
                break
            if line.startswith("- "):
                bullet_count += 1
    print(f"  SKILL.md has {bullet_count} trigger phrases")
    if bullet_count < 3:
        print(f"  WARNING: SKILL.md should have ≥3 trigger phrases")


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
