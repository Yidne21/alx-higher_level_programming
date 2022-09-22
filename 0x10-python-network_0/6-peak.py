#!/usr/bin/python3
#This function returns the peak elements in the list

def find_peak(list_of_integers):
    if len(list_of_integers) > 0 :
        return max(list_of_integers)
    else:
        return None
