import pytest

from homework3.task4.Armstrong import is_armstrong


def test_function_is_armstrong_positive_case():
    """
    Testing that function is_armstrong works correct in positive case
    """
    assert is_armstrong(9) is True


def test_function_is_armstrong_negative_case():
    """
    Testing that function is_armstrong works correct in negative case
    """
    assert is_armstrong(10) is False
