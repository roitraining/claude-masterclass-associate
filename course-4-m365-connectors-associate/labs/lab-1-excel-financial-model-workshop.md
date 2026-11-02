# Lab 1: Excel Financial Model Workshop

**Course:** Microsoft 365 Connectors Associate
**Duration:** 45 minutes
**Format:** Instructor-led, in-class hands-on lab (200 level)

> Part of **[Microsoft 365 Connectors Associate: Labs](README.md)**. `$FILES` is the `demo-files` folder your instructor gives you. Read the [guide preamble](README.md) for prerequisites, scenario notes and token-cost caps before you start.

---

## Prerequisites

- [ ] Microsoft Excel with Claude for Excel available
- [ ] `demo-files\harbor-peak-forecast-model.xlsx`
- [ ] `demo-files\industry-benchmarks.csv`
- [ ] No financial data connector is required. If none appears, use the CSV — that is expected

---

## Overview

The FY2027 board pack of Harbor Peak goes out Friday. **The model has errors.** Dana needs it checked and one peer comparison with a source.

Three things are wrong. You find each one, check it yourself before accepting a fix, and record what you changed.

---

## Part 1: Open the Workbook

### Step 1: Save a Working Copy and Enable Editing

Save a copy of the workbook as `forecast-model-working.xlsx`.

**Expected result:** an editable copy. The original stays untouched.

> **Troubleshooting:** if the workbook shows zeros or empty cells, select Enable Editing and recalculate.

### Step 2: Open the Claude Pane

---

## Part 2: Trace the Model

### Step 3: Ask How the Five Tabs Connect

**Expected result:** an explanation you can check against the formulas.

---

## Part 3: Find and Fix the Totals Error

### Step 4: Ask Claude to Check Every Total — Do Not Accept the List Yet

**Acceptance criteria:** a list of anything that does not add up, held for review.

> **Troubleshooting:** if Claude says the model looks fine, ask it to trace the Revenue total from the service lines.

### Step 5: Check Revenue Row 9 Yourself

**Acceptance criteria:** you confirmed the cause by opening the formula, not by reading the summary.

> **Key Insight:** this is the habit the lab is really teaching. A total that looks right can come from a range that stops early.

### Step 6: Have Claude Fix It and List the Changed Cells

**Acceptance criteria:** the fix applied and the changed cells listed.

> **Common Pitfall:** if Claude changes more than you asked, say "list the cells you will change first" and stop it before it writes.

---

## Part 4: Find and Fix the Hard-Coded Rate

### Step 7: Find Any Number Typed Inside a Formula on the Costs Tab

**Expected result:** the hard-coded value located.

### Step 8: Replace It with the Assumptions Reference and Check the Cell

**Acceptance criteria:** the cell now references Assumptions, verified by opening it.

> **Common Pitfall:** the plan growth rate stays at 6 percent. If Claude changes it because of the 4 percent in the thread, revert that.

---

## Part 5: Resolve the Tax Rate Conflict

### Step 9: Compare the Summary Tax Rate with Assumptions

**Expected result:** the two values and the discrepancy identified.

### Step 10: Decide Which Rate to Present, and Record Why

Write your choice and reason in a cell note.

**Acceptance criteria:** a stated decision with a reason, not a silent fix.

### Step 11: Make the Model Use That Rate from One Place Only

**Acceptance criteria:** one source of truth for the tax rate.

---

## Part 6: Add the Benchmark

### Step 12: Add a Benchmarks Tab and Import the CSV

Import `industry-benchmarks.csv`.

### Step 13: Compare the FY2027 EBIT Margin with the Peer Median

**Acceptance criteria:** the comparison cites the cells it used.

### Step 14: Add a Summary Row with the Source and As-Of Date

**Acceptance criteria:** the peer median sits in the workbook with its source note and as-of date.

---

## Part 7: Write the Summary

### Step 15: Write Three Sentences in a Cell

Cover what was wrong, what you changed, and what you decided.

**Acceptance criteria:** all three, specific to this workbook.

---

## Part 8: Checkpoint

### Step 16: Verify Your Progress

- [ ] A working copy was saved; the original is untouched
- [ ] You can explain how the five tabs connect
- [ ] All three planted errors found
- [ ] Revenue row 9 checked by opening the formula yourself
- [ ] FY2026 total revenue is 12,380,000
- [ ] FY2027 total revenue is 13,122,800
- [ ] The hard-coded percentage on the Costs tab now references Assumptions
- [ ] Marketing grows at the Assumptions inflation rate
- [ ] The plan growth rate is still 6 percent, not 4 percent
- [ ] A tax rate decision is recorded in a cell note, with a reason
- [ ] The model takes that tax rate from one place only
- [ ] Summary after-tax profit equals P&L net income for the rate you chose
- [ ] A Benchmarks tab exists with the imported CSV
- [ ] A sourced peer figure sits in the workbook with its as-of date
- [ ] Every Claude change was listed before or after it was made
- [ ] Three sentences recorded: what was wrong, what changed, what you decided

---

## Troubleshooting Reference

| Issue | Symptom | Solution |
|---|---|---|
| Blank or zero cells | The workbook shows nothing | Select Enable Editing and recalculate |
| Overreaching edits | Claude changes more than asked | Say "list the cells you will change first" and stop it before it writes |
| No errors reported | Claude says the model looks fine | Ask it to trace the Revenue total from the service lines |
| Growth rate altered | The 6 percent becomes 4 percent | The 4 percent is from the thread. The plan stays at 6 percent. Revert it |
| No connector | No financial data connector appears | Use the CSV. That is expected and the lab does not depend on one |

---

## What You Built

In 45 minutes, you:

- Found three planted errors in a multi-tab model, including a SUM range that stopped early and still looked plausible
- Checked each one by opening the formula yourself before accepting a fix
- Replaced a number typed inside a formula with a single source of truth
- Made a judgment call on conflicting tax rates and recorded the reason in the workbook
- Added a peer figure with a source and an as-of date, so the comparison can be re-checked later

---

## What's Next

Lab 2, the Cross-App Deliverable Sprint, carries this corrected workbook into a memo and a deck without re-explaining it.

---

## Facilitator Notes

Three errors are planted: a SUM range that stops at row 7 (Revenue B9:D9), a typed 12 percent inside the Marketing formula (Costs C7), and a typed 21 percent tax rate on the Summary tab against 24 percent in Assumptions.

A good result has all three found, each checked by the student by eye, the cell changes listed, and a stated tax decision.

After the fixes at 24 percent, FY2027 EBIT is 2,561,960 and net income is 1,947,090; the full table is in `demo-files\ANSWER-KEY.md`.

Watch for students who accept the totals from Claude without opening a formula. The financial data connector names in the outline are UNVERIFIED; the lab does not depend on a connector.

---

*Lab 1 Complete*
