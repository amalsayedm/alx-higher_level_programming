#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None
    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    i = 1
    for i in range(length-2):
        if ((list_of_integers[i] > list_of_integers[i-1]) and
                (list_of_integers[i] > list_of_integers[i+1])):
            return list_of_integers[i]
        else:
            i += 1
    return list_of_integers[i]
