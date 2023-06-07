#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = str
    if n < 0:
        return str_cpy
    return str_cpy[:n] + str_cpy[n+1:]
