#!/usr/bin/python3
"""student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            # If attrs is not specified, retrieve all attributes
            return self.__dict__

        # Initialize an empty dictionary to store the selected attributes
        selected_attrs = {}

        # Loop through the attrs list and only include valid attributes
        for attr in attrs:
            if hasattr(self, attr):
                selected_attrs[attr] = getattr(self, attr)

        return selected_attrs

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
