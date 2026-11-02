# Lab 1: Persistent Workspace

**Course:** Claude Desktop Associate
**Duration:** 45 minutes
**Format:** Instructor-led, in-class hands-on lab (200 level)

> Part of **[Claude Desktop Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] Claude Desktop installed, on a paid plan
- [ ] Local administrator rights, or an IT policy that permits extension installs
- [ ] The facilitator-prepared `.mcpb` file
- [ ] `demo-files/knowledge-folder`, `demo-files/keep-out-of-the-workspace`
- [ ] `demo-files/lab1-test-questions.md`, `demo-files/lab1-workspace-boundary-worksheet.md`

> **Note:** machine-level policy overrides in-app controls. If the install is blocked, that is a finding worth recording, not a failure on your part.

---

## Overview

In Essentials you gave Claude a folder for a single session. Here you install an extension that keeps a folder available in **every** conversation.

A wider and longer exposure needs a boundary and a test. That is what this lab builds.

---

## Part 1: Set Up the Folders and Install the Extension

### Step 1: Copy Both Folders as Siblings

Copy `knowledge-folder` and `keep-out-of-the-workspace` to your Documents folder as siblings. **Do not put one inside the other.**

**Expected result:** two folders at the same level in Documents.

### Step 2: Open Extension Developer

In Claude Desktop, go to **Settings**, then **Advanced settings**, then **Extension Developer**.

> **Troubleshooting:** if the install option is missing, check the Desktop version and that the account is on a paid plan.

### Step 3: Install the Extension

Select **Install Extension** and choose the `.mcpb` file your facilitator provides.

**Expected result:** the extension installs and appears enabled.

### Step 4: Read the Install Prompt and Record Its Reach

**Acceptance criteria:** you have written down what the prompt says the extension can reach.

---

## Part 2: Ground Claude in the Knowledge Folder

### Step 5: Confirm Claude Can See the Folder

Open a new conversation and ask: "List the files in the knowledge folder."

**Expected result:** the files are listed.

> **Troubleshooting:** if Claude lists no files, confirm the extension is enabled in this conversation and that the folder path in the extension is correct.

---

## Part 3: Test the Answers

### Step 6: Ask Questions 1 and 2, and Check the Cited File

Open `lab1-test-questions.md`.

**Acceptance criteria:** both answers checked against the cited file, not just read.

> **Common Pitfall:** if an answer has no file name, the citation is missing. Remind yourself the map file asks for citations, then record the miss.

### Step 7: Ask Questions 3 to 6

Record each answer in a copy of the table.

**Expected result:** four recorded answers, including at least one "not covered".

### Step 8: Ask Question 7, About the Salary Band

**Acceptance criteria:** you have recorded whether the keep-out folder was reachable.

> **Key Insight:** if Claude answers question 7, the extension reaches more than the knowledge folder. Record it as a finding, then narrow the folder. The folder boundary, not the instruction file, is the control.

### Step 9: Ask Question 8 and Check the Scope

**Acceptance criteria:** Claude stays inside file 01.

---

## Part 4: Define the Boundary

### Step 10: Complete the Boundary Worksheet

**Acceptance criteria:** at least five categories listed that must stay out of a persistent workspace.

### Step 11: Write a Review Plan

**Acceptance criteria:** the plan names who reviews the folder and how a stale file is found.

---

## Part 5: Checkpoint

### Step 12: Verify Your Progress

- [ ] Both folders copied to Documents as siblings, neither inside the other
- [ ] The extension is installed and enabled
- [ ] What the install prompt said the extension can reach is written down
- [ ] Claude lists the files in the knowledge folder
- [ ] Questions 1 and 2 answered, each checked against the cited file
- [ ] Questions 3 to 6 recorded in the table
- [ ] Question 7 recorded, with whether the keep-out folder was reachable
- [ ] Question 8 stayed inside file 01
- [ ] Any missing citation recorded as a miss
- [ ] At least five must-stay-out categories on the worksheet
- [ ] A review plan naming who reviews the folder and how a stale file is found

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| No install option | Extension Developer missing | Check the Desktop version and that the account is on a paid plan |
| Install blocked | The install refuses | Local administrator rights or an IT policy may be preventing it. Machine-level policy overrides in-app controls |
| No files listed | Claude sees nothing | Confirm the extension is enabled in this conversation and that the folder path in the extension is correct |
| Keep-out folder reachable | Claude answers question 7 | The extension reaches more than the knowledge folder. Record it as a finding, then narrow the folder |
| Answers lack citations | No file name in the answer | The map file asks for citations. Record the miss rather than ignoring it |

---

## What You Built

In 45 minutes, you:

- Installed a local extension that keeps a folder available in every conversation, and read what the install prompt actually granted
- Tested the workspace for citations, for a question it should refuse, and for a file it should not reach
- Found out whether the boundary was the folder or just an instruction, by asking for something out of scope
- Wrote down five categories that must never enter a persistent workspace, and a plan for catching a stale file

---

## What's Next

Lab 2, Scheduled Task Automation, removes you from the loop. The same workspace runs without you watching it.

---

## Facilitator Notes

Prepare the `.mcpb` in advance from the Anthropic MCPB documentation (a zip holding a local MCP server and `manifest.json`) and rehearse it on the class VM. Whether Claude Desktop and custom extension install work on the class VM is **unconfirmed**. This guide deliberately provides no extension code because the manifest fields are not in our verified facts.

A good result: question 1 says $25,000 (file 01); question 2 says 1:00 p.m. Eastern; question 3 names the credit committee and flags that a written exception is needed because no level sits above it; question 4 is "not covered"; question 5 is declined or labeled superseded; question 6 is closed with no wires; question 7 is "not covered".

Do not penalize a student whose extension reaches the keep-out folder. The lesson is that the folder boundary, not the instruction file, is the control.

---

*Lab 1 Complete*
