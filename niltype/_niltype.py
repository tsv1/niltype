from typing import Any, Dict

__all__ = ("NilType",)


class _Singleton(type):
    _instances: Dict[Any, '_Singleton'] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> '_Singleton':
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class NilType(metaclass=_Singleton):
    __slots__ = ()

    def __str__(self) -> str:
        return "Nil"

    def __repr__(self) -> str:
        return str(self)

    def __init_subclass__(cls, **kwargs: Any) -> None:
        raise TypeError("'NilType' is final")
