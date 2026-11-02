# Capstone brief: the async invoice endpoint

Replace the batch script with a FastAPI endpoint in `app.py`.

## Endpoint

`POST /invoices/batch` with a JSON body:

```json
{"orders": [{"oid": "1001", "cust": "C1", "st": "CA", "qty": "4", "price": "12.50"}]}
```

Response:

```json
{
  "invoices": [{"oid": "1001", "customer": "Northwind Pottery", "state": "CA", "total": "53.62"}],
  "errors": [{"oid": "1007", "reason": "qty is not a number"}],
  "grand_total": "2021.37"
}
```

## Requirements

1. Same totals as the legacy script for every valid row in `orders.csv`, including the 5 percent default tax for an unknown state, the 5 percent discount over 500, and the 12 dollar New York surcharge.
2. Customer and tax lookups are `async` and run concurrently across orders. The 10-row sample finishes in under 0.5 seconds with the original 0.05 second lookup delay.
3. No global state. Two requests in a row return the same answer.
4. A bad row is reported in `errors` with a reason. It is never dropped silently.
5. New tests in `tests/test_app.py`. The legacy tests must still pass.
6. Short documentation in `README.md`: what the endpoint does, the request, the response, and three known limits.
