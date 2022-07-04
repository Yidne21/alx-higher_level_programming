#!/usr/bin/python3

"""
Module which checks weather an instance is the same as 
the specified classh
"""

def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    return False
