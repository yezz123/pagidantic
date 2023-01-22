from typing import Type

from pydantic.dataclasses import dataclass

from pagidantic.dict import PagidanticDict
from pagidantic.paginator import Paginator
from pagidantic.set import PagidanticSet


@dataclass
class PagidanticFactory:
    """A factory class for creating paginator instances based on the type of objects to be paginated."""

    objects_type: str

    def get_paginator(self) -> Type[Paginator]:
        """
        Returns paginator class/subclass.

        :return: The appropriate paginator class/subclass based on the type of objects to be paginated.
        :rtype: Type[Paginator]
        :raise TypeError: If object_list is of an unsupported type.
        """
        if self.objects_type in ["list", "tuple"]:
            return Paginator
        elif self.objects_type == "dict":
            return PagidanticDict
        elif self.objects_type == "set":
            return PagidanticSet
        else:
            raise TypeError(
                f"Unsupported type {self.objects_type} for object_list param."
            )
