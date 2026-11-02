# Demo 6: Partition a Batch Across Sub-Agents

**Course:** Claude Desktop Associate: Persistent Workspaces and Unattended Work (Claude MasterClass Associate, Course 2)
**Demo:** 6 of 7
**Time:** about 12 minutes

> Part of **[Claude Desktop Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Partition a folder, define what each sub-agent returns, combine the results, and decide what happens when one file fails. Time: about 12 minutes.

**Files:** [`demo-files/batch-demo`](../demo-files/batch-demo): `complaint-01.txt` through `complaint-09.txt` and `partition-plan-template.md`.

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

**Previous:** [Demo 5: Break It on Purpose: Unattended Failure](demo-5-break-it-on-purpose-unattended-failure.md) · **Next:** [Demo 7: Tour a Data Plugin](demo-7-tour-a-data-plugin.md)


*Demo 6 of 7*
