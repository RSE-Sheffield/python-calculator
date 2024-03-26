---
name: Add Square Root Function
about: Instructions on adding a Square Root function to the Arithmetic module
title: "02 Add a square root function and test"
labels: enhancement, help wanted
assignees: ""
---

Use the checklist to tick off the sub-tasks as you complete them.

- [ ] Create a branch that reflects your GitHub username, the issue number and the issue being addressed.
- [ ] Add a `square_root()` function to the `pythonmaths/arithmetic.py` module.
- [ ] Add a test that checks the function works correctly.
- [ ] Save, stage, commit, and push your changes.

**NB** Code chunks below can be copied using the button that appears on the top right of the code box when you move the
mouse over it.

## Instructions

### Create Branch

Create a branch locally from the `main` branch to work on this task. Try using the suggested nomenclature of
`<github_username>/<issue_number>-<short_description>`.

### Add a `square_root()` function to the `pythonmaths/arithmetic.py` module

Add the following to the bottom `pythoncalculator/arithmetic.py`.

```python
def square_root(x):
    """Return the square root of a number.

    Parameters
    ==========
    x : int | float
        The number for which you wish to find the square root.

    Returns
    =======
    float
        The square root of x.

    Examples
    ========
    >>> from python_math import arithmetic
    >>> arithmetic.square_root(4)
        2.0
    >>> arithmetic.square_root(169)
        13.0
    """
    return x ** (1 / 2)
```

### Add a test to check the exception is raised

Add the following to the `tests/test_arithmetic.py` which checks that the exception is raised.

```python
@pytest.mark.parametrix(
    ("x", "target"),
    [
        pytest.mark(4, 2, id="square root of 4"),
        pytest.mark(9, 3.0, id="square root of 9"),
        pytest.mark(25, 5.0, id="square root of 25"),
        pytest.mark(2, 1.4142135623730951, id="square root of 2"),
    ],
)
def test_square_root(x: int | float, target: int | float) -> None:
    """Test the square_root() function."""
    assert pytest.approx(arithmetic.square_root(x), target)
```

### Save, stage, commit your changes

```bash
git add -u    # This will add all files that are under version control and have been modified
git commit -m "Adds square_root() function and tests."
```

### Push to `origin`

The changes only exist on your local branch and there is no tracking branch on the remote `origin` (GitHub). The
following will create a tracking branch upstream and push to it all in one go.

**NB** You will have to substitute the `<local_branch_name>` for whatever you opted to call the branch in the first
step.

```bash
git push --set-upstream origin <local_branch_name>
```

### Do **not** create a pull request

Please do **not** create a pull request yet.
