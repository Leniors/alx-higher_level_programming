#!/usr/bin/python3
"""function that writes a json string to a file"""
import json


def save_to_json_file(my_obj, filename):
    """implimenting the function"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json_string = json.dumps(my_obj)
        f.write(json_string)
