# Lab 2: Subagent Team Sprint

**Course:** Claude Code Associate
**Duration:** 40 minutes
**Format:** Instructor-led, in-class hands-on lab (200 level)

> Part of **[Claude Code Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] Lab 1 completed
- [ ] Python 3.11 or later, with `venv`
- [ ] Git 2.31 or later
- [ ] `claude` signed in
- [ ] `$FILES/shipdesk`: `TICKET-SD-142.md`, `docs/ROLE-CONTRACT.template.md`, `.claude/agents/planner.md`, `implementer.md`, `tester.md`
- [ ] `$FILES/hooks`

---

## Overview

The ticket adds promo codes. The three starter agents have tool lists and models you can change.

**The contract governs the run, and the hook gates the commit.** You write the contract before you run anything.

---

## Part 1: Set Up the Branch

### Step 1: Make a Fresh Copy on a Branch, with the Environment

```
cp -r $FILES/shipdesk ~/work/shipdesk-lab2 && cd ~/work/shipdesk-lab2
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
git init -q && git add -A && git commit -qm "baseline"
git switch -c sd-142
```

**Expected result:** a baseline commit on branch `sd-142`.

### Step 2: Read the Ticket, Including Its Limits

**Expected result:** you can state the ticket file list and its size limit.

---

## Part 2: Write the Role Contract First

### Step 3: Fill In Every Cell of the Contract

Copy the template to `docs/ROLE-CONTRACT.md` and fill in every cell: the three roles, tools, a model for each, what each must not do, the three handoffs, and the stop rules.

**Acceptance criteria:** no blank cells, and each role has a "Must not" line.

> **Key Insight:** a contract that gives every role every tool is not a contract. The planner should have no write tools and the tester no source edits.

### Step 4: Align the Agent Files with Your Contract

Open the three files in `.claude/agents/` and change anything that disagrees with your contract.

**Acceptance criteria:** the agent files and the contract say the same thing.

---

## Part 3: Install the Commit Gate

### Step 5: Install the Tests-Before-Commit Hook

```
mkdir -p .claude/hooks && cp $FILES/hooks/run_tests_before_commit.py .claude/hooks/
```

### Step 6: Register the Hook and Restart

Add this to `.claude/settings.json`, keeping the existing `worktree` block, then restart `claude`:

```
"hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [{"type": "command", "command": "python3 .claude/hooks/run_tests_before_commit.py"}]}]}
```

**Expected result:** the hook is registered and the session restarted.

---

## Part 4: Run the Three Roles

### Step 7: Run the Planner

Ask: "Use the planner agent on TICKET-SD-142.md. Return the plan only."

**Expected result:** a plan and no code changes.

> **Troubleshooting:** if Claude does the work itself and never calls an agent, name the agent in the prompt as written here.

### Step 8: Review the Plan Before Acting On It

Check it against the ticket and your contract. Fix it by asking, or accept it.

**Acceptance criteria:** the plan lists no file the ticket does not name.

> **Common Pitfall:** if the plan lists extra files, ask the planner to justify each, then cut the extras.

### Step 9: Run the Implementer

Ask: "Use the implementer agent to carry out this plan."

**Acceptance criteria:** the implementer changed source and not tests.

### Step 10: Run the Tester

Ask: "Use the tester agent to write and run tests for the change."

**Acceptance criteria:** the tester wrote tests and did not edit source.

> **Note:** if the tester reports a failure, that is the system working. Send the cause back to the implementer.

---

## Part 5: Review Against Your Stop Rules

### Step 11: Count the Diff Against Your Stop Rules

```
git diff --stat
```

**Acceptance criteria:** the changed files and lines are inside the stop rules you wrote in Step 3.

### Step 12: Review the Diff with the Demo 6 Checklist

Check scope, size, that tests cover each criterion, and that no test was changed to fit the code.

**Acceptance criteria:** all four checks pass, or the failure is sent back to the right role.

---

## Part 6: Commit Through the Hook

### Step 13: Commit to the Branch

Ask Claude to commit to the `sd-142` branch. **The hook must run first.**

**Acceptance criteria:** the commit lands on `sd-142` and the hook ran before it.

> **Troubleshooting:** if the hook blocks the commit although tests pass, it cannot find pytest. Activate the environment, or keep it at `.venv`.

---

## Part 7: Checkpoint

### Step 14: Verify Your Progress

- [ ] A baseline commit exists on branch `sd-142`
- [ ] `docs/ROLE-CONTRACT.md` is complete, with no blank cells
- [ ] Every role has a "Must not" line
- [ ] The planner has no write tools; the tester cannot edit source
- [ ] The agent files agree with the contract
- [ ] The tests-before-commit hook is installed and registered
- [ ] The planner returned a plan only, with no code changes
- [ ] The plan names no file outside the ticket
- [ ] The implementer changed source and not tests
- [ ] The tester wrote tests and did not edit source
- [ ] `git diff --stat` is inside your stop rules for files and lines
- [ ] No test was changed to fit the code
- [ ] All tests pass, and one test rejects an expired promo
- [ ] A commit on `sd-142` went through the hook

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| No agent invoked | Claude does the work itself | Name the agent in the prompt, as in Steps 7 to 10 |
| Roles bleed | The implementer edits tests, or the tester edits source | Tighten its tool list and its "Must not" line, then rerun |
| Hook blocks a passing build | Commit refused although tests pass | The hook cannot find pytest. Activate the environment, or keep it at `.venv` |
| Plan too broad | Files the ticket does not name | Ask the planner to justify each, then cut the extras |
| Tester reports failure | A test fails | That is the system working. Send the cause back to the implementer |

---

## What You Built

In 40 minutes, you:

- Wrote the role contract **before** the run, so the tool lists came from a decision rather than a default
- Ran a planner that could not write, and a tester that could not edit source, and saw the handoffs hold
- Checked the diff against stop rules you set yourself, rather than against how the result looked
- Gated the commit behind a hook, so passing tests became a precondition instead of a hope

---

## What's Next

Lab 3, the Legacy API Modernization Capstone, puts the worktrees and the role contract together on a larger change.

---

## Facilitator Notes

A good result matches the ticket: a new `shipdesk/promos.py` with a promo table, `order_total(items, promo=None, today=None)`, and `ValueError("promo expired")` and `ValueError("unknown promo")`.

A good tester writes a boundary test for an expiry date equal to today, which must be accepted, and one for the day after, which must be rejected.

A strong contract gives the planner no write tools and the tester no source edits. Common weak contracts give every role every tool. Ask each student which handoff would have lost the most context.

Whether a named agent is always invoked when its name appears in a prompt can vary, so be ready to reword the prompt.

The Demo 6 diff is a sample of what a careless team produces for this same ticket, so do not show it before students finish.

---

*Lab 2 Complete*
