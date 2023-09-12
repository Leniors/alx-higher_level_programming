#!/usr/bin/python3
"""return object"""


def class_to_json(obj):
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, bool):
        return obj
