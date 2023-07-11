#!/usr/bin/python3
"""Module for `read_file` function"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r') as f:
        data = f.read()

    print(data)
