# Development Guide — Kold

Agent framework: OpenClaw / Claude Code / OpenCode / Codex CLI / any agentskills.io-compatible runtime.

## Architecture

Kold is a pure documentation repository. The agent's behavior is defined entirely by:

- `AGENTS.md` — identity, hard rules, working agreements
- `SKILL.md` — skill definition with trigger phrases and execution rules
- `skills/` — supplementary skill files with deep references

There is no runtime code. No `npm install`, no build step. The agent reads these files at startup and follows the instructions.

## AGENTS.md Structure

```
Identity
Core Capabilities
Hard Rules          <- CI-enforced invariants
Working Agreements
Version Management
Relationship with Argus
```

Hard rules must never be weakened. If a rule proves unworkable in practice, open an issue first, then change.

## SKILL.md Structure

```
YAML frontmatter (name, description, version)
Body:
  - Core Principles
  - Reference Data (tokens, patterns)
  - Common Patterns (with code)
  - Anti-Patterns (with wrong/right pairs)
  - Pre-Commit Checklist
```

### Description Writing

The `description` field is a trigger mechanism, not a summary. It must contain 3+ real-world trigger phrases that a user would actually type.

```
description: "Use when building UI components, fixing layout on mobile,
  integrating design tokens, or implementing dark mode.
  Trigger phrases: '帮我写一个卡片组件'、'布局在手机上乱了'、'接入 design tokens'"
```

## Cross-Platform Compatibility

SKILL.md follows the agentskills.io open standard. It works in:

| Platform | Skill Path |
|---|---|
| Claude Code | `.claude/skills/<name>/SKILL.md` |
| Codex CLI | `.agents/skills/<name>/SKILL.md` |
| OpenCode | `skills/<name>/SKILL.md` |
| OpenClaw | `<workspace>/skills/<name>/SKILL.md` |

The content is identical across all platforms. Only the file location differs.

## Version Bumping

```bash
echo "0.2.0" > VERSION
git add -A && git commit -m "chore(release): bump to v0.2.0"
git tag v0.2.0 && git push origin main --tags
```

VERSION is the only source of truth. No other files track version.

## Adding a New Skill

1. Create `skills/<name>/SKILL.md`
2. Write description with 3+ trigger phrases
3. Write body following the SKILL.md structure above
4. Add `references/` subdirectory for deep content
5. Update VERSION if meaningful
6. PR with change summary