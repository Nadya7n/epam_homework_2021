import pytest

from homework1.task4.check_sum import check_sum_of_four


def test_checking_sum_of_four_lists_with_3_el():
    """Testing that checking sum of four lists
    is correct when len of lists equals 3
    """
    a = [1, 2, 3]
    b = [57, -1, 53]
    c = [200, 500, 0]
    d = [900, 0, 1000]
    assert check_sum_of_four(a, b, c, d) == 1


def test_checking_sum_of_four_lists_with_0_el():
    """Testing that checking sum of four lists
    is correct when len of lists equals 0
    """
    a, b, c, d = [], [], [], []
    assert check_sum_of_four(a, b, c, d) == 0
