import pytest
from leap_year import is_leap_year


# --- Not divisible by 4: never leap ---

@pytest.mark.parametrize("year", [2023, 2021, 1999], ids=["2023", "2021", "1999"])
def test_not_divisible_by_four_is_not_leap(year):
    assert is_leap_year(year) is False


# --- Divisible by 4, not by 100: leap ---

@pytest.mark.parametrize("year", [2024, 2020, 1996], ids=["2024", "2020", "1996"])
def test_divisible_by_four_not_hundred_is_leap(year):
    assert is_leap_year(year) is True


# --- Divisible by 100, not by 400: not leap (the classic trap) ---

@pytest.mark.parametrize("year", [1900, 2100, 1800], ids=["1900", "2100", "1800"])
def test_divisible_by_hundred_not_four_hundred_is_not_leap(year):
    assert is_leap_year(year) is False


# --- Divisible by 400: leap after all ---

@pytest.mark.parametrize("year", [2000, 1600, 2400], ids=["2000", "1600", "2400"])
def test_divisible_by_four_hundred_is_leap(year):
    assert is_leap_year(year) is True