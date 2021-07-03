import pytest

from homework1.task1.calc import check_power_of_2


def test_check_power_of_2_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536) is True


def test_check_power_of_2_negative_case():
    """Testing that non-powers of 2 give False"""
    assert check_power_of_2(12) is False
