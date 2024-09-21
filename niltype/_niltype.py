from enum import Enum
from typing import Any

__all__ = ("NilType",)


class _Nil:
    """
    Represents a sentinel Nil object for use in the NilType enumeration.

    This class defines a unique object, "Nil", that can be used as a placeholder
    to signify a 'null' or 'missing' value in contexts where None may not be suitable.
    """

    def __str__(self) -> str:
        """
        Return the string representation of the Nil object.

        :return: The string "Nil".
        """
        return "Nil"

    def __repr__(self) -> str:
        """
        Return the official string representation of the Nil object.

        :return: The string "Nil".
        """
        return str(self)


class NilType(Enum):
    """
    Defines a NilType enumeration that holds a single value, _nil.

    This enum provides a type-safe representation of a 'Nil' value, which can be
    used as a sentinel or marker in situations where None may not be appropriate.
    """

    _nil = _Nil()

    def __str__(self) -> str:
        """
        Return the string representation of the NilType's value.

        :return: The string representation of the Nil object.
        """
        return str(self.value)

    def __repr__(self) -> str:
        """
        Return the official string representation of the NilType's value.

        :return: The official string representation of the Nil object.
        """
        return repr(self.value)

    def __bool__(self) -> bool:
        """
        Return a boolean representation of the NilType instance.

        :return: Always returns False, indicating that NilType evaluates as false.
        """
        return False

    def __setattr__(self, key: str, value: Any) -> None:
        """
        Prevent setting attributes on NilType except for private attributes.

        :param key: The attribute name to set.
        :param value: The value to assign to the attribute.
        :raises AttributeError: If attempting to set any attribute that does not start
                                with an underscore.
        """
        if not key.startswith("_"):
            raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {key!r}")
        super().__setattr__(key, value)
