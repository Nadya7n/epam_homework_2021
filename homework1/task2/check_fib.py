"""
'''
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.
'''

from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    ...
"""
from typing import Sequence


def fibonacci(start):
    first, second = 0, 1
    while True:
        if first >= start:
            yield first
        first, second = second, first + second


def check_fibonacci(data: Sequence[int]) -> bool:
    if not data:
        return False
    else:
        if all([isinstance(i, int) for i in data]):
            for values_from_data, from_fibonacci in zip(data, fibonacci(data[0])):
                if values_from_data != from_fibonacci:
                    return False
            return True
        else:
            return False
