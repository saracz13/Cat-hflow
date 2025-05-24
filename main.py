from catshflow.transactions.controller import transactions_controller
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
        elif option == 0:
            flag = False
        else:
            print("Wrong option")

        print()

main()