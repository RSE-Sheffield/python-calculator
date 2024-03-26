"""Test the arithmetic functions."""

import pytest

from pythonmaths import arithmetic


@pytest.mark.parametrize(  # type: ignore[misc]
    ("x", "y", "expected"),
    [
        pytest.param(1, 3, 4, id="Add two positive integers"),
        pytest.param(1, -3, -2, id="Add a positive and negative integer"),
        pytest.param(-1, -3, -4, id="Add two negative integers"),
        pytest.param(10, 0, 10, id="Add zero to integer"),
        pytest.param(0, 10, 10, id="Add integer to zero"),
        pytest.param(0.1, 10.34, 10.44, id="Add two positive floats"),
    ],
)
def test_add(x: int | float, y: int | float, expected: int | float) -> None:
    """Test the add function."""
    assert arithmetic.add(x, y) == pytest.approx(expected)


@pytest.mark.parametrize(  # type: ignore[misc]
    ("x", "y", "expected"),
    [
        pytest.param(10, 2, 8, id="Subtract two positive integers"),
        pytest.param(1, -3, 4, id="Subtract negative integer from positive integer"),
        pytest.param(-1, -3, 2, id="Subtract two negative integers"),
        pytest.param(10, 0, 10, id="Subtract zero from integer"),
        pytest.param(1.6, 1.2, 0.4, id="Subtract two positive integers"),
        pytest.param(-1.6, 1.2, -2.8, id="Subtract positive integer from negative"),
    ],
)
def test_subtract(x: int | float, y: int | float, expected: int | float) -> None:
    """Test the subtract function."""
    assert arithmetic.subtract(x, y) == pytest.approx(expected)


@pytest.mark.parametrize(  # type: ignore[misc]
    ("x", "y", "expected"),
    [
        pytest.param(10, 2, 20, id="Multiply two positive integers"),
        pytest.param(1, -3, -3, id="Multiply positive and integers"),
        pytest.param(-1, -3, 3, id="Multiply two negative integers"),
        pytest.param(10, 0, 0, id="Multiply by zero"),
        pytest.param(1.5, 2.6, 3.9, id="Multiply two positive floats"),
    ],
)
def test_multiply(x: int | float, y: int | float, expected: int | float) -> None:
    """Test the multiply function."""
    assert arithmetic.multiply(x, y) == pytest.approx(expected)


@pytest.mark.parametrize(  # type: ignore[misc]
    ("x", "y", "expected"),
    [
        pytest.param(10, 2, 5, id="Two positive integers"),
        pytest.param(1, -2, -0.5, id="One positive, on negative integer"),
        pytest.param(-5, 2, -2.5, id="Two negative integers"),
        pytest.param(-9, -3, 3.0, id="Add zero to integer"),
    ],
)
def test_divide(x: int | float, y: int | float, expected: int | float) -> None:
    """Test the divide function."""
    assert arithmetic.divide(x, y) == pytest.approx(expected)


@pytest.mark.parametrize(  # type: ignore[misc]
    ("x", "y"),
    [
        pytest.param(10, 0, id="Divide by zero"),
    ],
)
def test_divide_zerodivision_error(x: int | float, y: int | float) -> None:
    """Test ZeroDivision is raised."""
    with pytest.raises(ZeroDivisionError):
        arithmetic.divide(x, y)
