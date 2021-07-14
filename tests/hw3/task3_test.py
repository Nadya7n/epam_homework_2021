import pytest

from homework3.task3 import mistakes


def test_class_filter_positive_case():
    """
    Testing that class Filter works correct in positive case
    """
    instance_of_filter = mistakes.Filter((lambda a: a % 2 == 0, lambda a: a > 5))
    assert instance_of_filter.apply(range(10)) == [6, 8]


def test_class_filter_negative_case():
    """
    Testing that class Filter works correct in negative case
    """
    instance_of_filter = mistakes.Filter((lambda a: a % 2 == 0, lambda a: a > 10))
    assert instance_of_filter.apply(range(10)) == []


def test_function_make_filter_positive_case():
    """
    Testing that function make_filter works correct in positive case
    """
    request = mistakes.make_filter(is_dead=True, kind="parrot").apply(
        mistakes.sample_data
    )
    response = [{"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}]
    assert request == response


def test_function_make_filter_negative_case():
    """
    Testing that function make_filter works correct in negative case
    """
    request = mistakes.make_filter(is_dead=True, kind="mouse").apply(
        mistakes.sample_data
    )
    response = []
    assert request == response
