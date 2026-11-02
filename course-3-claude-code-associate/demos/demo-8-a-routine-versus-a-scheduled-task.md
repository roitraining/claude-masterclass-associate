# Demo 8: A Routine Versus a Scheduled Task

**Course:** Claude Code Associate, Parallel Agents and Team Workflows (Claude MasterClass Associate, Course 3)
**Demo:** 8 of 9
**Time:** about 10 minutes

> Part of **[Claude Code Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

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

**Previous:** [Demo 7: Agent Teams, Instructor Only](demo-7-agent-teams-instructor-only.md) · **Next:** [Demo 9: Test a Managed Policy](demo-9-test-a-managed-policy.md)


*Demo 8 of 9*
