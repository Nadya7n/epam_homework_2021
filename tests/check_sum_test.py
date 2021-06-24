import pytest

from homework1.task4.check_sum_of_four.check_sum_of_four import check_sum_of_four


def test_correct_work_1000():
    """Testing that checking sum of four lists is correct when len of lists equals 1000"""
    a, b, c, d = [], [], [], []
    for i in range(1000):
        a.append(-1)
        b.append(1)
        c.append(0)
        d.append(0)
    assert check_sum_of_four(a, b, c, d)


def test_correct_work_0():
    """Testing that checking sum of four lists is correct when len of lists equals 0"""
    a, b, c, d = [], [], [], []
    assert not check_sum_of_four(a, b, c, d)
