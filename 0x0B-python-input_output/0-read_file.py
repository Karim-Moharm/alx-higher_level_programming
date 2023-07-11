#!/usr/bin/python3
"""
Module having a function that reads a text file
"""


def read_file(filename=""):
    """reads a text file

    Args:
        filename: the file to be readed
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
