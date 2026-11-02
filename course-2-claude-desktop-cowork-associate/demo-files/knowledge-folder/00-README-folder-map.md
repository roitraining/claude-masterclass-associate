# Harbor Ridge Credit Union: Operations Knowledge Folder

Harbor Ridge Credit Union is a fictional credit union used for training.

This folder is the persistent knowledge base for the operations assistant. Claude should answer only from the files listed here and name the file each answer came from.

| File | Covers | Owner | Last reviewed |
|---|---|---|---|
| 01-wire-transfer-procedure.md | Domestic and international wires, limits, callbacks | Payments | 2026-08-14 |
| 02-kyc-onboarding-checklist.md | Identity checks for new members | Compliance | 2026-07-02 |
| 03-lending-approval-matrix.md | Who may approve which loan | Lending | 2026-09-01 |
| 04-vendor-risk-policy.md | Vendor onboarding and review tiers | Risk | 2026-06-20 |
| 05-complaint-handling.md | Complaint intake, deadlines, escalation | Member Care | 2026-08-30 |
| 06-fee-schedule.csv | Current member fees | Finance | 2026-09-15 |
| 07-holiday-calendar-2026.csv | Branch closures and wire cutoffs | Operations | 2026-01-05 |
| 99-archive-old-wire-limits-2024.md | Superseded wire limits. Kept for audit only | Payments | 2024-11-01 |

## Rules for answers
1. Cite the file name for every fact.
2. If no file covers the question, say "not covered in the knowledge folder". Do not guess.
3. If two files disagree, say so and prefer the file with the later review date, except that files named archive are never a source.
