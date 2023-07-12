#!/usr/bin/python3
"""Student class Module
"""


class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        is_string = True

        if type(attrs) == list:
            for elem in attrs:
                if type(elem) != str:
                    is_string = False

        if type(attrs) == list and is_string:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__
