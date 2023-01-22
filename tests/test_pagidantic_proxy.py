import pytest
from conftest import dict_to_list

from pagidantic import PagidanticDict, PagidanticSet


class TestPaginatorDictProxy:
    """Tests for Test PagidanticDict"""

    def test_init(self, paginator_dict_proxy: PagidanticDict, dict_data: dict):
        """Validate init assigment."""
        assert paginator_dict_proxy.object_list == dict_to_list(dict_data)
        assert paginator_dict_proxy.page_limit == 5
        assert paginator_dict_proxy.start_page == 0

    def test_invalid_object_list(self):
        """Validate object_list param."""
        with pytest.raises(TypeError):
            PagidanticDict([1, 2, 3])
        with pytest.raises(TypeError):
            PagidanticDict({1, 2, 3})
        with pytest.raises(TypeError):
            PagidanticDict((1, 2, 3))


class TestPaginatorSetProxy:
    """Tests for Test PagidanticSet"""

    def test_init(self, paginator_set_proxy: PagidanticSet):
        """Validate init assigment."""
        assert paginator_set_proxy.object_list == [1, 2, 3, 4, 5, 6, 7, 8]
        assert paginator_set_proxy.page_limit == 3
        assert paginator_set_proxy.start_page == 0

    def test_invalid_object_list(self):
        """Validate object_list param."""
        with pytest.raises(TypeError):
            PagidanticSet([1, 2, 3])
        with pytest.raises(TypeError):
            PagidanticSet({"a": 1})
        with pytest.raises(TypeError):
            PagidanticSet((1, 2, 3))
