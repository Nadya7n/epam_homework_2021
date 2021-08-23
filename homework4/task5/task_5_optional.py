"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests

#
# >>> list(fizzbuzz(5))
# ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator[None, None, str]:
    """
    Function takes a number N as an input,
    returns N FizzBuzz numbers

    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']

    >>> list(fizzbuzz(1))
    ['1']

    >>> list(fizzbuzz(15))
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    """
    return map(
        lambda i: "fizz" * (i % 3 == 0) + "buzz" * (i % 5 == 0) or str(i),
        range(1, n + 1),
    )
