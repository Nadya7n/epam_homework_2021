import pytest

from homework2.task5.iteration import custom_range


def test_range_function_is_positive():
    """
    Testing that range function works good
    """
    iterable_object = ["abc", 12, 0.76, "e", 90, "()"]
    assert custom_range(iterable_object, "e") == ["abc", 12, 0.76]
    assert custom_range(iterable_object, 12, "e") == [12, 0.76]
    assert custom_range(iterable_object, 90, 12, -2) == [90, 0.76]
