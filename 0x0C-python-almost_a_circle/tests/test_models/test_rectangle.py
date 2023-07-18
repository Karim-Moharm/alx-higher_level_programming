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
        Base._Base__nb_objects = 0  # reset ip value to 0
        r2 = Rectangle(4, 1)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 1)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 1)

    def test_negative_attr(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 12)
        with self.assertRaises(ValueError):
            rect = Rectangle(4, -12)
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, -12)

    def test_one_attr(self):
        """passing only one attribute
        """
        with self.assertRaises(TypeError):
            r3 = Rectangle(1)

    def test_no_attr(self):
        """test in case no attribute are passed
        """
        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_wrong_types_1(self):
        """test with wrong attributes types
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(0.855, 4.4)

        with self.assertRaises(TypeError):
            rect = Rectangle('w', 'h')
        
        with self.assertRaises(TypeError):
            rect = Rectangle(True, False)
        
        
    def test_wrong_types_2(self):
        """test with wrong attributes types
        """ 
        with self.assertRaises(TypeError):
            rect = Rectangle((1, 2), (3, 4))
        
        with self.assertRaises(TypeError):
            rect = Rectangle([1, 2], [3, 4])
        
        with self.assertRaises(TypeError):
            rect = Rectangle({1: 3, 2: 4}, 5)

    def test_get_width(self):
        """test case of trying to access the private 
        attr width
        """
        rec = Rectangle(3, 5)
        with self.assertRaises(AttributeError):
            print(rec.__width)

    def test_get_height(self):
        """test case of trying to access the private 
        attr height
        """
        rec = Rectangle(3, 5)
        with self.assertRaises(AttributeError):
            print(rec.__height)

    def test_get_x(self):
        """test case of trying to access the private 
        attr x
        """
        rec = Rectangle(3, 5)
        with self.assertRaises(AttributeError):
            print(rec.__x)

    def test_get_y(self):
        """test case of trying to access the private 
        attr y
        """
        rec = Rectangle(3, 5)
        with self.assertRaises(AttributeError):
            print(rec.__y)

    def test_area_normal_attr(self):
        """test area method for rectangle
        """
        r1 = Rectangle(4, 8)
        self.assertEqual(r1.area(), 32)
        r2 = Rectangle(4, 8, 0, 4, 6)
        self.assertEqual(r2.area(), 32)

    def test_area_wrong_types(self):
        """test area method with types not int
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, "8")
        with self.assertRaises(TypeError):
            r2 = Rectangle("4", 8)
        with self.assertRaises(TypeError):
            r3 = Rectangle(4, 8, 0, "4", 6)
        with self.assertRaises(TypeError):
            r4 = Rectangle(4, False)

    def test_area_no_attr(self):
        """test area in case no attributes passed
        """
        with self.assertRaises(TypeError):
            rec = Rectangle()
            rec.area()
    
    ''' TODO
    def test_display(self):
        r1 = Rectangle(3, 4)
        actual = "###\n###\n###\n###\n"
        self.assertEqual(r1.display(), actual)
    '''

    def test_str_method(self):
        """test __str__ metjof for rectangle 
        class
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1, id=1)
        actual_1 = '[Rectangle] (12) 2/1 - 4/6'
        actual_2 = '[Rectangle] (1) 1/0 - 5/5'

        self.assertEqual(str(r1), actual_1)
        self.assertEqual(str(r2), actual_2)

        Base._Base__nb_objects = 0
        r3= Rectangle(8, 3, 1)
        actual_3 = '[Rectangle] (1) 1/0 - 8/3'
        self.assertEqual(str(r3), actual_3)

    def test_update_args_1(self):
        """update method testing
        """
        Base._Base__nb_objects = 0

        # order => id    width   height  x   y

        r = Rectangle(7, 7, 7, 7, 7)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [7, 7, 7, 7, 7])

        r = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [1, 2, 3, 4, 5])

        rec = Rectangle(1, 1, 1, 1, 89)
        self.assertEqual(89, rec.id)

        rec.update(12, 7)
        self.assertEqual(12, rec.id)
        self.assertEqual(7, rec.width)

        rec.update(12, 7, 4)
        self.assertEqual(4, rec.height)
        rec.update(12, 7, 4, 3)
        self.assertEqual(3, rec.x)

    def test_update_wrong_args(self):
        """test cases for update using bad args
        """
        r = Rectangle(5, 9)
        
        with self.assertRaises(ValueError):
            r.update(12, -8)

        with self.assertRaises(ValueError):
            r.update(0, 5, -4)

        with self.assertRaises(ValueError):
            r.update(10, 5, 17, -20)
    
        with self.assertRaises(TypeError):
            r.update(10, 5, 17.22, 20)

        with self.assertRaises(ValueError):
            r.update(5, 6, 4, 20, -12)
