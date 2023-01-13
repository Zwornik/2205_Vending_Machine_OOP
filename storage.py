class Storage:
    SNACK_NAMES = {'1': 'CHOCOLATE', '2': 'MUESLI BAR', '3': 'APPLE', '4': 'POPCORN', '5': 'CHEESE PUFFS'}  # user
                    # selection number assigned to snack names
    snacks_in = dict

    def auto_supply(self):  # automatically insert snack supply
        self.snacks_in = {'CHOCOLATE': 5, 'MUESLI BAR': 5, 'APPLE': 5, 'POPCORN': 5,
                          'CHEESE PUFFS': 5}

    def empty_storage(self):  # Empty snack storage
        self.snacks_in = {'CHOCOLATE': 0, 'MUESLI BAR': 0, 'APPLE': 0, 'POPCORN': 0,
                          'CHEESE PUFFS': 0}

    def load_snacks(self, snack_name, quantity):  # Load snacks to the machine(inventory)
        self.snacks_in[snack_name] += quantity

    def snack_inventory(self):  # Return snack inventory
        print(self.snacks_in)
        return self.snacks_in

    def check_snack(self, snack_no):  # Returns count of selected snack in the machine
        return self.snacks_in[Storage.SNACK_NAMES[snack_no]]

    def give_snacks(self, basket):  # Deduct basket snacks from snacks inventory
        for snack in basket.keys():
            self.snacks_in[snack] -= basket[snack]


basket = {'CHOCOLATE': 0, 'MUESLI BAR': 0, 'APPLE': 1, 'POPCORN': 3,
          'CHEESE PUFFS': 5}
supply = Storage()
supply.auto_supply()
print(supply.snacks_in)
print(supply.give_snacks(basket))

# if __name__ == '__main__':
#     main()
