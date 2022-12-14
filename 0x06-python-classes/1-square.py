#!/usr/bin/python3
"""Square module
This module contains a class that defines a square
and initializes it with a size
"""


class Square:
    """Class Square that defines a square object
    """
    def __init__(self, size):
        """Initialize method that stores only the size of the square

        Args:
            param1 (int): size of the square
        """
        self.__size = size
