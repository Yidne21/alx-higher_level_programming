#!/usr/bin/python3
"""Module which read_files"""


def read_file(filename=""):
    """open file and read the content and print it"""

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
