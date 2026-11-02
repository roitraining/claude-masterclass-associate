import json
from pathlib import Path

from shipdesk.reports import render_text, summarize_orders

ORDERS = json.loads((Path(__file__).parent.parent / "data" / "orders.json").read_text())


def test_summary_counts_orders():
    assert summarize_orders(ORDERS)["count"] == 4


def test_summary_largest_order():
    assert summarize_orders(ORDERS)["largest"] == "SD-1003"


def test_empty_summary():
    assert summarize_orders([]) == {"count": 0, "grand_total": "0.00", "largest": None}


def test_render_text_has_three_lines():
    assert len(render_text(summarize_orders(ORDERS)).splitlines()) == 3
