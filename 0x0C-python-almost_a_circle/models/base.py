#!/usr/bin/python3
"""creating a class named Base"""
import json


class Base:
    """implimrnting the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string"""
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json to a file"""
        filename = f"{cls.__name__}.json"
        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """json string to list"""
        my_list = []
        if json_string:
            my_list = json.loads(json_string)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """create an instance of csls"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        filename = f"{cls.__name__}.json"
        obj = []
        with open(filename, mode="r", encoding="utf-8") as file:
            json_string = file.read()
            my_list = json.loads(json_string)
            for i in my_list:
                obj.append(cls.create(**i))

        return obj
