#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lens = len(sys.argv) - 1
    if lens == 0:
        print("{} arguments.".format(lens))
    elif lens == 1:
        print("{} argument:".format(lens))
    else:
        print("{} arguments:".format(lens))
    for i in range(1, lens+1):
        print("{}: {}".format(i, sys.argv[i]))
