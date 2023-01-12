print("111111111111111")

class Storage:
    snacks_in = dict

    def auto_supply(self):  # automatically insert snack supply
        self.snacks_in = {'CHOCOLATE': 5, 'MUESLI BAR': 5, 'APPLE': 5, 'POPCORN': 5,
                          'CHEESE PUFFS': 5}

    def empty_storage(self):
        self.snacks_in = {'CHOCOLATE': 0, 'MUESLI BAR': 0, 'APPLE': 0, 'POPCORN': 0,
                          'CHEESE PUFFS': 0}

    def load_snacks(self):
        self.empty_storage()
        for i in self.snacks_in:
            while True:
                sanck_no = input(f'How many {i}S are you adding?  ')
                if sanck_no.isdigit():  # Verifying if user typed integer
                    self.snacks_in[i] = int(sanck_no)  # Loading snacks to machine
                    break
                else:
                    print('Wrong input. Please type integer number.')
        print(f'You have loaded: {self.snacks_in}')

    def snack_inventory(self):
        print(self.snacks_in)
        return self.snacks_in

    def check_snack(self, snack_no):
        if self.snacks_in[snacksNames[snack_no]]:
            return True
        return False

    def give_snacks(self, basket):
        for snack in basket.keys():
            self.snacks_in[snack] -= basket[snack]

print("22222222222222")

# basket = {'CHOCOLATE': 0, 'MUESLI BAR': 0, 'APPLE': 1, 'POPCORN': 3,
#             'CHEESE PUFFS': 5}
# supply = Storage()
# supply.auto_supply()
# print(supply.snacks_in)
# print(supply.give_snacks(basket))


# if __name__ == '__main__':
#     main()
