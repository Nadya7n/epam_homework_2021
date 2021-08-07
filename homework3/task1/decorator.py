"""
In previous homework task 4, you wrote a cache function
that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')
        # careful with input() in python2, use raw_input() instead

    # >>> f()
    ? 1
    '1'
    # >>> f()     # will remember previous value
    '1'
    # >>> f()     # but use it up to two times only
    '1'
    # >>> f()
    ? 2
    '2'
"""
from typing import Callable


def cache(times) -> Callable:
    dict_of_cache = {}
    counter_cache = []

    def check_cache(function):
        def check_times(*args, **kwargs):
            inputting = f"{str(function)},{[*args, *kwargs]}"
            if inputting in dict_of_cache.keys():
                counter_cache[0] = counter_cache[0] + 1
                if counter_cache[0] <= times:
                    return dict_of_cache[inputting]
                elif counter_cache[0] > times:
                    counter = 0
                    counter_cache[0] = counter
                    dict_of_cache[inputting] = function(args, kwargs)
                    return dict_of_cache[inputting]

            elif inputting not in dict_of_cache.keys():
                counter = 0
                counter_cache.append(counter)
                dict_of_cache[inputting] = function(args, kwargs)
                return dict_of_cache[inputting]

        return check_times

    return check_cache
