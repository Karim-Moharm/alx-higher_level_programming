#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """in case normal integer number
        """
        self.assertEqual(max_integer([12, 44, 7, 8, 5]), 44)
    
    def test_pos_and_neg_numbers(self):
        """in case the numbers in list are positive
            and negative
        """
        self.assertEqual(max_integer([-12, -9, 1, 0, -65, 0.9998, -87]), 1)

    def test_float_numbers(self):
        """in case the list have some float numbers
        """
        self.assertEqual(max_integer([8, 4.223, 78.33, 0.87, -120.77]), 78.33)

    def test_empty_list(self):
        """in case the list was empty
        """
        self.assertEqual(max_integer([]), None)

    def test_max_in_last(self):
        """in case max integer last element in the list
        """
        self.assertEqual(max_integer([77, 5, 8, 997]), 997)

    def test_equal_element(self):
        """in case all element in list are equal
        """
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_string_element(self):
        """in case the one of the element was a sring
        """
        test_list = [44, 3, "str", 78.88]
        self.assertRaises(TypeError, max_integer, test_list)
