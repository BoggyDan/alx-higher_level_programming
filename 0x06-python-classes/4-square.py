#!/usr/bin/python3

class Square:
    """Class Square creates a square object
    """
    def __init__(self, size=0):
        """Initialize method that stores the size of the square

        Args:
            Param1 (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """Method that returns the area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method to return the size of the square
        """
        return self.__size
    @size.setter
    def size(self, value):
        """Method to set the value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
