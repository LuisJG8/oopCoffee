from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
the_menu = Menu()
flag = True

while True:
    options = the_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        flag = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = the_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)






