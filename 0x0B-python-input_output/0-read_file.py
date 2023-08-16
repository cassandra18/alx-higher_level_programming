#!/usr/bin/python3
"""Defines a function read_file."""


def read_file(filename=""):
    """Read and print the content of a text file to stdout.

    Args:
        filename: The path of the text file to be read.
                  Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
