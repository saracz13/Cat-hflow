import pandas as pd
from datetime import datetime
from catshflow.history.service import history_service
from catshflow.classification.repository import classification_repository

def historial(email):
    """
    Displays and manages the history menu for the user, allowing transaction filtering by date, amount, type, or classification.

    Args:
        email (str): The user's email address.

    Returns:
        None
    """
    print("""
          _______________________________
          📜 Transaction History Filters
          ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
           [1] Date
           [2] Amount
           [3] Type
           [4] Classification
          ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          """)
    filter_option = input("Select the number corresponding to the filter you want to apply:")
    if filter_option == "1":
        print("""
              _______________________
                 📅 Date Filters
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
               1️⃣  Before a date
               2️⃣  After a date
               3️⃣  Exact date
               4️⃣  Between two dates
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """)
        action = input("Enter the corresponding number:")
        if action == "1":
            date = datetime.fromisoformat(input("Enter the date(YYYY-MM-DD):"))
            result,validation = history_service.before_filter(email,date)
            if result:
                df = pd.DataFrame(result)
                print("\n📝 Results:\n", df)
            print("🔔", validation["Message"])
        if action == "2":
            date = datetime.fromisoformat(input("Enter the date(YYYY-MM-DD):"))
            result,validation = history_service.after_filter(email,date)
            if result:
                df = pd.DataFrame(result)
                print("\n📝 Results:\n", df)
            print("\n📝 Results:\n", df)
        if action == "3":
            date = datetime.fromisoformat(input("Enter the date(YYYY-MM-DD):"))
            result,validation = history_service.exact_filter(email,date)
            if result:
                df = pd.DataFrame(result)
                print("\n📝 Results:\n", df)
            print("\n📝 Results:\n", df)
        if action == "4":
            start_date = datetime.fromisoformat(input("Enter the start date(YYYY-MM-DD):"))
            end_date = datetime.fromisoformat(input("Enter the end date(YYYY-MM-DD):"))
            result,validation = history_service.between_dates_filter(email,start_date,end_date)
            if result:
                df = pd.DataFrame(result)
                print("\n📝 Results:\n", df)
            print("🔔", validation["Message"])
        else:
            print("⚠️  Please choose one of the displayed options!")

    elif filter_option == "2":
        print("""
              __________________________
                  💲 Amount Filters
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              1️⃣  Greater than ...
              2️⃣  Less than ...
              3️⃣  Same as ...
              4️⃣  Between two values...
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """)
        action = input("Enter the corresponding number:")
        if action == "1":
            amount = float(input("💲 Enter the value:"))
            result,validation = history_service.great_than_amount(email,amount)
            if result:
                df = pd.DataFrame(result)
                print("\n📝 Results:\n", df)
            print("🔔", validation["Message"])
        elif action == "2":
            amount = float(input("💲 Enter the value:"))
            result,validation = history_service.less_than_amount(email,amount)
            if result:
                df = pd.DataFrame(result)
                print("\n📝 Results:\n", df)
            print("🔔", validation["Message"])
        elif action == "3":
            amount = float(input("💲 Enter the value:"))
            result,validation = history_service.same_as_amount(email,amount)
            if result:
                df = pd.DataFrame(result)
                print("\n📝 Results:\n", df)
            print("🔔", validation["Message"])
        elif action == "4":
            amount_1 = float(input("💲 Enter the start value:"))
            amount_2 = float(input("💲 Enter the end value:"))
            result,validation = history_service.between_amounts(email,amount_1,amount_2)
            if result:
                df = pd.DataFrame(result)
                print("\n📝 Results:\n", df)
            print("🔔", validation["Message"])
    elif filter_option == "3":
        print("""
              ____________________
              "🔖 Type Filters"
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              1️⃣  INCOMES
              2️⃣  EXPENSES
              3️⃣  SAVINGS
              4️⃣  WITHDRAWALS
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """)
        action = input("Enter the corresponding number:")
        action_code = {
            "1": "INCOME",
            "2": "EXPENSE",
            "3": "SAVING",
            "4": "WITHDRAWAL"
        }
        transaction_type = action_code.get(action)
        result,validation = history_service.type_filter(email,transaction_type)
        if result:
            df = pd.DataFrame(result)
            print("\n📝 Results:\n", df)
        print("🔔", validation["Message"])
    elif filter_option == "4":
        print("""
              ____________________________
              🏷️  Classification Filters
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              [1]CATEGORIES
              [2]FUNDS
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """)
        action = input("Enter the corresponding number:")
        if action == "1":
            catalog = (classification_repository.reader_categories(email))
            df = pd.DataFrame(catalog)
            print("\n📚 Categories:\n", df)
            index_category = input("Enter the corresponding number:")
            result,validation = history_service.category_filter(email,index_category)
            if result:
                df = pd.DataFrame(result)
                print("\n📝 Results:\n", df)
            print("🔔", validation["Message"])
        elif action == "2":
            catalog = (classification_repository.reader_funds(email))
            df = pd.DataFrame(catalog)
            print("\n💰 Funds:\n", df)
            index_fund = input("Enter the corresponding number:")
            result,validation = history_service.fund_filter(email,index_fund)
            if result:
                df = pd.DataFrame(result)
                print("\n📝 Results:\n", df)
            print("🔔", validation["Message"])
    