#!/usr/bin/python3
"""Module for testing Rectangle class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleModule(unittest.TestCase):
    """test Cases for rectangle class
    """

    def test_all_attributes(self):
        """test rectangle class when all attributes 
        are passed
        """
        r1 = Rectangle(2, 4, 8, 0, 45)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 45)

    def test_only_two_attrs(self):
        """passing width and height attrivutes only
        """
        r2 = Rectangle(4, 1)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 1)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 1)
