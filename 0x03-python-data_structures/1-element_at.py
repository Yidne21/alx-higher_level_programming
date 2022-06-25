#!/usr/bin/python3
def element_at(my_list, index):
    if index < 0:
        return None
    i = len(my_list) - 1
    if index > i:
        return None
    return my_list[index]
