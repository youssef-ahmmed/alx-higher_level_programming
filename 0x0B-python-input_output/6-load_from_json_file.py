#!/usr/bin/python3
"""Module for `load_from_json_file` function"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a `JSON file`"""
    with open(filename, mode="r", encoding="UTF-8") as f:
        return json.load(f)
