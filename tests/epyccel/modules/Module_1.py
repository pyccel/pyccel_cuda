# pylint: disable=missing-function-docstring, missing-module-docstring

__all__ = ('f', 'g', 'h')

def f(x : 'float [:]'):
    x[0] = 2.

def g(x : 'float [:]'):
    x[1] = 4.

def h(x : 'float [:]'):
    x[2] = 8.
