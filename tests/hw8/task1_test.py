import tempfile

import pytest

from homework8.task1 import KeyValueStorage


@pytest.fixture
def test_file_correct() -> str:
    text = "name=kek\nlast_name=top\npower=9001\nsong=shadilay"
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/test.txt"
    with open(temp_file, "w") as f:
        f.write(text)
    return temp_file


@pytest.fixture
def test_file_incorrect() -> str:
    text = "name=kek\nlast_name=top\npower=9001\nsong=shadilay\n1=something"
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/test.txt"
    with open(temp_file, "w") as f:
        f.write(text)
    return temp_file


@pytest.fixture
def creation_instance_of_class(test_file_correct):
    storage = KeyValueStorage(test_file_correct)
    return storage


def test_access_through_key(creation_instance_of_class):
    assert creation_instance_of_class["name"] == "kek"


def test_access_trough_attribute(creation_instance_of_class):
    assert creation_instance_of_class.song == "shadilay"


def test_access_trough_attribute_when_value_int(creation_instance_of_class):
    assert creation_instance_of_class.power == "9001"


def test_raising_value_error_when_key_isdigit(test_file_incorrect):
    with pytest.raises(ValueError):
        KeyValueStorage(test_file_incorrect)
