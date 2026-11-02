# Lab 3: Batch + Plugin Capstone

> Part of **[Claude Desktop Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

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
