# TOOLS.md — Kold 工具使用规范

**Version:** 0.2.0 | **Part of:** cgartlab/kold

---

## 概述

Kold 使用一套标准化的工具链完成前端开发任务。所有工具都是纯本地命令或 HTTP API 调用，不依赖特定的 IDE 插件或 GUI 工具。

---

## 核心工具集

### 文件操作

| 工具 | 用途 | 规范 |
|------|------|------|
| `write` | 创建或覆写文件 | 用于新文件或大规模重写；精确编辑用 `edit` |
| `edit` | 精确替换文件内容 | 只改目标区域，不影响其他代码；多条编辑尽量合并 |
| `read` | 读取文件内容 | 优先用 `offset/limit` 控制范围；大文件分片读取 |
| `exec` | 运行 shell 命令 | 需要时才用；不做纯粹的 CLI 代替 |

**规范：**
- 相对路径基于 workspace 根目录
- `read` 优先于 `exec cat`，前者更可靠
- 不在 `exec` 里做文件编辑（`sed -i` 等容易出错）

### Git 操作

| 工具 | 用途 | 规范 |
|------|------|------|
| `exec git` | 所有 git 操作 | 不用专门的 git 封装工具，直接 `git` 命令 |

**规范：**
- 每次 `push` 前检查 `git status`，确认没有不该推的内容
- commit message 用 `type(scope): description` 格式
- 不 force push 到 main
- force push 只用于 Argus review 后的修复循环（同一 PR 分支）

### 代码质量

| 工具 | 用途 | 规范 |
|------|------|------|
| `exec make validate` | 运行本地验证 | push/PR 前必须通过 |
| `exec make lint` | 代码风格检查 | HTML/CSS/JS 各自对应 lint 规则 |

**规范：**
- `make validate` 是强制 gate，不过不推
- lint 错误优先修复，再提交

### 设计系统

| 工具 | 用途 | 规范 |
|------|------|------|
| tokens.json | 设计 Token 定义 | 所有颜色/字体/间距值来自此处 |
| CSS custom properties | Token 在 CSS 中的映射 | `--color-primary: var(--token-color-primary)` |

**规范：**
- 组件 CSS 中永远不出现 bare value（`#fff`、`24px`）
- 先查 tokens.json，不存在则报 Token 缺失，不猜测

---

## 外部服务

### GitHub

| 用途 | 工具 |
|------|------|
| 开 PR | `exec gh pr create` |
| 查看 review | `exec gh pr view` / `exec gh api` |
| 合并 PR | **永远不自己合并**，human gate |
| 发布 Release | `make release`（自动触发 GitHub Actions） |

### Argus Review

Argus 是 Kold 的代码审查 Agent，接收 Kold 的 PR 后自动评论。

| 场景 | 操作 |
|------|------|
| 开 PR 后等待 Argus | 等待 `argus-flash[bot]` 评论 |
| 读取 Argus 评论 | 解析 `[P0]` / `[P1]` / `[P2]` / `[P3]` 格式 |
| 修复 P0/P1 | 修复 → `git commit --amend` → `git push --force` 同一分支 |
| P0/P1 归零 | 通知 human review 可开始 |
| 审查期间 human 有意见 | 优先于 Argus，先修 human 的 |

---

## 工作流中的工具使用顺序

```
1. read 设计稿 / 需求
2. read tokens.json（设计依据）
3. write/edit 实现
4. exec make validate（本地 gate）
5. exec git add . && git commit
6. exec git push origin <branch>
7. exec gh pr create
8. 等待 Argus review
9. 读 Argus 评论 → 修复 P0/P1 → force push（循环）
10. Argus PASS + 无 P0/P1 → 通知 human
```

---

## 禁忌

- ❌ 不用 `exec` 做 `rm -rf` 大规模删除（先 `git status` 确认）
- ❌ 不用 `exec sed/awk` 做精确文件编辑
- ❌ 不跳过 `make validate` 直接 push
- ❌ 不在未经 human 确认的情况下 merge 自己的 PR
- ❌ 不向 Argus 或 human 以外的系统发送代码或 token 信息
