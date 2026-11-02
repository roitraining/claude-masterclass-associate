"""Address helpers for ShipDesk."""

STATES = {"california": "CA", "texas": "TX", "new york": "NY", "ohio": "OH", "oregon": "OR"}


def normalize_state(raw):
    """Return a two-letter state code, or None if the state is unknown."""
    key = raw.strip().lower()
    if len(key) == 2 and key.upper() in STATES.values():
        return key.upper()
    return STATES.get(key)


def format_address(addr):
    """Render an address dict as a single mailing line."""
    state = normalize_state(addr["state"]) or addr["state"].strip()
    return f'{addr["street"].strip()}, {addr["city"].strip()}, {state} {addr["zip"].strip()}'
