from vending_machine.money import Money


def test_exists_money_1():
    actual = Money.M_1
    expected = 1
    assert actual == expected
