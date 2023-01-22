from pagidantic.paginator import Paginator


class PagidanticSet(Paginator):
    """
    Initialize a Paginator for paginating a set.

    :param object_list: The set to be paginated.
    :type object_list: dict
    :param page_limit: Number of items per page.
    :type page_limit: int, optional
    :param start_page: The page to start pagination from.
    :type start_page: int, optional
    """

    def __init__(self, object_list: set, page_limit: int = 10, start_page: int = 0):
        self.object_list = object_list
        super().__init__(
            object_list=self._set_to_list(),
            page_limit=page_limit,
            start_page=start_page,
        )

    def _set_to_list(self) -> list[set]:
        """Transform set to list of sets."""
        if not isinstance(self.object_list, set):
            raise TypeError(f"Expected set object, not {type(self.object_list)}")
        return list(self.object_list)
