import pytest

from homework2.task4.cache import cache


def func(a, b):
    return (a ** b) ** 2


def test_good_working_of_cache_func():
    """
    Testing that cache function works good
    """
    cache_func = cache(func)
    some = 2, 3
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2
