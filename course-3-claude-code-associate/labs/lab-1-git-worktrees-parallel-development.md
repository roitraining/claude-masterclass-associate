# Lab 1: Git Worktrees Parallel Development

> Part of **[Claude Code Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

**Learning objective:** Run three tasks in parallel in separate worktrees, merge them in order, and clean up. Time: 45 minutes.

**Files:** `$FILES/shipdesk`: `TASKS.md`, `.worktreeinclude`, `.gitignore`, `CLAUDE.md`, and `tests/`.

**Context:** `TASKS.md` holds three independent tasks. Each touches different files, so the branches merge without conflicts. Each worktree is a fresh checkout and needs its own environment.

**Steps:**

1. Copy the project and commit a baseline:

```
mkdir -p ~/work && cp -r $FILES/shipdesk ~/work/shipdesk-lab1
cd ~/work/shipdesk-lab1
git init -q && git add -A && git commit -qm "baseline"
```

2. Create the environment and run the tests:

```
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

3. Create a file that should reach every worktree: `echo "SHIPDESK_REGION=demo" > .env`
4. Read `TASKS.md`.
5. Open three terminals in `~/work/shipdesk-lab1`. In terminal 1 run `claude --worktree zip-check`.
6. In terminal 2 run `claude --worktree bulk-discount`.
7. In terminal 3 run `claude --worktree csv-export`.
8. In each session, check for the `.env` file with `ls -a`, then run: `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt`
9. In each session, ask for that session's task only: "Do Task A in TASKS.md and nothing else" (zip-check), "Task B" (bulk-discount), "Task C" (csv-export).
10. In each session, ask Claude to run the tests and show the result.
11. In each session, ask Claude to commit the work with a clear message.
12. In terminal 4, in the main checkout, list the worktrees: `git worktree list`
13. Merge in this order, one at a time, running the tests after each:

```
git merge worktree-zip-check
python -m pytest -q
git merge worktree-csv-export
python -m pytest -q
git merge worktree-bulk-discount
python -m pytest -q
```

14. Remove the worktrees and branches:

```
git worktree remove .claude/worktrees/zip-check
git worktree remove .claude/worktrees/csv-export
git worktree remove .claude/worktrees/bulk-discount
git branch -d worktree-zip-check worktree-csv-export worktree-bulk-discount
git worktree list
```

**Checkpoint:** `git log --oneline` shows the baseline and three task commits. `python -m pytest -q` passes on the main checkout with more than 14 tests. `git worktree list` shows only the main checkout.

**Common problems:**

- A worktree branches from an old commit and lacks your baseline files: the base reference points at the wrong place. Ask your instructor.
- Tests fail with `No module named pytest` in a worktree: that worktree has no `.venv`. Run step 8 there.
- A worktree has no `.env`: the file was created after the worktree. Copy it by hand, and note that `.worktreeinclude` applies at creation.
- `git worktree remove` refuses because of changes: commit or discard them first.
- A merge conflict: two sessions touched the same file. Read each diff and ask which task owns that file.

**Facilitator note:** A good result is three small commits, each changing only the files its task names, with every test passing after every merge. Task A adds `normalize_zip` with `12345`, `12345-6789`, hyphen-less nine digits, and `None` for bad input. Task B takes 5 percent off lines of 10 to 24 and 10 percent off 25 or more, with boundary tests at 9, 10, 24, and 25. Task C adds `to_csv` with header `id,customer,total`. Note that after Task B the totals in `orders.json` change, but the largest order stays `SD-1003`. Watch for a student whose session edited a file outside its task, and ask how they would have caught it from the diff. This lab depends on the `worktree.baseRef` setting in the project's `.claude/settings.json` working on a local-only repository. That is unconfirmed, so rehearse it on the class VM before the day.
