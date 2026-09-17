import pytest
from brackets import is_balanced


# --- Valid: simple pairs ---

@pytest.mark.parametrize("s", ['()', '[]', '{}'], ids=["parens", "square", "curly"])
def test_simple_pairs(s):
    assert is_balanced(s) is True


# --- Valid: nested ---

@pytest.mark.parametrize("s, expected", [
    ('([{}])', True),
    ('{[()()]}', True),
    ('((()))', True),
], ids=["all-types-nested", "mixed-nested-siblings", "deep-single-type"])
def test_nested(s, expected):
    assert is_balanced(s) is expected


# --- Valid: sequential (not nested) ---

@pytest.mark.parametrize("s", ['()[]{}', '()()()', '[]{}()'], ids=["all-types-sequential", "repeated-parens", "reordered-sequential"])
def test_sequential(s):
    assert is_balanced(s) is True


# --- Valid: brackets mixed with other characters ---

@pytest.mark.parametrize("s", [
    '(a+b)*[c-d]',
    'foo(bar[baz]{qux})',
    'no brackets here',
], ids=["arithmetic-expression", "nested-with-identifiers", "no-brackets-at-all"])
def test_mixed_with_other_characters(s):
    assert is_balanced(s) is True


# --- Invalid: unmatched opening ---

@pytest.mark.parametrize("s", ['(', '([)', '((()', '['], ids=["single-open-paren", "open-inside-mismatch", "extra-open-paren", "single-open-square"])
def test_unmatched_opening_raises(s):
    assert is_balanced(s) is False


# --- Invalid: unmatched closing ---

@pytest.mark.parametrize("s", [')', '())', '}', 'abc)'], ids=["single-close-paren", "extra-close-paren", "single-close-curly", "close-after-text"])
def test_unmatched_closing_raises(s):
    assert is_balanced(s) is False


# --- Invalid: wrong nesting order ---

@pytest.mark.parametrize("s", ['([)]', '{[}]', '(]}[)'], ids=["interleaved-parens-square", "interleaved-curly-square", "fully-scrambled"])
def test_wrong_nesting_order_raises(s):
    assert is_balanced(s) is False


# --- Invalid: mismatched pair type ---

@pytest.mark.parametrize("s", ['(]', '{)', '[}', '(}'], ids=["paren-open-square-close", "curly-open-paren-close", "square-open-curly-close", "paren-open-curly-close"])
def test_mismatched_pair_type_raises(s):
    assert is_balanced(s) is False


# --- Invalid: empty string edge case (explicit, since it's ambiguous) ---

def test_empty_string_is_balanced():
    assert is_balanced('') is True