"""
abc.py - Micropython runtime Abstract Base Classes module
"""

def abstractmethod(funcobj):
    return funcobj

def update_abstractmethods(cls):
    return cls

class abstractclassmethod(classmethod):
    def __init__(self, callable) -> None: ...


class abstractstaticmethod(staticmethod):
    def __init__(self, callable) -> None: ...


class abstractproperty(property): ...



# class ABC(metaclass=ABCMeta):
class ABC:
    __slots__ = ()
