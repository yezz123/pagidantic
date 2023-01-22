from pagidantic import PagidanticDict, PagidanticFactory, PagidanticSet, Paginator


def get_paginator(object_list):
    factory = PagidanticFactory(type(object_list).__name__)
    return factory.get_paginator()


class TestPaginatorFactory:
    """Tests for PaginatorFactory."""

    def test_factory_result(self):
        """
        Test if expected paginator class/subclass is returned based on object_list input type.
        """
        object_list = [1, 2]
        assert get_paginator(object_list) == Paginator
        object_list = (1, 2, 3)
        assert get_paginator(object_list) == Paginator
        object_list = {"a": 1, "b": 3}
        assert get_paginator(object_list) == PagidanticDict
        object_list = {1, "b", True}
        assert get_paginator(object_list) == PagidanticSet
