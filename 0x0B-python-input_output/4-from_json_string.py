#!/usr/bin/python3
"""function to turn json string to object"""
import json


def from_json_string(my_str):
    """implimenting the function"""
    return json.loads(my_str)
