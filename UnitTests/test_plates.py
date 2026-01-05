from plates import is_valid





def test_short():
    assert is_valid("H") == False


def test_long():
    assert is_valid("HEL000000000") == False


def test_empty():
    assert is_valid("") == False

def test_first_number_not_zero():
    assert is_valid("AA011") == False


def test_special_chars():
    assert is_valid("??????23432!#@$") == False

def test_first_two_letters():
    assert is_valid("B0111") == False

def test_validPlate():
    assert is_valid("HELL10") == True

def test_all_alpha():
    assert is_valid("HELLO") == True



