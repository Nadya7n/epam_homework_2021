import pytest

from homework7.hw2 import compare_strings_with_backspace


@pytest.mark.parametrize(
    "arg_1, arg_2", [("ab#c", "ad#c"), ("a##c", "#a#c"), ("a#c", "c")]
)
def test_removing_backspaces_with_standard_examples(arg_1, arg_2):
    """
    Testing that function compare_strings_with_backspace works correct with examples from task
    :param arg_1: string
    :param arg_2: string
    :return: None
    """
    result = compare_strings_with_backspace(arg_1, arg_2)
    assert result is True


@pytest.mark.parametrize(
    "arg_1, arg_2", [("###", ""), ("###abc", "abc"), ("a#b#c#de", "##de")]
)
def test_removing_backspaces_with_my_examples_positive(arg_1, arg_2):
    """
    Testing that function compare_strings_with_backspace works correct with my examples
    :param arg_1: string
    :param arg_2: string
    :return: None
    """
    result = compare_strings_with_backspace(arg_1, arg_2)
    assert result is True


@pytest.mark.parametrize(
    "arg_1, arg_2", [("###", "a"), ("#abco####df", "abc"), ("d#e", "de")]
)
def test_removing_backspaces_with_my_examples_negative(arg_1, arg_2):
    """
    Testing that function compare_strings_with_backspace works correct with my examples. Negative case
    :param arg_1: string
    :param arg_2: string
    :return: None
    """
    result = compare_strings_with_backspace(arg_1, arg_2)
    assert result is False
