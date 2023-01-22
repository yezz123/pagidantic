![Logo](https://raw.githubusercontent.com/yezz123/pagidantic/main/.github/logo.png)

<p align="center">
    <em>Pagination using Pydantic. Easy to use, lightweight, and easy to integrate with existing projects ✨</em>
</p>

<p align="center">
<a href="https://github.com/yezz123/pagidantic/actions/workflows/test.yml" target="_blank">
    <img src="https://github.com/yezz123/pagidantic/actions/workflows/test.yml/badge.svg" alt="Test">
</a>
<a href="https://codecov.io/gh/yezz123/pagidantic">
    <img src="https://codecov.io/gh/yezz123/pagidantic/branch/main/graph/badge.svg"/>
</a>
<a href="https://pypi.org/project/pagidantic" target="_blank">
    <img src="https://img.shields.io/pypi/v/pagidantic?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/pagidantic" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/pagidantic.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

## Requirements

A recent and currently supported version of Python (right now, <a href="https://www.python.org/downloads/" class="external-link" target="_blank">Python supports versions 3.9 and above</a>).

As **Pagidantic** is based on **Pydantic**, it requires them. They will be automatically installed when you install **Pagidantic**.

## Installation

You can add Pagidantic in a few easy steps. First of all, install the dependency:

```shell
$ pip install pagidantic

---> 100%

Successfully installed pagidantic
```

## Usage

```py
from pagidantic import pagidantic

# Generate a list here: https://json-generator.com/
object_list = [...]  # list of objects


pagination = pagidantic(object_list, page_limit=2, start_page=0)

# get current returned page
def get_current_page():
    return pagination.response


# get next pageg
def get_next_page():
    return pagination.get_next()


# get previous page
def get_previous_page():
    return pagination.get_previous()


# get page by number
def get_page_by_number():
    return pagination.get_page_response(page_number=0)


# get total pages
def get_total_pages():
    return pagination.total_pages


# Count total objects
def count_total_objects():
    return pagination.total
```

## Development 🚧

### Setup environment 📦

You should create a virtual environment and activate it:

```bash
python -m venv venv/
```

```bash
source venv/bin/activate
```

And then install the development dependencies:

```bash
# Install dependencies
pip install -e .[test,lint]
```

### Run tests 🌝

You can run all the tests with:

```bash
bash scripts/test.sh
```

> Note: You can also generate a coverage report with:

```bash
bash scripts/test_html.sh
```

### Format the code 🍂

Execute the following command to apply `pre-commit` formatting:

```bash
bash scripts/format.sh
```

Execute the following command to apply `mypy` type checking:

```bash
bash scripts/lint.sh
```

**NOTE**: We need to Fix more than 90+ errors in the codebase. If you want to contribute, please fix the errors and send a PR.

## License

This project is licensed under the terms of the MIT license.
