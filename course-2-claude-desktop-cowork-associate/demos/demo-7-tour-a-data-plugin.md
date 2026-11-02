# Demo 7: Tour a Data Plugin

**Course:** Claude Desktop Associate: Persistent Workspaces and Unattended Work (Claude MasterClass Associate, Course 2)
**Demo:** 7 of 7
**Time:** about 12 minutes

> Part of **[Claude Desktop Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Describe what a plugin bundles, and tour a data plugin from raw data to a chart. Time: about 12 minutes.

**Files:** [`demo-files/data-plugin-dashboard/branch-monthly.csv`](../demo-files/data-plugin-dashboard/branch-monthly.csv).

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

---

**Previous:** [Demo 6: Partition a Batch Across Sub-Agents](demo-6-partition-a-batch-across-sub-agents.md)


*Demo 7 of 7*
