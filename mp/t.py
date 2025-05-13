from typing import Generic, TypeVar, trace

assert Generic 

class A(Generic[int]):
    # @trace
    def __init__(self, x: int):
        self.x = x

a = A(1)
print(a)
assert isinstance(a, A)
print( "=" * 20)


T = TypeVar('T')
print(f"{repr(T)=}")

class Foo:
    def __init__(self, x: T):
        self.x = x
        print("Foo.__init__")
        print("self.x", self.x)
    



print ("+" * 20)
assert T , "TypeVar not defined"
assert Generic , "Generic not defined"
assert Generic[T] , "Generic[T] not defined"

print(f"{repr(Generic[T])=}")

# class LoggedVar(Generic[T]):
# class LoggedVar(Foo):
class LoggedVar(Generic[T]):
    # @trace
    def __init__(self, value: T, name: str, logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value
        print("LoggedVar.__init__")
        print("self.name", self.name)
        print("self.logger", self.logger)
        print("self.value", self.value)
      
    # @trace
    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    # @trace
    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    # @trace
    def log(self, message: str) -> None:
        if self.logger: 
            self.logger.info('%s: %s', self.name, message)
        else:
            print('%s: %s', self.name, message)



x = LoggedVar(0, 'x', None)
y = LoggedVar(0, 'y', None)
z = LoggedVar(0, 'z', None)
print("x,y,z") 
print(repr(x))
print(repr(y))  
print(repr(z))

coord = [x, y, z]
print( "coord")
print(coord)
print(repr(coord))

from collections.abc import Iterable

def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)

zero_all_vars(coord)





# print("Done")
