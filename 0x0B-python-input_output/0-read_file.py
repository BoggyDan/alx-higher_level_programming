#!/usr/bin/python3
"""This contains a function"""


def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """
    with open(filename, 'r', encoding="utf-8") as z:
        reading = z.read()
        print(reading, end='')
