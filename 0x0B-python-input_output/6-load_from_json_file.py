#!/usr/bin/python3
"""function to get object from a json string"""
import json


def load_from_json_file(filename):
    """implimenting the function"""
    json_string = ""
    with open(filename, mode="r", encoding="utf-8") as f:
        json_string += f.read()
        return json.loads(json_string)
