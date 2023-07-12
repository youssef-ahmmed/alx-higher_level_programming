#!/usr/bin/python3
"""Module for `append_after` function"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
        after each line containing a specific string """
    text = ""
    with open(filename, mode='r', encoding='UTF-8') as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode='w', encoding='UTF-8') as file:
        file.write(text)
