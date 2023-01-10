#!/usr/bin/python3
import json
"""This contains a function"""


def to_json_string(my_obj):
    """Returns the JSON format of an object

    Args:
        my_obj (any): _description_

    Returns:
        JSON: JSON format
    """
    return json.dumps(my_obj)
