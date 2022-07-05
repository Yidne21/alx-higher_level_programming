#!/usr/bin/python3
"""Module which has a function Class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description of Python object"""

    return obj.__dict__
