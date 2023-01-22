from pagidantic.paginator import Paginator


class PagidanticDict(Paginator):
    """
    Initialize a Paginator for paginating a dictionary.

    :param object_list: The dictionary to be paginated.
    :type object_list: dict
    :param page_limit: Number of items per page.
    :type page_limit: int, optional
    :param start_page: The page to start pagination from.
    :type start_page: int, optional
    """

    def __init__(self, object_list: dict, page_limit: int = 10, start_page: int = 0):
        self.object_list = object_list
        super().__init__(
            object_list=self._dict_to_list(),
            page_limit=page_limit,
            start_page=start_page,
        )

    def _dict_to_list(self) -> list[dict]:
        """Transform dict to list of dicts."""
        if not isinstance(self.object_list, dict):
            raise TypeError(f"Expected dict object, not {type(self.object_list)}")
        return [{k: v} for k, v in self.object_list.items()]
