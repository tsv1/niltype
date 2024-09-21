from ._nilable import Nilable
from ._niltype import NilType
from ._version import version

__version__ = version
__all__ = ("Nil", "NilType", "Nilable",)

# Singleton instance of NilType._nil.
# Use Nil to represent the 'Nil' value in the codebase.
Nil = NilType._nil
