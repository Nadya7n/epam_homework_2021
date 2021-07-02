import pytest

from homework2.task5.iteration import range_function


def test_range_function_is_positive():
    """
    Testing that range function works good
    """
    assert range_function("g", "p") == ["g", "h", "i", "j", "k", "l", "m", "n", "o"]
    assert range_function("p", "g", -2) == ["p", "n", "l", "j", "h"]
