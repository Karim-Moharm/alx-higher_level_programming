#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Insert an element at a specific index in a list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = list(my_list)
    new_list[idx] = element
    return new_list

