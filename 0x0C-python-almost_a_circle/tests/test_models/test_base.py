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
