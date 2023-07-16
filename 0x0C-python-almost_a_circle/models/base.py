#!/usr/bin/python3
"""Base class module
"""
import  json


class Base:
    """
    The Base Class of the project

    Attrs:
         __nb_objects: private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init special method that works as constructor
        Attrs:
            id (int): integer attribute for id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a json string of dict
        """
        if list_dictionaries is not None or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """write a jsong format into a file
        """
        lst = []
        file_name = cls.__name__ + '.json'

        if list_objs is None:
            list_objs = lst
        else:
            for i in list_objs:
                lst.append(i.__dict__)

        with open (file_name , mode='w', encoding='utf-8') as fp:
            fp.write(cls.to_json_string(lst))
