# Lab 1: Excel Financial Model Workshop

> Part of **[Microsoft 365 Connectors Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

**Learning objective:** Trace, debug and adjust a messy multi-tab model with Claude for Excel, then add a sourced figure. Time: 45 minutes.

**Files:** `demo-files\harbor-peak-forecast-model.xlsx`, `demo-files\industry-benchmarks.csv`

**Context:** Harbor Peak's FY2027 board pack goes out Friday. The model has errors. Dana needs it checked and one peer comparison with a source.

**Steps:**

1. Save a copy of the workbook as `forecast-model-working.xlsx` and enable editing.
2. Open the Claude pane.
3. Ask Claude to explain how the five tabs connect.
4. Ask Claude to check every total and subtotal and list anything that does not add up. Do not accept the list yet.
5. Check Revenue row 9 yourself. Confirm the cause.
6. Ask Claude to fix it and list the cells changed.
7. Ask Claude to find any number typed inside a formula on the Costs tab.
8. Ask Claude to replace it with the Assumptions reference. Check the cell.
9. Ask Claude to compare the tax rate on the Summary tab with the Assumptions tab.
10. Decide which tax rate to present. Write your choice and reason in a cell note.
11. Ask Claude to make the model use that rate from one place only.
12. Add a tab named Benchmarks and import `industry-benchmarks.csv`.
13. Ask Claude to compare the FY2027 EBIT margin with the peer median and cite the cells.
14. Add a Summary row that holds the peer median, its source note and its as-of date.
15. Write three sentences in a cell: what was wrong, what you changed, what you decided.

**Checkpoint:** FY2026 total revenue is 12,380,000 and FY2027 is 13,122,800. Marketing grows at the Assumptions inflation rate. Summary after-tax profit equals P&L net income for the rate you chose. A sourced peer figure sits in the workbook with its date.

**Common problems:**

- The workbook shows zeros or empty cells: select Enable Editing and recalculate.
- Claude changes more than you asked: say "list the cells you will change first" and stop it before it writes.
- Claude says the model looks fine: ask it to trace the Revenue total from the service lines.
- Claude changes the 6 percent growth rate because of the 4 percent in the thread: the plan stays at 6 percent.
- No financial data connector appears: use the CSV. That is expected.

**Facilitator note:** Three errors are planted: a SUM range that stops at row 7 (Revenue B9:D9), a typed 12 percent inside the Marketing formula (Costs C7), and a typed 21 percent tax rate on the Summary tab against 24 percent in Assumptions. A good result has all three found, each checked by the student by eye, the cell changes listed, and a stated tax decision. After the fixes at 24 percent, FY2027 EBIT is 2,561,960 and net income is 1,947,090; the full table is in `demo-files\ANSWER-KEY.md`. Watch for students who accept Claude's totals without opening a formula. The financial data connector names in the outline are UNVERIFIED; the lab does not depend on a connector.
