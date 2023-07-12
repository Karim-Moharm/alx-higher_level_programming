#!/usr/bin/python3
"""
Module for returning an object from json file
"""


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    from json import loads

    return loads(my_str)
