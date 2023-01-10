#!/usr/bin/python3
import json
"""This contains a function"""


def load_from_json_file(filename):
    """This returns the python structure
    of a file from JSON representation

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.load(f)
