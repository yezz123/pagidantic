import pytest

from pagidantic import PagidanticDict, PagidanticSet, Paginator, pagidantic


def dict_to_list(dict_object: dict) -> list[dict]:
    """Transform dict to list of dicts."""
    return [{k: v} for k, v in dict_object.items()]


@pytest.fixture()
def list_of_int() -> list[int]:
    """Generate list of integers."""
    return list(range(1, 51))


@pytest.fixture()
def list_of_dict() -> list[dict]:
    """Generate list of dictionary."""
    d = {f"{x}": x for x in range(1, 21)}
    return dict_to_list(d)


@pytest.fixture()
def dict_data() -> dict:
    """Generate single dictionary."""
    return {f"{x}": x for x in range(1, 11)}


@pytest.fixture()
def paginator(list_of_int) -> Paginator:
    """Return paginator object with list of integers as input."""
    return pagidantic(object_list=list_of_int)


@pytest.fixture()
def second_paginator(list_of_dict) -> Paginator:
    """Return paginator object with list of dictionary as input, start page set to 1, limit 3."""
    return pagidantic(list_of_dict, page_limit=3, start_page=1)


@pytest.fixture()
def paginator_dict_proxy(dict_data) -> PagidanticDict:
    """Return PaginatorDictProxy object with dictionary as input."""
    return PagidanticDict(dict_data, page_limit=5)


@pytest.fixture()
def paginator_set_proxy() -> PagidanticSet:
    """Return PaginatorSetProxy object with set as input, limit set to 3."""
    return PagidanticSet({1, 2, 3, 4, 5, 6, 7, 8}, page_limit=3)
