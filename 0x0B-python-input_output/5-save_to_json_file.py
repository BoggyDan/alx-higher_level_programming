#!/usr/bin/python3
import json
"""This contains a function"""


def save_to_json_file(my_obj, filename):
    """This writes an object to a file in JSON
    representation

    Args:
        my_obj (_type_): object
        filename (_type_): name of textfile
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
