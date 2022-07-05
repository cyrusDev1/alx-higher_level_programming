#!/usr/bin/python3
"""Defines write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'w',  encoding="utf-8") as f:
       return f.write(text)
