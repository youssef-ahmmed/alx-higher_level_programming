#!/usr/bin/python3
"""Module for `Student` class"""


class Student:
    """Define a `Student` class"""
    def __init__(self, first_name, last_name, age):
        """Initialization of `Student` class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
