from typing import Type, Union

from pagidantic.factory import PagidanticFactory
from pagidantic.paginator import Paginator


def pagidantic(
    object_list: Union[list, tuple, dict, set],
    page_limit: int = 10,
    start_page: int = 0,
):
    """
    This function create a paginator instance based on the type of the object list passed

    :param object_list: list, tuple, dict or set of objects to be paginated.
    :type object_list: Union[list, tuple, dict, set]
    :param page_limit: Number of items per page.
    :type page_limit: int, optional
    :param start_page: The page to start pagination from.
    :type start_page: int, optional
    :return: paginator instance
    :rtype: Paginator
    """
    factory = PagidanticFactory(type(object_list).__name__)
    paginator: Type[Paginator] = factory.get_paginator()
    return paginator(
        object_list=object_list,
        page_limit=page_limit,
        start_page=start_page,
    )
