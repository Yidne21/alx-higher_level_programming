#!/usr/bin/python3
"""
Module which returns list of All the available attributes and methods of an object
"""


def lookup(obj):
    """
    This function Returns the list of All the  available 
    attributes and methods of an object
    """
    return dir(obj)
