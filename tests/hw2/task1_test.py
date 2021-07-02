import pytest

from homework2.task1.for_text import (count_non_ascii_chars,
                                      count_punctuation_chars,
                                      get_longest_diverse_words,
                                      get_most_common_non_ascii_char,
                                      get_rarest_char)

file_path = "task1_file1.txt"


def test_get_longest_diverse_words_with_unicode():
    """Testing that actual diversity of words is positive"""
    correct = [
        "ssuummeerr",
        "aaaabbbbcccc",
        "Ñ\x84Ð°Ñ\x84Ð°Ð°",
        "nr",
        "aa",
        "..",
        "--",
        ",,",
        "))",
        "!!",
    ]
    assert get_longest_diverse_words(file_path) == correct


def test_get_rarest_char_with_unicode():
    """Testing that get rarest char is positive"""
    assert get_rarest_char(file_path) == "n"


def test_count_punctuation_chars_with_unicode():
    """Testing that count punctuation char is positive"""
    assert count_punctuation_chars(file_path) == 10


def test_count_non_ascii_chars_with_unicode():
    """Testing that count non-ascii char is positive"""
    assert count_non_ascii_chars(file_path) == 10


def test_get_most_common_non_ascii_char_with_unicode():
    """Testing that get most common non-ascii char is positive"""
    assert get_most_common_non_ascii_char(file_path) == "Ð"
