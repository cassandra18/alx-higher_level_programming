#!/usr/bin/python3
"""Defines a function class_to_json"""


def class_to_json(obj):
    """A function that returns dictionary representation of data structure.

    Args:
        obj: An object which is an instance of a class

    Returns:
        dictionary description with simple data structure for JSON
        serialization of an object
    """
    dictionary = {}
    for attr_name in dir(obj):
        if not attr_name.startswith("__") and hasattr(obj, attr_name):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                dictionary[attr_name] = attr_value
    return dictionary
