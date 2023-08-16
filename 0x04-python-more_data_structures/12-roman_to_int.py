#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    prev = 0
    char = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    for i in reversed(roman_string):
        value = char[i]
        if value >= prev:
            total += value
        else:
            total -= value
        prev = value
    return total
