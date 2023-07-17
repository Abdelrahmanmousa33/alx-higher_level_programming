#!/usr/bin/python3
"""Defines a base model class."""


class Base:
    """Base model for all classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initilizing new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of a list of dicts"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
