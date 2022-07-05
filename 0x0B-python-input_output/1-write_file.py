#!/usr/bin/python3
"""Module which has a function to Opens a file and write on it"""


def write_file(filename="", text=""):
    """Opens a file and write on it"""

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
