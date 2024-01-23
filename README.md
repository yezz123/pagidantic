![Logo](https://raw.githubusercontent.com/yezz123/pagidantic/main/.github/logo.png)

<p align="center">
    <em>Pagination using Pydantic. Easy to use, lightweight, and easy to integrate with existing projects ✨</em>
</p>

<p align="center">
<a href="https://github.com/yezz123/pagidantic/actions/workflows/ci.yml" target="_blank">
    <img src="https://github.com/yezz123/pagidantic/actions/workflows/ci.yml/badge.svg" alt="Continuous Integration">
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
<a href="https://pydantic.dev" target="_blank">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json" alt="Pydantic v2">
</a>
</p>

## Requirements

A recent and currently supported version of Python (right now, <a href="https://www.python.org/downloads/" class="external-link" target="_blank">Python supports versions 3.9 and above</a>).

As **Pagidantic** is based on **Pydantic**, it requires them. They will be automatically installed when you install **Pagidantic**.

**Notes**: we support only Pydantic v2. If you are using Pydantic v1, you can install it using `pip install pagidantic==1.1.0`

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

### Format the code 🍂

Execute the following command to apply `pre-commit` formatting:

```bash
bash scripts/format.sh
```

Execute the following command to apply `mypy` type checking:

```bash
bash scripts/lint.sh
```

## License

This project is licensed under the terms of the MIT license.
