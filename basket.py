"""Represents shopping basket of the client"""

class Basket:

    def __init__(self):
        self.basket_has = {}  # Contains selected snacks

    def add_snack(self, snack, ):  # Add snack to basket
        print(snack, type(self.basket_has), self.basket_has)
        if snack in self.basket_has:
            self.basket_has[snack] += 1
        else:
            self.basket_has[snack] = 1

    def basket_inventory(self):  # Return snack in basket
        return self.basket_has  # e.g. {'CHOCOLATE': 2, 'MUESLI BAR': 3}

    def reset_basket(self):
        self.basket_has = {}

    def basket_value(self):
        if self.basket_has:
            return sum(x for x in self.basket_has.values()) * 10
        else:
            return 0


