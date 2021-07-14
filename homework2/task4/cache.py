"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2


from typing import Callable


def cache(func: Callable) -> Callable:
    ...
"""
from typing import Callable


def cache(func: Callable) -> Callable:
    dict_of_cache = {}

    def check_cache(a, b):
        inputting = f"{str(func)},{a},{b}"
        if inputting in dict_of_cache.keys():
            return dict_of_cache[inputting]
        elif inputting not in dict_of_cache.keys():
            dict_of_cache[inputting] = func(a, b)
            return dict_of_cache[inputting]

    return check_cache
