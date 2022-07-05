#!/usr/bin/python3
"""Module which has a function to convert Json file to a python object"""


from json import loads


def from_json_string(my_str):
    """Function which returns python object from JSON file"""

    return loads(my_str)
