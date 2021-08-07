import pytest

from homework3.task1.decorator import cache


def test_correct_work_of_cache():
    """
    Testing that cache function works correct
    """

    @cache(times=2)
    def func(*args):
        return args

    args_1 = (123, 12)
    args_2 = (12, 13)

    val_1 = func(*args_1)
    val_2 = func(*args_1)
    val_3 = func(*args_2)
    val_4 = func(*args_1)

    assert val_1 is val_2 and val_1 is val_4 and val_1 is not val_3
