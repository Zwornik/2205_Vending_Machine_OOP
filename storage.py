"""Snacks container in the machine"""

import configuration


class Storage:

    SNACK_PRICES = configuration.INITIAL_SNACK_PRICES  # Snack names with prices in pence

    def __init__(self):
        self.snacks_and_prices_in = Storage.SNACK_PRICES.copy()  # Contains dict of snacks with price and initial
        # quantity e.g. {Snack names: [price, quantity when auto supplied/loaded ], ...}.

    def get_snack_price(self, name):
        return self.snacks_and_prices_in[name][0]

    def get_snack_quantity(self, name):
        return self.snacks_and_prices_in[name][1]

    # def auto_supply(self):  # automatically insert snack supply
    #     self.snacks_and_prices_in = Storage.SNACK_PRICES

    def load_snacks(self, snacks):  # Load snacks (dictionary e.g. e.g. {1: 'CHOCOLATE',...) to the machine(inventory)
        self.snacks_and_prices_in = snacks

    def inventory(self):  # Return snack inventory with prices
        return self.snacks_and_prices_in

    def check_snack(self, snack_no):  # Returns count of selected snack number in the machine
        re = self.get_snack_quantity(self.snack_name_by_selection_no(snack_no))
        return re

    def give_snacks(self, basket):  # Deduct basket snacks from snacks inventory
        for snack in basket.keys():
            self.snacks_and_prices_in[snack][1] -= basket[snack][1]

    def snack_name_by_selection_no(self, snack_no):  # return name (key) of dict item when menu number is given, where
        # menu number is 1 larger than item index
        index = snack_no - 1
        return list(self.inventory())[index]

    def snack_selection_no_by_name(self, name):  # return index+1 of dict item when name (key) is given
        return list(self.inventory().keys()).index(name) + 1

    def snack_price_by_selection_no(self, snack_no):
        return self.get_snack_price(self.snack_name_by_selection_no(int(snack_no)))

    def cheapest_snack(self):  # Return price of the cheapest snack available
        cheapest = 1000
        for i in self.snacks_and_prices_in:
            if self.snacks_and_prices_in[i][0] < cheapest and self.snacks_and_prices_in[i][1] > 0:
                cheapest = self.snacks_and_prices_in[i][0]
        print("cheapest ", cheapest)
        return cheapest
