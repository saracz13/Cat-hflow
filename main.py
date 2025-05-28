from catshflow.transactions.controller import transactions_controller
from catshflow.classification.controller import classification_controller
from catshflow.history.controller import history_controller
from catshflow.reports.controller import reports_controller
from catshflow.login.controller import login_controller

def main():
    """
    Main entry point for the Catshflow application.
    Handles user login and displays the main menu for navigation.

    Returns:
        None
    """
    email,validation = login_controller.login()
    if not email:
        print("Login failed. Exiting the application.")
        return
    if not validation:
        print("User not found. Exiting the application.")
        return
    menu = ("""
            _____________________
                 🏠 MENU 🏠
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            [1] Transactions💸
            [2] Classification🗂️
            [3] History📜
            [4] Reports📊
            [0] Exit🚪
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            """)
    flag = True
    while flag:
        print()
        transactions_controller.balance_format(email)
        print(menu)
        option = int(input("Option:"))
        if option == 1:
            transactions_controller.transaction(email)
        elif option == 2:
            classification_controller.classifications(email)
        elif option == 3:
            history_controller.historial(email)
        elif option == 4:
            reports_controller.graphics(email)
        elif option == 0:
            flag = False
        else:
            print("Please choose one of the displayed options!")
        print()

main()