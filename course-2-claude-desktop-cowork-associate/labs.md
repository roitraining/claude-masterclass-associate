# Claude Desktop Associate: Labs

**Course:** Claude Desktop Associate: Persistent Workspaces and Unattended Work (Claude MasterClass Associate, Course 2)
**Contents:** Three timed hands-on labs and a take-home lab. The numbers match the course outline.

---

## About this guide

Labs are student-run. Each has a learning objective, a time, a Files line, a Context paragraph, numbered Steps, a Checkpoint, Common problems, and a Facilitator note.

Files are in the `demo-files` folder. Scenario: Harbor Ridge Credit Union, a fictional credit union. Every person, company, and figure is fictional.

**Swap the scenario.** For healthcare, use a fictional clinic network, with scheduling, referral, and complaint procedures as the knowledge files and referral letters or equipment quotes as the batch. For government, use a fictional county office, with permit, fee, and records procedures and contractor bids as the batch. Keep the planted traps: an archive file, an unanswerable question, a keep-out file, and one bad file in the batch.

> **Accounts and connectors.** Students use sample files only. Anything that touches a connector or an account is instructor-only on an ROI sandbox account, and students do the offline version.

> **Essentials baseline.** Students already know how to hand Claude a task on a folder, the three approval modes, cloud versus local, and proving a folder restriction. These labs do not re-teach them.
>
> Say "task", not "Cowork". The two merged into one Claude on September 16, 2026, and no replacement product name was introduced.

---

## Lab 1: Persistent Workspace

**Learning objective:** Install a custom local extension, ground Claude in a knowledge folder, test answers for citations and missing files, and decide what must stay out. Time: 45 minutes.

**Files:** `demo-files/knowledge-folder`, `demo-files/keep-out-of-the-workspace`, `demo-files/lab1-test-questions.md`, `demo-files/lab1-workspace-boundary-worksheet.md`, and the facilitator-prepared `.mcpb` file.

**Context:** In Essentials you gave Claude a folder for a single session. Here you install an extension that keeps a folder available in every conversation. A wider and longer exposure needs a boundary and a test.

**Steps:**

1. Copy `knowledge-folder` and `keep-out-of-the-workspace` to your Documents folder as siblings. Do not put one inside the other.
2. Open Claude Desktop. Go to **Settings**, then **Advanced settings**, then **Extension Developer**.
3. Select **Install Extension** and choose the `.mcpb` file your facilitator provides.
4. Read the install prompt. Write down what it says the extension can reach.
5. Open a new conversation and ask: "List the files in the knowledge folder."
6. Open `lab1-test-questions.md`. Ask questions 1 and 2. Check each answer and the cited file.
7. Ask questions 3 to 6. Record each answer in a copy of the table.
8. Ask question 7 about the salary band. Record whether the keep-out folder was reachable.
9. Ask question 8. Check that Claude stays inside file 01.
10. Open the worksheet and complete it. List at least five categories that must stay out of a persistent workspace.
11. Write a review plan: who reviews the folder and how a stale file is found.

**Checkpoint:** Each student leaves with an installed extension, a completed test table, a worksheet with at least five must-stay-out categories, and a review plan.

**Common problems:**

- The install option is missing. Check the Desktop version and that the account is on a paid plan.
- The install is blocked. Local administrator rights or an IT policy may be preventing it. Machine-level policy overrides in-app controls.
- Claude lists no files. Confirm the extension is enabled in the conversation and the folder path in the extension is correct.
- Claude answers question 7. The extension can reach more than the knowledge folder. Record it as a finding, then narrow the folder.
- Answers have no file name. Remind the student that the map file asks for citations, then record the miss.

**Facilitator note:** Prepare the `.mcpb` in advance from Anthropic's MCPB documentation (a zip holding a local MCP server and `manifest.json`) and rehearse it on the class VM. Whether Claude Desktop and custom extension install work on the class VM is **unconfirmed**. This guide deliberately provides no extension code because the manifest fields are not in our verified facts. A good result: question 1 says $25,000 (file 01); question 2 says 1:00 p.m. Eastern; question 3 names the credit committee and flags that a written exception is needed because no level sits above it; question 4 is "not covered"; question 5 is declined or labeled superseded; question 6 is closed with no wires; question 7 is "not covered". Do not penalize a student whose extension reaches the keep-out folder. The lesson is that the folder boundary, not the instruction file, is the control.

---

## Lab 2: Scheduled Task Automation

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

---

## Lab 3: Batch + Plugin Capstone

**Learning objective:** Split a folder of sample files across sub-agents, combine the results, recover from a failed file, and package the workflow as a plugin. Time: 60 minutes.

**Files:** `demo-files/vendor-quotes` (14 files), `demo-files/lab3-batch-design-sheet.md`, `demo-files/lab3-timing-sheet.csv`, `demo-files/lab3-plugin-spec.md`, `demo-files/quote-comparison-skill.md`, `demo-files/quote-subagent-roles.md`.

**Context:** You will compare 14 vendor quotes for the same branch security camera project. One file is bad on purpose. You design the batch before you run it, time it against one at a time, and package the result so a team can reuse it.

**Steps:**

1. Copy `vendor-quotes` to your Documents folder. Treat it as read only.
2. Open `lab3-batch-design-sheet.md`. Fill in the partition, the return fields, the output location, the combine rule, and the rule for a failed file.
3. Start the timing sheet. In a task on the folder, process only the first 3 files one at a time. Ask for the vendor, total, payment terms, and validity. Record the minutes.
4. In a new task, give Claude the folder and your design. Ask it to use sub-agents where it helps, return one row per file, and write results to a new folder named `batch-output`.
5. Record the end time and the minutes on the timing sheet.
6. Count the rows in the combined table. They should equal the number of files.
7. Find the file that failed. Record its name and the reason Claude gave.
8. Check that Claude did not guess a total for the failed file.
9. Pick any three rows and check each total against the source file.
10. Ask Claude to rank the valid quotes by total and name the lowest.
11. Open `lab3-plugin-spec.md`. Fill in the name, description, who may run it, and the version and owner.
12. Package the skill from `quote-comparison-skill.md` and the roles from `quote-subagent-roles.md` as a plugin, using the method your facilitator rehearsed.
13. Write one sentence on what a connector would add to this plugin, and who would need to approve it.
14. Present your consolidated table and the time saved against one at a time.

**Checkpoint:** Each student presents a consolidated table of all 14 files with the failed file flagged, a time comparison, and a completed plugin spec.

**Common problems:**

- Claude reports 13 rows. The failed file was dropped. Ask it to return a failed row for any unreadable file.
- Claude invents a total for the bad file. Tighten the rule: never guess, report failed.
- Results are written into `vendor-quotes`. Move them and restate the output location.
- The parallel run is not faster. Record the real time. Sub-agent use is not guaranteed and not always visible.
- A usage limit message appears. Lab 3 uses more of the usage limit. Reduce to the first 8 files and say so on the timing sheet.

**Facilitator note:** The answer key: 14 files, 13 valid, 1 failed (`quote-09.txt`, garbled and truncated, no total). Lowest valid total is Granite Peak Security at $5,924. The highest is Ironwood Technical at $7,412. The ranking from low to high is quotes 13, 2, 10, 6, 4, 1, 8, 12, 11, 7, 3, 14, 5. Every valid quote totals 12 cameras, 2 recorders, and installation, so scope is the same. The quote totals are below $25,000, so the three-quote rule in the vendor risk policy is used here as a design check and not as a trigger. How to create a plugin from a task is **not in our verified facts**, so rehearse the method and, if it is not available to students, accept the completed spec and skill files as the deliverable. Per-sub-agent usage is not stated. A good result: all 14 files accounted for, the bad file flagged and not guessed, a measured time comparison (even if parallel was not faster), and a spec with a named owner.

---

## Lab 4: Data Plugin Dashboard (take-home)

**Learning objective:** Clean, analyze, and visualize a dataset on your own with a data plugin. No timed session.

**Files:** `demo-files/data-plugin-dashboard`: `loan-applications.csv` and `README.md`. Do not open the README until you finish a cleaning pass.

**Context:** `loan-applications.csv` holds 60 fictional loan applications with planted data problems. Use a data plugin to find them, clean the file, and build a dashboard. Use sample data only. Do not connect any account.

**Steps:**

1. Copy the folder to your Documents folder.
2. Give Claude access to the folder. Make sure a data plugin is installed on your account.
3. Ask Claude to profile the file and list every data quality problem it finds. Do not fix anything yet.
4. List the problems in your own words. Then open `README.md` and check how many you found.
5. Ask Claude to write a cleaned copy named `loan-applications-clean.csv` and a short change log. The original must stay unchanged.
6. Check the change log. Confirm that no row was silently dropped or invented.
7. Ask for approval rate and average days to decision by branch and by month.
8. Ask for a dashboard with three charts: applications by month, approval rate by branch, and average days to decision by product.
9. Check two numbers on the dashboard against the cleaned file by hand.
10. Write three sentences: what the data plugin did for you, what you still had to check yourself, and one thing you would not let it do unattended.

**Checkpoint:** A cleaned file, a change log, a dashboard, and your three sentences.

**Common problems:**

- The data plugin is not available on your plan or account. Do the same steps without it and note the difference.
- Claude fixes the typo branches but not the case problem. Ask for an exact list of distinct branch values after cleaning.
- The duplicate application ID is merged without a note. Require a change log entry for every row touched.
- The impossible date is guessed. Ask Claude to flag it, not repair it.

**Facilitator note:** The nine planted problems are listed in the folder README. A good result lists all nine, keeps the original file, logs each change, and does not invent values for the missing amount or the missing credit score. Whether a data plugin is available to students, and what it is called, is **unconfirmed**. If it is not available, the lab still works without one. Review submitted change logs first, since they show whether the student verified the work.
