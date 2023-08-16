#!/usr/bin/python3
def best_score(a_dictionary):
    minimum = 0
    if not a_dictionary:
        return
    for i in a_dictionary:
        minimum = a_dictionary.get(i)
        break
    for i in a_dictionary:
        n = a_dictionary.get(i)
        if n > minimum:
            minimum = n
            maximum = i
    return maximum
