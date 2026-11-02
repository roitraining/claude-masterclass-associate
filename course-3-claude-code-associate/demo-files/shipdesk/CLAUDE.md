# ShipDesk

Small fictional parcel-shipping desk library. Python 3.11 or later.

- Run the tests with `python -m pytest -q`. They must pass before any commit.
- Money is `Decimal`, rounded with `pricing.money`. Never use float for money.
- Keep a change inside the files its ticket names. Do not edit unrelated modules.
- Add or update tests in the matching `tests/test_<module>.py`.
- Do not run `git push`. Commit locally only.
