"""Money container in the machine"""

class Money:
    INIT_NOMINATIONS = {200: 6, 100: 6, 50: 0, 20: 2, 10: 1, 5: 333, 2: 22, 1: 2, }  # initial nominations machine contains

    def __init__(self):
        self.money_in = Money.INIT_NOMINATIONS.copy()  # Coins container, stores info about nominations in the machine
        self.initial_value = self.amount_in()  # Money in machine at the beginning of the day

    def coins_in(self):  # list nominations possessed
        return self.money_in

    def amount_in(self):  # print amount possessed
        amount = 0  # total value of all coins in the machine
        for key, value in self.money_in.items():
            amount += key * value
        return amount

    def reset_bank(self):  # reset to initial state
        self.money_in = Money.INIT_NOMINATIONS.copy()  # Coins container, stores info about nominations in the machine

    def add_money(self, cash):  # add user money, e.g. cash = {1:3, 10:2, 100:1}
        for i in cash:
            self.money_in[i] += cash[i]

    def income_today(self):  # calculate income since last reset
        return self.initial_value - self.amount_in()

    def return_change(self, user_amount, basket_value):  # return change after payment e.g. cash = {1:3, 10:2, 100:1},
        # basket = {'CHOCOLATE': 1, 'APPLE': 3, }, user money
        change = user_amount - basket_value  # change to return to user
        change_coins = {}  # Coins to be returned
        change_value = 0  # Value of all returned coins
        returned = True  # Flags if full amount was returned
        for i in self.money_in:  # "i" is a coin nominal

            if change == i:  # Return change of a single coin
                change -= i  # Reduce balance to return
                self.money_in[i] -= 1  # Subtracts coin from coins container
                change_coins[i] = 1  # Add coin to be returned
                return change_coins

            elif change > i:  # return change of more than a single coins
                quotient = change // i
                while quotient > self.money_in[i]:  # check if coins are available
                    quotient -= 1
                if quotient > 0:
                    change -= i * quotient  # reduces money to return by number of available nominal
                    self.money_in[i] -= quotient  # subtracts coins from coins container
                    change_coins[i] = quotient  # Add coins to be returned
            print(change)
        for k, v in change_coins.items():  # Calculate value of all returned coins
            change_value += k * v
        if change:  # Check if full amount was returned
            returned = False
        return change_coins, change_value, returned  # e.g. ({50: 1, 20: 2, 5: 1, 1:3}, 78, True)

