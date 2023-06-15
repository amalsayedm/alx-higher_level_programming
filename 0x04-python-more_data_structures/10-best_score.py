#!/usr/bin/python3


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    t = list(a_dictionary.keys())[0]
    g = a_dictionary[t]
    for k, v in a_dictionary.items():
        if v > g:
            g = v
            t = k
    return (t)
