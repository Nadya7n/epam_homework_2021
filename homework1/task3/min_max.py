from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    set_of_numbers = set()
    with open(file_name) as fh:
        for line in fh:
            set_of_numbers.add(int(line.strip("\n")))
    return tuple((min(set_of_numbers), max(set_of_numbers)))
