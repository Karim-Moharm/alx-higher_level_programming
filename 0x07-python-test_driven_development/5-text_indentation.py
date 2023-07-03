#!/usr/bin/python3
"""
The module have a function that separated and print it into new lines

Author: Karim Moharm
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these chars: ., ? and :

    Args:
        test: text to be printed

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    char = ['.', '?', ':']

    string = text.replace(char[0], char[0] + "\n\n")
    string = string.replace(char[1], char[1] + "\n\n")
    string = string.replace(char[2], char[2] + "\n\n")

    for _ in range(len(text)):
        string = string.replace("\n ", "\n")

    print(string, end="")
