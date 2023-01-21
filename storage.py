"""Snacks container in the machine"""


class Storage:

    SNACK_NAMES = {1: 'CHOCOLATE', 2: 'MUESLI BAR', 3: 'APPLE', 4: 'POPCORN', 5: 'CHEESE PUFFS'}  # Stores snacks names
    # with assigned number for easier user selection

    def __init__(self):
        self.snacks_in = {}  # Contains dict with snacks e.g. {1: 'CHOCOLATE', 2: 'MUESLI BAR'...}

    def auto_supply(self):  # automatically insert snack supply
        self.snacks_in = {'CHOCOLATE': 1, 'MUESLI BAR': 2, 'APPLE': 3, 'POPCORN': 5,
                          'CHEESE PUFFS': 5}

    def empty_storage(self):  # Empty snack storage
        self.snacks_in = {'CHOCOLATE': 0, 'MUESLI BAR': 0, 'APPLE': 0, 'POPCORN': 0,
                          'CHEESE PUFFS': 0}

    def load_snacks(self, snacks):  # Load snacks (dictionary e.g. e.g. {1: 'CHOCOLATE',...) to the machine(inventory)
        self.snacks_in = snacks

    def inventory(self):  # Return snack inventory
        return self.snacks_in


    def check_snack(self, snack_no):  # Returns count of selected snack number in the machine
        return self.snacks_in[Storage.SNACK_NAMES[snack_no]]

    def give_snacks(self, basket):  # Deduct basket snacks from snacks inventory
        for snack in basket.keys():
            self.snacks_in[snack] -= basket[snack]


# s=Storage()
# print(s.check_snack(2))