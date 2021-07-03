import pytest

from homework1.task2.check_fib import check_fibonacci


def test_check_fibonacci_is_positive_with_3_el():
    """Testing that fibonacci checking True"""
    assert check_fibonacci((55, 89, 144)) is True


def test_check_fibonacci_is_negative_with_3_el():
    """Testing that fibonacci checking False"""
    assert check_fibonacci((12, 13, 14)) is False


def test_check_fibonacci_is_positive_with_1_el():
    """Testing that fibonacci checking True, even when length <= 2"""
    assert check_fibonacci((55,)) is True


def test_check_fibonacci_is_negative_with_1_el():
    """Testing that fibonacci checking False, even when length <= 2"""
    assert check_fibonacci((54,)) is False


def test_check_fibonacci_is_negative_with_0_el():
    """Testing that fibonacci checking False
    when sequence has 0 integers inside
    """
    assert check_fibonacci(()) is False
