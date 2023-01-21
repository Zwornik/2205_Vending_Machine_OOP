"""Represents the User's walet in the machine"""


class User_walet:

    def __init__(self):
        self.coins = {}  # Contains user coins e.g. {20: 2, 10: 1, 2: 2, 1: 2}

    def user_value(self):  # Return total value of user's all coins
        amount = 0  # Total value of all coins in the machine
        for key, value in self.coins.items():  # Calculate value of all coins
            amount += key * value
        return amount

    def add_coin(self, coin):  # Add single coin to the user's walet
        if coin in self.coins:  # Make sure that the key in the dict exists before adding 1 to it.
            self.coins[coin] += 1
        else:
            self.coins[coin] = 1

    def user_coins(self):  # Return user's walet coins e.g. {20: 2, 10: 1, 2: 2, 1: 2}
        return self.coins

    def reset_user_coins(self):  # Zero user's walet
        self.coins = {}


