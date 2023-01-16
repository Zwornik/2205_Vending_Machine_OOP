from storage import Storage
from user import User
from interface import Interface
from money import Money
from usercash import User_cash


def main():

    storge = Storage() #??????
    money = Money()
    user_cash = User_cash()
    interface = Interface()  # Initiate interface instance
    if interface.load_menu() == True:  # Ask if user wants to load snacks to the machine. True if yes.
        add_snack = interface.add_snack()
        storge.load_snacks(add_snack)

    interface.i_contain_msg(money.amount_in())
    interface.intro(33)
    print(user_cash.user_value())



# User_interface -> DIsplay: main_menu, return: coins and snacks selected or login for admin
# call Storage.check_snack() for each snack from mine
# when confirmed check if there is enough user_cash
# run Money.add_money(cash/coins) and Storage.give_snack() and Money.return.change()
#



if __name__ == '__main__':
    main()
