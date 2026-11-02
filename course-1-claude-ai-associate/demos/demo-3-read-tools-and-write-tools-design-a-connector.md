# Demo 3: Read Tools and Write Tools: Design a Connector

**Course:** Claude.ai Associate: Skills, Connectors and Real Deliverables (Claude MasterClass, Associate Course 1)
**Demo:** 3 of 6
**Time:** about 15 minutes

> Part of **[Claude.ai Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Decide which tools a custom connector should expose, which stay read-only, and how to name them so Claude picks the right one. Time: about 15 minutes.

**Files:** [`demo-files/demo3/tool-catalog.csv`](../demo-files/demo3/tool-catalog.csv), [`demo-files/demo3/connector-design-worksheet.md`](../demo-files/demo3/connector-design-worksheet.md)

**Context:** A custom connector is a remote MCP server. Everyone who connects reaches whatever its tools reach. The ten candidate tools mix safe reads, dangerous reads, and writes. This is a design exercise on paper, run as a group.

**Steps:**

1. Open `tool-catalog.csv` on the screen and read the ten tools.
2. Fill Part 1 of the worksheet as a group, tool by tool: Expose now, Later phase, or Never.
3. Compare with the key below and discuss each difference.
4. Fill Part 2: rename `query1`, `get_data` and `doStuff`, and write a one-sentence description for each.
5. Fill Part 3 and Part 4: authentication, reach, and the order of the approval path.
6. Optional, instructor only: on an ROI sandbox Team or Enterprise account, open the admin Connectors settings and show where a custom web connector is added (server URL, optional OAuth fields). Do not enter a real server.

**Expected result:** The key below. Good names read like search_service_tickets: a verb, a noun, and a description that says when to use it. The approval path runs: request with the tool list, security review, pilot group, publish.

| Tool | Decision | Reason |
|------|----------|--------|
| get_member_summary | Expose now | Read, minimal fields |
| search_service_tickets | Expose now | Read, no identifiers beyond ticket |
| get_fee_schedule | Expose now | Read, public data |
| list_branch_hours | Expose now | Read, public data |
| get_full_member_record | Never | Returns tax ID, date of birth, account numbers |
| run_sql_query | Never | Unbounded read, bypasses every field decision |
| create_service_ticket | Later phase | Write, reversible, pilot first |
| update_member_address | Later phase | Write to a member file, needs approval flow |
| send_member_email | Never | Write, external, cannot be recalled |
| close_account | Never | Write, moves money, irreversible |

> **Instructor note:** Beta status, owner setup on Team and Enterprise, individual user connection, and the public-reachability requirement are verified. Per-tool permission controls inside Claude are UNVERIFIED. Do not promise that a student can switch off a single tool in the Claude interface. Teach the design decision as one made in the server and in the approval review. Anthropic warns that custom connectors reach services it has not verified, so say that. The optional admin screen is instructor-only and the exact labels may differ from this guide.

> **Why this matters:** A connector is a standing door into your systems. Deciding what stays closed, before anyone connects, is cheaper than discovering it afterward. Tool names and descriptions decide whether Claude picks the right tool at all.

---

**Previous:** [Demo 2: A Multi-File Skill, Loaded Only When Needed](demo-2-a-multi-file-skill-loaded-only-when-needed.md) · **Next:** [Demo 4: Research With Conflicting Sources](demo-4-research-with-conflicting-sources.md)


*Demo 3 of 6*
