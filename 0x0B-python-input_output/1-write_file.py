#!/usr/bin/python3
"""Defines a funtion write_file."""


def write_file(filename="", text=""):
    """A function that writes a string to a text file.

    Args:
        filename: File to write to.
        text: The text to write into the file.
    Returns:
        The number of characters written.
    """
    chars_written = 0
    with open(filename, 'w', encoding='utf-8') as f:
        chars_written = f.write(text)
    return (chars_written)
