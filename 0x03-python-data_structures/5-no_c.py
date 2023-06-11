#!/usr/bin/python3
def no_c(my_string):
    remove_C = 'Cc'
    new_str = ''.join([char for char in my_string if char not in remove_C])
    return new_str
