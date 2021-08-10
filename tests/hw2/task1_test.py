import os
import tempfile

import pytest

from homework2.task1 import for_text


@pytest.fixture()
def temp_file() -> str:
    text = "фафаа\n\u006e\u0072\n--\nssuummeerr\naa\naaaabbbbcccc\n))\n!!\n..\n,,\nr)\n"
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/task1_file1.txt"
    with open(temp_file, "w") as fw:
        fw.write(text)
    return temp_file


def test_get_longest_diverse_words_with_unicode(temp_file):
    """Testing that actual diversity of words is positive"""
    correct = [
        "ssuummeerr",
        "aaaabbbbcccc",
        "Ñ\x84Ð°Ñ\x84Ð°Ð°",
        "nr",
        "r)",
        "--",
        "aa",
        "))",
        "!!",
        "..",
    ]
    assert for_text.get_longest_diverse_words(temp_file) == correct


def test_get_rarest_char_with_unicode(temp_file):
    """Testing that get rarest char is positive"""
    assert for_text.get_rarest_char(temp_file) == "n"


def test_count_punctuation_chars_with_unicode(temp_file):
    """Testing that count punctuation char is positive"""
    assert for_text.count_punctuation_chars(temp_file) == 11


def test_count_non_ascii_chars_with_unicode(temp_file):
    """Testing that count non-ascii char is positive"""
    assert for_text.count_non_ascii_chars(temp_file) == 10


def test_get_most_common_non_ascii_char_with_unicode(temp_file):
    """Testing that get most common non-ascii char is positive"""
    assert for_text.get_most_common_non_ascii_char(temp_file) == "Ð"
