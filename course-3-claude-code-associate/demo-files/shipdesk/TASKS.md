# Lab 1 tasks

Three independent tasks. Each touches different files, so the branches merge without conflicts.

## Task A: ZIP validation (worktree `zip-check`)

Files: `shipdesk/addresses.py`, `tests/test_addresses.py`

Add `normalize_zip(raw)`. It accepts a 5-digit ZIP or a 9-digit ZIP+4 (with or without a hyphen), and returns `12345` or `12345-6789`. Anything else returns `None`. Add at least four tests.

## Task B: Bulk discount (worktree `bulk-discount`)

Files: `shipdesk/pricing.py`, `tests/test_pricing.py`

Add a per-line discount in `line_total`: a quantity of 10 to 24 takes 5 percent off, and 25 or more takes 10 percent off. Keep `Decimal` and `money`. Add at least four tests, including both boundaries.

## Task C: CSV export (worktree `csv-export`)

Files: `shipdesk/reports.py`, `tests/test_reports.py`

Add `to_csv(orders)`. It returns CSV text with the header `id,customer,total` and one row per order, using `order_total`. Add at least three tests.
