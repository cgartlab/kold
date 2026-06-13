# Kold

**代号 Kold** — 淬火之名，让滚烫的代码冷却成器。

Code agent for frontend design and development. Works in any agent framework.

---

## What is Kold?

Kold is a cross-platform AI coding agent specialized in **frontend design and UI implementation**. It runs independently in any agent framework (OpenClaw, Claude Code, OpenCode, Codex CLI, etc.) and can also be invoked by other agents as a sub-task specialist.

Kold's core strength: it is equally sensitive to **visual design** and **code quality**. It doesn't just make things work — it makes them right.

---

## Core Capabilities

- **UI Design Implementation** — build components, pages, and systems that are visually precise and consistent with established design languages
- **Design Token Integration** — use design tokens (CSS custom properties, OKLch colors, spacing scales) correctly without hardcoding values
- **Responsive & Accessible** — mobile-first, touch-friendly, WCAG compliant by default
- **Code Quality** — semantic HTML, maintainable CSS, clean JS; never ships half-baked code
- **Self-Evolving** — learns from every real task it completes; continuously absorbs new framework support and avoids past mistakes

---

## How to Use

### Clone & Go

```bash
git clone https://github.com/cgartlab/kold.git
cd kold
```

Kold is framework-agnostic. Drop it into your agent's workspace and it will read `AGENTS.md` and load its skills on startup. No installation, no build step.

### For OpenClaw / Claude Code / OpenCode / Codex CLI

The repository contains a complete `AGENTS.md` and `skills/` directory. Your agent reads them automatically on every session start. You don't need to configure anything.

### For Other Frameworks

Reference `AGENTS.md` as your agent's behavioral foundation. Copy the `skills/` directory into your agent's equivalent skill directory. The SKILL.md format follows the [agentskills.io](https://agentskills.io) open standard and works across all major agent frameworks.

---

## Project Structure

```
kold/
├── AGENTS.md           # Core identity, rules, and working agreements
├── SKILL.md            # Primary skill: frontend design & development
├── skills/
│   └── ui-design/      # UI design skill with deep references
│       ├── SKILL.md
│       └── references/
├── references/         # Design system references, a11y checklists
└── README.md
```

---

## Kold's Design Principles

1. **Design before code** — understand the intent, then implement
2. **Tokens over magic numbers** — every visual value comes from a design token
3. **Self-review before commit** — always check: correctness, style, accessibility
4. **No hardcoding** — colors, spacing, and type scale must be token-driven
5. **Accessibility is not optional** — WCAG AA baseline, always

---

## Relationship with Argus

Kold and Argus are companion agents:

- **Kold** produces frontend code — components, pages, design systems
- **Argus** reviews frontend code — catches style issues, hardcoded values, a11y problems, design token violations

They share the same design principles and can work together in a Kold → Argus workflow, or independently.

---

## Version

`VERSION` file = source of truth. Increment after meaningful changes.

---

## License

MIT