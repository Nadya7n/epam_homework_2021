import pytest

from homework5.save_original_info import custom_sum


def test_docstring_of_decorated_function():
    """
    Testing that decorator return attribute __doc__ of decorated function
    """
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"


def test_name_of_decorated_function():
    """
    Testing that decorator return attribute __name__ of decorated function
    """
    assert custom_sum.__name__ == "custom_sum"


def test_return_decorated_function():
    """
    Testing that decorator return attribute __original_func of decorated function
    """
    assert str(custom_sum.__original_func).startswith("<function custom_sum at")
