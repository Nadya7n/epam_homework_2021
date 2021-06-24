import pytest

from homework1.task3.min_max.min_max import find_maximum_and_minimum


def test_correcting_work():
    """Testing that finding maximum and minimum correct"""
    assert find_maximum_and_minimum("sample_1.txt")


def test_correcting_work_1_line():
    """Testing that finding maximum and minimum correct when number of line = 1"""
    assert find_maximum_and_minimum("sample_2.txt")
