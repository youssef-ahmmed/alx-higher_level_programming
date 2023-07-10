#!/usr/bin/python3
"""Module for `MyInt` class"""


class MyInt(int):
    """Rebel Int class"""

    def __eq__(self, other):
        """Inverted equal"""
        return self.real != other.real

    def __ne__(self, other):
        """Inverted not-equal"""
        return self.real == other.real
