import pytest

from homework4.task3.task_3_get_print_output import my_precious_logger


def test_logger_with_error(capsys):
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"
    assert captured.out == ""


def test_logger_with_ok(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out == "OK"
