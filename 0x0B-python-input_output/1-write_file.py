#!/usr/bin/python3
"""This contains a function"""


def write_file(filename="", text=""):
    """This is a function that writes to a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
