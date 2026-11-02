"""Order reports for ShipDesk."""
from shipdesk.pricing import order_total


def summarize_orders(orders):
    """Return order count, grand total and the biggest order id."""
    totals = {o["id"]: order_total(o["items"]) for o in orders}
    if not totals:
        return {"count": 0, "grand_total": "0.00", "largest": None}
    largest = max(totals, key=totals.get)
    return {
        "count": len(totals),
        "grand_total": str(sum(totals.values())),
        "largest": largest,
    }


def render_text(summary):
    """Plain-text version of a summary."""
    return (
        f'Orders: {summary["count"]}\n'
        f'Grand total: {summary["grand_total"]}\n'
        f'Largest order: {summary["largest"]}\n'
    )
