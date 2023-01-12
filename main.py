from storage import Storage

coinTypes = ('1p', '2p', '5p', '10p', '20p', '50p', '1gbp', '2gbp')
menu = ('0', '1', '2', '3', '4', '5')
startSnacksIn = {'CHOCOLATE': 5, 'MUESLI BAR': 5, 'APPLE': 5, 'POPCORN': 5,
                 'CHEESE PUFFS': 5}  # Snacks in the machine at the beginning of the day
snacksNames = {'1': 'CHOCOLATE', '2': 'MUESLI BAR', '3': 'APPLE', '4': 'POPCORN', '5': 'CHEESE PUFFS'}
nominations = {1: 20, 2: 10, 5: 6, 10: 4, 20: 2, 50: 1, 100: 1, 200: 1}  # initial nominations machine contains
startMoneyIn = 0  # Money in machine at the start of the day
coins = 0  # sum of user's coins
spent = 0  # money spent by user
moneyReturn = 0  # amount to be returned to user


class Money:
    INIT_NOMINATIONS = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 1, 200: 1}  # initial nominations machine contains

    def __init__(self):
        Money.reset_bank(self)  # stores info about nominations possessed
        self.initial_value = self.amount_in()

    def coins_in(self):  # list nominations possessed
        print("Nomination   Pieces")
        [(print("{0:^10} {1:>6}".format(key, value))) for key, value in self.money_in.items()]
        print("TOTAL        {0:.2f} GBP".format(self.amount_in() / 100))

    def amount_in(self):  # print amount possessed
        amount = 0
        for key, value in self.money_in.items():
            amount += key * value
        return amount

    def reset_bank(self):  # reset to initial state
        self.money_in = Money.INIT_NOMINATIONS  # stores info about nominations possessed

    def add_money(self, cash):  # add user money, e.g. cash = {1:3, 10:2, 100:1}
        for i in cash:
            self.money_in[i] += cash[i]

    def return_change(self, cash, basket):  # return change after payment e.g. cash = {1:3, 10:2, 100:1},
        # basket = {'CHOCOLATE': 1, 'APPLE': 3, }


    def income_today(self):  # calculate income since last reset
        return self.amount_in() - self.initial_value


money = Money()
# print(money.money_in, Money.INIT_NOMINATIONS)
l = {1: 1, 5: 1, 50: 1, 100: 1, 200: 1}
print(money.amount_in())
money.add_money(l)
# print(money.money_in, Money.INIT_NOMINATIONS)

money.coins_in()
print(money.income_today())

# def menuMessage():
#     """display INTRODUCTION MESSAGE"""
#
#     global coins, spent, basket, flag
#     coins = spent = 0
#     flag = True # prevents from sales summary display during transaction.
#     basket = dict.fromkeys(startSnacksIn, 0)  # initiate empty user's shopping basket
#     input('\n\nPress enter to start using machine\n__________________________________\n')
#     print('\n Welcome new customer! I am perfect Vending Machine. How can I help? \n\n'
#           'MENU:\n'
#           'Type one of the following to insert a coin: 1p, 2p, 5p, 10p, 20p, 50p, 1GBP or 2GBP\n'
#           'or type 1-6 to select an below option:\n'
#           '1 - Chocolate bar     - 10p\n'
#           '2 - Sesame bar        - 10p\n'
#           '3 - Milk bar          - 10p\n'
#           '4 - Pure gluten bar   - 10p\n'
#           '5 - No gluten bar     - 10p\n'
#           '6 - Display sales summary\n'
#           '0 - Confirm your choice\n\n'
#           'Please insert a coin.')
#
#
# # INITIAL PART
# for i in nominations:  # money in the machine at the start of the day
#     startMoneyIn = startMoneyIn + i * nominations[i]
# print('I contain £{:.2f} of change.'.format(startMoneyIn/100))
# menuMessage()
#
#
# while True:
#     print('You have £{:.2f}'.format(coins / 100))
#     userIn = input('---->')  # user input
#     #print('-' * 14)
#     if userIn.lower() in coinTypes:  # user adds a coin
#         flag = False
#         coin = userIn.lower()  # makes user input case insensitive
#         if coin == '1gbp':
#             coin = '100'
#         elif coin == '2gbp':
#             coin = '200'
#         coin = coin.strip('pgb')  # get rid of letters
#         coin = int(coin)  # converts user input to integer
#         nominations[coin] += 1  # adds coin to machine container
#         coins += coin   # adds coin to user's coins
#         if coins >= 10:
#             print('Select a snack (1-5), confirm (0) or insert more coins')
#         else:
#             print('Add more coins.')
#     elif userIn in ('1', '2', '3', '4', '5') and coins >= 10:  # user selected a snack
#         flag = False
#         snackName = snacksNames[userIn] # Selected snack name
#         if snacksIn[snackName] < 1: # checking if selected snack available
#             print(f'No more {snackName}S available. \n'
#                   f'Please select another snack (1-5), confirm (0) or add a coin')
#         else:   # if snack is available
#             coins -= 10  # reducing user's money
#             basket[snackName] += 1  # adding snack to user's basket
#             snacksIn[snackName] -= 1   # reducing amount of available snack
#             print('You have selected:')
#             spent += 10  # calculating money spent by user
#             for i in basket:
#                 if basket[i] > 0:
#                     if basket[i] > 1:  # confirmation of snack selection (plural)
#                         message = '{} {}S'
#                         print(message.format(basket[i], i))
#                     else:  # confirmation of snack selection (singular)
#                         print(basket[i], i)
#             print('\nConfirm selection (0) or insert a coin.')
#             if coins >= 10:
#                 print('Select another snack (1-5).')
#     elif userIn in ('1', '2', '3', '4', '5') and coins < 10:  # user selects snack with no funds
#         print('Insufficient founds for a snack.\n'
#               'Please insert a coin.')
#     elif userIn == '0':  # user confirms snack selection
#         flag = False
#         if spent == 0:
#             print('You have not selected anything')
#             coinReturn(coins)
#         else:  # dispensing snack
#             print('Here is your:')
#             for i in basket:
#                 if basket[i] > 0:
#                     if basket[i] > 1:  # info about snack dispensed plural
#                         message = '{} {}S'
#                         print(message.format(basket[i], i))
#                     else:  # info about snack dispensed singular
#                         print(basket[i], i)
#             print('HAVE A GOOD MEAL!\n')
#             coinReturn(coins) # go to change return module
#             menuMessage()
#     elif userIn == '6' and flag:  # user displays sales summary
#         moneyIn = 0  # Money in machine when checked
#         print('I sold today:')
#         for i in snacksIn:  # printing sold snacks
#             if startSnacksIn[i] - snacksIn[i] > 0:
#                 print('{} {}S'.format(startSnacksIn[i] - snacksIn[i], i))
#         for i in nominations:  # calculating money in the machine now from coins in container
#             moneyIn += nominations[i] * i
#         print(f'for £{(moneyIn - startMoneyIn) / 100}')
#         menuMessage()
#     else:  # wrong user input
#         print('Invalid choice, try again.')
#
#
# basket = {'CHOCOLATE': 0, 'MUESLI BAR': 0, 'APPLE': 1, 'POPCORN': 3,
#           'CHEESE PUFFS': 5}
# supply = Storage()
# supply.auto_supply()
# print(supply.snacks_in)
# print(supply.give_snacks(basket))
#
#
#
#
#
# # if __name__ == '__main__':
# #     main()
