# python-calculator
Basic calculator functions in python


## Working in a conda environment

Make sure you have [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed.
### Create conda environment

```
conda create --name python-calculator python=3.8
```

### Activate conda environment


```
conda activate python-calculator
```


### Install dependencies


```
python -m pip install -r requirements.txt
```

## Install the package

Make sure you have activated your conda environment.

```
conda activate python-calculator
```

Then run:

```
pip install .
```

## Running tests

Make sure you have activated your conda environment. Then run:

```
python -m pytest
```
