#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or (not roman_string):
        return 0
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
