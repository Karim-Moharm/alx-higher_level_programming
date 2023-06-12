#!/usr/bin/python3
def element_at(my_list, idx):
    """
    a function that retrieves an element from a list
    """
    return (None if idx < 0 or idx >= len(my_list) else my_list[idx])
