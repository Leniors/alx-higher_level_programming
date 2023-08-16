#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    total = 0
    for i in my_list:
        a, b = i
        total += a * b
        weight += b
    return total / weight
