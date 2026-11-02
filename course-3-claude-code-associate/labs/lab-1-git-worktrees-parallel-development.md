# Lab 1: Git Worktrees Parallel Development

**Course:** Claude Code Associate
**Duration:** 45 minutes
**Format:** Instructor-led, in-class hands-on lab (200 level)

> Part of **[Claude Code Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] Python 3.11 or later, with `venv`
- [ ] Git 2.31 or later
- [ ] `claude` signed in
- [ ] Four terminals you can keep open at once
- [ ] `$FILES/shipdesk`: `TASKS.md`, `.worktreeinclude`, `.gitignore`, `CLAUDE.md`, and `tests/`

---

## Overview

`TASKS.md` holds three independent tasks. Each touches different files, so the branches merge without conflicts.

**Each worktree is a fresh checkout and needs its own environment.** That is the detail most students trip on.

---

## Part 1: Set Up the Baseline

### Step 1: Copy the Project and Commit a Baseline

```
mkdir -p ~/work && cp -r $FILES/shipdesk ~/work/shipdesk-lab1
cd ~/work/shipdesk-lab1
git init -q && git add -A && git commit -qm "baseline"
```

**Expected result:** a single baseline commit.

### Step 2: Create the Environment and Run the Tests

```
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

**Expected result:** the tests pass on the main checkout before you branch anything.

### Step 3: Create a File That Should Reach Every Worktree

```
echo "SHIPDESK_REGION=demo" > .env
```

### Step 4: Read the Tasks

Read `TASKS.md`.

**Expected result:** you can say which files each of the three tasks owns.

---

## Part 2: Create Three Worktrees

### Step 5: Start the zip-check Worktree

Open three terminals in `~/work/shipdesk-lab1`. In terminal 1:

```
claude --worktree zip-check
```

### Step 6: Start the bulk-discount Worktree

In terminal 2: `claude --worktree bulk-discount`

### Step 7: Start the csv-export Worktree

In terminal 3: `claude --worktree csv-export`

### Step 8: Give Each Worktree Its Own Environment

In each session, check for the `.env` file with `ls -a`, then run:

```
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
```

**Acceptance criteria:** each worktree has its own `.venv` and you have noted whether `.env` arrived.

> **Common Pitfall:** if a worktree has no `.env`, the file was created after the worktree. Copy it by hand, and note that `.worktreeinclude` applies at creation time only.

---

## Part 3: Run the Three Tasks in Parallel

### Step 9: Ask Each Session for Its Own Task Only

- zip-check: "Do Task A in TASKS.md and nothing else"
- bulk-discount: "Task B"
- csv-export: "Task C"

**Acceptance criteria:** each session changes only the files its task names.

### Step 10: Run the Tests in Each Session

**Expected result:** tests pass in each worktree.

### Step 11: Commit in Each Session

Ask Claude to commit the work with a clear message.

**Acceptance criteria:** three small commits, one per worktree.

---

## Part 4: Merge in Order

### Step 12: List the Worktrees

In terminal 4, in the main checkout:

```
git worktree list
```

**Expected result:** the main checkout plus three worktrees.

### Step 13: Merge One at a Time, Testing After Each

```
git merge worktree-zip-check
python -m pytest -q
git merge worktree-csv-export
python -m pytest -q
git merge worktree-bulk-discount
python -m pytest -q
```

**Acceptance criteria:** tests pass after every merge, not just at the end.

> **Troubleshooting:** a merge conflict means two sessions touched the same file. Read each diff and ask which task owns that file.

---

## Part 5: Clean Up

### Step 14: Remove the Worktrees and Branches

```
git worktree remove .claude/worktrees/zip-check
git worktree remove .claude/worktrees/csv-export
git worktree remove .claude/worktrees/bulk-discount
git branch -d worktree-zip-check worktree-csv-export worktree-bulk-discount
git worktree list
```

**Acceptance criteria:** `git worktree list` shows only the main checkout.

> **Troubleshooting:** if `git worktree remove` refuses because of changes, commit or discard them first.

---

## Part 6: Checkpoint

### Step 15: Verify Your Progress

- [ ] `git log --oneline` shows the baseline and three task commits
- [ ] Each commit changes only the files its task names
- [ ] Each worktree got its own `.venv`
- [ ] Whether `.env` reached each worktree was checked and noted
- [ ] Tests ran and passed inside each worktree
- [ ] Tests passed after each of the three merges, not only at the end
- [ ] `python -m pytest -q` passes on the main checkout with more than 14 tests
- [ ] All three worktrees removed and their branches deleted
- [ ] `git worktree list` shows only the main checkout

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| Worktree missing baseline files | A worktree branches from an old commit | The base reference points at the wrong place. Ask your instructor |
| `No module named pytest` | Tests fail inside a worktree | That worktree has no `.venv`. Run Step 8 there |
| No `.env` in a worktree | The file is absent | It was created after the worktree. Copy it by hand. `.worktreeinclude` applies at creation |
| Remove refused | `git worktree remove` errors | Uncommitted changes. Commit or discard them first |
| Merge conflict | Two branches touch one file | Two sessions edited the same file. Read each diff and decide which task owns it |

---

## What You Built

In 45 minutes, you:

- Ran three Claude sessions in parallel on one repository without them colliding
- Learned that each worktree is a fresh checkout: its own environment, and `.worktreeinclude` applying only at creation
- Merged in a deliberate order and tested after every merge, so a break would be attributable to one branch
- Cleaned up completely, leaving only the main checkout

---

## What's Next

Lab 2, Subagent Team Sprint, moves from three parallel sessions you drive to three roles that hand work to each other.

---

## Facilitator Notes

A good result is three small commits, each changing only the files its task names, with every test passing after every merge.

Task A adds `normalize_zip` with `12345`, `12345-6789`, hyphen-less nine digits, and `None` for bad input. Task B takes 5 percent off lines of 10 to 24 and 10 percent off 25 or more, with boundary tests at 9, 10, 24, and 25. Task C adds `to_csv` with header `id,customer,total`.

Note that after Task B the totals in `orders.json` change, but the largest order stays `SD-1003`.

Watch for a student whose session edited a file outside its task, and ask how they would have caught it from the diff.

This lab depends on the `worktree.baseRef` setting in `.claude/settings.json` of the project working on a local-only repository. That is unconfirmed, so rehearse it on the class VM before the day.

---

*Lab 1 Complete*
