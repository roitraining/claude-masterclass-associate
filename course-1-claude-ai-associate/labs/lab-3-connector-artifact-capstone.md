# Lab 3: Connector + Artifact Capstone

**Course:** Claude.ai Associate
**Duration:** 60 minutes
**Format:** Instructor-led, in-class hands-on lab (200 level)

> Part of **[Claude.ai Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] Labs 1 and 2 completed — you need your Lab 1 Skill
- [ ] A Claude.ai account on a plan that supports artifacts
- [ ] `demo-files/lab3/connector-spec-template.md`, `service-requests-4weeks.csv`, `artifact-prompt.md`, `capstone-test-set.csv`, `readout-template.md`
- [ ] `demo-files/demo3/tool-catalog.csv`
- [ ] A live connector **only** if IT pre-approved one before class. Otherwise use the sample file

---

## Overview

You design the connector **on paper** and use sample data as a stand-in for its read tool. The artifact is your small internal tool.

Students connect a live connector only if IT pre-approved one before class. Otherwise use the sample file throughout.

---

## Part 1: Design the Connector

### Step 1: Name the Connector and State Its Purpose

Open `connector-spec-template.md`. Write the purpose in one sentence.

**Expected result:** a named connector with a one-sentence purpose.

### Step 2: Choose Four to Six Tools from the Catalog

Mark each read or write, and write a one-sentence description for each.

**Acceptance criteria:** four to six tools, each marked read or write, each with a description.

### Step 3: List at Least Two Tools You Refused to Expose

**Acceptance criteria:** at least two refusals, each with a reason.

> **Key Insight:** what you leave out is part of the design. A connector that exposes everything available has not been designed.

### Step 4: Fill In Authentication, Reach and the Approval Path

**Acceptance criteria:** an owner named for every step of the approval path.

---

## Part 2: Run Your Skill on the Sample Data

### Step 5: Open the Stand-In Tool Output

Open `service-requests-4weeks.csv`. This stands in for the output of your search tool.

**Expected result:** 40 rows of sample request data.

### Step 6: Run Your Lab 1 Skill on the File

Use the default brief task if you built a different Skill. Save the output.

**Expected result:** a saved Skill output you can score later.

---

## Part 3: Build the Artifact

### Step 7: Adapt the Artifact Prompt

Open `artifact-prompt.md`, adapt it to your Skill, and paste it into a new chat.

**Expected result:** an artifact renders.

> **Troubleshooting:** if the artifact does not call Claude, ask Claude to rebuild it so the button sends the pasted text to Claude, and tell your instructor.

### Step 8: Paste the Rows and Run It

When the artifact renders, paste the file rows into it and press Brief.

**Acceptance criteria:** the artifact produces a brief from the pasted data.

> **Troubleshooting:** if the CSV is too long to paste, paste the first 40 rows only — that is the whole file.

---

## Part 4: Measure Against the Test Set

### Step 9: Ask the Eight Test Questions

Ask the eight questions in `capstone-test-set.csv` against the file, one at a time, in a new chat with the file attached. Score each 1 or 0.

**Acceptance criteria:** eight scored answers.

### Step 10: Score the Artifact Separately

Check the artifact output against the same known answers. Record its score separately.

**Acceptance criteria:** two scores — chat and artifact — not one combined number.

> **Common Pitfall:** if the artifact returns invented counts, add "use only the pasted data, never estimate" to the prompt.

---

## Part 5: Fix and Rerun

### Step 11: Fix the Largest Error and Rerun the Misses

Fix it in the Skill or in the artifact prompt, then rerun only the questions you missed.

**Acceptance criteria:** the largest error addressed, with the rerun recorded.

> **Note:** optional if time is short. Skip to Part 6 and say in the readout what you would have fixed.

---

## Part 6: Prepare the Readout

### Step 12: Build Your One-Minute Readout

Use `readout-template.md`.

**Acceptance criteria:** the readout includes your connector spec decisions and the pass rate from the test set.

---

## Part 7: Checkpoint

### Step 13: Verify Your Progress

- [ ] The connector is named with a one-sentence purpose
- [ ] Four to six tools chosen, each marked read or write with a description
- [ ] At least two refused tools listed, each with a reason
- [ ] No tool that returns tax IDs or full records is exposed
- [ ] Authentication, reach and approval path filled in, with an owner per step
- [ ] Your Lab 1 Skill was run on the sample file and the output saved
- [ ] An artifact renders and actually calls Claude
- [ ] The artifact produced a brief from pasted rows
- [ ] All eight test questions scored 1 or 0 in chat
- [ ] The artifact scored separately against the same answers
- [ ] The largest error fixed and the missed questions rerun, or noted as skipped for time
- [ ] A one-minute readout naming connector decisions and the pass rate

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| Artifact is static | The button does nothing | It does not call Claude. Ask Claude to rebuild it so the button sends the pasted text to Claude, and tell the instructor |
| Invented counts | The artifact reports totals not in the data | Add "use only the pasted data, never estimate" to the prompt |
| CSV will not paste | Input too long | Paste the first 40 rows only. That is the whole file |
| Spec exposes sensitive data | A tool returns tax IDs | Remove it and say why in the Left out section |
| Out of time | Readout at risk | Skip the optional fix in Step 11 and say what you would have fixed |

---

## What You Built

In 60 minutes, you:

- Designed a connector on paper, including the tools you refused to expose and why
- Ran your own Skill against a four-week dataset instead of a toy example
- Built an artifact that calls Claude, and caught it inventing counts if it did
- Scored the chat path and the artifact path separately against the same eight known answers
- Gave a readout with a real pass rate rather than an impression

---

## What's Next

Lab 4, Research Deep Dive, is the take-home. It moves from a dataset you were given to sources you have to judge yourself.

---

## Facilitator Notes

The known answers for `capstone-test-set.csv` are: 40 requests; 12 in Fees; 11 open; 4 open more than 5 days; Eastgate has the most (17); 5 open High priority; SR-4003 open longest (23 days); 5 Fees requests from Eastgate.

A good connector spec exposes search, summary, fee schedule and hours as reads, defers writes, and refuses full records, free SQL, and money movement or external email.

A good readout names one error category and one next step before a pilot.

Billing for artifact calls is unconfirmed in the verified facts, so do not claim whose usage is charged. Any live connector use must be a sandbox or pre-approved one.

---

*Lab 3 Complete*
