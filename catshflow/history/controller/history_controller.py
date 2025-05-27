import pandas as pd
from catshflow.history.service import history_service

def historial():
    print("""
          __________________
          FILTERS
          ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          1. Date
          2. Amount
          3. Type
          4. Classification
          ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          """)
    filter_option = input("Select the number corresponding to the filter you want to apply:")
    if filter_option == "2":
        print("""
              1. Greater than _____
              2. Less than _____
              3. Same as _____
              """)
        action = input("How would you like to filter your transactions? Enter the corresponding number:")
        if action == "1":
            filter = float(input("Enter the value:"))
            result,validation = history_service.great_than_amount(filter)
            df = pd.DataFrame(result)
            print(validation)
            print(df)
        elif action == "2":
            filter = float(input("Enter the value:"))
            result,validation = history_service.less_than_amount(filter)
            df = pd.DataFrame(result)
            print(validation)
            print(df)
        elif action == "3":
            filter = float(input("Enter the value:"))
            result,validation = history_service.same_as_amount(filter)
            df = pd.DataFrame(result)
            print(validation)
            print(df)