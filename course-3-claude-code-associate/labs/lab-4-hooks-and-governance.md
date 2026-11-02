# Lab 4: Hooks and Governance (take-home)

> Part of **[Claude Code Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

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
