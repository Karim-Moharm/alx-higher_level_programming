#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    New_list = list(my_list)
    New_list = list(map(lambda idx: idx * number, my_list))
    return New_list
