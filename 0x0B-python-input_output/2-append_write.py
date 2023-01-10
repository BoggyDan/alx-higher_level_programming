#!/usr/bin/python3
"""This contains a function"""


def append_write(filename="", text=""):
    """Function that helps to append a text to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
