#!/usr/bin/python3
"""This module contains a function which find a peak of a list"""


def find_peak(list_of_integers):
    """Finds the peak value"""

    if len(list_of_integers) > 0 :
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
