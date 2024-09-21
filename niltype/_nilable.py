from typing import TypeVar, Union

from ._niltype import NilType

__all__ = ("Nilable",)

_T = TypeVar("_T")

# Nilable can be either a value of type _T or NilType.
# Used to allow a type or a 'Nil' placeholder.
Nilable = Union[_T, NilType]
