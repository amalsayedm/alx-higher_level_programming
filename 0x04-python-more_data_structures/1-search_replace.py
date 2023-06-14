#!/usr/bin/python3


def search_replace(my_list, search, replace):
    templist = my_list[:]
    for n in range(len(templist)):
        if templist[n] == search:
            templist[n] = replace
    return (templist)
