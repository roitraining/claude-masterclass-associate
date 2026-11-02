# Lab 1: Build and Test a Skill

**Course:** Claude.ai Associate
**Duration:** 45 minutes
**Format:** Instructor-led, in-class hands-on lab (200 level)

> Part of **[Claude.ai Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] A Claude.ai account you can install a Skill into
- [ ] A real recurring task from your own work, or use the default task provided
- [ ] `demo-files/lab1/default-task-brief.md`, `SKILL-template.md`, `service-requests-week-42.csv`, `trigger-test-inputs.md`, `trigger-test-log.csv`
- [ ] Your other Skills ready to be turned off, so only the one you build can fire

---

## Overview

Choose a real recurring task from your own work. If you do not have one, use the default task in `default-task-brief.md`.

**The description is the trigger, so most of your effort goes there.** Do not start from a blank page: use the template.

---

## Part 1: Define the Task

### Step 1: Pick Your Task and Write Its Output Layout

Write the output layout in three to six numbered parts.

**Expected result:** a numbered layout you can hand to someone else and have them produce the same shape of output.

### Step 2: Copy the Template into a Named Folder

Copy `SKILL-template.md` into a folder named for your Skill.

**Expected result:** a folder with a `SKILL.md` at its top.

---

## Part 2: Write the Skill

### Step 3: Write the Description

Cover what the Skill does, when to use it, and when **not** to.

**Acceptance criteria:** the description names the task and the words a user would actually say.

> **Key Insight:** the description is the trigger. A general description never fires; a narrow one fires on nothing. Specific beats long.

### Step 4: Fill In the Layout and the Rules

Include what to write when information is missing.

**Acceptance criteria:** the body states the layout, the order, and the rule for missing information.

---

## Part 3: Install and Prepare the Tests

### Step 5: Install the Skill and Turn Off the Others

**Expected result:** your Skill is installed and no other Skill can fire during testing.

> **Troubleshooting:** if the upload fails, check that the folder has a `SKILL.md` at its top, and ask your instructor for the upload steps rehearsed in class.

### Step 6: Prepare Five Test Inputs

Open `trigger-test-inputs.md`, or write five of your own: **three that should trigger** the Skill in different wording, and **two that should not**.

**Acceptance criteria:** five inputs, with the expected outcome of each written down before you run anything.

---

## Part 4: Run the Trigger Tests

### Step 7: Run Each Input in Its Own New Chat

Record triggered or not, and whether the output is correct, in `trigger-test-log.csv`.

**Acceptance criteria:** five logged runs, each in a fresh chat.

### Step 8: Compare Outputs with the Known Answers

Compare against the known answers in the inputs file, or against answers you worked out yourself.

**Expected result:** each run marked correct or incorrect, with the difference noted.

---

## Part 5: Revise and Re-Test

### Step 9: Revise to Fix Each Miss

Change the description or the body. **Change one thing at a time.**

**Acceptance criteria:** each miss has a specific change behind it, recorded in the log.

### Step 10: Rerun the Failures, Then All Five

Rerun only the inputs that failed, then rerun all five once.

**Acceptance criteria:** the Skill passes its own five trigger tests.

> **Note:** triggering is not fully deterministic. If results change between runs, rerun twice and decide by the majority.

---

## Part 6: Checkpoint

### Step 11: Verify Your Progress

- [ ] A numbered output layout of three to six parts
- [ ] A folder named for your Skill, with `SKILL.md` at its top
- [ ] A description stating what the Skill does, when to use it, and when not to
- [ ] A "do not use for" sentence present
- [ ] The body states the layout, the order, and what to write when information is missing
- [ ] The Skill is installed and your other Skills are off
- [ ] Five test inputs: three that should trigger, two that should not
- [ ] Expected outcomes written down before running
- [ ] All five run in separate fresh chats and logged
- [ ] Outputs compared against known or pre-stated answers
- [ ] Each miss traced to a single change
- [ ] The Skill passes its own five trigger tests
- [ ] A note of what changed between the first and last run

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| Skill never triggers | No fire on any input | The description is too general. Name the task and the words a user would say |
| Fires on the negatives | Triggers on inputs 4 and 5 | Add a "do not use for" sentence |
| Layout ignored | Output in the wrong shape | Shorten the body, number the parts, and state the order |
| Wrong count in output | A total does not match the data | Add "use only the data supplied, never estimate a count" |
| Upload fails | Skill will not install | Check that the folder has a `SKILL.md` at its top, and ask your instructor for the rehearsed upload steps |
| Results vary | Same input behaves differently | Triggering is not fully deterministic. Rerun twice and decide by the majority |

---

## What You Built

In 45 minutes, you:

- Built a Skill for a task you actually repeat, starting from a template rather than a blank page
- Learned that the description is the trigger, and tested it on wording a real user would use
- Tested what the Skill should **not** do, not only what it should
- Changed one thing at a time, so you know which change fixed which miss
- Left with a test log showing what moved between the first run and the last

---

## What's Next

Lab 2, Scoring a Portfolio of Skill Candidates, steps back from building one Skill to deciding which tasks deserve one at all.

---

## Facilitator Notes

A good result for the default task is a description that names the weekly service request brief, and a log where inputs 1 to 3 trigger and 4 to 5 do not.

On the default data, correct output shows 12 requests with 8 open; Fees 4, Cards 2, Wires 2, Online banking 2, Fraud 1, Other 1; open High-priority SR-4101, SR-4105 and SR-4106; open 3 days or more SR-4101, SR-4104 and SR-4105.

Students with their own tasks will not have an answer key, so make them state the expected output before they run it.

Skill upload steps and size limits are unconfirmed and need rehearsal on the class setup, so have a working path ready before the lab starts. Triggering is not fully deterministic, so a single miss is not a fail. Look for the reasoning in the log and not for a perfect score.

---

*Lab 1 Complete*
