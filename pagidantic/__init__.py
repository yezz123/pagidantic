"""
Pagidantic is a Python package for pagination using Pydantic.

It's easy to use, lightweight, and easy to integrate with existing projects.

It helps in creating efficient pagination solution with minimal code, while maintaining type checking and data validation with Pydantic.
"""


__version__ = "1.0.0"

from pagidantic.dict import PagidanticDict
from pagidantic.factory import PagidanticFactory
from pagidantic.page import Page
from pagidantic.pagidantic import pagidantic
from pagidantic.paginator import Paginator
from pagidantic.set import PagidanticSet

__all__ = [
    "PagidanticFactory",
    "Paginator",
    "pagidantic",
    "PagidanticDict",
    "PagidanticSet",
    "Page",
]
