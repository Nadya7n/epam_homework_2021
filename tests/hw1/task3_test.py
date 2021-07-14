import os

import pytest

from homework1.task3.min_max import find_maximum_and_minimum


def test_finding_max_min_in_file_with_3_el():
    """Testing that finding maximum and minimum is correct"""
    path_to_file_1 = os.path.join(os.path.dirname(__file__), "./task3_file1.txt")
    my_file = open(path_to_file_1, "w+")
    my_file.write("45\n")
    my_file.write("99\n")
    my_file.write("104\n")
    my_file.close()
    assert find_maximum_and_minimum("task3_file1.txt") == (45, 104)


def test_finding_max_min_in_file_with_1_el():
    """Testing that finding maximum and minimum
    is correct when number of line = 1
    """
    path_to_file_2 = os.path.join(os.path.dirname(__file__), "./task3_file2.txt")
    my_file = open(path_to_file_2, "w+")
    my_file.write("1")
    my_file.close()
    assert find_maximum_and_minimum("task3_file2.txt") == (1, 1)
