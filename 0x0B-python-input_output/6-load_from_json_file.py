#!/usr/bin/python3
"""Module which has a functio to load a JSON file"""


from json import loads


def load_from_json_file(filename):
    """Function which loads a JSON file"""

    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
