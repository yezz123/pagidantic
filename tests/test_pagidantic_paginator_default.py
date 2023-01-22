import pytest
from pydantic import ValidationError

from pagidantic import Paginator, pagidantic


class TestDefaultPaginator:
    """Tests for Paginator object."""

    def test_pagidantic_init(self):
        """Test pagidantic function initial values."""
        assert pagidantic(object_list=[], page_limit=5, start_page=0)
        assert pagidantic(object_list={1, "a"})
        assert pagidantic(object_list=(1, "a"))
        assert pagidantic(object_list={"a": 1})
        assert pagidantic(object_list=[], page_limit=True, start_page=0)
        assert pagidantic(object_list=[], page_limit=True, start_page=False)
        assert pagidantic(object_list=[], page_limit=False, start_page="0")
        with pytest.raises(TypeError):
            assert pagidantic(object_list=None, page_limit=5, start_page=0)
        with pytest.raises(TypeError):
            assert pagidantic(object_list="", page_limit=5, start_page=0)
        with pytest.raises(TypeError):
            assert pagidantic(object_list=0, page_limit=5, start_page=0)
        with pytest.raises(TypeError):
            assert pagidantic(object_list=True, page_limit=5, start_page=0)
        with pytest.raises(ValidationError):
            assert pagidantic(object_list=[], page_limit="str", start_page=0)
        with pytest.raises(ValidationError):
            assert pagidantic(object_list=[], page_limit=3, start_page="str")
        with pytest.raises(ValidationError):
            assert pagidantic(object_list=[], page_limit=None, start_page=0)
        with pytest.raises(ValidationError):
            assert pagidantic(object_list=[], page_limit=None, start_page=None)
        with pytest.raises(ValidationError):
            assert pagidantic(object_list=[], page_limit=3, start_page=None)

    def test_init(self, paginator: Paginator, list_of_int: list[int]):
        """Validate init assigment."""
        assert paginator.object_list == list_of_int
        assert paginator.page_limit == 10
        assert paginator.start_page == 0

    def test_init_valid_object_list(self):
        """Validate object list."""
        paginator_list = pagidantic([1, 2, 3])
        assert paginator_list.object_list == [1, 2, 3]
        paginator_tuple = pagidantic((1, 2, 3))
        assert paginator_tuple.object_list == [1, 2, 3]
        paginator_dict = pagidantic({"a": 1, "b": 2})
        assert paginator_dict.object_list == [
            {
                "a": 1,
            },
            {"b": 2},
        ]
        paginator_set = pagidantic({1, 2, 3})
        assert paginator_set.object_list == [1, 2, 3]

    def test_response(self, paginator: Paginator):
        """Validate current object data."""
        expected = {
            "total_pages": 4,
            "data": list(range(1, 11)),
            "page_number": 0,
            "has_next": True,
            "has_previous": False,
        }
        assert paginator.response == expected

    def test_get_next(self, paginator: Paginator):
        """Validate if response data is changed after calling next page data."""
        paginator.get_next()
        expected = {
            "total_pages": 4,
            "data": list(range(11, 21)),
            "page_number": 1,
            "has_next": True,
            "has_previous": True,
        }
        assert paginator.response == expected

    def test_get_previous(self):
        """Validate if response data is changed after calling next previous data."""
        p = pagidantic(object_list=[1, 2, 3, 4, 5], page_limit=2, start_page=1)
        p.get_previous()
        expected = {
            "total_pages": 2,
            "data": list(range(1, 3)),
            "page_number": 0,
            "has_next": True,
            "has_previous": False,
        }
        assert p.response == expected

    def test_get_current_data(self, paginator: Paginator):
        """
        Validate if page\'s object list is changed after multiple next/previous page calls.
        """
        paginator.get_next()
        paginator.get_next()
        assert paginator.page.object_list == list(range(21, 31))
        paginator.get_previous()
        assert paginator.page.object_list == list(range(11, 21))
        paginator.get_previous()
        assert paginator.page.object_list == list(range(1, 11))
        paginator.get_previous()
        paginator.get_previous()
        paginator.get_previous()
        paginator.get_previous()
        assert paginator.page.object_list == list(range(1, 11))

    def test_get_previous_from_first_page(self, paginator: Paginator):
        """
        Check if response data is unchanged after previous page call while start_page is set to 0.
        """
        paginator.get_previous()
        expected = {
            "total_pages": 4,
            "data": list(range(1, 11)),
            "page_number": 0,
            "has_next": True,
            "has_previous": False,
        }
        assert paginator.response == expected

    def test_get_next_previous(self, paginator: Paginator):
        """Check if response data is changed correctly after multiple next/previous page calls."""
        paginator.get_next()
        paginator.get_next()
        paginator.get_next()
        expected = {
            "total_pages": 4,
            "data": list(range(31, 41)),
            "page_number": 3,
            "has_next": True,
            "has_previous": True,
        }
        assert paginator.response == expected
        paginator.get_previous()
        expected = {
            "total_pages": 4,
            "data": list(range(21, 31)),
            "page_number": 2,
            "has_next": True,
            "has_previous": True,
        }
        assert paginator.response == expected

    def test_get_page_response(self, paginator: Paginator):
        """Validate if requested page data is correct."""
        response = paginator.get_page_response(4)
        expected = {
            "total_pages": 4,
            "data": list(range(41, 51)),
            "page_number": 4,
            "has_next": False,
            "has_previous": True,
        }
        assert response == expected

    def test_get_page_response_page_number(self, paginator: Paginator):
        """Validate page_number param in get_page_response method."""
        assert paginator.get_page_response(1)
        assert paginator.get_page_response(True)
        assert paginator.get_page_response(False)
        with pytest.raises(TypeError):
            assert paginator.get_page_response("test")
        with pytest.raises(TypeError):
            assert paginator.get_page_response("1")

    def test_total(self, paginator: Paginator):
        """Validate total property."""
        assert paginator.total == 50

    def test_total_pages(self, paginator: Paginator):
        """Validate total_pages property."""
        assert paginator.total_pages == 4

    def test_page_range(self, paginator: Paginator):
        """Validate page_range property."""
        assert paginator.page_range == range(5)

    def test_get_objects(self, paginator: Paginator):
        """Validate get_objects method with given page number will return expected object_list."""
        assert paginator.get_objects(1) == list(range(11, 21))

    def test_get_objects_page_number(self, paginator: Paginator):
        """Validate page_number param in get_objects method."""
        assert paginator.get_objects(1)
        assert paginator.get_objects(True)
        assert paginator.get_objects(False)
        with pytest.raises(TypeError):
            assert paginator.get_objects("test")
        with pytest.raises(TypeError):
            assert paginator.get_objects("1")

    def test_has_next(self, paginator: Paginator):
        """Check if paginator have next page."""
        assert paginator.has_next

    def test_not_has_next(self):
        """Check if paginator does not have next page."""
        p = pagidantic(object_list=[1, 2, 3], page_limit=5)
        assert not p.has_next

    def test_has_previous(self):
        """Check if paginator have previous page."""
        p = pagidantic(object_list=[1, 2, 3, 4, 5], page_limit=2, start_page=1)
        assert p.has_previous

    def test_not_has_previous(self, paginator: Paginator):
        """Check if paginator does not have previous page."""
        assert not paginator.has_previous

    def test_iter(self, paginator: Paginator):
        """Check __iter__ method."""
        for current_page in paginator:
            expected = {
                "total_pages": 4,
                "data": current_page.object_list,
                "page_number": current_page.page_number,
                "has_next": current_page.has_next(),
                "has_previous": current_page.has_previous(),
            }
            assert paginator.response == expected

    def test_page(self, paginator: Paginator):
        """Check if Page creates expected data."""
        page = paginator._page(
            object_list=list(range(1, 11)), page_number=0, paginator=paginator
        )
        assert page.object_list == list(range(1, 11))
        assert page.has_next()
        assert not page.has_previous()
        assert page.count == 10

    def test_page_count(self):
        """Validate Page 'count' with different start_page value while iterating over paginator."""
        object_list = [1, 2, 3, 4, 5]
        limit = 2
        paginator = pagidantic(object_list=object_list, page_limit=limit)
        for index, page in enumerate(paginator):
            if index == 2:  # last page in this example
                assert page.count == 1
            else:
                assert page.count == 2

        paginator = pagidantic(object_list=object_list, page_limit=limit, start_page=1)
        for index, page in enumerate(paginator):
            if index == 1:  # last page in this example
                assert page.count == 1
            else:
                assert page.count == 2
        paginator = pagidantic(object_list=object_list, page_limit=limit, start_page=2)
        for page in paginator:
            assert page.count == 1
