"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16

from typing import List


def find_maximal_sub_array_sum(nums: List[int], k: int) -> int:
    ...
"""
from typing import List


def find_maximal_sub_array_sum(nums: List[int], k: int) -> int:
    set_of_sum = set()
    for i in range(len(nums) + 1):
        for j in range(i):
            slice_of_list = nums[j:i]
            if len(slice_of_list) <= k:
                set_of_sum.add(sum(slice_of_list))
    return max(set_of_sum)
