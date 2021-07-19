import pytest
import requests_mock

from homework4.task2.task_2_mock_input import count_dots_on_i


# пока не сообразила, как прописать, чтобы без инета тоже работал
def test_positive_case_of_request():
    with requests_mock.Mocker() as mock_request:
        mock_request.get("https://example.com/", text="iii")

    assert count_dots_on_i("https://example.com/") == 59


def test_negative_case_of_request():
    with requests_mock.Mocker() as mock_request:
        try:
            mock_request.get("https://exampaskjalkfjakjhkjlkfjalkfjle.com/", text="iii")
            count_dots_on_i("https://exampaskjalkfjakjhkjlkfjalkfjle.com/")
        except ValueError:
            assert True
        else:
            assert False
