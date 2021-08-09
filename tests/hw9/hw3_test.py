import os

import pytest

from homework9.hw3 import universal_file_counter


def test_counter_with_6_lines_without_tokenizer():
    path_to_dir = f"{os.path.dirname(__file__)}"
    assert universal_file_counter(path_to_dir, "txt") == 5


def test_counter_with_10_tokens_with_tokenizer():
    path_to_dir = f"{os.path.dirname(__file__)}"
    assert universal_file_counter(path_to_dir, "txt", str.split) == 7


def test_counter_with_10_tokens_with_parametrize_tokenizer():
    path_to_dir = f"{os.path.dirname(__file__)}"
    assert universal_file_counter(path_to_dir, "txt", str.split(".")) == 8
