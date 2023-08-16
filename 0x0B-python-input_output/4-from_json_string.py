#!/usr/bin/python3
"""Defines a function from_json_string."""


import json


def from_json_string(my_str):
    """A function that parses data back to python data structure.

    Args:
        my_str: the string to convert to python structure.
    Return:
        An object (Python data structure).
    """
    parsed_data = json.load(my_str)
    return (parsed_data)
