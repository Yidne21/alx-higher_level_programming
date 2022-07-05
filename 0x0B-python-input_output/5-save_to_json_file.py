#!/usr/bin/python3
"""Module which has a function to save a python object in to a json file"""


from json import dumps


def save_to_json_file(my_obj, filename):
    """Function which save python object in to a JSON file"""

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
