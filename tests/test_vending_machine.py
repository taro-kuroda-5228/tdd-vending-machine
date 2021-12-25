from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Money
import pytest


def test_allowed_money():
    actual = VendingMachine.allowed_money
    expected = [
        Money.M_10,
        Money.M_50,
        Money.M_100,
        Money.M_500,
        Money.M_1000,
        Money.M_2000,
        Money.M_5000,
        Money.M_10000,
    ]
    assert actual == expected


# def test_vending_machine_total_money():
#     actual = total_money
#     expected =
#     assert actual == expected
