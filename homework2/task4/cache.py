from typing import Callable


def cache(func: Callable) -> Callable:
    cache_list = list()

    def check_cache(a, b):
        if func in cache_list:
            for i in cache_list:
                if i == func:
                    return i
        elif func not in cache_list:
            cache_list.append(func)
            for i in cache_list:
                if i == func:
                    return i

    return check_cache
