#!/usr/bin/python3
"""Defines a function that prints a square."""


def print_square(size):
    """Print a square with # character.

    Args:
        size (int): The width and height of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0.
        TypeError: If size is a float and is  < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
