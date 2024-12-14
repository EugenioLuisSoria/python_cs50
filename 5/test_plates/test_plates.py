from plates import is_valid


def test_length():
    assert is_valid("AAABBBCCC") == False

def test_spaces():
    assert is_valid("AA**50") == False

def test_first_cero():
    assert is_valid("AA02") == False

def test_starting_letters():
    assert is_valid("11BB") == False

def test_number_placement():
    assert is_valid("AA1A2B") == False

def test_aplhabetical_checks():
    assert is_valid("11") == False

