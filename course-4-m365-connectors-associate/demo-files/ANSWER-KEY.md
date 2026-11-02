# Answer Key (Facilitator Only): Harbor Peak Sample Files

Do not hand this file to students. Everything here is fictional.

Harbor Peak Wealth Partners is a fictional wealth and fund administration firm. Names in the thread and memo are fictional. The workbook has no cached values, so Excel calculates it when it opens. If the file opens in Protected View, select Enable Editing first.

## Files

- `harbor-peak-forecast-model.xlsx`: tabs Assumptions, Revenue, Costs, P&L, Summary. Used in Demo 1, Demo 4, Lab 1, Lab 2.
- `industry-benchmarks.csv`: fictional peer medians. Used in Demo 2 and Lab 1.
- `email-thread-forecast-review.txt`: a five-message thread that references the workbook as an attachment. Used in Demo 4 and Lab 2.
- `draft-board-memo.docx`: a draft with tone and consistency problems. Used in Demo 3.
- `plays\`: four finance plays, each with a dataset (.csv) and a brief (.md). Used in Demo 6 and Lab 3.

## Planted errors in the workbook

1. **Broken formula (silent).** `Revenue!B9:D9` is `=SUM(x4:x7)` and stops one row short. It leaves out Reporting Subscriptions (row 8, 980,000 in FY2026). The total reads 11,400,000 and should read 12,380,000. It flows into the P&L and Summary. Summary `B7` (growth) still shows 6.0 percent because both sides of the ratio are short, which hides the problem.
2. **Hardcoded value hiding in a formula.** `Costs!C7` (Marketing, FY2027) is `=B7*1.12`. A 12 percent increase is typed into the formula. Every other cost line uses `Assumptions!$B$5` (3.5 percent). Fix: `=B7*(1+Assumptions!$B$5)`. This matches Marcus's remark in the thread that marketing grew faster than other lines.
3. **Inconsistent assumption.** `Summary!B8:C8` hold a typed 21 percent tax rate. `Assumptions!B6` holds 24 percent, and the P&L uses 24 percent. The Summary after-tax profit does not match P&L net income. This is a decision, not only a fix. Dana's last email asks someone to confirm the rate. Accept either answer if the student states the source, but the model must use one rate in one place. The recommended fix is `=Assumptions!$B$6` in both cells.

A fourth item is a distractor from the thread. The 4 percent growth rate was a downside scenario. The plan stays at 6 percent. Claude should not change it.

## Expected values after all three fixes (tax at 24 percent)

| Item | FY2026 | FY2027 | FY2028 |
|---|---|---|---|
| Total revenue | 12,380,000 | 13,122,800 | 13,910,168 |
| Operating costs | 6,400,000 | 6,624,000 | 6,855,840 |
| Operating profit (EBIT) | 2,266,000 | 2,561,960 | 2,881,278 |
| Net income | 1,722,160 | 1,947,090 | 2,189,771 |

Values before the fixes, as built: FY2027 revenue 12,084,000 and FY2027 EBIT 1,800,800. Summary FY2027 after-tax profit at 21 percent after fixes 1 and 2 is 1,997,088, against a P&L net income of 1,947,090.

The benchmark file gives a peer median EBIT margin of 18 percent. The corrected model shows 19.5 percent in FY2027 (EBIT 2,561,960 over revenue 13,122,800). FY2026 is 18.3 percent.

## Planted problems in `draft-board-memo.docx`

- Tone: "pretty great", "gonna", "honestly", "guys", "ASAP!!", "circle back", "nothing to see here". It is a memo for a finance committee.
- Passive and vague wording: "It is expected that revenue will be grown by", "Approval is hoped for by the committee".
- Inconsistent terms: customers, clients; Q3, third quarter; Fund Admin, fund administration; FY2026 and "fiscal year"; 6% and "three percent" and "24 percent".
- Figures that conflict with the workbook: forecast "approx. $13.1M" is right only after fix 1 (13,122,800). The memo says costs rise "roughly three percent", but the model raises marketing 12 percent and other lines 3.5 percent. The memo says tax is 21 percent in one place and 24 percent in another.
- An unsupported claim: "strong activity" in Q3 and "new accounts" have no support in the workbook. Claude should flag them, not confirm them.
- Missing: no decision framing for the finance committee. Elena's email asks for what changed and what needs a decision.
- Heading case is inconsistent ("Decision requested" against "Next Steps").

## Plays: what a good result looks like

- Play 1: Fund Administration has the steepest decline, 41 to 30 bps, about 27 percent. Wealth Advisory is about 13 percent. Retirement Planning is about 8 percent. Tax Services is about 4 percent.
- Play 2: total is 12,380,000. Top 3 clients hold 3,330,000 (26.9 percent). Top 5 hold 4,390,000 (35.5 percent). Alder & Finch alone holds 12.0 percent.
- Play 3: the steps sum to 12,712,800, but the workbook FY2027 revenue is 13,122,800. The bridge includes a 410,000 fee compression step that the workbook does not model. A strong student notices the 410,000 gap against the workbook and says so. This is deliberate and shows why Claude should be asked to check a bridge.
- Play 4: total outstanding is 549,000. Two clients are more than 30 days late: Corbel Retail (41) and Tamarind Logistics (33). Plover & Dunn is at 27 and should not be flagged.
