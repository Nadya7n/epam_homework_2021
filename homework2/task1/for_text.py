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
from operator import itemgetter
from typing import Iterator, List


def encoding_file(file_path: str, encoding="unicode-escape") -> Iterator:
    """
    Generator that return lines from encoding file
    :param file_path: path to file, str
    :param encoding: mode to encode file, by default utf8 mode
    :return: Iterator
    """
    file_input = open(file_path, encoding=encoding)
    for line in file_input:
        yield line


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Find 10 longest words consisting
    from largest amount of unique symbols
    :param file_path: path to file, str
    :return: list of 10 longest diverse words
    """
    dict_of_unique = {}
    for line in encoding_file(file_path):
        for el in line.split():
            if el not in dict_of_unique.keys():
                dict_of_unique[el] = len(set(el)) + len(el)

    maximum_value = sorted(
        list(dict_of_unique.items()), key=itemgetter(1), reverse=True
    )
    return [key for key in dict(maximum_value[:10]).keys()]


def get_rarest_char(file_path: str) -> str:
    """
    Find rarest symbol for document
    :param file_path: path to file, str
    :return: rarest symbol, str
    """
    dict_of_unique_symbol = {}
    for line in encoding_file(file_path):
        for el in line.split():
            for el_2 in el:
                if el_2 not in dict_of_unique_symbol:
                    dict_of_unique_symbol[el_2] = 1
                else:
                    dict_of_unique_symbol[el_2] += 1
    return min(dict_of_unique_symbol, key=dict_of_unique_symbol.get)


def count_punctuation_chars(file_path: str) -> int:
    """
    Count every punctuation char for document
    :param file_path: path to file, str
    :return: number of all punctuation char, int
    """
    counter_punctuation_chars = 0
    for line in encoding_file(file_path):
        for el in line.split():
            for el_2 in el:
                if unicodedata.category(el_2).startswith("P"):
                    counter_punctuation_chars += 1
    return counter_punctuation_chars


def count_non_ascii_chars(file_path: str) -> int:
    """
    Count every non ascii char for document
    :param file_path: path to file, str
    :return: number of all non ascii char, int
    """
    result_score = 0
    for line in encoding_file(file_path):
        for el in line:
            for char in el:
                if ord(char) > 127:
                    result_score += 1
    return result_score


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Find most common non ascii char for document
    :param file_path: path to file, str
    :return: most common non ascii char, str
    """
    counter = {}
    for line in encoding_file(file_path):
        for el in line:
            for char in el:
                if ord(char) > 127:
                    if char not in counter:
                        counter[char] = 1
                    else:
                        counter[char] += 1

    return max(counter, key=counter.get)
