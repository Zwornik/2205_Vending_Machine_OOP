from storage import Storage
from interface import Interface
from money import Money
from userwalet import User_walet
from basket import Basket

storage = Storage()  # Represents snack container in the Machine
money = Money()  # Represents money container in the machine
user_walet = User_walet()  # Represents User cash in the machine
interface = Interface()  # It is machine touch display showing messages to the user and collecting user inputs
basket = Basket()  # It is user snacks selection before transaction


def main(count):  # Main program sequence.

    while True:
        intro(count)
        shopping_sequence()
        count += 1  # making sure that first iteration have different message than following iterations


def intro(count):  # Initial menu for loading snacks

    if count == 0:  # making sure that first iteration have different message than following iterations
        if interface.load_menu():  # Ask if user wants to load snacks manually to the machine. True if yes.
            add_snack = interface.add_snack("client")  # Collect snack loaded to the machine
            storage.load_snacks(add_snack)  # Load snacks do the machine storage
        else:
            storage.auto_supply()  # Automatically load snacks to the machine
    interface.next_client(money.inventory(), storage.inventory(), count)  # Initial message of shopping sequence
    user_money = user_walet.user_value()  # get current value of user walet
    interface.intro(user_money)  # Welcome message with menu for the client

    # return storage, money, user_walet, interface, basket


def shopping_sequence():  # Shopping sequence
    while True:  # main shopping loop
        user_money = user_walet.user_value()
        user_input = interface.user_input("client")

        if user_input in (1, 2, 3, 4, 5) and user_money >= basket.basket_value() + 10:  # User adds snack to his basket
            snack = storage.SNACK_NAMES[user_input]  # Selected snack name
            in_basket = 0
            try:
                basket.basket_inventory()[snack]
            except KeyError:
                pass
            else:
                in_basket = basket.basket_inventory()[snack]

            if in_basket < storage.check_snack(user_input):
                basket.add_snack(snack)  # Add snack to the basket
                interface.your_basket_msg(basket.basket_inventory())
            else:
                interface.out_of_snacks(snack)

        elif user_input in (1, 2, 3, 4, 5) and user_money < basket.basket_value() + 10:  # User adds snack to his
            # basket but has no money
            interface.insufficient_funds_msg(basket.basket_value() + 10 - user_money)  # Display message about
            # insufficient funds.

        elif user_input == 0:  # User confirms purchase
            money.add_money(user_walet.user_coins())  # Add user coins to the machine
            change_returned = money.return_change(user_walet.user_value(), basket.basket_value())  # e.g. ({dict of
            # coins to be returned}, returned amount, Amount not returned)
            interface.change_return_msg(change_returned[0], change_returned[1])  # Display returned coins
            storage.give_snacks(basket.basket_has)  # Deducting snack from basket from machine inventory
            interface.snacks_bought_msg(basket.basket_has)  # Display bought snacks
            if change_returned[2]:
                interface.no_change_msg(change_returned[2])
            basket.reset_basket()  # Reset basket to empty
            user_walet.reset_user_coins()  # Empty user money
            break

        elif user_input == 9:  # Go to admin menu
            admin_choice()

        elif type(user_input) == str:  # User adds coin
            user_input = user_input[0:-1]  # Get rid of letters
            user_walet.add_coin(int(user_input))  # Adds coin to user walet

        if user_walet.user_value() > basket.basket_value() + 10:  # Check if there is enough money in the Clients wallet
            # to buy selected snacks in basket
            affordable = True
        else:
            affordable = False
        interface.you_have_msg(user_walet.user_value() - basket.basket_value(), affordable, len(basket.basket_has))  #
        # Display current money in the wallet and message suggesting next step


def admin_choice():  # Sequence of admin menu
    while True:
        interface.admin_menu()  # Print admin menu
        admin_input = interface.user_input("admin")  # Collect use input

        if admin_input == 1:  # Show machine inventory coins and snacks
            interface.double_table(money.inventory(), storage.inventory())

        elif admin_input == 2:  # Load snacks
            add_snack = interface.add_snack("admin")  # ???? these 2 lines are repeated in line 26 and 27.
            # Should I create separate function for that?  # Collect snack loaded to the machine
            storage.load_snacks(add_snack)  # Load snacks do the machine storage

        elif admin_input == 3:  # Show today's income and coins inventory
            interface.i_contain_coins_msg(money.inventory(), money.income_today(), True)

        elif admin_input == 4:  # Manually load the coins.
            money.add_money(interface.add_coins())
            interface.i_contain_coins_msg(money.inventory(), 0, False)  # Print coins inventory

        elif admin_input == 5:  # Automatically load the coins, 5 of each.
            money.reset_bank()  # Reset money in the machine to initial values
            interface.i_contain_coins_msg(money.inventory(), 0, False)  # Print coins inventory

        elif admin_input == 9:  # Leave Admin Menu continuing current shopping sequence
            return

        elif admin_input == 0:  # Leave Admin Menu canceling current shopping sequence
            main(0)


if __name__ == '__main__':
    count = 0
    main(count)
