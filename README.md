# python-math

Basic math functions in Python

## Working in a Conda environment

Make sure you have [Conda][conda] or [Miniconda][miniconda] installed.

### Create conda environment

```bash
conda create --name python-calculator python=3.8
```

### Activate conda environment

```bash
conda activate python-calculator
```

### Install the package and dependencies

```bash
pip install .
```

## Running tests

Make sure you have activated your virtual environment environment. Then run:

```bash
pytest
```

[conda]: https://conda.io/projects/conda/en/latest/user-guide/install/index.html
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
