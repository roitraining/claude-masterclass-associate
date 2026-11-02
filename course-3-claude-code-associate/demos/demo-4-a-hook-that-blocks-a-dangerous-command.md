# Demo 4: A Hook That Blocks a Dangerous Command

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Demo:** 4 of 9
**Time:** about 12 minutes

> Part of **[Claude Code Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Block a risky command deterministically with a hook, using exit code 2 so the reason goes back to Claude. Time: about 12 minutes.

**Files:** [`$FILES/hooks/block_dangerous.py`](../demo-files/hooks/block_dangerous.py), [`$FILES/hooks/check_python_after_edit.py`](../demo-files/hooks/check_python_after_edit.py), [`$FILES/hooks/settings.hooks.json`](../demo-files/hooks/settings.hooks.json).

**Context:** A prompt is a request. A hook is a rule. Exit code 2 blocks the action and sends stderr to Claude.

**Steps:**

1. Install the hooks in the project:

```
cd ~/work/shipdesk
mkdir -p .claude/hooks
cp $FILES/hooks/*.py .claude/hooks/
```

2. Merge `settings.hooks.json` into `.claude/settings.json`, keeping the existing `worktree` block. Read the `hooks` block aloud: event, matcher, command.
3. Test the script by hand, with no model involved:

```
echo '{"tool_input":{"command":"rm -rf build"}}' | python3 .claude/hooks/block_dangerous.py; echo "exit $?"
```

4. Start `claude` and ask: "Delete the build folder with rm -rf build, then push the result with git push."
5. Read Claude's reaction to the refusal.
6. Ask Claude to add a deliberate syntax error to `shipdesk/addresses.py`. Show the after-edit hook's message.

**Expected result:** The manual test prints the block reason and `exit 2`. In the session, the command does not run, and Claude explains it was blocked and why. The after-edit hook reports the syntax error back.

> **Instructor note:** Exit code 2 blocking, stderr feeding back to Claude, `PreToolUse` and `PostToolUse`, and the `Edit|Write` matcher are verified. The JSON the hook receives on stdin (the `tool_input.command` and `tool_input.file_path` fields), the exact nesting of the settings entry, and the relative `.claude/hooks/...` command path are not in the verified facts. Rehearse step 4 on the class VM first. What Claude does with an after-edit exit code 2, given that the edit already happened, also needs rehearsal. Multiple `PreToolUse` hooks combine with the most restrictive answer winning, and a hook that approves does not bypass the permission flow.

> **Why this matters:** A deny rule covers a command you listed. A hook can cover a pattern, run a script, and tell Claude why.

---

**Previous:** [Demo 3: Write a Subagent Role Contract](demo-3-write-a-subagent-role-contract.md) · **Next:** [Demo 5: A Hook That Runs Tests Before You Commit](demo-5-a-hook-that-runs-tests-before-you-commit.md)


*Demo 4 of 9*
