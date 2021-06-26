from math import sqrt
from typing import Sequence


def is_fibonacci(element) -> bool:
    element_1 = 5 * element ** 2 - 4
    element_2 = 5 * element ** 2 + 4
    if element == 0:
        return True
    else:
        if sqrt(element_1).is_integer() or sqrt(element_2).is_integer():
            return True
        else:
            return False


def check_fibonacci(data: Sequence[int]) -> bool:
    answer = True
    if not data:
        answer = False
    else:
        for element in data:
            answer &= is_fibonacci(int(element))
    return answer
