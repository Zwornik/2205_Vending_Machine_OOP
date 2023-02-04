"""Represents shopping basket of the client"""


class Basket:

    def __init__(self):
        self.basket_has = {}  # Contains selected snacks e.g. {'CHOCOLATE': [100, 2],...}

    def add_snack(self, snack_name, snacks_and_prices):  # Add single snack with price to the basket
        if snack_name in self.basket_has:  # Make sure that the key in the dict exists before adding 1 to it.
            self.basket_has[snack_name][1] += 1
        else:
            self.basket_has[snack_name] = [snacks_and_prices[snack_name][0], 1]

    def basket_inventory(self):  # Return snack in basket
        return self.basket_has  # e.g. {'CHOCOLATE': 2, 'MUESLI BAR': 3}

    def reset_basket(self):  # Zero the basket
        self.basket_has = {}

    def basket_value(self):  # Return value of the basket
        if self.basket_has:
            return sum(x[0] * x[1] for x in self.basket_has.values())
        else:
            return 0
