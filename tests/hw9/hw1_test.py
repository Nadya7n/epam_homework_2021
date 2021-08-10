import tempfile

import pytest

from homework9.hw1 import merge_sorted_files


@pytest.fixture()
def tmp_files(file_list, values) -> str:
    list_of_files = []
    temp_dir = tempfile.gettempdir()
    for i in range(len(file_list)):
        temp_file = f"{temp_dir}/file{i}.txt"
        with open(temp_file, "w") as fw:
            fw.write(values[int(i)])
        list_of_files.append(temp_file)
    return list_of_files


@pytest.mark.parametrize(
    "file_list, values",
    [
        (
            ["1", "2"],
            ["1\n3\n5", "2\n4\n6"],
        )
    ],
)
def test_merging_sorted_2_files(tmp_files, file_list, values):
    assert list(merge_sorted_files(tmp_files)) == [1, 2, 3, 4, 5, 6]


@pytest.mark.parametrize(
    "file_list, values",
    [
        (
            ["1", "2", "3"],
            ["4\n10", "2\n6", "1\n40"],
        )
    ],
)
def test_merging_sorted_3_files(tmp_files, file_list, values):
    assert list(merge_sorted_files(tmp_files)) == [1, 2, 4, 6, 10, 40]


@pytest.mark.parametrize(
    "file_list, values",
    [
        (
            ["1", "2"],
            ["4\n10", ""],
        )
    ],
)
def test_merging_sorted_with_one_empty_file(tmp_files, file_list, values):
    assert list(merge_sorted_files(tmp_files)) == [4, 10]
