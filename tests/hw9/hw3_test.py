import tempfile

import pytest

from homework9.hw3 import universal_file_counter


@pytest.fixture()
def tmp_files(file_list, values) -> str:
    temp_dir = tempfile.gettempdir()
    for i in file_list:
        temp_file = f"{temp_dir}/file{i}.txt"
        with open(temp_file, "w") as fw:
            fw.write(values[int(i)])
    return temp_dir


@pytest.mark.parametrize(
    "file_list, values",
    [
        (
            ["0", "1", "2"],
            ["1 2 4\n", "2 3", "1\n2"],
        )
    ],
)
def test_counter_with_7_lines_without_tokenizer(tmp_files, file_list, values):
    assert universal_file_counter(tmp_files, "txt", str.split) == 7


@pytest.mark.parametrize(
    "file_list, values",
    [
        (
            ["0", "1", "2"],
            ["4 5\n10", "2\n6 7", "1\n40"],
        )
    ],
)
def test_counter_with_8_tokens_with_tokenizer(tmp_files, file_list, values):
    assert universal_file_counter(tmp_files, "txt", str.split) == 8


@pytest.mark.parametrize(
    "file_list, values",
    [
        (
            ["0", "1", "2"],
            ["4.5.6\n10", "1\n8.2", "1"],
        )
    ],
)
def test_counter_with_10_tokens_with_parametrize_tokenizer(
    tmp_files, file_list, values
):
    assert universal_file_counter(tmp_files, "txt", str.split(".")) == 8
