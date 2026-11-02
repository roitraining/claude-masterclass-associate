# Demo 7: Agent Teams, Instructor Only

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Demo:** 7 of 9
**Time:** about 12 minutes

> Part of **[Claude Code Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

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

**Previous:** [Demo 6: Review an Agent-Produced Pull Request](demo-6-review-an-agent-produced-pull-request.md) · **Next:** [Demo 8: A Routine Versus a Scheduled Task](demo-8-a-routine-versus-a-scheduled-task.md)


*Demo 7 of 9*
