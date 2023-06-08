#!/usr/bin/python3
import sys


def infinite_add(argv, n):
    sum = 0
    for i in range(0, n):
        sum += argv[i]

    print(sum)


if __name__ == "__main__":

    n = len(sys.argv) - 1
    int_argument = [int(arg) for arg in sys.argv[1:]]
    if n == 0:
        print('{:d}'.format(0))
    else:
        infinite_add(int_argument, n)
