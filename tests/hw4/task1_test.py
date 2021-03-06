import os
import tempfile

import pytest

from homework4.task1.task_1_read_file import read_magic_number


@pytest.fixture()
def test_file(param) -> str:
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/test.txt"
    with open(temp_file, "w") as f:
        f.write(param)
    yield temp_file
    os.remove(temp_file)


@pytest.mark.parametrize("param", ["1", "2"])
def test_reading_magic_number_positive_case(test_file, param):
    assert read_magic_number(test_file) is True


@pytest.mark.parametrize("param", ["12", "are", ""])
def test_reading_magic_number_negative_case(test_file, param):
    assert read_magic_number(test_file) is False


def test_reading_magic_number_file_error():
    with pytest.raises(ValueError):
        read_magic_number("test.txt")
