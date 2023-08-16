#!/usr/bin/python3
"""Defines a funtion append_write."""


def append_write(filename="", text=""):
    """A function that appends a string to a text file.

    Args:
        filename: File to write to.
        text: The text to add into the file.
    Returns:
        The number of characters added.
    """
    chars_written = 0
    with open(filename, 'a', encoding='utf-8') as f:
        chars_written = f.write(text)
    return (chars_written)
