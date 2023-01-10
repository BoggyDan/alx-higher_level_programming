#!/usr/bin/python3
"""This contains a function"""
import json


def from_json_string(my_str):
    """This returns the python format of a string

    Args:
        my_str (_type_): _description_

    Returns:
        _type_: _description_
    """
    return json.loads(my_str)
