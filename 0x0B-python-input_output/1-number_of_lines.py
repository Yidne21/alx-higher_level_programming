#!/usr/bin/python3
"""Module which has a function which reads number of line in file """


def number_of_lines(filename=""):
    """open a file and returns the number of lines"""

    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
