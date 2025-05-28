import pandas as pd
from datetime import datetime
from catshflow.history.service import history_service
from catshflow.classification.repository import classification_repository

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
    if filter_option == "1":
        print("""
              _____________________
              1. Before _____
              2. After than _____
              3. Exact_____
              4. Between ____
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """)
        action = input("Enter the corresponding number:")
        if action == "1":
            date = datetime.fromisoformat(input("Enter the date(YYYY-MM-DD):"))
            result,validation = history_service.before_filter(date)
            if result:
                df = pd.DataFrame(result)
                print(df)
        print(validation)
        if action == "2":
            date = datetime.fromisoformat(input("Enter the date(YYYY-MM-DD):"))
            result,validation = history_service.after_filter(date)
            if result:
                df = pd.DataFrame(result)
                print(df)
        print(validation)
        if action == "3":
            date = datetime.fromisoformat(input("Enter the date(YYYY-MM-DD):"))
            result,validation = history_service.exact_filter(date)
            if result:
                df = pd.DataFrame(result)
                print(df)
            print(validation)
        if action == "4":
            start_date = datetime.fromisoformat(input("Enter the start date(YYYY-MM-DD):"))
            end_date = datetime.fromisoformat(input("Enter the end date(YYYY-MM-DD):"))
            result,validation = history_service.between_dates_filter(start_date,end_date)
            if result:
                df = pd.DataFrame(result)
                print(df)
            print(validation)
        
    elif filter_option == "2":
        print("""
              ________________________
              1. Greater than _____
              2. Less than _____
              3. Same as _____
              4. Between _____
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """)
        action = input("Enter the corresponding number:")
        if action == "1":
            amount = float(input("Enter the value:"))
            result,validation = history_service.great_than_amount(amount)
            if result:
                df = pd.DataFrame(result)
                print(df)
            print(validation)
        elif action == "2":
            amount = float(input("Enter the value:"))
            result,validation = history_service.less_than_amount(amount)
            if result:
                df = pd.DataFrame(result)
                print(df)
            print(validation)
        elif action == "3":
            amount = float(input("Enter the value:"))
            result,validation = history_service.same_as_amount(amount)
            if result:
                df = pd.DataFrame(result)
                print(df)
            print(validation)
        elif action == "4":
            amount_1 = float(input("Enter the start value:"))
            amount_2 = float(input("Enter the end value:"))
            result,validation = history_service.between_amounts(amount_1,amount_2)
            if result:
                df = pd.DataFrame(result)
                print(df)
            print(validation)
    elif filter_option == "3":
        print("""
              ________________________
              1. INCOMES
              2. EXPENDITURES
              3. SAVINGS
              4. WITHDRAWALS
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """)
        action = input("Enter the corresponding number:")
        action_code = {
            "1": "INCOME",
            "2": "EXPENDITURE",
            "3": "SAVING",
            "4": "WITHDRAWAL"
        }
        transaction_type = action_code.get(action)
        result,validation = history_service.type_filter(transaction_type)
        if result:
            df = pd.DataFrame(result)
            print(df)
        print(validation)
    elif filter_option == "4":
        print("""
              ________________
              [1]CATEGORIES
              [2]FUNDS
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """)
        action = input("Enter the corresponding number:")
        if action == "1":
            catalog = (classification_repository.reader_categories())
            df = pd.DataFrame(catalog)
            print(df)
            index_category = input("Enter the corresponding number:")
            result,validation = history_service.category_filter(index_category)
            if result:
                df = pd.DataFrame(result)
                print(df)
            print(validation)
        elif action == "2":
            catalog = (classification_repository.reader_funds())
            df = pd.DataFrame(catalog)
            print(df)
            index_fund = input("Enter the corresponding number:")
            result,validation = history_service.fund_filter(index_fund)
            if result:
                df = pd.DataFrame(result)
                print(df)
            print(validation)
    