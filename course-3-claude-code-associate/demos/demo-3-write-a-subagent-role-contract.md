# Demo 3: Write a Subagent Role Contract

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Demo:** 3 of 9
**Time:** about 15 minutes

> Part of **[Claude Code Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Write a role contract before running a team: roles, a handoff contract, a tool matrix, and a model per role. Time: about 15 minutes.

**Files:** [`$FILES/shipdesk/docs/ROLE-CONTRACT.template.md`](../demo-files/shipdesk/docs/ROLE-CONTRACT.template.md), [`$FILES/shipdesk/TICKET-SD-142.md`](../demo-files/shipdesk/TICKET-SD-142.md), and `.claude/agents/planner.md`, `implementer.md`, `tester.md`.

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

**Previous:** [Demo 2: A Subagent in Its Own Worktree](demo-2-a-subagent-in-its-own-worktree.md) · **Next:** [Demo 4: A Hook That Blocks a Dangerous Command](demo-4-a-hook-that-blocks-a-dangerous-command.md)


*Demo 3 of 9*
