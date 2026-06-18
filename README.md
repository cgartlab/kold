# Kold

[![CI](https://github.com/cgartlab/kold/actions/workflows/ci.yml/badge.svg)](https://github.com/cgartlab/kold/actions/workflows/ci.yml)
[![Argus-Flash Review](https://github.com/cgartlab/kold/actions/workflows/argus-review.yml/badge.svg)](https://github.com/cgartlab/kold/actions/workflows/argus-review.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Version](https://img.shields.io/badge/version-0.2.0-blue)

**Frontend design agent — runs anywhere, ships with taste.**

Kold is a cross-platform AI coding agent specialized in frontend design and UI implementation. It works in any agent framework: OpenClaw, Claude Code, OpenCode, Codex CLI — or any other agentskills.io-compatible runtime.

Core strength: equally sensitive to visual design and code quality. Not just making things work — making them *right*.

---

## Quick Start

```bash
git clone https://github.com/cgartlab/kold.git
cd kold
# That's it. The agent reads AGENTS.md + SKILL.md on startup.
```

No installation. No build step. No dependencies.

### Run in any framework

| Framework | How to start |
|-----------|-------------|
| **OpenClaw** | Clone repo; agent auto-loads AGENTS.md as instructions |
| **Claude Code** | `claude` from repo root; `CLAUDE.md` bridges to AGENTS.md |
| **OpenCode** | `opencode` from repo root; reads AGENTS.md automatically |
| **Codex CLI** | `codex` from repo root; reads AGENTS.md automatically |

---

## What Kold Does

- **UI implementation** — components, pages, design systems in pure HTML/CSS/JS
- **Design token integration** — CSS custom properties, OKLch color system, spacing/type/radius scales
- **Accessibility-first** — semantic HTML, WCAG AA baseline, proper ARIA
- **Dark mode** — every component ships with `[data-theme="dark"]` overrides
- **Responsive** — mobile-first, progressive enhancement

---

## Kold-Argus Workflow

Kold and Argus form an automated review-and-fix loop:

```
Kold push → PR opened → Argus reviews → comments on PR
         → Kold reads comments → Kold fixes → force push
         → Argus re-reviews → loop until PASS
         → ready for human merge
```

> **Kold never merges its own PRs.** All merges require human approval.

This loop was [verified end-to-end](https://github.com/cgartlab/kold/pull/1) with a test PR:
- Round 1: **17 issues** (P0: 9, P1: 6, P2: 2) → **FAIL**
- Round 2: **2 issues** (P2: 1, P3: 1) → **PASS ✅**

### How Argus review works

1. Open a PR → `argus-flash` GitHub App triggers review automatically
2. Argus posts a structured comment with issues ranked by severity:
   - **P0** — blocking, must fix (bare colors, missing dark mode)
   - **P1** — high, must fix (missing a11y, hardcoded spacing)
   - **P2** — medium, should fix (magic numbers, minor violations)
   - **P3** — low, polish (cosmetic)
3. Kold reads the comment, fixes issues, force pushes to the same branch
4. Argus re-reviews on the `synchronize` event
5. Loop until P0/P1 are zero — verdict PASS — ready for human review

### Setup for a new repo

1. Install [argus-flash](https://github.com/apps/argus-flash) on the target repo
2. Add `ARGUS_FLASH_APP_ID` and `ARGUS_FLASH_PRIVATE_KEY` to repo secrets
3. Copy `.github/workflows/argus-review.yml` to the target repo

---

## Project Structure

```
kold/
├── AGENTS.md                # Identity, hard rules, workflow protocol
├── SKILL.md                 # Frontend design skill with token reference
├── CLAUDE.md                # Claude Code compatibility bridge (@AGENTS.md)
├── README.md
├── CHANGELOG.md
├── DEVELOPMENT-GUIDE.md     # Architecture and conventions
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE                  # MIT
├── VERSION                  # Semantic version
├── Makefile                 # check-version, validate, release, package
├── examples/                # Verified example components
│   └── profile-card.html
└── .github/
    └── workflows/
        ├── ci.yml           # Lint, validate structure, check CHANGELOG
        └── argus-review.yml # Argus-flash automated design review
```

---

## Design Philosophy

### Tokens over magic numbers

Every visual value comes from a CSS custom property. No bare `oklch()`, hex, or hardcoded numbers in component rules.

```css
/* ✓ Good */
.card { background: var(--ds-color-surface); border-radius: var(--ds-radius-lg); }

/* ✗ Bad */
.card { background: #16213e; border-radius: 16px; }
```

### Color system

Define colors in `oklch()` on `:root`, reference via `var(--ds-*)`. Every color needs a `[data-theme="dark"]` override.

### Progressive enhancement

Components should be usable without JavaScript. JavaScript enhances, never replaces.

---

## Relationship with Argus

- **Kold** — produces frontend code
- **Argus** — reviews frontend code (hardcoded values, a11y, design tokens, dark mode)

They operate in a strict **Kold → Argus → Human** workflow.

---

## License

MIT © [CGArtLab](https://github.com/cgartlab)
