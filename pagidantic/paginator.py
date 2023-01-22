import math
from functools import cached_property
from typing import Sequence, Union

from pydantic.dataclasses import dataclass

from pagidantic.page import Page


@dataclass
class Paginator:
    """
    Objects paginator. Should be initialised using paginate function.

    Arguments:
        :object_list: list of sequential objects that will be split across pages.
        :page_limit: number of objects per page.
        :start_page: number of page from which paginator will start.
    """

    object_list: Union[list, tuple, dict, set]
    page_limit: int = 10
    start_page: int = 0

    def __post_init_post_parse__(self):
        """Executed after initial validation. Set initial page."""
        self.page: Page = self._page(
            object_list=self.get_objects(self.start_page),
            page_number=self.start_page,
            paginator=self,
        )

    def __iter__(self):
        """Iterate over paginator pages. Every iteration updates paginator page object."""
        for _ in self.page_range:
            yield self.page
            self.get_next()

    def get_objects(self, page_number: int) -> Sequence:
        """Retrieve page list of data."""
        if not isinstance(page_number, int):
            raise TypeError(f"{page_number} expected to be int.")
        n = self.page_limit * page_number
        return self.object_list[n : n + self.page_limit]

    @property
    def response(self):
        """Retrieve response result property."""
        data = {
            "data": self.page.object_list,
            "page_number": self.page.page_number,
            "has_next": self.has_next,
            "has_previous": self.has_previous,
        }
        return self._create_response(**data)

    @property
    def has_next(self) -> bool:
        """Page's "has next" method."""
        return self.page.has_next()

    @property
    def has_previous(self) -> bool:
        """Page's "has previous" method."""
        return self.page.has_previous()

    def get_next(self) -> None:
        """Get next page. Overrides paginator\'s page attribute"""
        if self.has_next:
            self.page.page_number += 1
            next_page = self._page(
                object_list=self.get_objects(self.page.page_number),
                page_number=self.page.page_number,
                paginator=self,
            )
            self.page = next_page  # noqa

    def get_previous(self) -> None:
        """Get previous page. Overrides paginator\'s page attribute."""
        if self.has_previous:
            self.page.page_number -= 1
            previous_page = self._page(
                object_list=self.get_objects(self.page.page_number),
                page_number=self.page.page_number,
                paginator=self,
            )
            self.page = previous_page  # noqa

    @staticmethod
    def _page(*args, **kwargs) -> Page:
        """Returns Page object."""
        return Page(*args, **kwargs)

    def get_page_response(self, page_number: int = 0):
        """
        Get response of requested page number.
        number=0 equals first page.
        """
        if not isinstance(page_number, int):
            raise TypeError(f"{page_number} expected to be int.")
        page = self._page(
            object_list=self.get_objects(page_number),
            page_number=page_number,
            paginator=self,
        )
        data = {
            "data": page.object_list,
            "page_number": page_number,
            "has_next": page.has_next(),
            "has_previous": page.has_previous(),
        }
        return self._create_response(**data)

    @cached_property
    def total(self):
        """Return the total number of objects, across all pages."""
        return len(self.object_list)

    @property
    def total_pages(self):
        """Number of total pages. Lack of additional pages means total is 0."""
        return 0 if self.total == 0 else math.ceil(self.total / self.page_limit) - 1

    @property
    def page_range(self):
        """Return a range of pages."""
        return range(self.total_pages + 1 - self.start_page)

    def _create_response(self, **kwargs):
        """Creates json response object."""
        return {
            "total_pages": self.total_pages,
            "data": kwargs["data"],
            "page_number": kwargs["page_number"],
            "has_next": kwargs["has_next"],
            "has_previous": kwargs["has_previous"],
        }
