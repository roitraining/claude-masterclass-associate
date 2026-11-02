# Demo 2: Pull a Data Source Into Excel

**Course:** Microsoft 365 Connectors Associate: Claude Across Office (Claude MasterClass, Associate Course 4)
**Demo:** 2 of 6
**Time:** about 12 minutes

> Part of **[Microsoft 365 Connectors Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Bring an external figure into a model with its source and date attached. Time: about 12 minutes.

**Files:** [`demo-files\industry-benchmarks.csv`](../demo-files/industry-benchmarks.csv)

**Context:** The board will ask how the forecast compares with peers. This demo sources a peer median instead of pasting a number from memory. The default path uses the sample CSV so it works on every plan and tenant.

**Steps:**

1. In the corrected workbook, add a tab named Benchmarks.
2. Import `industry-benchmarks.csv` into that tab.
3. Ask Claude: "Compare our FY2027 EBIT margin with the peer median in the Benchmarks tab. Show the figure, its source and its as-of date."
4. Check the answer against the cells it cites.
5. Ask Claude to add a row to the Summary tab with the peer median, the source note and the as-of date.
6. Optional, only if the sandbox plan has a financial data connector in Excel: repeat step 3 against the connector and compare the figure with the CSV.

**Expected result:** Claude reports a peer median EBIT margin of 18 percent, the FY2027 model margin of about **19.3 percent**, and the source note and the 2026-06-30 date. The Summary tab has a sourced row.

> **On that 19.3 percent.** Demo 1 fixed only the Revenue SUM range, so at this point FY2027 EBIT is 2,527,960 on revenue of 13,122,800, which is 19.26 percent. The figure rises to **19.5 percent** (EBIT 2,561,960) only after the hardcoded 12 percent marketing cell in `Costs!C7` is also fixed, and that error is held back for Lab 1. Recomputed from the workbook on October 22, 2026. If you say 19.5 here, the screen will disagree with you.

> **Instructor note:** UNVERIFIED. The financial data connector names in the outline (S&P Global, LSEG, Moody's, FactSet) come from another course outline and are not confirmed. Do not promise them. Say that the demo works with the CSV and that a connector, if present, follows the same pattern. If you run step 6, rehearse it first and treat the result as unconfirmed.

> **Why this matters:** A figure without a source and a date cannot be defended in front of a board.

---

**Previous:** [Demo 1: Trace and Debug a Broken Formula](demo-1-trace-and-debug-a-broken-formula.md) · **Next:** [Demo 3: Redline a Draft With Judgment](demo-3-redline-a-draft-with-judgment.md)


*Demo 2 of 6*
