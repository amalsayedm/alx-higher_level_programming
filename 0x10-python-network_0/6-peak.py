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
    if list_of_integers[length - 1] > list_of_integers[length - 2]:
        return list_of_integers[length - 1]
    i = 1
    for i in range(length-3):
        if ((list_of_integers[i] > list_of_integers[i-1]) and
                (list_of_integers[i] > list_of_integers[i+1])):
            return list_of_integers[i]
        else:
            i += 1
    return list_of_integers[i]
