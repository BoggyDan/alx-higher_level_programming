#!/usr/bin/python3

""" This module contains a rectangle
"""


class Rectangle:
    """Represents a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Class that creates a rectangle

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """method that returns the value of width

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """method that defines the width

        Args:
            value (int): width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """method that returns the height of the rectangle

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """method that defines the height

        Args:
            value (int): height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Method that calculates the area of the rectangle

        Returns:
            _type_: rectangle area
        """
        return self.height * self.width

    def perimeter(self):
        """Method that calculates the perimeter of a rectangle

        Returns:
            _type_: rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ Method that returns the Rectangle #

        Returns:
            str of the rectangle

        """
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for _ in range(self.height):
            rectangle += (str(self.print_symbol) * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method that returns the string represantion of the instance

        Returns:
            string represenation of the object

        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a message when the instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method that returns the biggest rectangle

        Args:
            rect_1 (int): Rectangle 1
            rect_2 (int): Rectangle 2

        Raises:
            TypeError: When one of the rectangle is not
            an instance of the Rectangle Class


        Returns:
            The biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area >= rect_2.area:
            return rect_1
        else:
            return rect_2
