#!/usr/bin/python3
"""Defines read_file function"""


def read_file(filename=""):
    """Reads from filename and prints
    its contents to stdout.

    Args:
        filename: name of the file
    """
    with open(filename, encoding="utf-8") as f:
        r = f.read()
        print(r)
