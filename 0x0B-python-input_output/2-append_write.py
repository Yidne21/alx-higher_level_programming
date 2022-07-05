#!/usr/bin/python3
"""Module which has a function that write to a file with appending mode"""


def append_write(filename="", text=""):
    """Function which opens a file and appen a text on it"""
`
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
