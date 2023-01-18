from storage import Storage
from user import User
from interface import Interface
from money import Money
from userwalet import User_walet
from basket import Basket

storage = Storage()  # Represents snack container in the Machine
money = Money()  # Represents money container in the machine
user_walet = User_walet()  # Represents an User cash in the machine
interface = Interface()  # It is machine touch display showing messages to the user and collecting user inputs
basket = Basket()


def main():

    if interface.load_menu():  # Ask if user wants to load snacks manually to the machine. True if yes.
        add_snack = interface.add_snack()  # Collect snack loaded to the machine
        storage.load_snacks(add_snack)  # Load snacks do the machine storage
    else:
        storage.auto_supply()  # Automatically load snacks to the machine
        interface.auto_load_msg(storage.snack_inventory())  # Message confirming automating loading & display snacks in

    interface.i_contain_coins_msg(money.coins_in())  # Display coins in the machine
    # interface.i_contain_value_msg(money.amount_in())  # Message about money amount in the machine
    user_money = user_walet.user_value()
    interface.intro(user_money)  # Welcome message with menu for the client

    return storage, money, user_walet, interface, basket


def shopping_sequence():
    while True:  # main shopping loop
        user_money = user_walet.user_value()
        user_input = interface.user_input()

        if user_input in (1, 2, 3, 4, 5) and user_money >= basket.basket_value() + 10:  # User adds snack to his basket
            snack = storage.SNACK_NAMES[user_input]  # Selected snack name
            if storage.check_snack(user_input) > 0:
                basket.add_snack(snack)  # Add snack to the basket
                interface.your_basket_msg(basket.basket_inventory())

        elif user_input in (1, 2, 3, 4, 5) and user_money < basket.basket_value() + 10:  # User adds snack to his
            # basket but has no money
            interface.inefficient_funds_msg(basket.basket_value() + 10 - user_money)  # Display message about
            # insufficient funds.

        elif user_input == 0:  # User confirms purchase
            money.add_money(user_walet.user_coins())  # Add user coins to the machine
            change_returned = money.return_change(user_walet.user_value(), basket.basket_value())  # e.g. ({dict of
            # coins to be returned}, returned amount, Amount not returned)
            print(change_returned, change_returned[0])
            interface.change_return_msg(change_returned[0], change_returned[1])  # Display returned coins
            print(money.money_in)
            storage.give_snacks(basket.basket_has)  # Deducting snack from basket from machine inventory
            print(storage.snack_inventory())
            interface.snacks_bought_msg(basket.basket_has)  # Display bought snacks
            if change_returned[2]:
                interface.no_change_msg(change_returned[1])
            basket.reset_basket()  # Reset basket to empty
            user_walet.reset_user_coins()  # Empty user money
            break

        elif user_input == 6:  # User wants to see selling summary
            print("6")

        elif type(user_input) == str:  # User adds coin
            user_input = user_input[0:-1]  # Get rid of letters
            user_walet.add_coin(int(user_input))  # Adds coin to user walet
        interface.you_have_msg(user_walet.user_value())






# User_interface -> DIsplay: main_menu, return: coins and snacks selected or login for admin
# call Storage.check_snack() for each snack from mine
# when confirmed check if there is enough user_walet
# run Money.add_money(cash/coins) and Storage.give_snack() and Money.return.change()
#



if __name__ == '__main__':
    main()
shopping_sequence()
