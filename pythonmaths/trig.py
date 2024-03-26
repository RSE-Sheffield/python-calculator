"""Basic trigonometry functions."""


def hypotenuse(a: int | float, b: int | float) -> float:
    """
    Calculate the length of the hypotenuse of a right-angled triangle with sides a and b.

    Parameters
    ----------
    a : int | float
        Length of side `a`.
    b : int | float
        Legnt of side `b`.

    Returns
    -------
    float
        Square root of the sum of `a` and `b`.

    Examples
    --------
    >>> from pythonmat import trig
    >>> trig(3, 4)
      5.0
    """
    if a > 0.0 and b > 0.0:
        return (a**2 + b**2) ** 0.5  # type: ignore[no-any-return]
    raise ValueError("Triangles can not have negative lengths.")
