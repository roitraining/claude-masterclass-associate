# Lab 4: Hooks and Governance (take-home)

**Course:** Claude Code Associate
**Duration:** Untimed — no time limit, work at your own pace
**Format:** Take-home lab

> Part of **[Claude Code Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] Labs 1 through 3 completed
- [ ] Python 3.11 or later, Git, and `claude` signed in
- [ ] `$FILES/hooks`: `block_dangerous.py`, `run_tests_before_commit.py`, `check_python_after_edit.py`, `settings.hooks.json`, `test_hooks.py`
- [ ] `$FILES/managed-policy` and `$FILES/shipdesk`
- [ ] Three standards your own team actually cares about

> **Note:** testing with `--settings` is not the same as a real managed file, whose location needs the settings documentation and administrator rights.

---

## Overview

Work on a copy of `shipdesk`. Pick three standards your own team cares about. The starter hooks show the pattern. **You write the rest.**

A standard enforced by a prompt instruction is not enforced. The point of this lab is the difference between a request and a gate.

---

## Part 1: Set Up

### Step 1: Copy the Project and Create a Baseline

```
cp -r $FILES/shipdesk ~/work/shipdesk-gov
```

Then run `git init`, a baseline commit, and the environment setup.

**Expected result:** a clean baseline you can test gates against.

---

## Part 2: Define Your Standards and Gates

### Step 2: Write Down Three Standards

Record them in `docs/STANDARDS.md`. For example: no hard-coded secrets, every new function has a test, no edits to a protected folder.

**Acceptance criteria:** three standards, specific enough to test.

### Step 3: Decide the Gate for Each Standard

Choose for each: a hook that blocks, a hook that checks after an edit, a deny rule, or a review item.

**Acceptance criteria:** every standard has a named gate type.

> **Key Insight:** a prompt instruction such as "never delete files" is not a gate. It is a request. Pick a hook or a deny rule.

---

## Part 3: Write and Register the Hooks

### Step 4: Write One New Hook Script

Write it in `.claude/hooks/`. It reads the JSON from stdin and exits with code 2 and a clear message on a violation.

**Acceptance criteria:** the script exits 2 with an actionable message on a violation, and exits 0 on input it does not recognize.

> **Common Pitfall:** a hook that exits 2 on unexpected input blocks everything. Handle bad JSON by exiting 0.

> **Common Pitfall:** if Claude retries the blocked action in a loop, the stderr message does not say what to do instead. Make it say so.

### Step 5: Register All Your Hooks

Add them to `.claude/settings.json`.

**Acceptance criteria:** each hook has a matcher that actually matches.

> **Hint:** use `Bash` for commands and `Edit|Write` for edits. A hook that never fires usually has the wrong matcher.

---

## Part 4: Test the Hooks

### Step 6: Write a Passing and a Blocking Case for Each

Copy `test_hooks.py` to `.claude/hooks/test_my_hooks.py` and add both cases for each of your hooks. Run it.

**Acceptance criteria:** the hook tests pass, with a passing case **and** a blocking case per hook.

---

## Part 5: Add a Managed Policy

### Step 7: Adapt the Managed Settings

Copy `managed-settings.json` and change its deny rules and hook to match your standards.

### Step 8: Start with Your Policy and Check the Sources

```
claude --settings <your-policy-file>
```

Then run `/status`.

**Acceptance criteria:** `/status` shows your policy among the sources that apply.

---

## Part 6: Try to Break It

### Step 9: Attempt an Override from a Project File

Try to break your own policy from a project file, as in `project-settings-attempt.json`.

**Acceptance criteria:** you have recorded what held and what did not.

> **Troubleshooting:** if the managed policy seems ignored, a project file may be loosening it. Check `/status` for the sources that apply.

---

## Part 7: Write the Governance Note

### Step 10: Write Half a Page

Write `docs/GOVERNANCE.md`: the standards, the gate for each, what a project setting cannot override, and what you could not test.

**Acceptance criteria:** the note claims enforcement only for things you actually tried.

---

## Part 8: Checkpoint

### Step 11: Verify Your Progress

- [ ] A baseline commit exists on a copy of `shipdesk`
- [ ] Three standards written in `docs/STANDARDS.md`
- [ ] Each standard has a named gate: blocking hook, post-edit hook, deny rule, or review item
- [ ] No standard relies on a prompt instruction alone
- [ ] At least one new hook script written, reading JSON from stdin
- [ ] The hook exits 2 with an actionable message on a violation
- [ ] The hook exits 0 on input it does not recognize
- [ ] Every block message names the rule that blocked it
- [ ] All hooks registered in `.claude/settings.json` with matchers that fire
- [ ] `test_my_hooks.py` has a passing case and a blocking case for each hook, and passes
- [ ] A managed policy file adapted to your standards
- [ ] `/status` shows your policy among the applied sources
- [ ] An override attempt was made from a project file
- [ ] What held and what did not is recorded
- [ ] `docs/GOVERNANCE.md` states the standards, the gates, what cannot be overridden, and what you could not test

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| Hook never fires | No effect on any action | The matcher does not match the tool name. Use `Bash` for commands and `Edit|Write` for edits |
| Hook blocks everything | Every action refused | The script exits 2 on input it did not expect. Handle bad JSON by exiting 0 |
| Retry loop | Claude keeps retrying the blocked action | Make the stderr message say what to do instead |
| Policy appears ignored | Managed rules have no effect | A project file may be loosening it. Check `/status` for the sources that apply |
| Cannot attribute a block | You cannot tell which rule fired | Add the rule name to every block message |

---

## What You Built

Working at your own pace, you:

- Turned three of your own team standards into gates, rather than into instructions nobody enforces
- Wrote a hook that fails safe: blocking on a real violation, exiting cleanly on input it does not understand
- Gave every hook both a passing and a blocking test, so you know it fires and knows when not to
- Tried to break your own policy from a project file and recorded what actually held
- Wrote a governance note that claims enforcement only for what you tested

---

## What's Next

This is the final lab in Claude Code Associate. The distinction to carry forward: a commit made in your own terminal bypasses hooks that watch the Bash tool of Claude. Know what your gates do not cover.

---

## Facilitator Notes

A good result is three hooks or rules that each have a passing and a blocking test, a policy that survives an override attempt, and an honest list of what was not tested.

Review `GOVERNANCE.md` for claims of enforcement that were never tried. A common weak answer relies on a prompt instruction ("never delete files") instead of a hook or a deny rule.

Remind students that a commit made in their own terminal bypasses hooks that watch the Bash tool of Claude, and that testing with `--settings` is not the same as a real managed file, whose location needs the settings documentation and administrator rights.

---

*Lab 4 Complete*
