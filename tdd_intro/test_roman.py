import pytest
from roman import roman_to_int


# --- Valid: single symbols ---

@pytest.mark.parametrize("numeral, expected", [
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000),
], ids=["I", "V", "X", "L", "C", "D", "M"])
def test_single_symbols(numeral, expected):
    assert roman_to_int(numeral) == expected


# --- Valid: simple addition (no subtractive pairs) ---

@pytest.mark.parametrize("numeral, expected", [
    ('III', 3),
    ('VIII', 8),
    ('XXVI', 26),
], ids=["III", "VIII", "XXVI"])
def test_simple_addition(numeral, expected):
    assert roman_to_int(numeral) == expected


# --- Valid: subtractive notation ---

@pytest.mark.parametrize("numeral, expected", [
    ('IV', 4),
    ('IX', 9),
    ('XL', 40),
    ('XC', 90),
    ('CD', 400),
    ('CM', 900),
], ids=["IV", "IX", "XL", "XC", "CD", "CM"])
def test_subtractive_pairs(numeral, expected):
    assert roman_to_int(numeral) == expected


# --- Valid: complex numerals combining both rules ---

@pytest.mark.parametrize("numeral, expected", [
    ('MCMXCIV', 1994),
    ('LVIII', 58),
], ids=["MCMXCIV", "LVIII"])
def test_complex_numerals(numeral, expected):
    assert roman_to_int(numeral) == expected


# --- Invalid: malformed input ---

@pytest.mark.parametrize("numeral", [''], ids=["empty-string"])
def test_empty_string_raises(numeral):
    with pytest.raises(ValueError):
        roman_to_int(numeral)


@pytest.mark.parametrize("numeral", ['iv', 'mcm'], ids=["lowercase-simple", "lowercase-subtractive"])
def test_lowercase_raises(numeral):
    with pytest.raises(ValueError):
        roman_to_int(numeral)


@pytest.mark.parametrize("numeral", ['ABC', 'IZI'], ids=["non-roman-letters", "invalid-letter-embedded"])
def test_non_roman_characters_raise(numeral):
    with pytest.raises(ValueError):
        roman_to_int(numeral)


# --- Invalid: rule violations (well-formed characters, bad structure) ---

@pytest.mark.parametrize("numeral", ['IIVV', 'VX'], ids=["invalid-pair-order", "invalid-subtraction-VX"])
def test_invalid_ordering_raises(numeral):
    with pytest.raises(ValueError):
        roman_to_int(numeral)


@pytest.mark.parametrize("numeral", ['IIII', 'VV', 'LL'], ids=["invalid-repetition-I", "invalid-repetition-V", "invalid-repetition-L"])
def test_invalid_repetition_raises(numeral):
    with pytest.raises(ValueError):
        roman_to_int(numeral)