from enum import Enum
from typing import Any

__all__ = ("NilType",)


class _Nil:
    def __str__(self) -> str:
        return "Nil"

    def __repr__(self) -> str:
        return str(self)


class NilType(Enum):
    _nil = _Nil()

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return repr(self.value)

    def __bool__(self) -> bool:
        return False

    def __setattr__(self, key: str, value: Any) -> None:
        if not key.startswith("_"):
            raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {key!r}")
        super().__setattr__(key, value)
