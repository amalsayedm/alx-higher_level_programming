#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for col in matrix:
        for row in col:
            print("{:d}".format(row), end=" ")
        print()
