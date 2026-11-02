# Lab 3: Legacy API Modernization Capstone

> Part of **[Claude Code Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

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
