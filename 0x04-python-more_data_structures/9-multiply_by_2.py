#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i in a_dictionary:
        n = a_dictionary.get(i)
        new_dictionary[i] = n * 2
    return new_dictionary
