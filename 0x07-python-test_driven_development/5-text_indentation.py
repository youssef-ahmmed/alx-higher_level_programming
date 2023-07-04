#!/usr/bin/python3
"""Defines a printing text indented function"""


def text_indentation(text):
    """Printing a text with 2 new lines after
        each of these characters: `.`, `?` and `:`

    :param text: to be modified
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    formatted_str = (text.strip()
                         .replace('. ', '.\n\n')
                         .replace(': ', ':\n\n')
                         .replace('? ', '?\n\n'))
        
