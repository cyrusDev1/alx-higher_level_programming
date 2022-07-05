#!/usr/bin/python3
"""Defines write_file function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    and returns the number of characters added:

    Args:
        filename (str): The name of the file to write.
        text (str): The text to append to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'a',  encoding="utf-8") as f:
        return f.write(text)
