#!/usr/bin/python3
"""
Module which has a function inherits_from
"""


def inherits_from(obj, a_class):
    """
    This function returns true if obj is the instance of 
    a_class or it is the instance of it's subclass

    Args:
        obj(a_class): The object of a_class.
        a_class: The class.
    """

    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True
    return False
