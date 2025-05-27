from catshflow.transactions.controller import transactions_controller
from catshflow.classification.controller import classification_controller
from catshflow.history.controller import history_controller

def main():
    menu = ("""
            ___________________
                    MENU
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            0. Exit
            1. Transactions
            2. Classification
            3. History
            4. Reports
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            """)
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
        elif option == 3:
            history_controller.historial()
        elif option == 0:
            flag = False
        else:
            print("Please choose one of the displayed options!")
        print()

main()