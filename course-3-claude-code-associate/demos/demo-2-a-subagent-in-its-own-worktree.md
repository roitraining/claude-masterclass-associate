# Demo 2: A Subagent in Its Own Worktree

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Demo:** 2 of 9
**Time:** about 10 minutes

> Part of **[Claude Code Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Hand a side task to a subagent that works in an isolated worktree, so the current checkout is untouched. Time: about 10 minutes.

**Files:** [`$FILES/shipdesk/.claude/agents/worktree-implementer.md`](../demo-files/shipdesk/.claude/agents/worktree-implementer.md).

**Context:** A subagent has a fresh context window and returns only its final summary. The frontmatter field `isolation: worktree` runs it in its own worktree.

**Steps:**

1. Show the frontmatter of `worktree-implementer.md`: `name`, `description`, `tools`, `model`, `isolation: worktree`, `maxTurns`.
2. In `~/work/shipdesk`, start `claude` and ask: "Use the worktree-implementer agent to do Task C in TASKS.md."
3. While it runs, run `git status` and `git worktree list` in a second terminal.
4. When it returns, read the summary it sent back. Compare it with the files it changed.
5. Run `git status` in the main checkout.

**Expected result:** The main checkout stays clean while the subagent works. The subagent reports its changed files and a pytest summary line. It does not send back its full working history.

> **Instructor note:** `isolation: worktree` is a listed optional frontmatter field. What happens to the subagent's worktree and branch when it finishes (kept, removed, or prompted) was not recorded in the verified facts. Rehearse and say what you see. If the main session runs in `acceptEdits`, `bypassPermissions`, or auto mode, the subagent inherits that mode.

> **Why this matters:** A subagent is the cheap way to push a side task out of your context window and out of your working tree at once.

---

**Previous:** [Demo 1: Two Worktrees, Two Tasks](demo-1-two-worktrees-two-tasks.md) · **Next:** [Demo 3: Write a Subagent Role Contract](demo-3-write-a-subagent-role-contract.md)


*Demo 2 of 9*
