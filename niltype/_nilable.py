from typing import TypeVar, Union

from ._niltype import NilType

__all__ = ("Nilable",)

_T = TypeVar("_T")
Nilable = Union[_T, NilType]
