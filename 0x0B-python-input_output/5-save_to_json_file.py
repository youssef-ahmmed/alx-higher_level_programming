#!/usr/bin/python3
"""Module for `save_to_json_file` function"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file
        using a JSON representation"""
    with open(filename, mode="w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
