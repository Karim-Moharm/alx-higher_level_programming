#!/usr/bin/python3
"""Test module for Square class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareModule(unittest.TestCase):
    """test Cases for square class"""
    def setUp(self):
        """Method that called for each test
        in order reset id attributed if not mentioned in
        the method
        """
        Base._Base__nb_objects = 0

    def test_all_attributes(self):
        """test Square class when all attributes
        area passed
        """
        s1 = Square(2, 8, 0, 45)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 45)

    def test_only_size_attr(self):
        """passing size attribute only"""
        s2 = Square(4)
        self.assertEqual(s2.size, 4)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 1)

    def test_negative_attr(self):
        """test negative attributes of square"""
        with self.assertRaises(ValueError):
            s = Square(-4)

        with self.assertRaises(ValueError):
            s = Square(1, -2)

        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)

    def test_no_attr(self):
        """test in case no attribute are passed"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_wrong_types_1(self):
        """test with wrong attributes types"""
        with self.assertRaises(TypeError):
            s = Square(0.855)

        with self.assertRaises(TypeError):
            s = Square("s")

        with self.assertRaises(TypeError):
            s = Square("1")

        with self.assertRaises(TypeError):
            s = Square(1, "2")

        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")

        with self.assertRaises(TypeError):
            s = Square(True)

        with self.assertRaises(ValueError):
            s = Square(0)

    def test_wrong_types_2(self):
        """test with wrong attributes types"""

        with self.assertRaises(TypeError):
            s = Square((1, 2))

        with self.assertRaises(TypeError):
            s = Square([1, 2])

        with self.assertRaises(TypeError):
            s = Square({1: 3, 2: 4})

    def test_get_size(self):
        """test case of trying to access the private
        attr size
        """
        s = Square(3)
        with self.assertRaises(AttributeError):
            print(s.__size)

    def test_get_x(self):
        """test case of trying to access the private
        attr x
        """
        s = Square(3)
        with self.assertRaises(AttributeError):
            print(s.__x)

    def test_get_y(self):
        """test case of trying to access the private
        attr y
        """
        s = Square(3)
        with self.assertRaises(AttributeError):
            print(s.__y)

    def test_area_normal_attr(self):
        """test area method for Square"""
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)
        s2 = Square(4, 8, 4, 6)
        self.assertEqual(s2.area(), 16)

    def test_area_wrong_types(self):
        """test area method with types not int"""
        with self.assertRaises(TypeError):
            s1 = Square(4, "8")
        with self.assertRaises(TypeError):
            s2 = Square("4", 8)
        with self.assertRaises(ValueError):
            s3 = Square(-4, 8, 0, 4)
        with self.assertRaises(TypeError):
            s4 = Square(True, 8)

    def test_area_no_attr(self):
        """test area in case no attributes passed"""
        with self.assertRaises(TypeError):
            s = Square()
            s.area()

    def test_str_method(self):
        """test __str__ metjof for Square
        class
        """
        s1 = Square(4, 6, 2, 12)  # Square(size, x=0, y=0, id=None)
        s2 = Square(5, 5, id=11)
        actual_1 = "[Square] (12) 6/2 - 4"  # [Square] (<id>) <x>/<y> - <size>
        actual_2 = "[Square] (11) 5/0 - 5"

        self.assertEqual(str(s1), actual_1)
        self.assertEqual(str(s2), actual_2)

        Base._Base__nb_objects = 0
        s3 = Square(8, 3, 1)
        actual_3 = "[Square] (1) 3/1 - 8"
        self.assertEqual(str(s3), actual_3)

    def test_update_args_1(self):
        """update method testing"""
        # order of update() function => id   size   x   y

        s = Square(7, 7, 7, 7)
        self.assertEqual([s.id, s.size, s.x, s.y], [7, 7, 7, 7])

        s = Square(2, 3, 4, 5)  # Square(size, x=0, y=0, id=None)
        s.update()
        self.assertEqual([s.id, s.size, s.x, s.y], [5, 2, 3, 4])

        s = Square(1, 1, 1, 89)
        self.assertEqual(89, s.id)

        s.update(12, 7)
        self.assertEqual(12, s.id)
        self.assertEqual(7, s.size)

        s.update(12, 7, 4)
        self.assertEqual(12, s.id)
        self.assertEqual(7, s.size)
        self.assertEqual(4, s.x)

        s.update(12, 7, 4, 3)
        self.assertEqual(3, s.y)

    def test_update_with_wrong_args(self):
        """test cases for update using bad args"""
        s = Square(5)

        with self.assertRaises(TypeError):
            s.update(12, "4")

        with self.assertRaises(TypeError):
            s.update(7, 4, "9")

        with self.assertRaises(ValueError):
            s.update(12, -8)

        with self.assertRaises(ValueError):
            s.update(0, 5, -4)

        with self.assertRaises(ValueError):
            s.update(10, 5, 17, -20)

        with self.assertRaises(TypeError):
            s.update(10, 17.22, 20)

    def test_upadte_kwargs(self):
        """test cases for update kwargs
        test if kwargs is skipped if args exist
        """
        s = Square(1, 2, 3, 4)
        s.update(89, id=8)
        self.assertEqual([s.id, s.size, s.x, s.y], [89, 1, 2, 3])

        s.update(12, 7, 5, 7, id=3, size=12, x=9, y=10)
        self.assertEqual([s.id, s.size, s.x, s.y], [12, 7, 5, 7])

    def test_update_kwargs_2(self):
        """test update kwargs method"""
        s = Square(5, 9, 10, 10)

        s.update(id=7)
        self.assertEqual(str(s), "[Square] (7) 9/10 - 5")

        s.update(x=4, y=6)
        self.assertEqual(str(s), "[Square] (7) 4/6 - 5")

        s.update(size=1)
        self.assertEqual(str(s), "[Square] (7) 4/6 - 1")

        s.update(size=3, x=2, id=89)
        self.assertEqual(str(s), "[Square] (89) 2/6 - 3")

        Base._Base__nb_objects = 0
        s = Square(10, 10, 10)
        self.assertEqual(str(s), "[Square] (1) 10/10 - 10")

    def test_update_kwargs_3(self):
        """test kwargs for update method"""
        s = Square(4)

        s.update(**{"id": 89})
        self.assertEqual(s.id, 89)

        s.update(**{"id": 89, "size": 1})
        self.assertEqual(s.size, 1)

        s.update(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(s.x, 2)

        s.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        """test to_dictionary method for square
        class
        """
        s = Square(1, 2, 3, 4)
        d = {"x": 2, "y": 3, "size": 1, "id": 4}
        self.assertEqual(s.to_dictionary(), d)

        s = Square(5, 3)
        d = {"x": 3, "y": 0, "size": 5, "id": 1}
        self.assertEqual(s.to_dictionary(), d)

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 == s2)

    def test_to_dictionary2(self):
        """
        Tests_2 for dictionary method
        """
        s = Square(1, 2, 3, 4)
        d = s.to_dictionary()
        self.assertEqual(d["size"], 1)
        self.assertEqual(d["x"], 2)
        self.assertEqual(d["y"], 3)
        self.assertEqual(d["id"], 4)
