#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_list = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            my_list.append(i)
    for i in my_list:
        del a_dictionary[i]
    return a_dictionary
