#!/usr/bin/python3
"""Defines save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file,
    using a JSON representation:

    Args:
        my_obj (str): object
        filename (str): name of the filename
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
