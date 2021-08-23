import os

import pytest

from homework8.task2 import TableData


@pytest.fixture
def creation_instance():
    """
    Create the instance of class TableData
    :return: instance of TableData
    """
    path_to_file = os.path.join(os.path.dirname(__file__), "./example.sqlite")
    presidents = TableData(path_to_file, "presidents")
    return presidents


def test_access_through_key(creation_instance):
    """
    Testing that access through key works correct
    :param creation_instance: pytest fixture
    """
    assert creation_instance["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_contains_item_in_table_data(creation_instance):
    """
    Testing that check if row with key name exists in table works correct
    :param creation_instance: pytest fixture
    """
    assert ("Yeltsin" in creation_instance) is True


def test_correct_detection_of_length(creation_instance):
    """
    Testing that detection of length is correct
    :param creation_instance: pytest fixture
    """
    assert len(creation_instance) == 3


def test_ability_to_iterate_in_loop(creation_instance):
    """
    Testing that instance of class has an ability to be iterable
    :param creation_instance: pytest fixture
    """
    counter = -1
    answer = [
        ("Yeltsin", 999, "Russia"),
        ("Trump", 1337, "US"),
        ("Big Man Tyrone", 101, "Kekistan"),
    ]
    for element in creation_instance:
        counter += 1
        assert element == answer[counter]
