#!/usr/bin/python3
# 12-roman_to_int.py


def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0
    length = len(roman_string)

    for i in range(length):
        if roman_string[i] not in roman_dict:
            return 0

        if i != (length - 1) and
        roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            num -= roman_dict[roman_string[i]]
        else:
            num += roman_dict[roman_string[i]]
    return num
