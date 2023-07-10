#!/usr/bin/python3
"""Defines an inherited list class MyList"""


class MyList(list):
    """Defines an inherited list class MyList."""

    def print_sorted(self):
        """print a list in ascending order"""
        return (sorted(self))
