import pytest

from homework11 import hw2


def test_order_default_program():
    order_1 = hw2.Order(100)
    assert order_1.final_price() == 75


def test_morning_discount_program():
    order_1 = hw2.Order(100, hw2.morning_discount)
    assert order_1.final_price() == 50


def test_elder_discount_program():
    order_2 = hw2.Order(100, hw2.elder_discount)
    assert order_2.final_price() == 10
