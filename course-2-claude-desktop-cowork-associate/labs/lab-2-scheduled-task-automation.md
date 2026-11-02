# Lab 2: Scheduled Task Automation

> Part of **[Claude Desktop Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

**Learning objective:** Schedule a recurring task, set its approval mode on purpose, run it unattended, and record what happens. Time: 40 minutes.

**Files:** `demo-files/scheduled-task` (all files), including `briefing-task-prompt.md`, `run-log-template.csv`, and `review-plan-template.md`.

**Context:** How an unattended run handles approvals is not documented. This lab is a small experiment. You choose the approval mode deliberately, step away, and record what the run did. Your result is data, and another student may get a different one. A task that needs local files or apps runs only locally, so the computer must be on for this task.

**Steps:**

1. Copy `scheduled-task` to your Documents folder. Give Claude access to it.
2. Open `run-log-template.csv`. Write your chosen approval mode in the `approval_mode_set` column of row 1, and one sentence on why you chose it.
3. Open **Scheduled** in the left sidebar and select **New task**. Choose **Set up manually**.
4. Paste the prompt from `briefing-task-prompt.md`.
5. Set the cadence to run in about 10 minutes. Set the approval mode you chose.
6. Note the scheduled time in the log. Step away from the computer and do not touch it until the time has passed. Keep the computer awake.
7. When the run finishes, open it from the Scheduled page. Confirm it is its own session.
8. Record in the log: whether it ran without you, whether it asked for approval, whether it stalled waiting, and whether the briefing file was created.
9. Open the briefing. Check it against the feed: only MC-4401 is over 14 days, and the briefing ends with a Sources line.
10. Copy the files from `feed-days/2026-10-20` into `daily-ops-feed`. Select **Run now** and compare the new briefing with the first.
11. Complete `review-plan-template.md`: scope, kill switch, how a silent failure would be noticed, and a review date.
12. Optional, if you have Dispatch access: check the task result from your phone. Everyone else may check the briefing from the mobile app only if the task is a cloud task.
13. Pause the task when you finish.

**Checkpoint:** Each student leaves with one working scheduled task, a completed run log row, a review plan, and an optional Dispatch check.

**Common problems:**

- The run never starts. A local task may need the computer awake and Claude Desktop open. Record this as an observation.
- The run stops and waits for approval. That is a valid result. Record it in the `stalled_waiting` column, then approve and note how long it waited.
- The briefing is not in `briefings`. Check the task's folder access and the path in the prompt.
- The briefing skips a file silently. Record it. This is the silent failure from Demo 5.
- Skip all approvals is chosen for convenience. Ask what limits the damage if the feed holds a poisoned note.

**Facilitator note:** The expected behavior of an unattended run under each approval mode is **not documented**, so there is no single right result. Collect the room's log rows on a board by approval mode and compare. What a good result looks like: the student chose a mode with a stated reason, recorded all columns honestly, and wrote a kill switch and a silent-failure check in the review plan. The first briefing should list MC-4401 only as over 14 days. Rehearse the Scheduled page labels on the class VM beforehand. Whether a local task runs at all with the computer asleep is **unconfirmed** beyond Anthropic's statement that local-file tasks run only locally, so tell students to record what they observe and not to assume.
