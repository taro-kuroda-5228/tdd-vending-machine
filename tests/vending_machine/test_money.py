from vending_machine.money import Money
import pytest


@pytest.mark.parametrize(
    "money,value",
    [
        ("M_1", 1),
        ("M_5", 5),
        ("M_10", 10),
        ("M_50", 50),
        ("M_100", 100),
        ("M_500", 500),
        ("M_1000", 1000),
        ("M_2000", 2000),
        ("M_5000", 5000),
        ("M_10000", 10000),
    ],
)
def test_exists_money(money, value):
    actual = getattr(Money(), money)
    expected = value
    assert actual == expected
