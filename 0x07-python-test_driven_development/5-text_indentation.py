#!/usr/bin/python3
"""
The module have a function that separated and print it into new lines

Author: Karim Moharm
"""

def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        test: text to be printed

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    char = ['.', '?',':']

    for i in range(len(text)):
        print("{}".format(text[i]), end="")
        if text[i] in char:
            print("\n")
