#!/usr/bin/python3
"""

This is a module that containts a class that avoids
dynmaically created attributes

"""


class LockedClass:
    """Prevents tresspassing :)
    """
    __slots__ = ['first_name']
