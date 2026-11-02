# Lab 2: Subagent Team Sprint

> Part of **[Claude Code Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

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
