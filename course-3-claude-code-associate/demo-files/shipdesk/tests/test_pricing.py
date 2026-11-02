from decimal import Decimal

from shipdesk.pricing import order_total, shipping, subtotal, tax


def test_subtotal_sums_lines():
    items = [{"sku": "A", "qty": 2, "unit_price": "10.00"}, {"sku": "B", "qty": 1, "unit_price": "5.50"}]
    assert subtotal(items) == Decimal("25.50")


def test_shipping_charged_below_threshold():
    assert shipping(Decimal("10.00")) == Decimal("6.95")


def test_shipping_free_above_threshold():
    assert shipping(Decimal("100.00")) == Decimal("0.00")


def test_tax_on_subtotal_only():
    assert tax(Decimal("100.00")) == Decimal("7.00")


def test_order_total_small_order():
    items = [{"sku": "A", "qty": 1, "unit_price": "10.00"}]
    assert order_total(items) == Decimal("17.65")


def test_order_total_free_shipping_order():
    items = [{"sku": "A", "qty": 1, "unit_price": "100.00"}]
    assert order_total(items) == Decimal("107.00")
