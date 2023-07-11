#!/usr/bin/python3
"""
A module having a function that erites to a file
"""


def write_file(filename="", text=""):
    """function that writes a string to a file

    Args:
        filename: file name
        text (str): string to be written to the file

    Returns:
        number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
