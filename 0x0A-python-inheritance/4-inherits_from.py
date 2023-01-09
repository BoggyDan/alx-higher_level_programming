#!/usr/bin/python3
def inherits_from(obj, a_class):
    """This tests if an object is a subclass of a parent class"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
