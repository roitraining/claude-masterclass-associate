# Demo 5: Break It on Purpose: Unattended Failure

**Course:** Claude Desktop Associate: Persistent Workspaces and Unattended Work (Claude MasterClass Associate, Course 2)
**Demo:** 5 of 7
**Time:** about 15 minutes

> Part of **[Claude Desktop Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Cause four unattended-work failures on purpose, then design a scope, a kill switch, a log, and an alert. Time: about 15 minutes.

**Files:** [`demo-files/unattended-failure`](../demo-files/unattended-failure) (all files), plus the Demo 3 task and a copy of `daily-ops-feed`.

**Context:** The failure catalog is scope creep, a stale connector or input, a poisoned input, a silent failure, and a runaway cost. You break the Demo 3 task four ways and watch each result. Runaway cost is discussed, not run.

**Steps:**

1. Copy `daily-ops-feed` to `daily-ops-feed-test`. Point the task at the copy.
2. Add `poisoned-note.txt` to the copy. Run the task. Read the briefing. Did it follow the instruction in the note?
3. Add `stale-system-status.md`. Run again. Does the briefing report the old outage as current?
4. Add `unreadable-queue.csv`. Run again. Does the briefing say the file failed, or skip it silently?
5. Append `scope-creep-prompt-addition.md` to the task prompt. Run again. Check whether any file outside `briefings` changed.
6. Discuss runaway cost: a task set to hourly that starts a multi-step job each time.
7. Hand out `failure-design-worksheet.md`. Fill in the four controls as a class for the briefing task.

**Expected result:** The poisoned note and the stale status may each corrupt the briefing, depending on how the task reads them. The unreadable file may or may not be reported. The scope-creep sentence may cause files to be moved or archived. Record what happens, because the outcome differs between runs. The worksheet ends with a narrow scope, a kill switch (pause or delete the task), a log (the run history), and an alert (a human check that the briefing exists).

> **Instructor note:** The outcomes are not predictable and some failures may not reproduce. Rehearse and be ready to show a prepared result. Do not promise that a given failure always happens. Permanent deletes always ask, so do not demonstrate a delete. Per-run cost is not stated in our facts, and multi-step work uses more of the usage limit.

> **Why this matters:** When nobody is watching, the only protection is what you designed before the first run.

---

**Previous:** [Demo 4: Dispatch: Check and Steer From a Phone](demo-4-dispatch-check-and-steer-from-a-phone.md) · **Next:** [Demo 6: Partition a Batch Across Sub-Agents](demo-6-partition-a-batch-across-sub-agents.md)


*Demo 5 of 7*
