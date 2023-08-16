#!/usr/bin/python3
def roman_to_int(roman_string):
    my_list = []
    if not roman_string:
        return (0)
    for j in range(len(roman_string)):
        if roman_string[j] == "M" and roman_string[j - 1] != "C":
            my_list.append(1000)
        elif roman_string[j] == "X" and roman_string[j - 1] == "I":
            my_list.append(8)
        elif roman_string[j] == "C" and roman_string[j - 1] == "X":
            my_list.append(80)
        elif roman_string[j] == "M" and roman_string[j - 1] == "C":
            my_list.append(800)
        elif roman_string[j] == "I":
            my_list.append(1)
        elif roman_string[j] == "V":
            my_list.append(5)
        elif roman_string[j] == "X":
            my_list.append(10)
        elif roman_string[j] == "L":
            my_list.append(50)
        elif roman_string[j] == "C":
            my_list.append(100)
        elif roman_string[j] == "D":
            my_list.append(500)
    return sum(my_list)
