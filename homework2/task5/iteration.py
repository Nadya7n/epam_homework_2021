"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(*args):
    iter_object = list(args[0])
    start = 0
    step = 1
    if len(args) == 2:
        stop = iter_object.index(args[1])
    elif len(args) == 3:
        start = iter_object.index(args[1])
        stop = iter_object.index(args[2])
    else:
        start = iter_object.index(args[1])
        stop = iter_object.index(args[2])
        step = args[3]
    return iter_object[start:stop:step]
