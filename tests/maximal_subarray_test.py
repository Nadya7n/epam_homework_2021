import pytest

from homework1.task5.maximum_subarray.maximum_subarray import find_maximal_subarray_sum


def test_correct_k_maximum():
    """Testing that finding maximal sub-array sum is correct at the maximum k"""
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 4
    assert find_maximal_subarray_sum(nums, k)


def test_correct_k_minimum():
    """Testing that finding maximal sub-array sum is correct at the minimum k"""
    nums = [334, -334, -3, 4, 5, 6, 7]
    k = 4
    assert find_maximal_subarray_sum(nums, k)


def test_correct_k_average():
    """Testing that finding maximal sub-array sum is correct at the average k"""
    nums = [334, 334, -300, 4, 5, 6, 7]
    k = 3
    assert find_maximal_subarray_sum(nums, k)


def test_correct_k_equal_list_len():
    """Testing that finding maximal sub-array sum is correct at the average k"""
    nums = [334]
    k = 1
    assert find_maximal_subarray_sum(nums, k)
