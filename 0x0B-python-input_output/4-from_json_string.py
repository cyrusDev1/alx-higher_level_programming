#!/usr/bin/python3
"""Defines from_json_string function"""


import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string:

    Args:
        my_str (str): object
    """
    return json.loads(my_str)
