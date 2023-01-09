#!/usr/bin/python3
"""This is a module that contains a subclass"""


class MyList(list):
    """This is a subclass

    Args:
        list (class): Parent class
    """
    def print_sorted(self):
        """This will print the sorted list
        """
        done = self.copy()
        done.sort()
        print(done)
