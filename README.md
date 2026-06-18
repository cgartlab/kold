# Kold

[![CI](https://github.com/cgartlab/kold/actions/workflows/ci.yml/badge.svg)](https://github.com/cgartlab/kold/actions/workflows/ci.yml)
[![Argus-Flash Review](https://github.com/cgartlab/kold/actions/workflows/argus-review.yml/badge.svg)](https://github.com/cgartlab/kold/actions/workflows/argus-review.yml)

Code agent for frontend design and development. Works in any agent framework.

## What is Kold?

Kold is a cross-platform AI coding agent specialized in frontend design and UI implementation. It runs independently in any agent framework — OpenClaw, Claude Code, OpenCode, Codex CLI, or any other — and can be invoked by other agents as a sub-task specialist.

Core strength: equally sensitive to visual design and code quality.

## Capabilities

- UI design implementation (components, pages, design systems)
- Design token integration (CSS custom properties, OKLch color system)
- Responsive and accessible frontend code (mobile-first, WCAG AA)
- Semantic HTML, maintainable CSS, clean JavaScript
- Self-review before any commit

## Quick Start

Clone and the agent reads AGENTS.md and SKILL.md automatically on startup:

```bash
git clone https://github.com/cgartlab/kold.git
cd kold
```

No installation, no build step.

## Project Structure

```
kold/
├── AGENTS.md              # Identity, hard rules, working agreements
├── SKILL.md               # Frontend design skill with token reference
├── skills/                # Supplementary skills (TBD)
├── references/            # Deep reference docs (TBD)
├── README.md
├── VERSION                # Semantic version
├── LICENSE                # MIT
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── DEVELOPMENT-GUIDE.md
├── CHANGELOG.md
└── SECURITY.md
```

## Relationship with Argus

Kold and Argus are companion agents:

- **Kold** — produces frontend code
- **Argus** — reviews frontend code

They share design principles and can work in a Kold -> Argus workflow, or independently.

## License

MIT