from storage import Storage

"""It is machine touch display showing messages to the user and collecting user inputs"""


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
        self.print_table(start_snacks)
        return start_snacks

    def print_table(self, content):  # ???? function modified depending on type.
        # When new type added another ELIF would have to be added

        if type(list(content.keys())[1]) == str:  # Find the longest key in content(dict). Keys are strings
            longest = max(len(x) for x in content)
            justify = "<"
            text = "{0:<{2}}    {1:>6d}\n".format('TOTAL', sum(content.values()), longest)
        else:  # Keys are integers
            longest = str(max(x for x in content))
            longest = len(longest)
            justify = ">"
            text = "{0:>{2}} £{1:>6.2f}\n".format('TOTAL', sum(content.values()) / 100, longest)

        print("{0:{3}{2}}    {1:>6}".format("Item", "Quantity", longest, justify))
        [(print("{0:{3}{2}}    {1:>6}".format(key, value, longest, justify))) for key, value in content.items()]
        print(text)

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
                    if user_choice  == '1gbp':
                        user_choice = '100p'
                    elif user_choice == '2gbp':
                        user_choice = '200p'
                    return user_choice
            else:
                print("Wrong input. Try again: ")

    def auto_load_msg(self, load):
        print("I have automatically loaded snacks: ")
        self.print_table(load)

    def i_contain_coins_msg(self, coins):
        print("I contain following coins: ")
        self.print_table(coins)

    def inefficient_funds_msg(self):
        print("Insufficient funds. Please add more coins. ")

