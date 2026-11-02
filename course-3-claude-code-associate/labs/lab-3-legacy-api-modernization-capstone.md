# Lab 3: Legacy API Modernization Capstone

**Course:** Claude Code Associate
**Duration:** 60 minutes
**Format:** Instructor-led, in-class hands-on lab (200 level). Allow the full hour

> Part of **[Claude Code Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] Labs 1 and 2 completed — this lab uses worktrees, a role contract and hooks together
- [ ] Python 3.11 or later, with `venv`
- [ ] Git 2.31 or later, and `claude` signed in
- [ ] Three terminals you can keep open at once
- [ ] `$FILES/legacy-invoice`: `batch_invoices.py`, `orders.csv`, `tests/test_legacy.py`, `TARGET.md`, `CLAUDE.md`, `requirements.txt`
- [ ] `$FILES/hooks` and `$FILES/shipdesk/.claude/agents`

> **Note:** if `fastapi` or `httpx` fails to install, tell your instructor before debugging it yourself.

---

## Overview

`batch_invoices.py` has no documentation and several smells: global state, float money, bare `except` blocks that drop bad rows, a slow lookup per row, and hard-coded rates.

`tests/test_legacy.py` pins its behavior. **Those characterization tests are what make the modernization safe.** `TARGET.md` is the brief.

---

## Part 1: Set Up the Project, Agents and Hooks

### Step 1: Copy Everything and Create the Environment

```
cp -r $FILES/legacy-invoice ~/work/invoice-capstone && cd ~/work/invoice-capstone
mkdir -p .claude/agents .claude/hooks
cp $FILES/shipdesk/.claude/agents/planner.md $FILES/shipdesk/.claude/agents/implementer.md $FILES/shipdesk/.claude/agents/tester.md .claude/agents/
cp $FILES/hooks/block_dangerous.py $FILES/hooks/run_tests_before_commit.py .claude/hooks/
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
```

### Step 2: Register Both Hooks, Then Run the Tests

```
cat > .claude/settings.json <<'EOF'
{"worktree": {"baseRef": "head"},
 "hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [
   {"type": "command", "command": "python3 .claude/hooks/block_dangerous.py"},
   {"type": "command", "command": "python3 .claude/hooks/run_tests_before_commit.py"}]}]}}
EOF
python -m pytest -q
```

**Expected result:** the legacy tests pass before you change anything.

### Step 3: Commit a Baseline Including `.claude/`

```
git init -q && git add -A && git commit -qm "baseline"
```

---

## Part 2: Read the Brief and Write the Contract

### Step 4: Read the Target and the Script — Do Not Edit the Script

**Expected result:** you can list the six numbered requirements in `TARGET.md`.

### Step 5: Write a Short Role Contract

Name the three roles and what each hands off. Reuse your Lab 2 contract if you have it.

**Acceptance criteria:** three roles with handoffs and stop rules.

---

## Part 3: Create Two Worktrees

### Step 6: Start the api and docs Worktrees

Terminal 1: `claude --worktree api`. Terminal 2: `claude --worktree docs`.

### Step 7: Give Each Worktree Its Own Environment

```
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
```

**Acceptance criteria:** both worktrees have their own `.venv`.

> **Common Pitfall:** if the hook blocks every commit in a worktree, that worktree has no environment. Run this step there.

---

## Part 4: Build the Endpoint

### Step 8: Run the Planner

In the `api` session: "Use the planner agent on TARGET.md and batch_invoices.py. Return the plan only."

**Expected result:** a plan and no code changes.

### Step 9: Review the Plan, Then Implement

Read the plan against the six numbered requirements in `TARGET.md`. Fix it, then ask: "Use the implementer agent to build app.py from this plan."

**Acceptance criteria:** the plan was reviewed before implementation.

> **Key Insight:** teams that skip the plan review usually rebuild the same bugs in async form, such as swallowing exceptions.

### Step 10: Run the Tester

Ask: "Use the tester agent to write tests/test_app.py and run all tests."

**Acceptance criteria:** new tests pass alongside the legacy tests.

---

## Part 5: Write the Documentation

### Step 11: Write the README in the docs Worktree

In the `docs` session: "Write README.md for the endpoint described in TARGET.md: what it does, the request, the response, and three known limits. Change only README.md."

**Acceptance criteria:** only `README.md` changed in this worktree.

> **Troubleshooting:** if the `docs` session edits `app.py`, remind it of the one-file limit and discard the change.

---

## Part 6: Verify Speed and Commit

### Step 12: Test the Speed Requirement

In the `api` session, ask Claude to time the 10-row sample through the endpoint with the original 0.05 second lookup delay.

**Acceptance criteria:** the endpoint meets the speed requirement in `TARGET.md`.

> **Troubleshooting:** if the endpoint is `async` but still slow, a lookup uses `time.sleep` or the calls run one after another. Ask for `asyncio.sleep` and `asyncio.gather`.

### Step 13: Commit from Each Session

**Acceptance criteria:** the tests-before-commit hook ran on each commit.

---

## Part 7: Review and Merge

### Step 14: Review the Diff, Then Merge Docs First

In the main checkout, review the `api` diff with the Demo 6 checklist, then:

```
git merge worktree-docs && python -m pytest -q
git merge worktree-api && python -m pytest -q
```

**Acceptance criteria:** tests pass after each merge.

> **Troubleshooting:** if totals differ from the legacy output by a cent, the new code used `Decimal` rounding in a different order than the float rounding of the script. Match the legacy results first and note the difference as a known limit.

---

## Part 8: Clean Up and Present

### Step 15: Remove Both Worktrees

```
git worktree remove .claude/worktrees/api
git worktree remove .claude/worktrees/docs
```

### Step 16: Prepare a Two-Minute Readout

Cover the endpoint, the workflow, one thing a hook caught or would have caught, and one thing you would change next time.

**Acceptance criteria:** all four points covered.

---

## Part 9: Checkpoint

### Step 17: Verify Your Progress

- [ ] The legacy tests passed before any change
- [ ] A baseline commit includes `.claude/`
- [ ] The legacy script was never edited
- [ ] A role contract names three roles, handoffs and stop rules
- [ ] Both worktrees have their own `.venv`
- [ ] The planner returned a plan only
- [ ] The plan was reviewed against the six requirements before implementation
- [ ] `app.py`, `tests/test_app.py` and `README.md` are merged on the main checkout
- [ ] The legacy tests still pass alongside the new ones
- [ ] The endpoint returns the legacy totals for the nine valid rows
- [ ] Row 1007 is reported in `errors`, not silently dropped
- [ ] The speed requirement is met with the original 0.05 second delay
- [ ] The `docs` worktree changed only `README.md`
- [ ] Both commits went through the tests-before-commit hook
- [ ] Both worktrees removed
- [ ] A two-minute readout covering endpoint, workflow, a hook catch, and a change for next time

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| Hook blocks every commit | Commits refused in a worktree | That worktree has no environment. Run Step 7 there |
| Totals off by a cent | New output differs from legacy | `Decimal` rounding applied in a different order than the float rounding of the script. Match the legacy results and note the difference as a known limit |
| Async but still slow | Speed requirement missed | A lookup uses `time.sleep`, or the calls run sequentially. Ask for `asyncio.sleep` and `asyncio.gather` |
| Docs session overreaches | `app.py` edited in the `docs` worktree | Remind it of the one-file limit and discard the change |
| Install failure | `fastapi` or `httpx` will not install | Tell your instructor before debugging |

---

## What You Built

In 60 minutes, you:

- Modernized an undocumented script without editing it, using its characterization tests as the safety net
- Ran a planner, implementer and tester across two worktrees with hooks gating every commit
- Reviewed the plan before implementation, which is what stops the same bugs reappearing in async form
- Kept the error row visible instead of letting a bare `except` drop it
- Met a real speed requirement rather than assuming `async` made it fast

---

## What's Next

Lab 4, Hooks and Governance, is the take-home. It moves from using given hooks to writing the gates for your own team's standards.

---

## Facilitator Notes

A good result is a FastAPI `app.py` with one `POST /invoices/batch` route, async customer and tax lookups gathered across orders, no module-level totals, and an `errors` list that includes `{"oid": "1007", "reason": ...}`.

The legacy totals to match are 1001: 53.62, 1002: 102.00, 1003: 126.32, 1004: 10.56, 1005: 835.48, 1006: 60.56, 1008: 76.12, 1009: 0.00, 1010: 756.71, and a grand total of 2021.37.

A strong readout names the characterization tests as what made the modernization safe. Teams that skip the plan review usually rebuild the same bugs in async form, such as swallowing exceptions.

The instructor should rehearse the whole lab once, since it runs three agents across two worktrees and hooks together, and hook behavior inside worktrees was not verified. Allow the full 60 minutes. Ask students who finish early to add a `/health` route through the same team.

---

*Lab 3 Complete*
