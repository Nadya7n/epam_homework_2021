import pytest

from homework1.task3.min_max import find_maximum_and_minimum


def test_correct_work():
    """Testing that finding maximum and minimum is correct"""
    my_file = open("task3_file1.txt", "w+")
    my_file.write("45")
    my_file.write("99")
    my_file.write("104")
    my_file.close()
    assert find_maximum_and_minimum("task3_file1.txt")


def test_correct_work_1_line():
    """Testing that finding maximum and minimum
    is correct when number of line = 1
    """
    my_file = open("task3_file2.txt", "w+")
    my_file.write("1")
    my_file.close()
    assert find_maximum_and_minimum("task3_file2.txt")
