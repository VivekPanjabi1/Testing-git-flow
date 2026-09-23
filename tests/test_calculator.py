import pytest

from calculator import add, divide, multiply, subtract, calculate


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 7) == 21


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)


def test_calculate_dispatch():
    assert calculate("divide", 8, 4) == 2
    with pytest.raises(ValueError, match="Unsupported operation"):
        calculate("mod", 1, 1)
