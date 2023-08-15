#!/usr/bin/python3
"""Defines add_integer function that adds integers."""


def add_integer(a, b=98):
    """Return the  integer sum of a and b.

    Float arguments are typecasted to ints.

    Raises:
        TypeError: if a or b is a non-integer or non-float.
    """
    if ((not isinstance(a, int) or not isinstance(a, float))):
        raise TypeError(a must be an integer)
    if not isinstance(b, int):
        raise TypeError(b must be an integer)
    return (int(a) + int(b))
