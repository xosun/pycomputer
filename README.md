# Setup

## Prerequisites:

- Python 3.7+

## Steps

### Create virtual environment

`python -m venv .venv`

### Activate it

#### On Unix-like systems

`source .venv/bin/activate`

#### On Windows

`source .venv\Scripts\activate`

### Install dependencies

`pip install -r requirements.txt`

# Developing

### Formatting

#### Format with `black` for python

`black .`

#### And `mdformat` for markdown

`mdformat .`

### Unit testing

#### Test with `pytest`

`pytest`

### Updating requirements.txt

#### To update `requirments.txt` file with any new dependencies, run:

`pip freeze > requirements.txt`
