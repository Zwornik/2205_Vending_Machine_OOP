"""Represents an User walet in the machine"""


class User_walet:

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
        print(self.coins)

    def user_coins(self):  # ???? Wouldn't be better just to read value of COINS directly without using method?
        return self.coins

    def reset_user_coins(self):
        self.coins = {}


