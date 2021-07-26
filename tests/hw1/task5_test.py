import pytest

from homework1.task5.maximum_subarray import find_maximal_sub_array_sum


def test_finding_maximal_sub_array_with_length_3():
    """Testing that finding maximal sub-array sum
    is correct at the maximum k
    """
    nums = [0, 0, 3, 10, 7]
    k = 4
    assert find_maximal_sub_array_sum(nums, k) == 20


def test_finding_maximal_sub_array_with_length_1():
    """Testing that finding maximal sub-array sum
    is correct at the minimum k
    """
    nums = [334, -334, -3, 4, 5]
    k = 4
    assert find_maximal_sub_array_sum(nums, k) == 334


def test_finding_maximal_sub_array_with_length_2():
    """Testing that finding maximal sub-array sum
    is correct at the average k
    """
    nums = [334, 334, -300, 4, 5]
    k = 3
    assert find_maximal_sub_array_sum(nums, k) == 668


def test_finding_maximal_sub_array_in_list_where_1_el():
    """Testing that finding maximal sub-array sum
    is correct at the average k
    """
    nums = [334]
    k = 1
    assert find_maximal_sub_array_sum(nums, k) == 334
