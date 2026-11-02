# Lab 2: Scheduled Task Automation

**Course:** Claude Desktop Associate
**Duration:** 40 minutes
**Format:** Instructor-led, in-class hands-on lab (200 level). A small experiment — your result is data

> Part of **[Claude Desktop Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] Lab 1 completed
- [ ] Claude Desktop installed and able to stay open and awake for about 10 minutes
- [ ] `demo-files/scheduled-task` (all files), including `briefing-task-prompt.md`, `run-log-template.csv`, `review-plan-template.md`
- [ ] Dispatch access for the optional Step 12. Not required

> **Note:** a task that needs local files or apps runs only locally, so your computer must be on and awake for this task.

---

## Overview

**How an unattended run handles approvals is not documented.** This lab is a small experiment.

You choose the approval mode deliberately, step away, and record what the run did. Your result is data, and another student may get a different one. There is no single right answer here.

---

## Part 1: Set Up and Choose Your Approval Mode

### Step 1: Copy the Folder and Grant Access

Copy `scheduled-task` to your Documents folder. Give Claude access to it.

**Expected result:** Claude can read the folder.

### Step 2: Commit to an Approval Mode in Writing

Open `run-log-template.csv`. Write your chosen approval mode in the `approval_mode_set` column of row 1, and one sentence on why you chose it.

**Acceptance criteria:** a mode chosen **before** the run, with a stated reason.

> **Common Pitfall:** if you are tempted to skip all approvals for convenience, ask what limits the damage if the feed holds a poisoned note.

---

## Part 2: Create the Scheduled Task

### Step 3: Open Scheduled and Start a New Task

Open **Scheduled** in the left sidebar, select **New task**, and choose **Set up manually**.

### Step 4: Paste the Task Prompt

Paste the prompt from `briefing-task-prompt.md`.

### Step 5: Set the Cadence and the Approval Mode

Set the cadence to run in about 10 minutes. Set the approval mode you chose in Step 2.

**Expected result:** a task scheduled about 10 minutes out.

---

## Part 3: Run It Unattended

### Step 6: Step Away and Leave It Alone

Note the scheduled time in the log. Step away from the computer and do not touch it until the time has passed. Keep the computer awake.

**Acceptance criteria:** the run happened without your intervention, or you recorded that it did not.

### Step 7: Confirm the Run Is Its Own Session

When the run finishes, open it from the Scheduled page.

**Expected result:** the run is a separate session, not a continuation of your chat.

### Step 8: Record What Actually Happened

Record in the log: whether it ran without you, whether it asked for approval, whether it stalled waiting, and whether the briefing file was created.

**Acceptance criteria:** every column filled honestly, including a stall if one occurred.

> **Note:** a run that stops and waits for approval is a **valid result**. Record it in `stalled_waiting`, then approve it and note how long it waited.

---

## Part 4: Check the Output and Re-Run

### Step 9: Check the Briefing Against the Feed

Open the briefing.

**Acceptance criteria:** only MC-4401 is over 14 days, and the briefing ends with a Sources line.

> **Common Pitfall:** if the briefing skips a file silently, record it. That is the silent failure from Demo 5, and it is the whole point of checking.

### Step 10: Add New Feed Files and Run Again

Copy the files from `feed-days/2026-10-20` into `daily-ops-feed`. Select **Run now** and compare the new briefing with the first.

**Expected result:** a second briefing you can diff against the first.

---

## Part 5: Write the Review Plan

### Step 11: Complete the Review Plan

**Acceptance criteria:** scope, a kill switch, how a silent failure would be noticed, and a review date.

---

## Part 6: Optional Dispatch Check, Then Pause

### Step 12: Check the Result from Your Phone (optional)

If you have Dispatch access, check the task result from your phone. Everyone else may check the briefing from the mobile app only if the task is a cloud task.

### Step 13: Pause the Task

**Acceptance criteria:** the task is paused before you leave.

---

## Part 7: Checkpoint

### Step 14: Verify Your Progress

- [ ] An approval mode was chosen before the run, with a written reason
- [ ] One working scheduled task created manually
- [ ] The prompt came from `briefing-task-prompt.md`
- [ ] You stepped away and did not touch the computer during the run
- [ ] The computer stayed awake
- [ ] The run was confirmed to be its own session
- [ ] Every log column filled: ran unattended, asked for approval, stalled waiting, briefing created
- [ ] The briefing lists only MC-4401 as over 14 days
- [ ] The briefing ends with a Sources line
- [ ] Any silently skipped file recorded
- [ ] New feed files added and a second briefing compared with the first
- [ ] A review plan with scope, a kill switch, a silent-failure check and a review date
- [ ] The task is paused

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| Run never starts | Nothing happens at the scheduled time | A local task may need the computer awake and Claude Desktop open. Record this as an observation |
| Run waits for approval | The task stalls | A valid result. Record it in `stalled_waiting`, then approve and note how long it waited |
| Briefing missing | Nothing in `briefings` | Check the folder access of the task and the path in the prompt |
| File skipped silently | The briefing omits a feed file without saying so | Record it. This is the silent failure the lab is looking for |
| Tempted to skip approvals | Chose skip-all for convenience | Ask what limits the damage if the feed holds a poisoned note, then record your reasoning either way |

---

## What You Built

In 40 minutes, you:

- Chose an approval mode on purpose and wrote down why, before you knew what would happen
- Ran a task with nobody watching and recorded the real behavior, including a stall if you got one
- Checked the output against the feed rather than trusting it, and looked specifically for a silently skipped file
- Wrote a review plan with a kill switch and a way to notice a failure that makes no noise
- Produced a data point the room can compare, in an area the documentation does not cover

---

## What's Next

Lab 3, the Batch and Plugin Capstone, scales this from one scheduled task to batch work packaged for other people.

---

## Facilitator Notes

The expected behavior of an unattended run under each approval mode is **not documented**, so there is no single right result. Collect the log rows of the room on a board by approval mode and compare.

What a good result looks like: the student chose a mode with a stated reason, recorded all columns honestly, and wrote a kill switch and a silent-failure check in the review plan. The first briefing should list MC-4401 only as over 14 days.

Rehearse the Scheduled page labels on the class VM beforehand. Whether a local task runs at all with the computer asleep is **unconfirmed** beyond the Anthropic statement that local-file tasks run only locally, so tell students to record what they observe and not to assume.

---

*Lab 2 Complete*
