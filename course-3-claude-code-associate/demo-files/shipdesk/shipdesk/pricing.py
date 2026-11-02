"""Order pricing for ShipDesk, a fictional parcel-shipping desk."""
from decimal import Decimal, ROUND_HALF_UP

FREE_SHIPPING_THRESHOLD = Decimal("75.00")
FLAT_SHIPPING = Decimal("6.95")
TAX_RATE = Decimal("0.07")


def money(value):
    """Round a Decimal to cents."""
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def line_total(item):
    """Price of one order line: quantity times unit price."""
    return money(Decimal(item["unit_price"]) * item["qty"])


def subtotal(items):
    """Sum of all line totals."""
    return money(sum((line_total(i) for i in items), Decimal("0")))


def shipping(sub):
    """Flat shipping, free once the subtotal reaches the threshold."""
    if sub >= FREE_SHIPPING_THRESHOLD:
        return Decimal("0.00")
    return FLAT_SHIPPING


def tax(sub):
    """Sales tax on the subtotal only, not on shipping."""
    return money(sub * TAX_RATE)


def order_total(items):
    """Subtotal plus shipping plus tax."""
    sub = subtotal(items)
    return money(sub + shipping(sub) + tax(sub))
