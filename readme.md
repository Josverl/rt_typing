# runtime modules for type checking on MicroPython

This repo is a test of a few different ways to support type checking in MicroPython. 

The goal is to be able to run code on a MicroPython board that contains include statements and typing annotations unchanged.

By default the  `typing` module is not included in MicroPython. 
This repo contains an experiment in enhancing the modules
 - `typing`, 
 - `typing_extensions`, 
 - `abc` 
 - `collections.abc` 
 - `__future__`, 
in MicroPython as a cross-compiled module or frozen code.

Micropython-lib and Micropython PRs
 - https://github.com/Josverl/micropython-stubs/issues/755#issuecomment-2136479507
 - https://github.com/micropython/micropython-lib/pull/584

Micropython-stubs
 - [MicroPython’s typing.mpy module](https://micropython-stubs.readthedocs.io/en/main/typing_mpy.html)