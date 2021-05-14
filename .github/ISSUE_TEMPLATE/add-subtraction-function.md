---
name: Add subtraction function
about: Instructions on adding a subtraction function to the calculator package
title: "[FEATURE] Add subtraction function"
labels: enhancement, help wanted
assignees: ''

---

Use this checklist to tick off sub-tasks as you complete them.

- [ ] Add subtract function
- [ ] Import function in `__init__.py`
- [ ] Add subtract test


## Instructions

###  Create branch

Create a new `subtract` branch to work in
### Add subtraction function

Create a new `subtract.py` file in the `pythoncalculator/` directory.

```python
def subtract(x, y)
    return x - y
```

Open the `pythoncalculator/__init__.py` file and add the following line of code:

```python
from .subtract import subtract 
```

### Add subtraction test

Create a new `test_subtract.py` file in the `tests/` directory.

Add the following code and save:

```python
from pythoncalculator import subtract


def test_subtract():
    assert subtract(1, 3) == -2
```


