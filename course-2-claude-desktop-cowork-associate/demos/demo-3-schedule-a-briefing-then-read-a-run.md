# Demo 3: Schedule a Briefing, Then Read a Run

**Course:** Claude Desktop Associate: Persistent Workspaces and Unattended Work (Claude MasterClass Associate, Course 2)
**Demo:** 3 of 7
**Time:** about 15 minutes

> Part of **[Claude Desktop Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Create a scheduled task, state which tasks can run when the computer is asleep, and read a past run as its own session. Time: about 15 minutes.

**Files:** [`demo-files/scheduled-task`](../demo-files/scheduled-task): `daily-ops-feed`, `briefings`, and `briefing-task-prompt.md`.

**Context:** A scheduled task is not a one-time task with a timer. Each run is its own task session. Cadences are hourly, daily, weekly, weekdays, or manual. A task that needs local files or apps runs only locally, so it needs the computer on. A task that does not need local files can run remotely.

**Steps:**

1. Copy `scheduled-task` to the Documents folder. Give Claude access to it.
2. Open **Scheduled** in the left sidebar and select **New task**.
3. Choose **Set up manually**. Paste the prompt from `briefing-task-prompt.md`. Set the cadence to manual.
4. Ask the room: this task reads a local folder. Can it run with the computer asleep? Take answers, then state the rule.
5. Select **Run now** from the Scheduled page. Watch the run.
6. Open the finished run. Point out that it is its own session. Open `briefings/briefing-2026-10-19.md`.
7. Check the briefing against the feed. The Member Care section should list MC-4401 only (17 days old).
8. Show the controls: pause, resume, edit, and delete.

**Expected result:** A briefing file appears in `briefings` with five sections and a Sources line. Only MC-4401 is over 14 days. The run appears as its own session.

> **Instructor note:** How an unattended run handles approvals is **not documented**. In this demo you watch the run, so you will see prompts that an unattended run might not show. Say so plainly and tell the class that Lab 2 tests it. Permanent deletes always ask. Rehearse the exact menu names, because the labels for creating and running a task are taken from Anthropic's help article and have not been tested on the class VM.

> **Why this matters:** A task that runs without you still needs a scope, a review plan, and an owner.

---

**Previous:** [Demo 2: Design the Knowledge Folder](demo-2-design-the-knowledge-folder.md) · **Next:** [Demo 4: Dispatch: Check and Steer From a Phone](demo-4-dispatch-check-and-steer-from-a-phone.md)


*Demo 3 of 7*
