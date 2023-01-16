"""Represents an User cash in the machine"""

class User_cash:

    def __init__(self):
        self.coins = {}  # Contains user coins e.g. {20: 2, 10: 1, 2: 2, 1: 2}

    def user_value(self):
        amount = 0  # total value of all coins in the machine
        for key, value in self.coins.items():
            amount += key * value
        return amount

    def add_coin(self, coin):
        if coin in self.coins:
            self.coins[coin] += 1
        else:
            self.coins[coin] = 1

    def user_coins(self):
        return self.coins


