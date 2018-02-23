import pytest

from Fibonacci import Fibonacci

@pytest.fixture
def fibonacci():
    return Fibonacci()

def test_zero_for_first_number(fibonacci):
    assert 0 == get_number_at_index(fibonacci, 0)

def test_one_for_second_number(fibonacci):
    assert 1 == get_number_at_index(fibonacci, 1)

def test_one_for_third_number(fibonacci):
    assert 1 == get_number_at_index(fibonacci, 2)

def test_two_for_fourth_number(fibonacci):
    assert 2 == get_number_at_index(fibonacci, 3)

def test_three_for_fifth_number(fibonacci):
    assert 3 == get_number_at_index(fibonacci, 4)

def test_five_for_sixth_number(fibonacci):
    assert 5 == get_number_at_index(fibonacci, 5)

def test_huge_number_for_fiftieth_number(fibonacci):
    assert 10000000000 > get_number_at_index(fibonacci, 49)

def get_number_at_index(fibonacci, index):
    return fibonacci.generate(index + 1)[index]