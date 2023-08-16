#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_list = []
    for i in a_dictionary:
        my_list.append(i)
    my_list.sort()
    for i in my_list:
        print("{}: {}".format(i, a_dictionary[i]))
