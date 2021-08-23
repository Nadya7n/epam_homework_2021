"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List

import pytest


def fizzbuzz(n: int) -> List[str]:
    """
    Function takes a number N as an input,
    returns N FizzBuzz numbers

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(1)
    ['1']

    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz']
    """

    return_list = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            i = "fizz buzz"
        elif i % 3 == 0:
            i = "fizz"
        elif i % 5 == 0:
            i = "buzz"
        else:
            i = str(i)
        return_list.append(i)
    return return_list
