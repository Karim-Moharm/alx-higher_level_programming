#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """function that append a text to a file
    and return num of char added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
