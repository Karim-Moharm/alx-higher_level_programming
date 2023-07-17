#!/usr/bin/python3
"""Module to test Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Tests cases for Base Class
    """
    '''ERROR
    def test_class_attribute(self):
        """test if nb_object is initialized with zero
        """
        self.assertEqual(getattr(Base, 'Base.__nb_object'), 0)
    '''

    def test_id_attr(self):
        """test id attribute of Base class
        """
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def testA_id_attr_None(self):
        """test None case id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def testB_id_attr_None(self):
        """test None case id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_string_id(self):
        """Test string id"""
        b1 = Base("str")
        self.assertEqual(b1.id, "str")

    def test_to_json_string(self):
        """test converting python list of dict into
        json format
        """
        # accessing name mangle private attr from outside the class
        Base._Base__nb_objects = 0  # to set id to 0

        r1 = Rectangle(8, 5, 2, 4)
        py_dict = r1.to_dictionary()
        json_str = Base.to_json_string([py_dict])

        # convert py_dict to str to use replace method
        py_dict_str = str([py_dict])
        compared_dict = py_dict_str.replace("'", '"')

        self.assertEqual(json_str, compared_dict)
        self.assertEqual(len(json_str), len(py_dict_str))
        self.assertEqual(type(py_dict), dict)
        self.assertEqual(type(json_str), str)

        self.assertEqual(Base.to_json_string(None), "[]")

        py_dict = [{
            "name": "karim",
            "age": 22,
        }]

        py_dict_str = '[{"name": "karim", "age": 22}]'

        self.assertEqual(Base.to_json_string(py_dict), py_dict_str)

        self.assertEqual(Base.to_json_string([{}]), '[{}]')
