# Claude Desktop Associate: Demos

**Course:** Claude Desktop Associate: Persistent Workspaces and Unattended Work (Claude MasterClass Associate, Course 2)
**Contents:** 7 demos. Each takes 15 minutes or less and has a learning objective. The numbers match the Today's Demos slide.

---

## About this guide

All demos are instructor-led. Students watch and may follow along where a step says so. Each demo has the same layout: a learning objective, a time, a Files line when files are used, a short context paragraph, numbered steps, an Expected result, an Instructor note, and a Why this matters note.

The files are in the `demo-files` folder next to this guide:

- `knowledge-folder`, `keep-out-of-the-workspace`, and `lab1-test-questions.md` for Demos 1 and 2.
- `scheduled-task` for Demo 3.
- `dispatch` for Demo 4.
- `unattended-failure` for Demo 5.
- `batch-demo` for Demo 6.
- `data-plugin-dashboard` for Demo 7.

Scenario: Harbor Ridge Credit Union, a fictional credit union. Every person, company, and figure is fictional. Claude can word answers differently each time, so check results against the Expected result and not against exact text.

**Swap the scenario.** For healthcare, rename the credit union to a fictional clinic network and replace the knowledge files with a visit-scheduling procedure, a referral approval matrix, and a patient-complaint procedure. For government, use a fictional county office with a permit-processing procedure, a fee schedule, and a records-retention policy. Keep the same planted traps: an archived file, a question with no answer, and a keep-out file with staff pay or personal records.

> **Accounts and connectors.** Anything that touches a connector or an account is instructor-only and uses an ROI sandbox account. Students work with sample files only.

> **Essentials baseline.** Students already know how to hand Claude a task on a folder, the three approval modes, cloud versus local, and how to prove a folder restriction. Do not re-teach them. These demos start from there.
>
> Say "task", not "Cowork". Cowork and chat merged into one Claude on September 16, 2026, and no replacement product name was introduced. Students may still meet the old word in support article titles, in the Enterprise admin toggle "Chat and Cowork unified (beta)", and in accounts that have not migrated yet.

---

## Demo 1: Install a Custom Extension

**Learning objective:** Install a custom local extension that connects Claude to a persistent folder, and say how it differs from a per-session folder card and from a directory extension. Time: about 12 minutes.

**Files:** `demo-files/knowledge-folder` and a prepared `.mcpb` file (see the Instructor note).

**Context:** In Essentials, students gave Claude a folder for a single session. A custom local extension is installed once, stays installed, and runs a local MCP server on the machine. An `.mcpb` file is a zip that holds that local MCP server and a `manifest.json`. A directory extension is one published for general install. A custom extension is one you or your team built.

**Steps:**

1. Show the zip structure of the prepared `.mcpb` on screen. Point out `manifest.json` and the server file.
2. Open Claude Desktop. Go to **Settings**, then **Advanced settings**, then **Extension Developer**.
3. Select **Install Extension** and choose the prepared `.mcpb` file.
4. Read the install prompt aloud. Ask the room: what will this extension be able to reach?
5. Complete the install. Start a new conversation and ask: "List the files in the knowledge folder."
6. Ask: "What is the daily limit for a domestic wire in online banking? Name the file you used."
7. Open a second new conversation and ask the same question to show the extension persists without re-attaching a folder.

**Expected result:** The extension installs, Claude lists the **nine** files in the knowledge folder, and answers $25,000 citing `01-wire-transfer-procedure.md`. The second conversation answers without any folder being attached.

> **Eight or nine?** The folder holds nine files. The folder map `00-README-folder-map.md` tabulates the other **eight** and does not list itself, so "eight" is the count in the map and "nine" is the count on disk. Verified against the shipped folder and the extension on October 22, 2026.

> **Instructor note:** The facts we can confirm are the install path above and the `.mcpb` structure. The manifest fields, the server code, and the exact install prompt wording are not in our verified facts, so prepare the `.mcpb` in advance from Anthropic's MCPB documentation and rehearse it on the class VM. Whether Claude Desktop runs on the class VM operating system and installs custom extensions there is **unconfirmed**. If it does not, run this demo from the instructor's own machine. Team and Enterprise Owners can upload custom extensions for one-click team install, and a machine-level enterprise policy overrides in-app controls. Code signing and managed deployment for extensions are **unconfirmed**. Do not teach them as features.

> **Why this matters:** A persistent extension keeps its reach after the conversation ends. Install is a decision, not a convenience.

---

## Demo 2: Design the Knowledge Folder

**Learning objective:** Design a knowledge folder for retrieval, with a map file, an archive, and a boundary around what stays out. Time: about 12 minutes.

**Files:** `demo-files/knowledge-folder`, `demo-files/keep-out-of-the-workspace`, `demo-files/lab1-test-questions.md`.

**Context:** The folder from Demo 1 works because it was designed. It has a map file with owners and review dates, files named by topic, a clearly labeled archive, and nothing that should not be there.

**Steps:**

1. Open `00-README-folder-map.md`. Point out the owner and last reviewed columns and the three answer rules.
2. Open `99-archive-old-wire-limits-2024.md`. Ask: why keep this at all? Why name it archive?
3. In a conversation with the extension on, ask test question 5: "What was the old international wire limit?"
4. Ask test question 4: "Does the credit union waive overdraft fees for business accounts?"
5. Ask test question 3 (the $120,000 unsecured loan for a member with a credit score of 600). Read the answer against the matrix.
6. Show the `keep-out-of-the-workspace` folder. Ask the room what each file stands in for and why it must never go in a persistent folder.
7. Ask test question 7 about the branch manager salary band. Record whether the answer is "not covered".

**Expected result:** Question 5 is declined or labeled superseded. Question 4 is "not covered in the knowledge folder". Question 3 names the credit committee and flags that no higher level exists, so a written exception is needed. Question 7 is "not covered" if the keep-out folder is outside the extension's folder.

> **Instructor note:** Claude may still answer a question the rules say to decline, because the map file's rules are instructions, not enforcement. Treat any such answer as a finding about design, and show that only the folder boundary is enforcement. Whether the extension can reach a sibling folder depends on how the `.mcpb` server was written. Check this on the prepared extension before class.

> **Why this matters:** Retrieval quality is a design property of the folder. The exposure of a persistent workspace is whatever you put in it.

---

## Demo 3: Schedule a Briefing, Then Read a Run

**Learning objective:** Create a scheduled task, state which tasks can run when the computer is asleep, and read a past run as its own session. Time: about 15 minutes.

**Files:** `demo-files/scheduled-task`: `daily-ops-feed`, `briefings`, and `briefing-task-prompt.md`.

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

## Demo 4: Dispatch: Check and Steer From a Phone

**Learning objective:** Describe Dispatch, where it can and cannot be used today, and what a phone instruction can trigger on a desktop. Time: about 15 minutes.

**Files:** `demo-files/dispatch`: `dispatch-sandbox` and `phone-instructions.md`.

**Context:** Dispatch is one conversation across a phone and a desktop. The desktop does the work with local files, connectors, and plugins. **Dispatch is a limited beta on some Pro and Max plans. It is not available to new users.** Expect that most students cannot use it. The instructor demonstrates on an account that has it, and students who can access Dispatch may follow along. Everyone else follows the fallback path.

**Steps (instructor demonstration):**

1. State the access limits above. Ask who has Dispatch. Note the count.
2. On the instructor desktop, share only the `dispatch-sandbox` folder. Keep the computer awake and Claude Desktop open.
3. From the phone, send instruction 1 from `phone-instructions.md`. Read the result on the phone.
4. Send instruction 2. Then instruction 3, which edits a file. Open the file on the desktop to confirm.
5. Before sending instruction 4, ask the room: what will the desktop do? Send it and record what you were asked before the delete.
6. Close the demo: a phone instruction acted on files on a desktop. Ask who else could type that instruction if the phone was lost.

**Fallback path (no Dispatch):**

1. Start a cloud task from the desktop with `q3-exceptions-summary.csv` attached and ask for a two-sentence summary.
2. Check the task from the Claude mobile app or from claude.ai in a browser.
3. Ask: what could this phone check NOT do that Dispatch could? Answer: it cannot reach local files, connectors, or plugins on the desktop, and it cannot start work there.

**Expected result:** Instructions 1 and 2 are read only. Instruction 3 changes the file. Instruction 4 asks for approval or confirmation before the delete, and the file is only removed if approved. In the fallback, the cloud task completes and its result is visible from the phone.

> **Instructor note:** Everything about what Dispatch reaches comes from Anthropic's help article. The setup path is Dispatch on the left side panel, then Get started, then the file access and keep-awake toggles, then Finish setup. The exact approval behavior for a phone-sent delete is **unconfirmed**. Treat it as an observation, not a promise. Computer use is not available on Linux. Rehearse on the real account the day before.

> **Why this matters:** Remote steering extends your desktop's reach to anything that can send it an instruction. Treat the phone as a credential.

---

## Demo 5: Break It on Purpose: Unattended Failure

**Learning objective:** Cause four unattended-work failures on purpose, then design a scope, a kill switch, a log, and an alert. Time: about 15 minutes.

**Files:** `demo-files/unattended-failure` (all files), plus the Demo 3 task and a copy of `daily-ops-feed`.

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

## Demo 6: Partition a Batch Across Sub-Agents

**Learning objective:** Partition a folder, define what each sub-agent returns, combine the results, and decide what happens when one file fails. Time: about 12 minutes.

**Files:** `demo-files/batch-demo`: `complaint-01.txt` through `complaint-09.txt` and `partition-plan-template.md`.

**Context:** Claude breaks complex work into smaller tasks and may coordinate several sub-agents at once. You cannot assume how many it uses. Your job is to design the split and the contract so the result is complete and checkable.

**Steps:**

1. Open the folder. Ask the room: how many files, and which is the largest?
2. Fill in `partition-plan-template.md` as a class. Decide the split, and the exact fields each sub-agent returns: member, category, amount, urgent (yes or no), status, failure_reason.
3. Give Claude the folder and this prompt: "Extract the fields below from each letter, using sub-agents where it helps. Return one row per file. If a file cannot be read, return a failed row. Write a combined table to a new file named batch-output.md. State how many files you read."
4. Review the table. Count the rows. Check three rows against the source.
5. Ask: what proves nothing was dropped? Answer: the row count equals the file count.

**Expected result:** A table with nine rows. Letters 04 and 07 are marked urgent. Amounts match the letters, and the largest amount is $15,000 (letter 07, wire delay).

> **Instructor note:** Whether Claude uses sub-agents, and how many, is not under your control and not visible in every view. Do not claim a speedup in this demo. Lab 3 measures time. If the work looks sequential, say so.

> **Why this matters:** A batch is only as trustworthy as its contract and its completeness check.

---

## Demo 7: Tour a Data Plugin

**Learning objective:** Describe what a plugin bundles, and tour a data plugin from raw data to a chart. Time: about 12 minutes.

**Files:** `demo-files/data-plugin-dashboard/branch-monthly.csv`.

**Context:** A plugin bundles skills, connectors, and sub-agents into a single package. Plugins are saved to the account and work in chat, in Claude Code, and in tasks. Hooks and sub-agents run only in a task and in Claude Code. The take-home Lab 4 uses the larger and dirtier `loan-applications.csv`.

**Steps:**

1. Open the plugin area and find the data plugin you prepared. Name each part it bundles: skills, connectors, sub-agents.
2. Ask the room which of the three carries instructions, which reaches data, and which does parallel work.
3. Give Claude `branch-monthly.csv`. Ask: "Using the data plugin, summarize approvals by branch and month, and show a chart of average days to decision."
4. Read the summary. Check one branch against the file.
5. Show which part of the plugin ran, if it is visible.
6. Close: this plugin was built by someone else. Ask what a team would need to decide before sharing one.

**Expected result:** A summary and a chart. Harbor South's average days to decision rises from 5.1 to 6.2 across July to September. Harbor North improves from 4.2 to 3.9.

> **Instructor note:** Which data plugin is available, and what it contains, is **unconfirmed** and depends on the account. Verify the plugin exists on the demo account and rehearse. An organization plugin marketplace and plugin admin controls are not stated on Anthropic's page, so do not present them as features. Connector parts are instructor-only, using a sandbox account.

> **Why this matters:** A plugin turns a one-time workflow into something a team can reuse, and a reused workflow needs an owner.
