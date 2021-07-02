import string


def range_function(start="a", stop="z", step=1):
    set_of_vowels = list(string.ascii_lowercase)
    start = set_of_vowels.index(start)
    stop = set_of_vowels.index(stop)
    list_of_range = set_of_vowels[start:stop:step]
    return list_of_range
