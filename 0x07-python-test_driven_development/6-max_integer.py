#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    max_int = list[0]
    index = 1
    while index < len(list):
        if list[index] > max_int:
            max_int = list[index]
        index += 1
    return max_int
