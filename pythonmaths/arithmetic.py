"""Functions for basic arithmetic."""


def add(x: int | float, y: int | float) -> float:
    """
    Add two numbers together.

    Parameters
    ----------
    x : int | float
        The first number to be added.
    y : int | float
        The second number to be added.

    Returns
    -------
    float
        The sum of `x` and `y`.

    Examples
    --------
    >>> from python_math import arithmetic
    >>> arithmetic.add(4, 5)
      9
    >>> arithmetic.add(1.45, 1.89)
      3.34
    """
    return x + y


def divide(x: int | float, y: int | float) -> float:
    """
    Divide x by y.

    Parameters
    ----------
    x : int | float
        Numerator for division.
    y : int | float
        Denominator for division.

    Returns
    -------
    float
        The result of dividing `x` by `y`.

    Examples
    --------
    >>> from python_math import arithmetic
    >>> arithmetic.divide(10, 2)
        5.0
    >>> arithmetic.divide(5, 2)
        2.5
    """
    return x / y


def multiply(x: int | float, y: int | float) -> float:
    """
    Multiply x by y.

    Parameters
    ----------
    x : int | float
        First number to multiply.
    y : int | float
        Second number to multiply.

    Returns
    -------
    float
        The product of `x` and `y`.

    Examples
    --------
    >>> from python_math import arithmetic
    >>> arithmetic.multiply(10, 2)
        20.0
    >>> arithmetic.multiply(2.5, 2)
        5.0
    """
    return x * y


def subtract(x: int | float, y: int | float) -> float:
    """
    Subtract y from x.

    Parameters
    ----------
    x : int | float
        First number from which y is subtract.
    y : int | float
        Second number to subtract from x.

    Returns
    -------
    float
        The result of subtracting `y` from `x`.

    Examples
    --------
    >>> from python_math import arithmetic
    >>> arithmetic.subtract(10, 2)
        8.0
    >>> arithmetic.subtract(5, 2.5)
        2.5
    """
    return x - y
