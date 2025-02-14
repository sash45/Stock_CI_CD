import pytest

def test_example():
    """A dummy test to check pytest integration."""
    assert 1 + 1 == 2

def add_numbers(a, b):
    return a + b

def test_add_numbers():
    """Test for the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

