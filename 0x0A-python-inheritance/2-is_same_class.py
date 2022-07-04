#!/usr/bin/python3
"""
Module which checks weather an instance is the same as 
the specified classh
"""


def is_same_class(obj, a_class):
    """
    A function which returns True if obj is an instance of a_class
    otherwise it returns False
    """

    if type(obj) == a_class:
        return True
    return False
