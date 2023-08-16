#!/usr/bin/python3
"""Defines a function load_from_json_file."""


import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”

    Args:
        filename: The file containing the json object.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        json.loads(f)
