# Claude Code Associate: Demos

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Contents:** 9 instructor-led demos. Each takes 15 minutes or less and has a learning objective. The numbers match the Today's Demos slide.

---

## About this guide

Run the demos in order. Each has the same layout: a learning objective, a time, a Files line when it uses files, a short context paragraph, steps, an Expected result, an Instructor note, and a Why this matters note.

These demos assume Essentials Course 3. They do not re-teach the core loop, permission modes, plan mode, CLAUDE.md, checkpoints, a read-only reviewer subagent, review before merge, or deny rules.

All demos run on a class Anthropic account. Demo 7 is instructor-only because Agent Teams are experimental and off by default. No demo needs a cloud route, and none needs a credential. Every person, company, and figure in the files is fictional. Claude Code can word things differently each time, so check results against the Expected result and not against exact text.

**Files.** In this guide `$FILES` means the `demo-files` folder your instructor gives you:

- `$FILES/shipdesk` is a small Python project with tests, three starter subagents in `.claude/agents/`, and a ticket, for Demos 1, 2, 3, 5, and 6.
- `$FILES/hooks` holds hook scripts and a settings snippet, for Demos 4 and 5.
- `$FILES/agent-pr/sd-142-promo-codes.diff` is a pull request an agent produced, for Demo 6.
- `$FILES/managed-policy` holds a managed policy and a project file that tries to defeat it, for Demo 9.

> **Work in your own copy.** Demos with files start by copying `shipdesk` into `~/work` and committing a baseline. Commit locally only. Nothing in this course pushes to a remote.

> **Token cost.** Parallel sessions multiply usage. Use the small projects as given and keep prompts narrow.

---

## Setup: Copy the project once

**Time:** about 5 minutes, before Demo 1.

1. Copy the project, create an environment, and commit a baseline:

```
mkdir -p ~/work && cp -r $FILES/shipdesk ~/work/
cd ~/work/shipdesk
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
git init -q && git add -A && git commit -qm "baseline"
python -m pytest -q
```

**Expected result:** 14 tests pass.

> **Instructor note:** `.claude/settings.json` in the project sets `worktree.baseRef` to `"head"`, so new worktrees branch from the local baseline commit. With no remote, the default `"fresh"` branches from the remote default branch, and what that does in a local-only repository was not tested. The exact nesting of that key in a settings file is not in the verified facts. Rehearse once on the class VM. If worktrees do not start from your baseline commit, fix this before Demo 1.

---

## Demo 1: Two Worktrees, Two Tasks

**Learning objective:** Run two Claude Code sessions on the same project at once, with each session's edits isolated. Time: about 12 minutes.

**Files:** `$FILES/shipdesk`: `TASKS.md` (tasks A and B), `.worktreeinclude`, `.gitignore`.

**Context:** A worktree checks a second branch out into its own directory. It shares the repository history with the main checkout, but it has its own files, so two sessions cannot overwrite each other.

**Steps:**

1. In `~/work/shipdesk`, create a harmless `.env` and open `.gitignore` and `.worktreeinclude`. Show that `.claude/worktrees/` is ignored and that `.env` is listed for copying:

```
echo "SHIPDESK_REGION=demo" > .env
cat .gitignore .worktreeinclude
```

2. In terminal 1, start a session in a new worktree and give it Task A from `TASKS.md`:

```
claude --worktree zip-check
```

3. In terminal 2, from `~/work/shipdesk`, start a second worktree for Task B:

```
claude -w bulk-discount
```

4. In each session, ask: "Do the task in TASKS.md for this branch only: Task A" (terminal 1) and "Task B" (terminal 2).
5. In terminal 3, show what exists and where:

```
git worktree list
ls -a .claude/worktrees/zip-check
```

6. In terminal 2, ask Claude to edit `../../../shipdesk/addresses.py` (the main checkout). Show that Claude Code blocks it.
7. Point out that the new worktree has no `.venv`. Run `pip install -r requirements.txt` in it before the tests, as a fresh checkout needs.

**Expected result:** Two worktrees under `.claude/worktrees/`, on branches `worktree-zip-check` and `worktree-bulk-discount`. The `.env` file appears in each. Each session changes only its own files. The main checkout stays clean. The edit aimed at the main checkout is refused.

> **Instructor note:** Everything above is in the verified facts, except the blocked edit at step 6, whose exact wording you should capture in rehearsal. Claude Code blocks edits, working directories, and git redirects that target the main checkout. It does not track files a shell command writes (`cp`, redirects), so those fall under normal permissions. Do not demonstrate that gap as a safety feature. Show the desktop worktree option (choose it when starting a session) as a screenshot or live, and mention side chat in one sentence at most: it is documented only as a desktop feature in a release write-up and is not confirmed on the official docs page.

> **Why this matters:** Two tickets finish in the time of one only if the sessions cannot collide. The worktree is what makes that safe.

---

## Demo 2: A Subagent in Its Own Worktree

**Learning objective:** Hand a side task to a subagent that works in an isolated worktree, so the current checkout is untouched. Time: about 10 minutes.

**Files:** `$FILES/shipdesk/.claude/agents/worktree-implementer.md`.

**Context:** A subagent has a fresh context window and returns only its final summary. The frontmatter field `isolation: worktree` runs it in its own worktree.

**Steps:**

1. Show the frontmatter of `worktree-implementer.md`: `name`, `description`, `tools`, `model`, `isolation: worktree`, `maxTurns`.
2. In `~/work/shipdesk`, start `claude` and ask: "Use the worktree-implementer agent to do Task C in TASKS.md."
3. While it runs, run `git status` and `git worktree list` in a second terminal.
4. When it returns, read the summary it sent back. Compare it with the files it changed.
5. Run `git status` in the main checkout.

**Expected result:** The main checkout stays clean while the subagent works. The subagent reports its changed files and a pytest summary line. It does not send back its full working history.

> **Instructor note:** `isolation: worktree` is a listed optional frontmatter field. What happens to the subagent's worktree and branch when it finishes (kept, removed, or prompted) was not recorded in the verified facts. Rehearse and say what you see. If the main session runs in `acceptEdits`, `bypassPermissions`, or auto mode, the subagent inherits that mode.

> **Why this matters:** A subagent is the cheap way to push a side task out of your context window and out of your working tree at once.

---

## Demo 3: Write a Subagent Role Contract

**Learning objective:** Write a role contract before running a team: roles, a handoff contract, a tool matrix, and a model per role. Time: about 15 minutes.

**Files:** `$FILES/shipdesk/docs/ROLE-CONTRACT.template.md`, `$FILES/shipdesk/TICKET-SD-142.md`, and `.claude/agents/planner.md`, `implementer.md`, `tester.md`.

**Context:** A team of roles fails in two ways: a role does more than its job, and a handoff drops what the next role needs. The contract is written first so both are visible before any tokens are spent.

**Steps:**

1. Open `TICKET-SD-142.md` and read its acceptance criteria and its limits.
2. Fill in the template's Roles table with the room, row by row:

   | Role | Tools | Model | Must not |
   |---|---|---|---|
   | planner | Read, Grep, Glob | sonnet | edit files, run commands |
   | implementer | Read, Grep, Glob, Edit, Write | sonnet | write tests, run git |
   | tester | Read, Grep, Glob, Edit, Write, Bash | haiku | edit source files |

3. Fill in the Handoffs table: the planner returns files to change, files not changing, signatures, and test cases. The implementer returns files changed, deviations, and edge cases noticed. The tester returns test files, the pytest summary, and failures.
4. Open the three agent files. Show that each tool list, model, and "return exactly this" section matches the contract.
5. Ask: "Which role could most damage the project if it exceeded its remit?" Discuss, then show why the tester has Bash but no source edits, and the implementer has Edit but no Bash.
6. Fill in the Stop rules: 4 files and 150 diff lines, from the ticket.

**Expected result:** A completed contract whose tool matrix gives each role the least it needs. The room can name the two failure modes and where in the contract each one is guarded.

> **Instructor note:** Frontmatter fields used (`name`, `description`, `tools`, `model`, `maxTurns`) are all in the verified facts. Subagent scope precedence is managed, `--agents` flag, project, user, plugin. The model-per-role choice is a cost judgment, not a product rule. The model aliases `sonnet`, `opus`, `haiku`, `fable`, a full ID, or `inherit` are accepted. Check the alias names on your class account.

> **Why this matters:** A contract you can read in a minute prevents the two failures that cost the most: scope creep and lost context.

---

## Demo 4: A Hook That Blocks a Dangerous Command

**Learning objective:** Block a risky command deterministically with a hook, using exit code 2 so the reason goes back to Claude. Time: about 12 minutes.

**Files:** `$FILES/hooks/block_dangerous.py`, `$FILES/hooks/check_python_after_edit.py`, `$FILES/hooks/settings.hooks.json`.

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

## Demo 5: A Hook That Runs Tests Before You Commit

**Learning objective:** Require passing tests before a commit, with a hook as the gate. Time: about 10 minutes.

**Files:** `$FILES/hooks/run_tests_before_commit.py` (already copied in Demo 4) and `$FILES/shipdesk/tests/`.

**Context:** The same exit code 2 mechanism, used as a quality gate. The script runs only when the Bash command contains `git commit`.

**Steps:**

1. Confirm the hook is in `.claude/settings.json` from Demo 4. It is the second command under the `Bash` matcher.
2. In `~/work/shipdesk`, break a test on purpose by changing `17.65` to `18.65` in `tests/test_pricing.py`.
3. In `claude`, ask: "Commit the current changes with the message 'wip'."
4. Read the block message and the test failure it carries.
5. Ask Claude to fix the test, then commit again.
6. Run `git log --oneline` to show the commit landed only after the tests passed.

**Expected result:** The first commit is blocked with "Commit blocked: tests are failing" and the pytest tail. Claude fixes the cause and the second commit succeeds.

> **Instructor note:** Same unverified details as Demo 4: the stdin JSON, and that the hook runs in the project directory. The script uses `.venv/bin/python` when present, so activate the environment or keep it at that path. This gate protects commits made through Claude's Bash tool, and not commits a person makes in their own terminal. Say so.

> **Why this matters:** A test requirement that depends on a person remembering is a hope. A hook makes it a rule.

---

## Demo 6: Review an Agent-Produced Pull Request

**Learning objective:** Review a pull request an agent wrote with a checklist, a diff-size limit, a required-tests gate, and a merge order. Time: about 15 minutes.

**Files:** `$FILES/agent-pr/sd-142-promo-codes.diff`, with `$FILES/shipdesk/TICKET-SD-142.md` as the ticket.

**Context:** The diff passes its tests. It has two planted problems that a green test run does not reveal. Review it against the ticket.

**Steps:**

1. Put the checklist on screen:
   - Does the diff stay inside the ticket's files and scope?
   - Is the diff within the size limit (4 files, 150 lines)?
   - Do tests cover each acceptance criterion?
   - Did any test change to match the code instead of the other way round?
   - Is merge order clear when other branches are open?
2. Show the size: `git apply --stat $FILES/agent-pr/sd-142-promo-codes.diff`.
3. Read the diff aloud. Ask the room what they would not approve.
4. Ask Claude Code to review it: "Review this diff against TICKET-SD-142.md. List every change the ticket does not ask for and every test that does not match an acceptance criterion."
5. Compare Claude's findings with the room's. Decide: merge, change, or reject.
6. Apply it to a scratch copy to show the tests are green anyway:

```
git apply $FILES/agent-pr/sd-142-promo-codes.diff && python -m pytest -q
git checkout -- . && git clean -fdq shipdesk/promos.py tests/test_promos.py
```

7. State the merge-order rule: smallest and most independent first, shared files last, tests rerun after each merge.

**Expected result:** The room finds two problems. First, an expired promo is accepted: the date check does nothing (`pass`), and the test was rewritten as `test_expired_code_still_applies` to match, breaking acceptance criterion 3. Second, `FREE_SHIPPING_THRESHOLD` changed from 75.00 to 25.00, which the ticket puts out of scope, and no test notices. All 19 tests pass.

> **Instructor note:** Claude's review is advisory. It does not approve or block a pull request. The human gate before the merge is what stops a bad change. The size limit and the tests-before-commit hook from Demo 5 are the automated gates. Step 6 uses `git clean` on two named paths only. Run it in the scratch copy.

> **Why this matters:** A green test run proves the code matches its tests. It does not prove the tests match the ticket.

---

## Demo 7: Agent Teams, Instructor Only

**Learning objective:** Tell Agent Teams, an experimental layer, from the stable worktrees-plus-subagents pattern. Time: about 12 minutes. Instructor only.

**Context:** In Agent Teams a lead coordinates teammates that each have their own context window, message each other, and share a task list. It is off by default. Do not run this on student machines.

**Steps:**

1. In a scratch terminal (not a student environment), enable the feature for one session:

```
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude
```

2. Ask the lead: "Create a team of three teammates to review shipdesk from three angles: pricing correctness, address handling, and test coverage. Each reports back to you."
3. Show the teammates and the shared task list as they appear.
4. Compare with the subagent pattern from Demo 3: a subagent reports only to its caller, while teammates message each other.
5. Close with the limits: no session resumption with in-process teammates, one team per session, no nested teams, not for same-file edits or sequential work, and a start size of 3 to 5 teammates.

**Expected result:** The room sees several coordinated sessions and a shared task list, and leaves able to say when worktrees plus subagents is the safer default.

> **Instructor note:** Everything about the feature comes from the verified facts: experimental, off by default, the environment variable, the limits, and significantly higher token cost. The on-screen layout, and whether your prompt produces a team, are not documented and need rehearsal. Have a screenshot ready if it does not start. Do not present Agent Teams for critical work.

> **Why this matters:** The experimental layer shows where the field is heading. The stable pattern is what a team can depend on today.

---

## Demo 8: A Routine Versus a Scheduled Task

**Learning objective:** Distinguish a Routine from a Cowork scheduled task and from a local desktop scheduled task. Time: about 10 minutes. Instructor only.

**Context:** All three run a prompt on a schedule. They differ in where they run, what they can reach, and whether a person is asked.

**Steps:**

1. Put the comparison on screen:

   | Question | Routine | Cowork scheduled task | Desktop local scheduled task |
   |---|---|---|---|
   | Where it runs | Anthropic cloud | Remote on a schedule, or locally if it needs local files | Your machine |
   | Laptop closed | Keeps running | Runs remotely unless it needs local files or apps | Runs on your machine, so rehearse |
   | Triggers | Schedule (one hour minimum), API, GitHub events | Hourly, daily, weekly, weekdays, manual | Confirm before class |
   | Permission picker | None, runs autonomously | Approval mode set on the task (unattended handling not stated) | Confirm before class |

2. Open claude.ai/code/routines and show the creation form. Do not save a routine with write-capable connectors.
3. In a session, show the `/schedule` command to create one.
4. Ask the room: "A Routine runs as you, with every included connector's tools. What would you scope before you saved it?"

**Expected result:** The room can state that a Routine runs unattended in the cloud, with no permission-mode picker, as the account's owner, and that its connectors' write tools are usable.

> **Instructor note:** Routines are a research preview, belong to an individual account, and Team and Enterprise Owners can disable them. The bearer-token API trigger exists; do not show a token. How an unattended Cowork scheduled task handles approvals is not stated in the documentation, so teach it as an open question and set the approval mode deliberately. The Desktop local column is verified only as running on the machine instead of in the cloud. Its triggers and approval behavior are unconfirmed.

> **Why this matters:** Choosing the wrong one means work that stops when the laptop closes, or work that acts with more reach than anyone reviewed.

---

## Demo 9: Test a Managed Policy

**Learning objective:** Author a managed policy and test what a project setting, a hook, and a subagent cannot override. Time: about 15 minutes.

**Files:** `$FILES/managed-policy/managed-settings.json`, `project-settings-attempt.json`, and `README.md`.

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
