# Claude Code Associate: Labs

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Contents:** Three timed hands-on labs and a take-home lab. The numbers match the Today's Labs slide.

---

## About this guide

You run these labs yourself, on your class Anthropic account, in the order below. They assume Essentials Course 3: the core loop, permission modes, plan mode, CLAUDE.md, checkpoints, review before merge, and deny rules are not retaught here.

In this guide `$FILES` is the `demo-files` folder your instructor gives you. Everything is local. You commit locally and you never push. Every name, company, and figure is fictional, and no lab needs a credential or a cloud account.

Claude Code can word things differently each time. Check your result against the Checkpoint, not against exact text.

**Before Lab 1:** Python 3.11 or later, Git with your name and email set, and `claude` signed in.

---

## Lab 1: Git Worktrees Parallel Development

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

---

## Lab 2: Subagent Team Sprint

**Learning objective:** Write a role contract first, then run a planner, an implementer, and a tester to produce a reviewed branch from a single ticket. Time: 40 minutes.

**Files:** `$FILES/shipdesk`: `TICKET-SD-142.md`, `docs/ROLE-CONTRACT.template.md`, `.claude/agents/planner.md`, `implementer.md`, `tester.md`, and `$FILES/hooks`.

**Context:** The ticket adds promo codes. The three starter agents have tool lists and models you can change. The contract governs the run, and the hook gates the commit.

**Steps:**

1. Make a fresh copy on a branch, with the environment:

```
cp -r $FILES/shipdesk ~/work/shipdesk-lab2 && cd ~/work/shipdesk-lab2
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
git init -q && git add -A && git commit -qm "baseline"
git switch -c sd-142
```

2. Read `TICKET-SD-142.md`, including its limits.
3. Copy the contract template to `docs/ROLE-CONTRACT.md` and fill in every cell: the three roles, tools, a model for each, what each must not do, the three handoffs, and the stop rules.
4. Open the three files in `.claude/agents/`. Change anything that disagrees with your contract.
5. Install the tests-before-commit hook:

```
mkdir -p .claude/hooks && cp $FILES/hooks/run_tests_before_commit.py .claude/hooks/
```

6. Add this to `.claude/settings.json`, keeping the existing `worktree` block, then restart `claude`:

```
"hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [{"type": "command", "command": "python3 .claude/hooks/run_tests_before_commit.py"}]}]}
```

7. Start `claude` and ask: "Use the planner agent on TICKET-SD-142.md. Return the plan only."
8. Read the plan. Check it against the ticket and your contract. Fix it by asking, or accept it.
9. Ask: "Use the implementer agent to carry out this plan."
10. Ask: "Use the tester agent to write and run tests for the change."
11. Run `git diff --stat` and count the changed files and lines against your stop rules.
12. Review the diff with the Demo 6 checklist: scope, size, tests cover each criterion, and no test changed to fit the code.
13. Ask Claude to commit to the `sd-142` branch. The hook must run first.

**Checkpoint:** Branch `sd-142` has a local commit that stays inside the ticket's files and size limit, and `docs/ROLE-CONTRACT.md` is complete. All tests pass, and one test rejects an expired promo.

**Common problems:**

- Claude does the work itself and never calls an agent: name the agent in the prompt, as in steps 7 to 10.
- The implementer edits tests, or the tester edits source: tighten its tool list and its "Must not" line, then rerun.
- The commit is blocked by the hook although tests pass: the hook cannot find pytest. Activate the environment, or keep it at `.venv`.
- The plan lists files the ticket does not name: ask the planner to justify each, then cut the extras.
- The tester reports a failure: that is the system working. Send the cause back to the implementer.

**Facilitator note:** A good result matches the ticket: a new `shipdesk/promos.py` with a promo table, `order_total(items, promo=None, today=None)`, and `ValueError("promo expired")` and `ValueError("unknown promo")`. A good tester writes a boundary test for an expiry date equal to today, which must be accepted, and one for the day after, which must be rejected. A strong contract gives the planner no write tools and the tester no source edits. Common weak contracts give every role every tool. Ask each student which handoff would have lost the most context. Whether a named agent is always invoked when its name appears in a prompt can vary, so be ready to reword the prompt. The Demo 6 diff is a sample of what a careless team produces for this same ticket, so do not show it before students finish.

---

## Lab 3: Legacy API Modernization Capstone

**Learning objective:** Modernize an undocumented, synchronous script into an async endpoint, using worktrees, a subagent team, and hooks together. Time: 60 minutes.

**Files:** `$FILES/legacy-invoice`: `batch_invoices.py`, `orders.csv`, `tests/test_legacy.py`, `TARGET.md`, `CLAUDE.md`, and `requirements.txt`. Also `$FILES/hooks` and `$FILES/shipdesk/.claude/agents`.

**Context:** `batch_invoices.py` has no documentation and several smells: global state, float money, bare `except` blocks that drop bad rows, a slow lookup per row, and hard-coded rates. `tests/test_legacy.py` pins its behavior. `TARGET.md` is the brief.

**Steps:**

1. Copy the project and the starter agents, install the hooks, and create the environment:

```
cp -r $FILES/legacy-invoice ~/work/invoice-capstone && cd ~/work/invoice-capstone
mkdir -p .claude/agents .claude/hooks
cp $FILES/shipdesk/.claude/agents/planner.md $FILES/shipdesk/.claude/agents/implementer.md $FILES/shipdesk/.claude/agents/tester.md .claude/agents/
cp $FILES/hooks/block_dangerous.py $FILES/hooks/run_tests_before_commit.py .claude/hooks/
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
```

2. Create `.claude/settings.json` with the two hooks, then run the tests:

```
cat > .claude/settings.json <<'EOF'
{"worktree": {"baseRef": "head"},
 "hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [
   {"type": "command", "command": "python3 .claude/hooks/block_dangerous.py"},
   {"type": "command", "command": "python3 .claude/hooks/run_tests_before_commit.py"}]}]}}
EOF
python -m pytest -q
```

3. Commit a baseline that includes `.claude/`: `git init -q && git add -A && git commit -qm "baseline"`
4. Read `TARGET.md` and the script. Do not edit the script.
5. Write a short role contract: the three roles, and what each hands off. Reuse your Lab 2 contract if you have it.
6. In terminal 1, run `claude --worktree api`. In terminal 2, run `claude --worktree docs`.
7. In each worktree, run `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt`
8. In the `api` session, ask: "Use the planner agent on TARGET.md and batch_invoices.py. Return the plan only."
9. Read the plan against the six numbered requirements in `TARGET.md`. Fix it, then ask: "Use the implementer agent to build app.py from this plan."
10. Ask: "Use the tester agent to write tests/test_app.py and run all tests."
11. In the `docs` session, ask: "Write README.md for the endpoint described in TARGET.md: what it does, the request, the response, and three known limits. Change only README.md."
12. In the `api` session, test the speed requirement by asking Claude to time the 10-row sample through the endpoint with the original 0.05 second lookup delay.
13. Ask each session to commit. The tests-before-commit hook runs on each.
14. In the main checkout, review the `api` diff with the Demo 6 checklist. Merge `worktree-docs`, then `worktree-api`, and run the tests after each:

```
git merge worktree-docs && python -m pytest -q
git merge worktree-api && python -m pytest -q
```

15. Remove both worktrees: `git worktree remove .claude/worktrees/api` and `git worktree remove .claude/worktrees/docs`
16. Prepare a two-minute readout: the endpoint, the workflow, one thing a hook caught or would have caught, and one thing you would change next time.

**Checkpoint:** `app.py`, `tests/test_app.py`, and `README.md` are merged on the main checkout. The legacy tests still pass alongside the new ones. The endpoint returns the legacy totals for the nine valid rows, reports row 1007 in `errors`, and meets the speed requirement. You present the endpoint and the workflow.

**Common problems:**

- The hook blocks every commit in a worktree: that worktree has no environment. Run step 7 there.
- Totals differ from the legacy output by a cent: the new code used `Decimal` rounding in a different order than the script's float rounding. Match the legacy results first and note the difference as a known limit.
- The endpoint is `async` but still slow: a lookup uses `time.sleep` or the calls run one after another. Ask for `asyncio.sleep` and `asyncio.gather`.
- The `docs` session edits `app.py`: remind it of the one-file limit and discard the change.
- `fastapi` or `httpx` fails to install: tell your instructor before debugging.

**Facilitator note:** A good result is a FastAPI `app.py` with one `POST /invoices/batch` route, async customer and tax lookups gathered across orders, no module-level totals, and an `errors` list that includes `{"oid": "1007", "reason": ...}`. The legacy totals to match are 1001: 53.62, 1002: 102.00, 1003: 126.32, 1004: 10.56, 1005: 835.48, 1006: 60.56, 1008: 76.12, 1009: 0.00, 1010: 756.71, and a grand total of 2021.37. A strong readout names the characterization tests as what made the modernization safe. Teams that skip the plan review usually rebuild the same bugs in async form, such as swallowing exceptions. The Instructor should rehearse the whole lab once, since it runs three agents across two worktrees and hooks together, and hook behavior inside worktrees was not verified. Allow the full 60 minutes. Ask students who finish early to add a `/health` route through the same team.

---

## Lab 4: Hooks and Governance (take-home)

**Learning objective:** Configure a set of hooks and a managed policy that enforce your own team's coding standards, and prove each one works. No time limit.

**Files:** `$FILES/hooks`: `block_dangerous.py`, `run_tests_before_commit.py`, `check_python_after_edit.py`, `settings.hooks.json`, and `test_hooks.py`. Also `$FILES/managed-policy` and `$FILES/shipdesk`.

**Context:** Work on a copy of `shipdesk`. Pick three standards your own team cares about. The starter hooks show the pattern. You write the rest.

**Steps:**

1. Copy the project: `cp -r $FILES/shipdesk ~/work/shipdesk-gov` and run `git init`, a baseline commit, and the environment setup.
2. Write down three standards in `docs/STANDARDS.md`. Example: no hard-coded secrets, every new function has a test, no edits to a protected folder.
3. For each standard, decide the gate: a hook that blocks, a hook that checks after an edit, a deny rule, or a review item.
4. Write one new hook script in `.claude/hooks/` that reads the JSON from stdin and exits with code 2 and a clear message on a violation.
5. Add all your hooks to `.claude/settings.json`.
6. Copy `test_hooks.py` to `.claude/hooks/test_my_hooks.py` and add a passing case and a blocking case for each of your hooks. Run it.
7. Copy `managed-settings.json` and change its deny rules and hook to match your standards.
8. Start `claude --settings <your-policy-file>` and run `/status`.
9. Try to break your own policy from a project file, as in `project-settings-attempt.json`. Record what held and what did not.
10. Write a half-page `docs/GOVERNANCE.md`: the standards, the gate for each, what a project setting cannot override, and what you could not test.

**Checkpoint:** Your hook tests pass. Each standard has a gate you can name. `docs/GOVERNANCE.md` states which rules held under your override attempt and which did not.

**Common problems:**

- A hook never fires: the matcher does not match the tool name. Use `Bash` for commands and `Edit|Write` for edits.
- A hook blocks everything: the script exits 2 on input it did not expect. Handle bad JSON by exiting 0.
- Claude retries the blocked action in a loop: make the stderr message say what to do instead.
- The managed policy seems ignored: a project file may be loosening it. Check `/status` for the sources that apply.
- You cannot tell which rule blocked an action: add the rule name to every block message.

**Facilitator note:** A good result is three hooks or rules that each have a passing and a blocking test, a policy that survives an override attempt, and an honest list of what was not tested. Review `GOVERNANCE.md` for claims of enforcement that were never tried. A common weak answer relies on a prompt instruction ("never delete files") instead of a hook or a deny rule. Remind students that a commit made in their own terminal bypasses hooks that watch Claude's Bash tool, and that testing with `--settings` is not the same as a real managed file, whose location needs the settings documentation and administrator rights.
