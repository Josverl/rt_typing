"""
abc.py - Micropython runtime Abstract Base Classes module
"""
from typing import _AnyCall  # type: ignore

def abstractmethod(funcobj):
    return funcobj


class abstractproperty(property):
    def __init__(*args, **kwargs): ...


class abstractclassmethod(classmethod):
    def __init__(*args, **kwargs): ...


class abstractstaticmethod(staticmethod):
    def __init__(*args, **kwargs): ...


# class ABC(metaclass=ABCMeta):
class ABC:
    def __init__(*args, **kwargs): ...

ABCMeta = _AnyCall
# # class ABCMeta(type):
# class ABCMeta:
#     def __init__(*args, **kwargs): ...

#     # def __new__(
#     #     mcls: type, name: str, bases: tuple[type[Any], ...], namespace: dict[str, Any]
#     # ): ...

#     def register(*args, **kwargs): ...
