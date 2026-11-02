---
name: quote-comparison
description: Compares vendor quotes for the same scope. Use when a folder of vendor quotes needs to be extracted, checked for completeness against the vendor risk policy, and ranked by total cost.
---

# Quote Comparison

## Procedure
1. List the files in the quote folder. Count them.
2. Split the files into groups and give each group to a quote extractor sub-agent.
3. Each extractor returns one row per file with the fields: vendor, quote_number, date, total_usd, payment_terms, valid_for, status, failure_reason.
4. If a file cannot be read or has no total, set status to failed and give the reason. Never guess a total.
5. Combine all rows into one table. Confirm the number of rows equals the number of files.
6. A quote reviewer checks that each total equals the sum of its line items and that at least three valid quotes exist.
7. Rank valid quotes by total. Write the table and a short recommendation to the output folder.

## Rules
- Do not modify the source folder.
- State the count of files read, files failed, and files ranked.
