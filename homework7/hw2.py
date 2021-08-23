"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
from itertools import zip_longest


def remove_all_vowel_before_sharp(string: str):
    counter_sharp, i = 0, -1
    string = list(reversed(string))
    while i != len(string) - 1:
        i += 1
        if string[i] != "#" and counter_sharp != 0:
            string[i : i + counter_sharp] = "#" * counter_sharp
            i = i + counter_sharp - 1
        if string[i] == "#":
            counter_sharp += 1

    for el in reversed(string):
        if el == "#":
            string.remove(el)

    return string


def compare_strings_with_backspace(first: str, second: str):
    first = remove_all_vowel_before_sharp(first)
    second = remove_all_vowel_before_sharp(second)
    for el_1, el_2 in zip_longest(first, second):
        if el_1 != el_2:
            return False
    return True
