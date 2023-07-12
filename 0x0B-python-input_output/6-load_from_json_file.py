#!/usr/bin/python3
"""
Creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """a function that created an object from json file"""
    import json

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
