from ._nilable import Nilable
from ._niltype import NilType
from ._version import version

__version__ = version
__all__ = ("Nil", "NilType", "Nilable",)

Nil = NilType._nil
