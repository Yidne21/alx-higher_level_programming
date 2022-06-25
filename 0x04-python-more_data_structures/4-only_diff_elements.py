#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    c = set(set_1).difference(set(set_2))
    d = set(set_2).difference(set(set_1))
    u = c.union(d)
    return u
