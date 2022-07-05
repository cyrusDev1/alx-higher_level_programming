#!/usr/bin/python3
"""Defines read_file function"""


def read_file(filename=""):
    """Reads a file and prints it to output"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
