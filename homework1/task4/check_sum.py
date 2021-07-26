"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.

from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    ...
"""
from collections import Counter
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    dictionary_of_sums = Counter()
    for el_a in a:
        for el_b in b:
            dictionary_of_sums[el_a + el_b] += 1
    counter = 0
    for el_c in c:
        for el_d in d:
            if -1 * (el_c + el_d) in dictionary_of_sums:
                counter += dictionary_of_sums[-1 * (el_c + el_d)]
    return counter
