from vending_machine.money import Money


class VendingMachine:
    allowed_money = [
        Money.M_10,
        Money.M_50,
        Money.M_100,
        Money.M_500,
        Money.M_1000,
        Money.M_2000,
        Money.M_5000,
        Money.M_10000,
    ]

    def __init__(self):
        self.total_money = 0

    def insert(self, added_money):
        if added_money not in VendingMachine.allowed_money:
            raise ValueError("you can't insert 1 yen and 5 yen.")
        self.total_money += added_money
