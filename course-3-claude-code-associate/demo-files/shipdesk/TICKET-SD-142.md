# SD-142: Promo codes

As a desk clerk, I can apply one promo code to an order so the customer gets a percentage off the subtotal.

## Acceptance criteria

1. A promo has a `code`, a `percent` (1 to 100) and an `expires` date.
2. `order_total(items, promo=None, today=None)` applies at most one promo to the subtotal, before shipping and tax.
3. An expired promo is rejected with `ValueError("promo expired")`. A promo is valid through the end of its `expires` date.
4. An unknown code is rejected with `ValueError("unknown promo")`.
5. Existing calls to `order_total(items)` behave exactly as before.
6. New logic lives in `shipdesk/promos.py`. Tests live in `tests/test_promos.py`.

## Out of scope

Shipping rules, tax rules, addresses, reports.

## Limits

Maximum 4 files changed and 150 diff lines.
