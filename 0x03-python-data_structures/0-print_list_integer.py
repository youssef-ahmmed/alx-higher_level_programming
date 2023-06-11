#!/usr/bin/python3
def print_list_integer(my_list=[]):
    n = len(my_list)
    for i in range(n):
        print('{:d}'.format(my_list[i]))
