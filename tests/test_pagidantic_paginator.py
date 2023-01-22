from pagidantic import Paginator


class TestListOfDictPaginator:
    """Tests for paginator object with list of dict as input."""

    def test_init(self, second_paginator: Paginator, list_of_dict: list[dict]):
        assert second_paginator.object_list == list_of_dict
        assert second_paginator.page_limit == 3
        assert second_paginator.start_page == 1

    def test_response(self, second_paginator: Paginator):
        expected = {
            "total_pages": 6,
            "data": [{"4": 4}, {"5": 5}, {"6": 6}],
            "page_number": 1,
            "has_next": True,
            "has_previous": True,
        }
        assert second_paginator.response == expected
