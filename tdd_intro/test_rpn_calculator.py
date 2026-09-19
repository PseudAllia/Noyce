from rpn_calculator import evaluate


def test_single_number_returns_itself():
    assert evaluate("3") == 3


# Next steps to add, one at a time, each driven by a failing test first:
#
def test_addition():
    assert evaluate("3 4 +") == 7
#
def test_subtraction():
    assert evaluate("10 4 -") == 6
#
def test_multiplication():
    assert evaluate("3 4 *") == 12
#
def test_division():
    assert evaluate("12 4 /") == 3
#
def test_division_produces_a_float():
    assert evaluate("7 2 /") == 3.5
#
def test_chained_operations_use_a_stack():
    assert evaluate("5 1 2 + 4 * + 3 -") == 14  # 5 + ((1+2) * 4) - 3
#
def test_division_by_zero_raises():
    import pytest
    with pytest.raises(ZeroDivisionError):
        evaluate("1 0 /")
#
def test_too_few_operands_raises():
    import pytest
    with pytest.raises(ValueError):
        evaluate("+")
#
def test_too_many_operands_left_over_raises():
    import pytest
    with pytest.raises(ValueError):
        evaluate("1 2 3 +")
