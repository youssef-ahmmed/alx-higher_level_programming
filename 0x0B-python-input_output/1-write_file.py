#!/usr/bin/python3
"""Module for `write_file` function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
        and returns the number of characters written"""
    with open(filename, mode="w", encoding="UTF-8") as f:
        f.write(text)
        tell = f.tell()

    return tell
