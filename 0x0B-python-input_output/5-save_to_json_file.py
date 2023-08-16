#!/usr/bin/python3
"""Defines a function save_to_json_file."""


import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file, using a JSON format.

    Args:
        my_obj:The  python data to be written in json format.
        filename: The path to the file to be written to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
