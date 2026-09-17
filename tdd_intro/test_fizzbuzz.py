import pytest
from fizzbuzz import fizzbuzz


@pytest.mark.parametrize("n, expected", [
    (1, '1'),
    (2, '2'),
    (4, '4'),
], ids=["one", "two", "four"])
def test_regular_numbers(n, expected):
    assert fizzbuzz(n) == expected


@pytest.mark.parametrize("n", [3, 6, 9], ids=["three", "six", "nine"])
def test_multiples_of_three_return_fizz(n):
    assert fizzbuzz(n) == 'Fizz'


@pytest.mark.parametrize("n", [5, 10, 20], ids=["five", "ten", "twenty"])
def test_multiples_of_five_return_buzz(n):
    assert fizzbuzz(n) == 'Buzz'


@pytest.mark.parametrize("n", [15, 30, 45], ids=["fifteen", "thirty", "forty-five"])
def test_multiples_of_fifteen_return_fizzbuzz(n):
    assert fizzbuzz(n) == 'FizzBuzz'
