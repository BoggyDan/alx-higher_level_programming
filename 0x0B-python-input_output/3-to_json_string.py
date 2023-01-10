#!/usr/bin/python3
"""This contains a function"""
import json


def to_json_string(my_obj):
    """Returns the JSON format of an object

    Args:
        my_obj (any): _description_

    Returns:
        JSON: JSON format
    """
    return json.dumps(my_obj)
