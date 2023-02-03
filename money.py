"""Money container in the machine"""

import settings


class Money:

    INITIAL_NOMINATIONS = settings.INITIAL_NOMINATIONS  # initial nominations machine contains

    def __init__(self):
        self.money_in = self.get_nominations().copy()  # Coins container, coins in pence e.g. {200: 2, 100: 1, 50: 1,..}
        self.initial_value = self.amount_in()  # Money in machine at the beginning of the day

    def get_nominations(self):
        return Money.INITIAL_NOMINATIONS

    def inventory(self):  # return nominations possessed
        return self.money_in

    def amount_in(self):  # amount/value possessed
        amount = 0  # total value of all coins in the machine
        for key, value in self.money_in.items():
            amount += key * value
        return amount

    def reset_bank(self):  # reset to initial state
        self.money_in = self.get_nominations().copy()  # Coins container, coins as dict e.g. {200: 2, 100: 1, 50: 1,...}

    def add_money(self, cash):  # add user money, e.g. cash = {1:3, 10:2, 100:1}
        for i in cash:
            self.money_in[i] += cash[i]

    def income_today(self):  # calculate income since last reset
        return self.amount_in() - self.initial_value

    def return_change(self, user_amount, basket_value):  # return change after payment deducting coins from money_in
        change = user_amount - basket_value  # change to return to the user
        change_coins = {}  # Coins to be returned
        for i in self.money_in:  # "i" is a coin nominal

            if change == i:  # Return change of a single coin
                change -= i  # Reduce return balance
                self.money_in[i] -= 1  # Subtracts coin from coins container
                change_coins[i] = 1  # Add coin to be returned

            elif change > i:  # return change of more than a single coins
                quotient = change // i
                while quotient > self.money_in[i]:  # check if coins are available
                    quotient -= 1
                if quotient > 0:
                    change -= i * quotient  # reduces amount to be returned by number of available nominal
                    self.money_in[i] -= quotient  # subtracts coins from coins container
                    change_coins[i] = quotient  # Add coins to be returned

        change_value = sum(k * v for k, v in change_coins.items())  # Calculate value of all returned coins
        remaining = user_amount - basket_value - change_value  # Amount not fully returned

        return change_coins, change_value, remaining  # e.g. ({50: 1, 20: 2, 5: 1, 1:3},
        # 13 (amount that can not be returned because lack of coins), True)

