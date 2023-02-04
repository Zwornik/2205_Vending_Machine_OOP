"""Contains all hardcoded settings for Vending Machine program
Modify following comments"""

INITIAL_NOMINATIONS = {200: 3, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 5, 1: 5, }  # initial coins nominations in pence
# with quantity that machine contains at the start of the program.

INITIAL_SNACK_PRICES = {'CHOCOLATE': [100, 3],
                        'MUESLI BAR': [55, 3],
                        'APPLE': [10, 3],
                        'POPCORN': [15, 3],
                        'CHEESE PUFFS': [25, 3]}  # Contains dict of snacks with price and initial quantity e.g.
# {Snack names: [price, quantity when auto supplied/loaded ], ...}. DON'T ADD MORE SNACKS THAN 8

COIN_TYPES = ['2gbp', '1gbp', '50p', '20p', '10p', '5p', '2p', '1p']  # Coin names to be typed by the client

snack_menu = [i+1 for i in range(len(INITIAL_SNACK_PRICES))]  # List of numbers user can type to select a snack

MENU = [str(x) for x in snack_menu] + ['9', '0']  # all main menu choices as strings

