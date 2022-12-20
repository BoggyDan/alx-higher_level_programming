#!/usr/bin/python3
"""Square module
This module contains a class that defines a square
and initializes it with a size
"""


class Square:
    """Class Square creates a square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize method that stores the size and position of the square

        Args:
            Param1 (int): size of the square
            Param2 (int): position of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Method to return the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Method to set the position of the square
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Method to print the square using #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
