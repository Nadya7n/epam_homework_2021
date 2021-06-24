from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    set_of_sum = set()
    for i in range(len(nums) + 1):
        for j in range(i):
            if len(nums[j: i]) <= k:
                set_of_sum.add(sum(nums[j: i]))
    return max(set_of_sum)
