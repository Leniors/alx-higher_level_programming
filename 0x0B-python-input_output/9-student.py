#!/usr/bin/python3
"""class student"""


class Student:
    """defining class student"""

    def __init__(self, first_name, last_name, age):
        """initializing"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to json"""
        def serialize(obj):
            if isinstance(obj, dict):
                return {key: serialize(value) for key, value in obj.items()}
            elif isinstance(obj, list):
                return [serialize(item) for item in obj]
            elif isinstance(obj, str):
                return obj
            elif isinstance(obj, int):
                return obj
            elif isinstance(obj, bool):
                return obj
            else:
                raise ValueError("Unsupported data type")

        student_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        return serialize(student_dict)
