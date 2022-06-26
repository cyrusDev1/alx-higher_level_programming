#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """Return addition of a and b.
        Floats are typecasted to ints
        Raises:
            TypeError: when a or b is not int and not float.
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
