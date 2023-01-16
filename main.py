from storage import Storage
from user import User
from interface import Interface
from money import Money
from usercash import User_cash
from basket import Basket


def main():

    storage = Storage()  # Represents snack container in the Machine
    money = Money()  # Represents money container in the machine
    user_cash = User_cash()  # Represents an User cash in the machine
    interface = Interface()  # It is machine touch display showing messages to the user and collecting user inputs
    basket = Basket()

    if interface.load_menu():  # Ask if user wants to load snacks manually to the machine. True if yes.
        add_snack = interface.add_snack()  # Collect snack loaded to the machine
        storage.load_snacks(add_snack)  # Load snacks do the machine storage
    else:
        storage.auto_supply()  # Automatically load snacks to the machine
        interface.auto_load_msg(storage.snack_inventory())  # Message confirming automating loading & display snacks in

    interface.i_contain_coins_msg(money.coins_in())  # Display coins in the machine
    # interface.i_contain_value_msg(money.amount_in())  # Message about money amount in the machine
    user_money = user_cash.user_value()
    interface.intro(user_money)  # Welcome message with menu for the client

    while True:  # main shopping loop
        user_money = user_cash.user_value()
        user_input = interface.user_input()
        if user_input in (1, 2, 3, 4, 5) and user_money >= 10:  # User adds snack to his basket
            snack = storage.SNACK_NAMES[user_input]  # Selected snack name
            basket.add_snack(snack)  # Add snack to the basket
        elif user_input in (1, 2, 3, 4, 5) and user_money == 0:  # User adds snack to his basket but has no money
            interface.inefficient_funds_msg()  # Display message about insufficient funds.
        elif user_input == 0:  # User confirm purchase
            pass
        elif user_input == 6:  # User to see selling summary
            pass
        elif user_input is str:  # User adds coin
            user_input = user_input[0:-1]  # Get rid of letters
            user_cash.add_coin(int(user_input))  #

        print(basket.basket_inventory())
        print(user_cash.user_coins())



# User_interface -> DIsplay: main_menu, return: coins and snacks selected or login for admin
# call Storage.check_snack() for each snack from mine
# when confirmed check if there is enough user_cash
# run Money.add_money(cash/coins) and Storage.give_snack() and Money.return.change()
#



if __name__ == '__main__':
    main()
