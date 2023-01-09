#!/usr/bin/python3
"""This contains a geometry class"""


class BaseGeometry:
    """class that defines the attributes of a geometric shape"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value argument"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
