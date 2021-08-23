import pytest

from homework2.task2.major_minor import major_and_minor_elem


def test_getting_major_minor_is_positive():
    """
    Testing that function find correct major and minor element
    """
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)
