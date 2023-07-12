#!/usr/bin/python3
"""Module for `Student` class"""


class Student:
    """Define a `Student` class"""

    def __init__(self, first_name, last_name, age):
        """Initialization of `Student` class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, val in self.__dict__.items():
            setattr(self, key, val)
