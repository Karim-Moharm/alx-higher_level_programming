#!/usr/bin/python3
"""
A module having a function that convert dict into json string
"""


def to_json_string(my_obj):
    """eturns the JSON representation of an object (string)"""
    from json import dumps

    JSON_str = dumps(my_obj)
    return JSON_str
