"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
# [1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def read_files(list_with_files: str) -> Iterator:
    for file in list_with_files:
        with open(file) as fh:
            for line in fh:
                yield int(line.strip())


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    for item in sorted(list(read_files(file_list))):
        yield item
