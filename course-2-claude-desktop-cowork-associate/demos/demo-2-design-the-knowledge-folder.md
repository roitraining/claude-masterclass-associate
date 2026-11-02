# Demo 2: Design the Knowledge Folder

**Course:** Claude Desktop Associate: Persistent Workspaces and Unattended Work (Claude MasterClass Associate, Course 2)
**Demo:** 2 of 7
**Time:** about 12 minutes

> Part of **[Claude Desktop Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Design a knowledge folder for retrieval, with a map file, an archive, and a boundary around what stays out. Time: about 12 minutes.

**Files:** [`demo-files/knowledge-folder`](../demo-files/knowledge-folder), [`demo-files/keep-out-of-the-workspace`](../demo-files/keep-out-of-the-workspace), [`demo-files/lab1-test-questions.md`](../demo-files/lab1-test-questions.md).

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

**Previous:** [Demo 1: Install a Custom Extension](demo-1-install-a-custom-extension.md) · **Next:** [Demo 3: Schedule a Briefing, Then Read a Run](demo-3-schedule-a-briefing-then-read-a-run.md)


*Demo 2 of 7*
