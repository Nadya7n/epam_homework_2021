import pytest

from homework2.task3.mix_of_lists import combinations


def test_good_working_of_mix_lists():
    """
    Testing that function combinations works good
    """
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]
