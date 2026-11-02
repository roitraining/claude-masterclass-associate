# Lab 1: Persistent Workspace

> Part of **[Claude Desktop Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

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
