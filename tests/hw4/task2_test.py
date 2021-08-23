import mock
import pytest

from homework4.task2.task_2_mock_input import count_dots_on_i


@mock.patch("homework4.task2.task_2_mock_input.take_text_from_page")
def test_positive_case_of_request(mock_service_func):
    mock_service_func.return_value = "iii"
    assert count_dots_on_i("any path") == 3
