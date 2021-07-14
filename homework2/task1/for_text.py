"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document

from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    ...


def get_rarest_char(file_path: str) -> str:
    ...


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...
"""
import unicodedata
from typing import List


def get_longest_diverse_words(file_path: str, encoding="utf8") -> List[str]:
    set_of_unique = set()
    file_input = open(file_path, encoding=encoding)
    for line in file_input:
        line = line.encode().decode("unicode-escape")
        for el in line.split():
            if el not in set_of_unique:
                set_of_unique.add((len(set(el)) + len(el), el))
    return [i[1] for i in sorted(set_of_unique)[:-11:-1]]


def get_rarest_char(file_path: str, encoding="utf8") -> str:
    dict_of_unique_symbol = {}
    file_input = open(file_path, encoding=encoding)
    for line in file_input:
        line = line.encode().decode("unicode-escape")
        for el in line.split():
            for el_2 in el:
                if el_2 not in dict_of_unique_symbol:
                    dict_of_unique_symbol[el_2] = 1
                else:
                    dict_of_unique_symbol[el_2] += 1
    return [key for key, value in dict_of_unique_symbol.items() if value == 1][0]


def count_punctuation_chars(file_path: str, encoding="utf8") -> int:
    dict_of_punctuation_chars = {"punctuation": 0}
    file_input = open(file_path, encoding=encoding)
    for line in file_input:
        line = line.encode().decode("unicode-escape")
        for el in line.split():
            for el_2 in el:
                if unicodedata.category(el_2).startswith("P"):
                    dict_of_punctuation_chars["punctuation"] += 1
    return sum(dict_of_punctuation_chars.values())


def count_non_ascii_chars(file_path: str, encoding="utf8") -> int:
    result_score = 0
    file_input = open(file_path, encoding=encoding)
    for line in file_input:
        line = line.encode().decode("unicode-escape")
        for el in line:
            for char in el:
                if ord(char) > 127:
                    result_score += 1
    return result_score


def get_most_common_non_ascii_char(file_path: str, encoding="utf8") -> str:
    counter = {}
    file_input = open(file_path, encoding=encoding)
    for line in file_input:
        line = line.encode().decode("unicode-escape")
        for el in line:
            for char in el:
                if ord(char) > 127:
                    if char not in counter:
                        counter[char] = 1
                    else:
                        counter[char] += 1
    max_key = 0
    max_value = 0
    for key, value in counter.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
