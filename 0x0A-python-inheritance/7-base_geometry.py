#!/usr/bin/python3
"""
BaseGeomerty class
"""


class BaseGeometry:
    """BaseGeometry Class"""
    def area(self):
        """instance method for calculating area

        Raises:
            Exception: in case the area method are not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """instance method that validates integer input
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
