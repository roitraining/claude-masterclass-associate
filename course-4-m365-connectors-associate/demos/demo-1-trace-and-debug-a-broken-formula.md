# Demo 1: Trace and Debug a Broken Formula

**Course:** Microsoft 365 Connectors Associate: Claude Across Office (Claude MasterClass, Associate Course 4)
**Demo:** 1 of 6
**Time:** about 12 minutes

> Part of **[Microsoft 365 Connectors Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Use Claude for Excel to trace a number across tabs and find a formula that is silently wrong. Time: about 12 minutes.

**Files:** [`demo-files\harbor-peak-forecast-model.xlsx`](../demo-files/harbor-peak-forecast-model.xlsx)

**Context:** Total revenue looks low against its service lines, and nobody has traced it. Do not look at the formulas first. Let Claude find the cause.

**Steps:**

1. Open a copy of the workbook in Excel and enable editing.
2. Open the Claude pane.
3. Ask: "Map how the five tabs connect. Which tabs feed the P&L?"
4. Ask: "Total revenue on the Revenue tab looks low compared with the lines above it. Trace it and tell me why."
5. Read the explanation. Select `Revenue!B9` and check the range yourself.
6. Ask Claude to fix the totals for all three years and to list every cell it changed.
7. Ask: "Which cells on the P&L and Summary tabs change because of this?"

**Expected result:** Claude explains that the Revenue totals sum rows 4 to 7 and leave out row 8, Reporting Subscriptions. FY2026 total moves from 11,400,000 to 12,380,000. The fix flows to the P&L and Summary. Claude lists the cells it changed.

> **Instructor note:** The workbook contains two further planted errors. Do not reveal them here. They are the work of Lab 1. The Excel add-in reading and writing cells, formulas and formatting is documented. The exact menu wording and how it presents its change list need rehearsal on the class build.

> **Why this matters:** A total that is a little low reads as plausible. Claude's trace is only useful if you check the formula it points to.

---

**Next:** [Demo 2: Pull a Data Source Into Excel](demo-2-pull-a-data-source-into-excel.md)


*Demo 1 of 6*
