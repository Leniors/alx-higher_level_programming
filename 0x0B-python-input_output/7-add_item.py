#!/usr/bin/python3
"""function thats adds arguments to a list"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    my_list = []
    my_list = load_from_json_file("add_item.json")
except:
    pass

for arg in sys.argv:
    if arg == sys.argv[0]:
        continue
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
