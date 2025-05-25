from catshflow.transactions.controller import transactions_controller
from catshflow.classification.controller import classification_controller
def main():
    menu = """_______________
0. Exit
1. Transactions
2. Categories
3. History
4. Reports
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"""
    flag = True
    while flag:
        print()
        transactions_controller.balance_format()
        print(menu)
        option = int(input("Option:"))
        if option == 1:
            transactions_controller.transaction()
        elif option == 2:
            classification_controller.classifications()
        elif option == 0:
            flag = False
        else:
            print("Wrong option, choose one of the displayed options!")
        print()

main()