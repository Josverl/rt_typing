"""
This module provides runtime support for type hints.	
based on : https://github.com/micropython/micropython-lib/pull/584
"""

DEBUG = False


# def trace(func):
#     if DEBUG:

#         def wrapper(*args, **kwargs):
#             print(f"Trace: {func.__name__} called with args={args}, kwargs={kwargs}")
#             return func(*args, **kwargs)

#         return wrapper
#     else:
#         return func


def cast(type, val):
    return val


def reveal_type(val):
    # https://docs.python.org/3/library/typing.html#typing.reveal_type
    print(val.__class__.__name__)
    return val


# not clear if we need this ( 23 bytes)
# def get_origin(type):
#     # https://docs.python.org/3/library/typing.html#typing.get_origin
#     #  Return None for all unsupported objects.
#     return None


# not clear if we need this ( 22 bytes)
# def get_args(type):
#     # https://docs.python.org/3/library/typing.html#typing.get_args
#     # Python 3.8+ only
#     return ()


def no_type_check(x):
    # decorator to disable type checking on a function or method
    # https://docs.python.org/3/library/typing.html#typing.no_type_check
    return x


def final(x):
    # decorator to indicate that a method should not be overridden
    # https://docs.python.org/3/library/typing.html#typing.final
    return x


def overload(func):
    # ignore functions with overload decorator
    return None


def NewType(name, type):
    # https://docs.python.org/3/library/typing.html#newtype
    # just use the original type.
    return type


class __Ignore:
    """A class to ignore type hints in code."""

    # @trace
    def __init__(*args, **kwargs):
        pass

    # @trace
    def __call__(*args, **kwargs):
        # May need some guardrails here
        pass

    # @trace
    def __getitem__(self, arg):
        # May need some guardrails here
        return __ignore

    # @trace
    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        return __ignore


__ignore = __Ignore()


# ref: https://github.com/micropython/micropython-lib/pull/584#issuecomment-2317690854
# @trace
def __getattr__(attr):
    return __ignore
