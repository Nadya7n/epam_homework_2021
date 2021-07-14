import os

import pytest

from homework2.task1 import for_text

path_to_file = os.path.join(os.path.dirname(__file__), "./task1_file1.txt")
file = open(path_to_file, "w+")
file.write(
    "фафаа\n\u006e\u0072\n--\nssuummeerr\naa\naaaabbbbcccc\n))\n!!\n..\n,,\nr)\n"
)
file.close()


def test_get_longest_diverse_words_with_unicode():
    """Testing that actual diversity of words is positive"""
    correct = [
        "ssuummeerr",
        "aaaabbbbcccc",
        "Ñ\x84Ð°Ñ\x84Ð°Ð°",
        "r)",
        "nr",
        "aa",
        "..",
        "--",
        ",,",
        "))",
    ]
    assert for_text.get_longest_diverse_words(path_to_file) == correct


def test_get_rarest_char_with_unicode():
    """Testing that get rarest char is positive"""
    assert for_text.get_rarest_char(path_to_file) == "n"


def test_count_punctuation_chars_with_unicode():
    """Testing that count punctuation char is positive"""
    assert for_text.count_punctuation_chars(path_to_file) == 11


def test_count_non_ascii_chars_with_unicode():
    """Testing that count non-ascii char is positive"""
    assert for_text.count_non_ascii_chars(path_to_file) == 10


def test_get_most_common_non_ascii_char_with_unicode():
    """Testing that get most common non-ascii char is positive"""
    assert for_text.get_most_common_non_ascii_char(path_to_file) == "Ð"
