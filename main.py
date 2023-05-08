import configuration
from storage import Storage
from interface import Interface
from money import Money
from userwalet import User_walet
from basket import Basket
from checkout import Checkout


storage = Storage()  # Represents snack_name container in the Machine
money = Money()  # Represents money container in the machine
user_walet = User_walet()  # Represents User cash in the machine
interface = Interface()  # It is machine touch display showing messages to the user and collecting user inputs
basket = Basket()  # It is user snacks selection before transaction
checkout = Checkout(money, user_walet, storage,)  # Responsible for all processes related to
# approving transaction


def main(count):  # Main program sequence.

    while True:
        intro(count)
        shopping_sequence()
        count += 1  # making sure that first iteration have different message than following iterations


def intro(count):  # Initial menu for loading snacks

    if count == 0:  # making sure that first iteration have different message than following iterations
        if interface.ask_for_loading_snacks():  # Ask if user wants to load snacks manually to the machine. True if yes.
            load_snacks()
    interface.next_client(money.inventory(), storage.inventory(), count, money.amount_in())  # Initial message of
    # shopping sequence
    interface.main_menu(user_walet.user_value(), storage.inventory())  # Welcome message
    # with menu for the client


def shopping_sequence():  # Main shopping sequence loop
    in_basket = {}
    while True:  # main shopping loop
        user_money = user_walet.user_value()
        user_input = interface.user_input("client")

        if user_input in configuration.snack_menu:  # Get snack_name price if user selected snack_name
            input_price = storage.snack_price_by_selection_no(user_input)
        else:
            input_price = 0

        if user_input in configuration.snack_menu and user_money >= basket.basket_value() + input_price:  # User adds snack_name
            # to his basket
            snack_name = storage.snack_name_by_selection_no(user_input)  # Selected snack name

            try:  # Check if snack name already exist in the basket  ???? I check this second time in Basket.add_snack
                # is that okey????
                basket.basket_inventory()[snack_name]
            except KeyError:  # Pass if it doesn't exist
                in_basket[snack_name] = [0,0]
            else:
                in_basket[snack_name] = basket.basket_inventory()[snack_name]
            if in_basket[snack_name][1] < storage.check_snack(user_input):  # Add snack to the basket if no. of snacks
                # in basket is less thank in the machine/storage
                basket.add_snack(snack_name, storage.inventory())  # Add 1 snack with price to the basket
                interface.your_basket_msg(basket.basket_inventory())
            else:
                interface.out_of_snacks(snack_name)

        elif user_input in configuration.snack_menu and user_money < basket.basket_value() + input_price:  # User adds
            # snack_name to his basket but has no money
            interface.insufficient_funds_msg(basket.basket_value() + input_price - user_money)
            # Display message about insufficient funds.

        elif user_input == 0:  # User confirms purchase
            checkout.complete_purchase(basket, user_walet)
            break

        elif user_input == 9:  # Go to admin menu
            admin_choice()

        elif type(user_input) == str:  # User adds coin
            user_input = user_input[0:-1]  # Get rid of letters
            user_walet.add_coin(int(user_input))  # Adds coin to user walet

        if user_walet.user_value() >= basket.basket_value() + input_price:
            # Check if there is enough money in the Client's wallet to buy selected snacks in basket
            affordable = True
        else:
            affordable = False
        interface.you_have_msg(user_walet.user_value() - basket.basket_value(), affordable, len(basket.basket_has))
        # Display current money in the wallet and message suggesting next step


def admin_choice():  # Sequence of admin menu
    while True:
        interface.admin_menu()  # Print admin menu
        admin_input = interface.user_input("admin")  # Collect use input

        if admin_input == 1:  # Show machine inventory coins and snacks
            interface.double_table(money.inventory(), storage.inventory(), money.amount_in())

        elif admin_input == 2:  # Load snacks
            load_snacks()

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


def load_snacks():
    add_snack = interface.add_snack(storage.inventory())  # Collect user input as dict of snacks with prices
    # e.g {"APPLE": [25, 5], ...} to be loaded to the machine
    storage.load_snacks(add_snack)  # Load snacks do the machine storage


if __name__ == '__main__':
    count = 0
    main(count)
