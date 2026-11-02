from shipdesk.addresses import format_address, normalize_state


def test_normalize_state_full_name():
    assert normalize_state("Texas") == "TX"


def test_normalize_state_code_passthrough():
    assert normalize_state("oh") == "OH"


def test_normalize_state_unknown():
    assert normalize_state("Atlantis") is None


def test_format_address():
    addr = {"street": " 12 Mill Rd ", "city": "Austin", "state": "texas", "zip": "78701"}
    assert format_address(addr) == "12 Mill Rd, Austin, TX 78701"
