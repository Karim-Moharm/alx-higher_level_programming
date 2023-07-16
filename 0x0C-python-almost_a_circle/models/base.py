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
        # NOT DONE
        """write a jsong format into a file
        """
        lst = []
        # cls.__name__ returns name of the class
        file_name = cls.__name__ + '.json'

        if list_objs is None:
            list_objs = lst
        else:
            for i in list_objs:
                lst.append(i.__dict__)

        with open (file_name , mode='w', encoding='utf-8') as fp:
            fp.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """return list of json format and save it in 
        python object
        """
        if json_string is not None:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        dummy_instance = 0
        class_name = cls.__name__

        if class_name == "Rectangle":
            dummy_instance = cls(5, 3, 1)
        if class_name == "Square":
            dummy_instance = cls(5)

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        # NOT_DONE
        """returns a list of instances
        """
        filename = cls.__name__ + '.json'
        lst = []

        if filename is None:
            return lst
        with open (filename, mode='r', encoding='utf-8') as fp:
            lst = cls.from_json_string(fp.read())
        return lst


