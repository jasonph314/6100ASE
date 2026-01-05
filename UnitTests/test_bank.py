from bank import value

# 3 cases - is hello, starts with h, everything else
# 2 more cases - empty string and number + special characters

def test_hello():
    assert value ("hello") == 0
    assert value("Hello") == 0

def test_starts_with_h():
    assert value("Home sweet home") == 20

def test_other():
    assert value("yogurt") == 100

def test_input_is_emput():
    assert value("") == 100

def test_input_is_special():
    assert value("123>@#!@$") == 100
