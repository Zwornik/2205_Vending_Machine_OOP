"""Responsible for all processes related to approving transaction like accepting money, returning change, realising
the snack bought, and displaying transaction confirmation"""

class Checkout:

    def __init__(self, money, storage, interface):  # ???? so many things passed to this class, it
        # definitely brakes the SRP. How can I avoid that?
        self.money = money
        self.storage = storage
        self.interface = interface

    def complete_purchase(self, basket, user_walet):
        self.return_change(user_walet.user_value(), basket.basket_value())
        self.transfer_money(user_walet)
        self.display_transaction_confirmation(basket.basket_has)
        self.deduct_snacks(basket)

    def return_change(self, user_value, basket_value):
        change_returned = self.money.return_change(user_value, basket_value)  # e.g. ({dict of coins to be returned},
        # returned amount, Amount not returned)
        self.interface.change_return_msg(change_returned[0], change_returned[1])  # Display returned coins
        if change_returned[2]:
            self.interface.no_change_msg(change_returned[2])

    def transfer_money(self, user_walet):  # Add user coins to the machine
        self.money.add_money(user_walet.user_coins())
        user_walet.reset_user_coins()  # Empty user money

    def display_transaction_confirmation(self, basket_has):
        self.interface.snacks_bought_msg(basket_has)  # Display bought snacks

    def deduct_snacks(self, basket):  # ???? Name of this parameter is the same as method in Basket, is it ok?
        self.storage.give_snacks(basket.basket_has)  # Deducting snack_name from basket from machine inventory
        basket.reset_basket()  # Reset basket to empty

