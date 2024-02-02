"""Tests of the trig module."""

import pytest

from pythonmaths import trig


@pytest.mark.parametrize(  # type: ignore[misc]
    ("a", "b", "hypotenuse"),
    [
        pytest.param(3, 4, 5.0, id="3-4-5 triangle"),
        pytest.param(1, 2, 2.23606797749979, id="1-2-? triangle"),
    ],
)
def test_hypotenuse(a: int | float, b: int | float, hypotenuse: float) -> None:
    """Test the hypotenuse function."""
    c = trig.hypotenuse(a, b)
    print(f"{c=}")
    assert trig.hypotenuse(a, b) == pytest.approx(hypotenuse)


@pytest.mark.parametrize(  # type: ignore[misc]
    ("a", "b"),
    [
        pytest.param(-3, 4, id="a is negative"),
        pytest.param(3, -4, id="b is negative"),
    ],
)
def test_hypotenuse_negative_length_valueerror(a: int | float, b: int | float) -> None:
    """Test ValueError raised if either parameter is negative."""
    with pytest.raises(ValueError, match="Triangles can not have negative lengths."):
        trig.hypotenuse(a, b)
