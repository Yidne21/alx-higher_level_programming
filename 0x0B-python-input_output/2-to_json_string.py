#!/usr/bin/python3
"""Module which has a function to reperesent an object in to JSON format"""


from json import dumps


def to_json_string(my_obj):
    """"Function which returns the json representation of an object"""

    return dumps(my_obj)
