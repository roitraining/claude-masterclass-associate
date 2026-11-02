"""Characterization tests: they pin what batch_invoices.py does today,
including its quirks. A modernized version must produce the same totals."""
import time
from pathlib import Path

import pytest

import batch_invoices

ORDERS = Path(__file__).parent.parent / "orders.csv"

EXPECTED = [
    "1001|Northwind Pottery|CA|53.62",
    "1002|Lakeside Books|TX|102.00",
    "1003|Fernhill Garden Supply|NY|126.32",
    "1004|Northwind Pottery|OH|10.56",
    "1005|Corner Bike Shop|CA|835.48",
    "1006|UNKNOWN|TX|60.56",
    "1008|Fernhill Garden Supply|ZZ|76.12",
    "1009|Corner Bike Shop|TX|0.00",
    "1010|Northwind Pottery|NY|756.71",
]


@pytest.fixture(autouse=True)
def fresh_state(monkeypatch):
    monkeypatch.setattr(time, "sleep", lambda s: None)
    batch_invoices.T = 0
    batch_invoices.E = 0


def run_legacy(tmp_path):
    out = tmp_path / "out.txt"
    batch_invoices.run(str(ORDERS), str(out))
    return out.read_text().splitlines()


def test_invoice_lines(tmp_path):
    assert run_legacy(tmp_path)[:-1] == EXPECTED


def test_total_line(tmp_path):
    assert run_legacy(tmp_path)[-1] == "TOTAL 2021.37 ERR 1"


def test_bad_quantity_row_is_dropped_silently(tmp_path):
    assert not any(line.startswith("1007") for line in run_legacy(tmp_path))


def test_unknown_state_uses_five_percent(tmp_path):
    assert "1008|Fernhill Garden Supply|ZZ|76.12" in run_legacy(tmp_path)
