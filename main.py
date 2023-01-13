from storage import Storage

coinTypes = ('1p', '2p', '5p', '10p', '20p', '50p', '1gbp', '2gbp')
menu = ('0', '1', '2', '3', '4', '5')
startSnacksIn = {'CHOCOLATE': 5, 'MUESLI BAR': 5, 'APPLE': 5, 'POPCORN': 5,
                 'CHEESE PUFFS': 5}  # Snacks in the machine at the beginning of the day
startMoneyIn = 0  # Money in machine at the start of the day
coins = 0  # sum of user's coins
spent = 0  # money spent by user
moneyReturn = 0  # amount to be returned to user


class Money:
    INIT_NOMINATIONS = {200: 6, 100: 6, 50: 0, 20: 2, 10: 1, 5: 3, 2: 2, 1: 2, }  # initial nominations machine contains

    def __init__(self):
        self.money_in = Money.INIT_NOMINATIONS.copy()  # Coins container, stores info about nominations in the machine
        self.initial_value = self.amount_in()  # Money in machine at the beginning of the day

    def coins_in(self):  # list nominations possessed
        print("Nomination   Pieces")
        [(print("{0:^10} {1:>6}".format(key, value))) for key, value in self.money_in.items()]
        print("TOTAL        {0:.2f} GBP".format(self.amount_in() / 100))
        return self.money_in

    def amount_in(self):  # print amount possessed
        amount = 0  # total value of all coins in the machine
        for key, value in self.money_in.items():
            amount += key * value
        return amount

    def reset_bank(self):  # reset to initial state
        self.money_in = Money.INIT_NOMINATIONS.copy()  # Coins container, stores info about nominations in the machine

    def add_money(self, cash):  # add user money, e.g. cash = {1:3, 10:2, 100:1}
        for i in cash:
            self.money_in[i] += cash[i]

    def income_today(self):  # calculate income since last reset
        return self.initial_value - self.amount_in()

    def return_change(self, user_amount, basket_value):  # return change after payment e.g. cash = {1:3, 10:2, 100:1},
        # basket = {'CHOCOLATE': 1, 'APPLE': 3, }, user money
        change = user_amount - basket_value  # change to return to user
        unavailable_coins = []
        change_coins = {}  # Coins to be returned
        change_value = 0  # Value of all returned coins
        returned = True  # Flags if full amount was returned
        for i in self.money_in:  # "i" is a coin nominal

            if change == i:  # Return change of a single coin
                change -= i  # Reduce balance to return
                self.money_in[i] -= 1  # Subtracts coin from coins container
                change_coins[i] = 1  # Add coin to be returned
                return change_coins

            elif change > i:  # return change of more than a single coins
                quotient = change // i
                while quotient > self.money_in[i]:  # check if coins are available
                    quotient -= 1
                    # if i not in unavailable_coins:
                    #     unavailable_coins.append(i)  # adds unavailable coin to list of unavailable coins
                    #     print(unavailable_coins)
                if quotient > 0:
                    change -= i * quotient  # reduces money to return by number of available nominal
                    self.money_in[i] -= quotient  # subtracts coins from coins container
                    change_coins[i] = quotient  # Add coins to be returned
            print(change)
        for k, v in change_coins.items():  # Calculate value of all returned coins
            change_value += k * v
        if change:  # Check if full amount was returned
            returned = False
        return change_coins, change_value, returned  # e.g. ({50: 1, 20: 2, 5: 1, 1:3}, 78, True)




money = Money()
# print(money.money_in, Money.INIT_NOMINATIONS)
# money.money_in[200] = 100
# print(money.money_in, Money.INIT_NOMINATIONS)
l = {1: 1, 5: 1, 50: 1, 100: 1, 200: 1}
cash = {1:3, 10:2, 100:1},
basket = {'CHOCOLATE': 1, 'APPLE': 3, }
print(money.amount_in())
print("return", money.return_change(83, 11))
money.coins_in()
print("income today", money.income_today())



def main():
    pass

#


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
