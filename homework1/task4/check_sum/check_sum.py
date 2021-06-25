from collections import Counter
from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    dictionary_of_sums = Counter()
    for element_a in a:
        for element_b in b:
            dictionary_of_sums[element_a + element_b] += 1
    counter = 0
    for element_c in c:
        for element_d in d:
            if -1 * (element_c + element_d) in dictionary_of_sums:
                counter += dictionary_of_sums[-1 * element_c + element_d]
    return counter
