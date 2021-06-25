import pytest
from homework1.task2.check_fib.check_fib import check_fibonacci


def test_positive_case():
    """Testing that fibonacci checking True"""
    assert check_fibonacci((55, 89, 144))


def test_negative_case():
    """Testing that fibonacci checking False"""
    assert not check_fibonacci((12, 13, 14))


def test_length_positive():
    """Testing that fibonacci checking True, even when length <= 2"""
    assert check_fibonacci((55,))


def test_length_negative():
    """Testing that fibonacci checking False, even when length <= 2"""
    assert not check_fibonacci((54,))


def test_empty_sequence():
    """Testing that fibonacci checking False
    when sequence has 0 integers inside
    """
    assert not check_fibonacci(())
