#!/usr/bin/python3
import json
"""Defines a function to_json_string."""


def to_json_string(my_obj):
    """A function that converts python srting to json format.

    Args:
        my_obj: The object(string) to convert to json.
    Return:
        JSON representation of an object (string).
    """
    json_data = json.dumps(my_obj)
    return (json_data)
