#!/usr/bin/python3
for digit1 in range(0, 10):
    for digit2 in range(0, 10):
        if digit1 == 9 and digit2 == 8:
            print("{}{}".format(digit2, digit1))
        else:
            print("{}{}".format(digit2, digit1), end=", ")
    digit2 = digit1 + 1       
