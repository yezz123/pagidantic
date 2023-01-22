from typing import Sequence


class Page:
    """
    A Page object, which contains a list of objects and some additional information such as the current page number and
    the paginator instance.
    """

    def __init__(self, object_list: Sequence, page_number: int, paginator):
        """
        Initialize a Page object with a list of objects, the current page number, and a paginator instance.

        :param object_list: A list of objects to be paginated.
        :type object_list: Sequence
        :param page_number: The current page number.
        :type page_number: int
        :param paginator: The paginator instance.
        :type paginator: object
        """
        self.object_list = object_list
        self.page_number = page_number
        self.paginator = paginator

    def has_next(self) -> bool:
        """
        Check if paginator has next page.

        :return: True if the paginator has a next page, False otherwise.
        :rtype: bool
        """
        return self.page_number < self.paginator.total_pages

    def has_previous(self) -> bool:
        """
        Check if paginator has previous page.

        :return: True if the paginator has a previous page, False otherwise.
        :rtype: bool
        """
        return self.page_number > 0

    @property
    def count(self):
        """
        Return a number of page objects.

        :return: The number of objects in the current page.
        :rtype: int
        """
        return len(self.object_list)
