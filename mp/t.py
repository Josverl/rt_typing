from typing import Generic, TypeVar, trace, _GenericClass

# assert Generic 

# class A(Generic[int]):
#     # @trace
#     def __init__(self, x: int):
#         self.x = x

# a = A(1)
# print(a)
# assert isinstance(a, A)
# print( "=" * 20)


# T = TypeVar('T')
# print(f"{repr(T)=}")

# class Foo:
#     def __init__(self, x: T):
#         self.x = x
#         print("Foo.__init__")
#         print("self.x", self.x)
    

print("*" * 20)
from typing import Dict, Generic, TypeVar, _GenericClass
T = TypeVar("T")

class Registry(Generic[T]):
    @trace
    def __init__(self) -> None:
        self._store: Dict[str, T] = {}

    def set_item(self, k: str, v: T) -> None:
        self._store[k] = v

    def get_item(self, k: str) -> T:
        return self._store[k]


g = Generic
assert g, "g is None"
assert isinstance(g, _GenericClass)


class Registry(_GenericClass):
    pass

bare = Registry()
assert bare, "bare is None"

family_name_reg = Registry[str]()
assert family_name_reg, "family_name_reg is None"

assert isinstance(bare, Registry)
assert isinstance(family_name_reg, Registry)
family_age_reg = Registry[int]()

family_name_reg.set_item("husband", "steve")
family_name_reg.set_item("dad", "john")

family_age_reg.set_item("steve", 30)

print(repr(family_name_reg.__dict__))

