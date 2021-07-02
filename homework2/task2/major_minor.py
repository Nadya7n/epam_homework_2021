from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    dict_of_occurrence = {}
    for el in inp:
        if el not in dict_of_occurrence:
            dict_of_occurrence[el] = 1
        else:
            dict_of_occurrence[el] += 1

    max_value = max(
        [value for value in dict_of_occurrence.values() if value >= len(inp) // 2]
    )
    max_key = [key for key, value in dict_of_occurrence.items() if value == max_value]

    min_value = min([value for value in dict_of_occurrence.values()])
    min_key = [key for key, value in dict_of_occurrence.items() if value == min_value]

    return tuple((max_key[0], min_key[0]))
