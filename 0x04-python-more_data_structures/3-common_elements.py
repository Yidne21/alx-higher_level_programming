#!/usr/bin/python3
def common_elements(set_1, set_2):
    c = set(set_1).intersection(set(set_2))
    return list(c)
