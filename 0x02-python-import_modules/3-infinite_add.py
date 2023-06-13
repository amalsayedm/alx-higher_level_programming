#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    argcount = len(sys.argv) - 1
    for count in range(argcount):
        sum = sum + int(sys.argv[count + 1])
    print("{}".format(sum))
