"""It is machine touch screen showing messages to the user and collecting user inputs.
    It also gives snacks (by displaying them) and return change (by displaying coins)."""

from storage import Storage
from money import Money


class Interface:
    COIN_TYPES = ('2gbp', '1gbp', '50p', '20p', '10p', '5p', '2p', '1p')
    MENU = ('1', '2', '3', '4', '5', '9', '0')

    def __init__(self):
        self.snack_names = Storage.SNACK_NAMES  # Stores snacks names with assigned number for easier user selection
        self.init_nominations = Money.INIT_NOMINATIONS  # ???? Should these 2 variables be in CAPITALS as they are
        # static  # Stores coins nominations

    def next_client(self, coins, snacks, count):  # Initial message of shopping sequence
        if count:
            print("\nNext client please. Press 'Enter' to continue.")
        else:
            print("\nPress 'Enter' to start using machine")
        input("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        self.double_table(coins, snacks)

    def intro(self, value):  # Intro menu for the client
        print('Welcome new customer! \n'
              'MENU:\n'
              'Type one of the following to insert a coin: 1p, 2p, 5p, 10p, 20p, 50p, 1GBP or 2GBP\n'
              'or option 1-6 to select an below option:\n'
              '1 - CHOCOLATE       - 10p\n'
              '2 - MUESLI BAR      - 10p\n'
              '3 - APPLE           - 10p\n'
              '4 - POPCORN         - 10p\n'
              '5 - CHEESE PUFFS    - 10p\n'
              '9 - Admin interface\n'
              '0 - Confirm your choice\n')
        print('You have £{:.2f}. Please insert a coin.'.format(value / 100))

    def load_menu(self):  # Starting program message
        resp = input('\nPlease load snacks (press 1) or skip (press Enter). \n'
                     '5 items of each snack will be automatically loaded if you skip loading procedure')
        if resp == "1":
            return True
        return False

    def add_snack(self, who):  # Iterate through all snacks, return new dict with snacks to be added.
        start_snacks = {}  # New snacks to be added

        if who == "admin":  # Additional message if run by admin
            print("I have deleted all snacks from storage. Type new quantity of each snack.")
        for i in self.snack_names.values():  # Iterate through all snack names
            while True:
                snack_qty = input(f'How many {i}S are you adding? >> ')
                if snack_qty.isdigit():  # Verifying if user typed integer
                    start_snacks[i] = int(snack_qty)  # Loading snacks to machine
                    break
                else:
                    print("Wrong input. Please type integer number and confirm by 'Enter'")
        print('\nYou have loaded: \n')
        self.print_table(start_snacks, True, True)  # Print snacks with quantities
        return start_snacks  # Return new dict with snacks to be added

    def add_coins(self):  # Return dict with coins to be added to the machine, not to the walet
        coins = {}
        for i in self.init_nominations:  # Iterate through all nominations
            while True:
                if i in (100, 200):  # Format ints to Pounds and Pence
                    str_i = "£" + str(int(i/100))
                else:
                    str_i = str(int(i)) + "p"
                coins_qty = input(f"How many {str_i} are you adding: >> ")  # Ask for each nomination

                if coins_qty.isdigit():  # Verifying if user typed integer
                    coins[i] = int(coins_qty)  # Add coin with quantity to dict
                    break
                else:
                    print("Wrong input. Please type integer number and confirm by 'Enter'")
        print('You have loaded: \n')
        self.print_table(coins, True, True)  # Print coins with quantities
        return coins  # Return new dict with coins to be added

    def print_table(self, content, summ, header):  # Print table with snacks or coins (dict, bool, bool)
        if len(content) > 0:
            if type(list(content.keys())[0]) == str:  # If Keys are strings (snacks) find the longest key in
                # content(dict).
                longest = max(len(x) for x in content)  # Find the longest item
                justify = "<"
                footer = "{0:<{2}}    {1:>6d}\n".format('TOTAL', sum(content.values()), longest)
            else:  # if keys are integers (coins), convert to str, format, and find the longest and adjust text
                total = sum(k * v for k, v in content.items()) / 100
                content_temp = {}  # Temporary dict to store coins names as str
                for k in content.keys():
                    if k in (100, 200):  # if key is 1 or 2 GBP
                        new_k = "£" + str(int(k / 100))  # format to Pounds
                    else:
                        new_k = str(k) + "p"  # Format to Pences
                    content_temp[new_k] = content[k]  # Add to new temporaty dict
                content = content_temp  # assign to content
                del content_temp  # delete temporary dict

                longest = max(len(x) for x in content)  # find the longest key in dict
                justify = ">"
                footer = "{0:>{2}} £{1:>6.2f}\n".format('TOTAL', total, longest)

            if header:
                print("{0:{3}{2}}    {1:>6}".format("Item", "Quantity", longest, justify))  # print heater
            [(print("{0:{3}{2}}    {1:>6}".format(key, value, longest, justify))) for key, value in content.items()]
            # print each item and quantity in separate line
            if summ:
                print(footer)  # Print footer with totals
        else:  # if content dict is empty
            print("None.")

    def double_table(self, coins_in, snacks_in):  # Print two dictionaries side by side at once
        print("I contain following number of coins and snacks:")
        coins_total = sum(k * v for k, v in coins_in.items()) / 100  # Calculate total of all coins
        snacks_total = sum(value for value in snacks_in.values())  # Calculate total of all snacks

        coins_temp = {}  # empty
        snacks = {}
        for k in coins_in.keys():  # Convert coins to str and add prefix '£' or 'p'
            if k in (100, 200):
                new_k = "£" + str(int(k / 100))
            else:
                new_k = str(k) + "p"
            coins_temp[new_k] = coins_in[k]  # Add coins to temporary dict
        coins = coins_temp
        del coins_temp

        print("{0:>5}    {1:>8}      │     {2:<12}  {3:>6}".format("Coins", "Quantity", "Snacks", "Quantity"))  # Header

        for i in range(len(coins)):  # Prints two dictionaries side by side
            if i > len(snacks_in) - 1:
                snacks[" " * i] = " "
            else:
                snacks[list(snacks_in)[i]] = snacks_in[list(snacks_in)[i]]
            print("{0:>5}    {1:>8}      │     {2:<12}  {3:>6}".format(list(coins)[i], coins[list(coins)[i]],  # Body of the table
                                                                       list(snacks)[i], snacks[list(snacks)[i]]))
        print("{0:>5}   £{2:>8.2f}      │     {0:<12}  {2:>6}\n".format('TOTAL', coins_total, snacks_total))  # Footer

    def i_contain_value_msg(self, value):  # prints value of money in the machine
        print('I contain £{:.2f} of change.'.format(value / 100))

    def you_have_msg(self, value, affordable, snack_selected):
        print('You have £{:.2f}.'.format(value / 100), end=" ")

        if not affordable:
            print("Please insert more coins.")
        elif affordable and not snack_selected:
            print("Add more coins or select a snack (1 -5).")
        elif affordable and snack_selected:
            print("Add more coins, select a snack (1 -5) or confirm purchase (0).")

    def user_input(self, who="client"):  # Collect user input and convert it
        while True:
            user_choice = input('----> ').lower()
            if user_choice in Interface.MENU:  # Check if user selection is in the menu
                user_choice = int(user_choice)  # convert to int if is
                return user_choice

            elif user_choice in Interface.COIN_TYPES and who == "client":  # If the client add a coin
                if user_choice == '1gbp':  # convert Pounds to Pence
                    user_choice = '100p'
                elif user_choice == '2gbp':
                    user_choice = '200p'
                return user_choice
            else:
                print("Wrong input. Try again: ")

    def i_contain_snacks(self, load, who):
        if who == "client":
            print("I have automatically loaded snacks: ")
        else:
            print("I contain following snacks:")
        self.print_table(load, True, True)

    def i_contain_coins_msg(self, coins, income, earned):
        if earned:
            print("I have earned £{:.2f} since the last reset.".format(income/100))
        print("I contain following coins: ")
        self.print_table(coins, True, True)

    def insufficient_funds_msg(self, missing):
        print("Insufficient funds. Please add £{:.2f} to buy this snack.".format(missing / 100))

    def change_return_msg(self, change_coins, value):
        if len(change_coins) > 0:
            print("Here is £{:.2f} change in following coins:".format(value / 100))
            self.print_table(change_coins, False, True)
        else:
            print("No change to be returned.")

    def snacks_bought_msg(self, snacks):
        if len(snacks) > 0:
            print("\nHere you have snacks you bought:")
            self.print_table(snacks, False, False)
            print("HAVE A GOOD MEAL!")
        else:
            print("You haven't selected any snack. \nThank you for using this machine. ")

    def no_change_msg(self, missing):
        print(f'I contain no more coins so I am not able to give you remaining £{missing / 100} change.\n'
              f'Please write to Prime Minister to get your money back.\n'
              f'SORRY :-(')

    def your_basket_msg(self, basket):
        print("Your basket contains:")
        self.print_table(basket, False, False)

    def out_of_snacks(self, snack_name):
        print("There is no more {} available. Please select other snack.".format(snack_name))

    def admin_menu(self):
        print("YOU ARE IN ADMIN MENU:\n"
              "1 - Show machine inventory\n"
              "2 - Load snacks\n"
              "3 - Show today's income\n"
              "4 - Manually add coins\n"
              "5 - Automatically load the coins, 3 of each.\n"
              "9 - Quit Admin Menu continuing current shopping sequence\n"
              "0 - Quit Admin Menu canceling current shopping sequence\n"
              "Select one of above and press 'Enter")
