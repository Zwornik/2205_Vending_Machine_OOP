"""Responsible for all processes related to approving transaction like accepting money, returning change, realising
the snack bought, and displaying transaction confirmation"""

class Checkout:

    def __init__(self, money, walet, storage, basket, interface):  # ???? so many things passed to this class, it
        # definitely brakes the SRP. How can I avoid that?
        self.money = money
        self.walet = walet
        self.storage = storage
        self.basket = basket
        self.interface = interface

    def return_change(self, user_value, basket_value):
        change_returned = self.money.return_change(user_value, basket_value)  # e.g. ({dict of coins to be returned},
        # returned amount, Amount not returned)
        self.interface.change_return_msg(change_returned[0], change_returned[1])  # Display returned coins
        if change_returned[2]:
            self.interface.no_change_msg(change_returned[2])

    def transfer_money(self, walet):  # Add user coins to the machine
        self.money.add_money(walet)
        self.walet.reset_user_coins()  # Empty user money

    def display_transaction_confirmation(self, basket_has):
        self.interface.snacks_bought_msg(basket_has)  # Display bought snacks

    def deduct_snacks(self, basket_has):  # ???? Name of this parameter is the same as method in Basket, is it ok?
        self.storage.give_snacks(basket_has)  # Deducting snack_name from basket from machine inventory
        self.basket.reset_basket()  # Reset basket to empty

