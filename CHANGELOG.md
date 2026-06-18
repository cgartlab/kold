# Changelog

All notable changes are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.2.0] — 2026-06-19

### Added
- Argus feedback loop protocol documented in AGENTS.md (7-step loop, comment format, config)
- `examples/profile-card.html` — test component; verified through full Argus review cycle

### Changed
- AGENTS.md: Kold-Argus Workflow section rewritten with full feedback loop flow diagram and protocol
- AGENTS.md: Argus Comment Format section added (P0-P3 severity, Found/Expected/Token structure)
- VERSION: 0.1.1 → 0.2.0

### Fixed
- CI workflow: bash syntax error from `$$` pseudo-escapes (missing GH Actions expression context)

### Verified
- Full Kold→PR→Argus→Kold fix→Argus re-review loop tested end-to-end on PR #1
- 17 issues found → all P0/P1 resolved → verdict PASS

## [0.1.0] — 2026-06-13

### Added
- `AGENTS.md` — identity, hard rules, Kold-Argus workflow, working agreements, self-evolution note
- `SKILL.md` — frontend design skill with design token reference, aesthetic judgment principles, anti-patterns, pre-commit checklist
- `README.md` — project overview, usage, project structure
- `VERSION` — 0.1.0
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `DEVELOPMENT-GUIDE.md`
- `SECURITY.md`
- `CHANGELOG.md`
- `LICENSE` — MIT
- `CLAUDE.md` — Claude Code compatibility bridge
- `Makefile` — check-version, validate, release, package
- `.github/workflows/ci.yml`
- `.github/workflows/release.yml`

### Changed
- AGENTS.md: Kold-Argus workflow formally documented (Kold -> PR -> Argus review -> human merge)
- SKILL.md: description expanded with aesthetic judgment trigger phrases
- SKILL.md: aesthetic quality added to pre-commit checklist

### Notes
- Kold and Argus are companion agents sharing the same design principles
- All merge operations require human approval; Kold never merges its own PRs
- Self-evolution mechanism is under development