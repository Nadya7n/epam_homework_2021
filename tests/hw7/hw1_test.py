import pytest

from homework7 import hw1

my_example = {"first": [1, 1, 1, True], True: {"True", "1", 1}}


def test_with_sample_from_task():
    """
    Testing that function find_occurrences works correct with data sample from task
    :return: None
    """
    result = hw1.find_occurrences(hw1.example_tree, "RED")
    assert result == 6


def test_with_my_sample_with_int_and_bool():
    """
    Testing that function find_occurrences works correct with my data sample, when we are searching
    integer 1 or bool True
    :return: None
    """
    result_1 = hw1.find_occurrences(my_example, 1)
    result_2 = hw1.find_occurrences(my_example, True)
    assert result_1 == 4
    assert result_2 == 2


def test_with_my_sample_with_set():
    """
    Testing that function find_occurrences works correct with my data sample, when we are searching
    complex structure - set
    :return: None
    """
    result = hw1.find_occurrences(my_example, {"True", "1", 1})
    assert result == 1
