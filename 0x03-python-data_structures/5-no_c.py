#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for i in my_string:
        if i not 'c' or i not 'C':
            new_str += i
    return new_str
