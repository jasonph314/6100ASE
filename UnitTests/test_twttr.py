from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_numbers_punctuation():
    assert shorten("TW1TT3R") == "TW1TT3R"

def test_all_vowels():
    assert shorten("AEIOUUUU") == ""

def test_no_vowels():
    assert shorten("TWTTR") == "TWTTR"
