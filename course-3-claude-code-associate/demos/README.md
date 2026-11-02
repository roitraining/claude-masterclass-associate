# Claude Code Associate: Demos

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Contents:** 9 instructor-led demos. Each takes 15 minutes or less and has a learning objective. The numbers match the Today's Demos slide.

---

## About this guide

Run the demos in order. Each has the same layout: a learning objective, a time, a Files line when it uses files, a short context paragraph, steps, an Expected result, an Instructor note, and a Why this matters note.

These demos assume Essentials Course 3. They do not re-teach the core loop, permission modes, plan mode, CLAUDE.md, checkpoints, a read-only reviewer subagent, review before merge, or deny rules.

All demos run on a class Anthropic account. Demo 7 is instructor-only because Agent Teams are experimental and off by default. No demo needs a cloud route, and none needs a credential. Every person, company, and figure in the files is fictional. Claude Code can word things differently each time, so check results against the Expected result and not against exact text.

**Files.** In this guide `$FILES` means the `demo-files` folder your instructor gives you:

- [`$FILES/shipdesk`](../demo-files/shipdesk) is a small Python project with tests, three starter subagents in `.claude/agents/`, and a ticket, for Demos 1, 2, 3, 5, and 6.
- [`$FILES/hooks`](../demo-files/hooks) holds hook scripts and a settings snippet, for Demos 4 and 5.
- [`$FILES/agent-pr/sd-142-promo-codes.diff`](../demo-files/agent-pr/sd-142-promo-codes.diff) is a pull request an agent produced, for Demo 6.
- [`$FILES/managed-policy`](../demo-files/managed-policy) holds a managed policy and a project file that tries to defeat it, for Demo 9.

> **Work in your own copy.** Demos with files start by copying `shipdesk` into `~/work` and committing a baseline. Commit locally only. Nothing in this course pushes to a remote.

> **Token cost.** Parallel sessions multiply usage. Use the small projects as given and keep prompts narrow.

---

## Setup: Copy the project once

**Time:** about 5 minutes, before Demo 1.

1. Copy the project, create an environment, and commit a baseline:

```
mkdir -p ~/work && cp -r $FILES/shipdesk ~/work/
cd ~/work/shipdesk
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
git init -q && git add -A && git commit -qm "baseline"
python -m pytest -q
```

**Expected result:** 14 tests pass.

> **Instructor note:** `.claude/settings.json` in the project sets `worktree.baseRef` to `"head"`, so new worktrees branch from the local baseline commit. With no remote, the default `"fresh"` branches from the remote default branch, and what that does in a local-only repository was not tested. The exact nesting of that key in a settings file is not in the verified facts. Rehearse once on the class VM. If worktrees do not start from your baseline commit, fix this before Demo 1.

---

## The demos

- **[Demo 1: Two Worktrees, Two Tasks](demo-1-two-worktrees-two-tasks.md)**
- **[Demo 2: A Subagent in Its Own Worktree](demo-2-a-subagent-in-its-own-worktree.md)**
- **[Demo 3: Write a Subagent Role Contract](demo-3-write-a-subagent-role-contract.md)**
- **[Demo 4: A Hook That Blocks a Dangerous Command](demo-4-a-hook-that-blocks-a-dangerous-command.md)**
- **[Demo 5: A Hook That Runs Tests Before You Commit](demo-5-a-hook-that-runs-tests-before-you-commit.md)**
- **[Demo 6: Review an Agent-Produced Pull Request](demo-6-review-an-agent-produced-pull-request.md)**
- **[Demo 7: Agent Teams, Instructor Only](demo-7-agent-teams-instructor-only.md)**
- **[Demo 8: A Routine Versus a Scheduled Task](demo-8-a-routine-versus-a-scheduled-task.md)**
- **[Demo 9: Test a Managed Policy](demo-9-test-a-managed-policy.md)**

---

The combined guide remains at [`../demos.md`](../demos.md) and is still the source of record. These per-demo files are split out of it for easier reading and review.

---

## Related

- **[Labs guide](../labs/README.md)** — the 4 hands-on labs for this course, one file per lab.
