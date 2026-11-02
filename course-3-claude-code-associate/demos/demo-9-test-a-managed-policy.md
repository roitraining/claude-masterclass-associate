# Demo 9: Test a Managed Policy

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Demo:** 9 of 9
**Time:** about 15 minutes

> Part of **[Claude Code Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Author a managed policy and test what a project setting, a hook, and a subagent cannot override. Time: about 15 minutes.

**Files:** [`$FILES/managed-policy/managed-settings.json`](../demo-files/managed-policy/managed-settings.json), `project-settings-attempt.json`, and `README.md`.

**Context:** Managed settings sit at the top of the precedence order: managed, command line, project local, shared project, user. List keys such as `permissions.allow` merge unless `allowManagedPermissionRulesOnly` is set.

**Steps:**

1. Read `managed-settings.json` aloud: three deny rules, `allowManagedPermissionRulesOnly`, `allowManagedHooksOnly`, and a managed hook.
2. Install the policy hook, then copy the project's attempt into place:

```
mkdir -p ~/policy && cp $FILES/hooks/block_dangerous.py ~/policy/
cd ~/work/shipdesk
cp $FILES/managed-policy/project-settings-attempt.json .claude/settings.local.json
```

3. Start Claude Code with the policy applied as a command-line settings file:

```
claude --settings $FILES/managed-policy/managed-settings.json
```

4. Run `/status` and read which sources apply.
5. Ask: "Run git push origin main." Then ask: "Show me the contents of .env."
6. Check the project hook: `ls project-hook-ran.txt`.
7. Press Shift+Tab to cycle modes and show that `bypassPermissions` is not the active mode, despite the project file.
8. Ask a subagent that has Bash to run the push: "Use the tester agent to run git push origin main." (Copy `.claude/agents/` from the project if it is not loaded.)
9. Clean up: `rm .claude/settings.local.json`.

**Expected result:** The push and the `.env` read are denied even though the project file allows them. The project hook marker file does not appear. The session is not in `bypassPermissions`. `/status` lists the sources that apply.

> **Instructor note:** This run uses `--settings`, which is second in precedence and so is a stand-in for a true managed file. Whether `allowManagedPermissionRulesOnly` and `allowManagedHooksOnly` are honored from `--settings`, and not only from a real managed file, is not in the verified facts. Rehearse. The installed location of a real `managed-settings.json` per operating system is also not in the verified facts, and installing it needs administrator rights: take it from the settings documentation and keep it instructor-only. Verified: `permissions.defaultMode` values `auto` and `bypassPermissions` do not take effect from project or local files, and `allowManagedHooksOnly` restricts hooks to managed settings. Whether a subagent's own `permissionMode` can loosen a managed deny rule is not in the verified facts, so step 8 is a live test of an open question: report what you see. Server-managed settings do not reach a Cowork session running on a machine.

> **Why this matters:** A team standard that a project file can switch off is a suggestion. Testing the policy is how you learn which is which.

---

**Previous:** [Demo 8: A Routine Versus a Scheduled Task](demo-8-a-routine-versus-a-scheduled-task.md)


*Demo 9 of 9*
