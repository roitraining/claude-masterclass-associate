# Demo 1: Two Worktrees, Two Tasks

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Demo:** 1 of 9
**Time:** about 12 minutes

> Part of **[Claude Code Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Run two Claude Code sessions on the same project at once, with each session's edits isolated. Time: about 12 minutes.

**Files:** [`$FILES/shipdesk`](../demo-files/shipdesk): `TASKS.md` (tasks A and B), `.worktreeinclude`, `.gitignore`.

**Context:** A worktree checks a second branch out into its own directory. It shares the repository history with the main checkout, but it has its own files, so two sessions cannot overwrite each other.

**Steps:**

1. In `~/work/shipdesk`, create a harmless `.env` and open `.gitignore` and `.worktreeinclude`. Show that `.claude/worktrees/` is ignored and that `.env` is listed for copying:

```
echo "SHIPDESK_REGION=demo" > .env
cat .gitignore .worktreeinclude
```

2. In terminal 1, start a session in a new worktree and give it Task A from `TASKS.md`:

```
claude --worktree zip-check
```

3. In terminal 2, from `~/work/shipdesk`, start a second worktree for Task B:

```
claude -w bulk-discount
```

4. In each session, ask: "Do the task in TASKS.md for this branch only: Task A" (terminal 1) and "Task B" (terminal 2).
5. In terminal 3, show what exists and where:

```
git worktree list
ls -a .claude/worktrees/zip-check
```

6. In terminal 2, ask Claude to edit `../../../shipdesk/addresses.py` (the main checkout). Show that Claude Code blocks it.
7. Point out that the new worktree has no `.venv`. Run `pip install -r requirements.txt` in it before the tests, as a fresh checkout needs.

**Expected result:** Two worktrees under `.claude/worktrees/`, on branches `worktree-zip-check` and `worktree-bulk-discount`. The `.env` file appears in each. Each session changes only its own files. The main checkout stays clean. The edit aimed at the main checkout is refused.

> **Instructor note:** Everything above is in the verified facts, except the blocked edit at step 6, whose exact wording you should capture in rehearsal. Claude Code blocks edits, working directories, and git redirects that target the main checkout. It does not track files a shell command writes (`cp`, redirects), so those fall under normal permissions. Do not demonstrate that gap as a safety feature. Show the desktop worktree option (choose it when starting a session) as a screenshot or live, and mention side chat in one sentence at most: it is documented only as a desktop feature in a release write-up and is not confirmed on the official docs page.

> **Why this matters:** Two tickets finish in the time of one only if the sessions cannot collide. The worktree is what makes that safe.

---

**Next:** [Demo 2: A Subagent in Its Own Worktree](demo-2-a-subagent-in-its-own-worktree.md)


*Demo 1 of 9*
