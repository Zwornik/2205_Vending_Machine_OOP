from storage import Storage

"""It is machine touch screen showing messages to the user and collecting user inputs.
    It also gives snacks (by displaying them) and return change (by displaying coins)."""


class Interface:
    COIN_TYPES = ('1p', '2p', '5p', '10p', '20p', '50p', '1gbp', '2gbp')
    MENU = ('0', '1', '2', '3', '4', '5', '6')

    def __init__(self):
        self.snack_names = Storage.SNACK_NAMES  # ???? Direct reference to parallel class.
        # Is it allowed with breaking SRP

    def intro(self, value):
        input('\nPress enter to start using machine\n__________________________________\n')
        print('Welcome new customer! How can I be of help? \n'
              'MENU:\n'
              'Type one of the following to insert a coin: 1p, 2p, 5p, 10p, 20p, 50p, 1GBP or 2GBP\n'
              'or option 1-6 to select an below option:\n'
              '1 - CHOCOLATE       - 10p\n'
              '2 - MUESLI BAR      - 10p\n'
              '3 - APPLE           - 10p\n'
              '4 - POPCORN         - 10p\n'
              '5 - CHEESE PUFFS    - 10p\n'
              '6 - Interface sales summary\n'
              '0 - Confirm your choice\n')
        print('You have £{:.2f}\n'
              'Please insert a coin.'.format(value / 100))

    def load_menu(self):
        resp = input('\nPlease load snacks (press 1) or skip (press Enter). \n'
                     '5 items of each snack will be automatically loaded if you skip loading procedure\n')
        if resp == "1":
            return True
        return False

    def add_snack(self):
        start_snacks = {}
        for i in self.snack_names.values():
            while True:
                snack_qty = input(f'How many {i}S are you adding?  ')
                if snack_qty.isdigit():  # Verifying if user typed integer
                    start_snacks[i] = int(snack_qty)  # Loading snacks to machine
                    break
                else:
                    print('Wrong input. Please option integer number.')
        print('\nYou have loaded: \n')
        self.print_table(start_snacks, True, True)
        return start_snacks

    def print_table(self, content, summ, header):  # ???? function modified depending on type.
        # When new type added another ELIF would have to be added
        if len(content) > 0:
            if type(list(content.keys())[0]) == str:  # Find the longest key in content(dict). Keys are strings
                longest = max(len(x) for x in content)
                justify = "<"
                footer = "{0:<{2}}    {1:>6d}\n".format('TOTAL', sum(content.values()), longest)
            else:  # Keys are integers
                total = sum(k * v for k, v in content.items()) / 100
                content_new = {}
                for k in content.keys():
                    if k in (100, 200):
                        new_k = "£" + str(int(k / 100))
                    else:
                        new_k = str(k) + "p"
                    content_new[new_k] = content[k]
                content = content_new
                del content_new

                longest = max(len(x) for x in content)
                justify = ">"
                footer = "{0:>{2}} £{1:>6.2f}\n".format('TOTAL', total, longest)

            if header:
                print("{0:{3}{2}}    {1:>6}".format("Item", "Quantity", longest, justify))
            [(print("{0:{3}{2}}    {1:>6}".format(key, value, longest, justify))) for key, value in content.items()]
            if summ:
                print(footer)
        else:
            print("None.")

    def i_contain_value_msg(self, value):  # prints value of money in the machine
        print('I contain £{:.2f} of change.'.format(value / 100))

    def you_have_msg(self, value):
        print('You have £{:.2f}'.format(value / 100))

    def user_input(self):  # ?????? return from this method is sent to several places in mian file. Does that break SRP

        while True:
            user_choice = input('----> ').lower()
            if user_choice in Interface.COIN_TYPES or user_choice in Interface.MENU:
                if user_choice.isnumeric():
                    user_choice = int(user_choice)
                    return user_choice
                else:
                    if user_choice == '1gbp':
                        user_choice = '100p'
                    elif user_choice == '2gbp':
                        user_choice = '200p'
                    return user_choice
            else:
                print("Wrong input. Try again: ")

    def auto_load_msg(self, load):
        print("I have automatically loaded snacks: ")
        self.print_table(load, True, True)

    def i_contain_coins_msg(self, coins):
        print("I contain following coins: ")
        self.print_table(coins, True, True)

    def inefficient_funds_msg(self, missing):
        print("Insufficient funds. Please add £{:.2f} to buy this snack.".format(missing/ 100))

    def small_menu(self):
        print("Select a snack (1-5), confirm (0) or insert more coins")

    def change_return_msg(self, change_coins, value):
        if len(change_coins) > 0:
            print("Here is £{:.2f} change in following coins:".format(value/100))
            self.print_table(change_coins, False, True)
        else:
            print("No change to be returned.")

    def snacks_bought_msg(self, snacks):
        if len(snacks) > 0:
            print("Here you have snacks you bought:")
            self.print_table(snacks, False, False)
            print("HAVE A GOOD MEAL!")
        else:
            print("You haven't selected any snack. \nThank you for using this machine. ")

    def no_change_msg(self, missing):
        print(f'Upsss! \n'
              f'I contain no more coins so I am not able to give you remaining £{missing/100} change.\n'
              f'Please write to Prime Minister to get your money back.\n'
              f'SORRY :-(')

    def you_added_msg(self, coin):
        print("You added")

    def your_basket_msg(self, basket):
        print("Your basket contains:")
        self.print_table(basket, False, False)