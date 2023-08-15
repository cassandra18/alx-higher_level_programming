#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    character = 0
    while character < len(text) and text[character] == ' ':
        character += 1

    while character < len(text):
        print(text[character], end="")
        if text[character] == "\n" or text[character] in ".?:":
            if text[character] in ".?:":
                print("\n")
            character += 1
            while character < len(text) and text[character] == ' ':
                character += 1
            continue
        character += 1
