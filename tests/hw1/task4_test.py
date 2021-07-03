import pytest

from homework1.task4.check_sum import check_sum_of_four


def test_checking_sum_of_four_lists_with_1000_el():
    """Testing that checking sum of four lists
    is correct when len of lists equals 1000
    """
    a, b, c, d = [], [], [], []
    for i in range(1000):
        a.append(-1)
        b.append(1)
        c.append(0)
        d.append(0)
    assert check_sum_of_four(a, b, c, d)


def test_checking_sum_of_four_lists_with_0_el():
    """Testing that checking sum of four lists
    is correct when len of lists equals 0
    """
    a, b, c, d = [], [], [], []
    assert check_sum_of_four(a, b, c, d) == 0
