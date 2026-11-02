# Lab 3: Batch + Plugin Capstone

**Course:** Claude Desktop Associate
**Duration:** 60 minutes
**Format:** Instructor-led, in-class hands-on lab (200 level)

> Part of **[Claude Desktop Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] Labs 1 and 2 completed
- [ ] `demo-files/vendor-quotes` (14 files)
- [ ] `demo-files/lab3-batch-design-sheet.md`, `lab3-timing-sheet.csv`, `lab3-plugin-spec.md`
- [ ] `demo-files/quote-comparison-skill.md`, `quote-subagent-roles.md`
- [ ] The plugin packaging method your facilitator rehearsed

> **Token cost.** This lab uses more of your usage limit than Labs 1 and 2. If you hit a limit message, reduce to the first 8 files and say so on the timing sheet.

---

## Overview

You compare 14 vendor quotes for the same branch security camera project. **One file is bad on purpose.**

You design the batch before you run it, time it against one at a time, and package the result so a team can reuse it.

---

## Part 1: Design the Batch Before You Run It

### Step 1: Copy the Folder and Treat It as Read Only

Copy `vendor-quotes` to your Documents folder.

**Expected result:** 14 files you will not modify.

### Step 2: Fill In the Batch Design Sheet

Open `lab3-batch-design-sheet.md` and fill in the partition, the return fields, the output location, the combine rule, and the rule for a failed file.

**Acceptance criteria:** a design written **before** any run, including an explicit rule for a file that cannot be read.

> **Key Insight:** the failed-file rule is the one that matters. Without it, a batch quietly returns 13 rows and looks complete.

---

## Part 2: Time One at a Time

### Step 3: Process the First Three Files Individually

Start the timing sheet. In a task on the folder, process only the first 3 files one at a time. Ask for the vendor, total, payment terms, and validity. Record the minutes.

**Expected result:** a per-file baseline time on the sheet.

---

## Part 3: Run the Batch

### Step 4: Run the Whole Folder with Your Design

In a new task, give Claude the folder and your design. Ask it to use sub-agents where it helps, return one row per file, and write results to a new folder named `batch-output`.

**Acceptance criteria:** results land in `batch-output`, not in `vendor-quotes`.

> **Common Pitfall:** if results are written into `vendor-quotes`, move them and restate the output location. The source folder is read only.

### Step 5: Record the Batch Time

**Acceptance criteria:** the real measured time on the sheet, whether or not it beat one at a time.

> **Note:** the parallel run may not be faster. Record the real time. Sub-agent use is not guaranteed and not always visible.

---

## Part 4: Verify the Results

### Step 6: Count the Rows Against the File Count

**Acceptance criteria:** the row count equals the number of files — 14, not 13.

> **Troubleshooting:** if Claude reports 13 rows, the failed file was dropped. Ask it to return a failed row for any unreadable file.

### Step 7: Find the File That Failed

**Acceptance criteria:** the file name and the reason Claude gave, both recorded.

### Step 8: Confirm No Total Was Guessed

**Acceptance criteria:** the failed file has no invented total.

> **Common Pitfall:** if Claude invented a total for the bad file, tighten the rule: never guess, report failed.

### Step 9: Spot-Check Three Totals Against Source Files

**Acceptance criteria:** three rows verified by hand against the source.

### Step 10: Rank the Valid Quotes

Ask Claude to rank the valid quotes by total and name the lowest.

**Expected result:** a ranking across the 13 valid quotes.

---

## Part 5: Package It as a Plugin

### Step 11: Fill In the Plugin Spec

Open `lab3-plugin-spec.md`. Fill in the name, description, who may run it, and the version and owner.

**Acceptance criteria:** a named owner, not a team.

### Step 12: Package the Skill and the Roles

Package the skill from `quote-comparison-skill.md` and the roles from `quote-subagent-roles.md` as a plugin, using the method your facilitator rehearsed.

> **Note:** if plugin creation is not available on your setup, the completed spec and skill files are the deliverable. Say so.

### Step 13: Say What a Connector Would Add

**Acceptance criteria:** one sentence on what a connector would add, and who would need to approve it.

---

## Part 6: Present

### Step 14: Present the Table and the Time Comparison

**Acceptance criteria:** a consolidated table of all 14 files with the failed file flagged, plus the time saved against one at a time.

---

## Part 7: Checkpoint

### Step 15: Verify Your Progress

- [ ] `vendor-quotes` was treated as read only
- [ ] A batch design was written before any run
- [ ] The design includes an explicit rule for a failed file
- [ ] A one-at-a-time baseline time recorded for 3 files
- [ ] The batch wrote results to `batch-output`
- [ ] The real batch time recorded, even if it was not faster
- [ ] The combined table has 14 rows, matching the file count
- [ ] The failed file is named, with the reason Claude gave
- [ ] No total was invented for the failed file
- [ ] Three totals verified by hand against source files
- [ ] The valid quotes ranked, with the lowest named
- [ ] A plugin spec with a named owner, version, description and who may run it
- [ ] The skill and roles packaged, or the spec accepted as the deliverable
- [ ] One sentence on what a connector would add and who approves it
- [ ] A consolidated table and time comparison presented

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| Row missing | Claude reports 13 rows | The failed file was dropped. Ask for a failed row for any unreadable file |
| Invented total | The bad file has a number | Tighten the rule: never guess, report failed |
| Source folder written to | Output inside `vendor-quotes` | Move it and restate the output location |
| Batch not faster | Parallel run takes as long or longer | Record the real time. Sub-agent use is not guaranteed and not always visible |
| Usage limit hit | A limit message appears | Reduce to the first 8 files and say so on the timing sheet |

---

## What You Built

In 60 minutes, you:

- Designed a batch before running it, including the failed-file rule that stops a silent 13-row result
- Measured parallel against one at a time and recorded the real number, even when it was not the flattering one
- Caught the planted bad file, confirmed no total was invented for it, and spot-checked three real totals by hand
- Packaged the workflow with a named owner so somebody else could run it

---

## What's Next

Lab 4, the Data Plugin Dashboard, is the take-home. It moves from 14 files to a dataset with nine planted data quality problems.

---

## Facilitator Notes

The answer key: 14 files, 13 valid, 1 failed (`quote-09.txt`, garbled and truncated, no total). Lowest valid total is Granite Peak Security at $5,924. The highest is Ironwood Technical at $7,412. The ranking from low to high is quotes 13, 2, 10, 6, 4, 1, 8, 12, 11, 7, 3, 14, 5.

Every valid quote totals 12 cameras, 2 recorders, and installation, so scope is the same. The quote totals are below $25,000, so the three-quote rule in the vendor risk policy is used here as a design check and not as a trigger.

How to create a plugin from a task is **not in our verified facts**, so rehearse the method and, if it is not available to students, accept the completed spec and skill files as the deliverable. Per-sub-agent usage is not stated.

A good result: all 14 files accounted for, the bad file flagged and not guessed, a measured time comparison (even if parallel was not faster), and a spec with a named owner.

---

*Lab 3 Complete*
