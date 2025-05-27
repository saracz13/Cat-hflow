import pandas as pd
from catshflow.classification.service import classification_service
from catshflow.classification.repository import classification_repository

def classifications():
    print("""
        What would you like to modify?
        ______________  
        [1] CATEGORIES
        [2] FUNDS
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        """)
    selection = input("Enter the corresponding number:")
    if selection == "1":
        print("""
              _______________________
              1. Add a new category 
              2. Eliminate a category
              3. Rename a category
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """
        )
        action = input("Choose an action(enter the number):")
        result = None
        if action == "1":
            new_category = input("How would you like to name your new category?").strip().upper()
            print("""
                  Category type:
                  ______________
                  [1]INCOME
                  [2]EXPENDITURE
                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                  """)
            c_type_index = input("Enter the corresponding number:")
            c_type_data = {
                "1": "INCOME",
                "2": "EXPENDITURE"
            }
            c_type = c_type_data.get(c_type_index)
            result = classification_service.new_categories(new_category,c_type)
            update =classification_repository.reader_categories()
            df = pd.DataFrame(update)
            print(df)
        elif action == "2":
            print("""
                  Available categories:
                  """)
            catalog = (classification_repository.reader_categories())
            df = pd.DataFrame(catalog)
            print(df)
            unwanted_category = input("Enter the number of the category you want to eliminate:")
            result = classification_service.eliminate_categories(unwanted_category)
            update = classification_repository.reader_categories()
            df = pd.DataFrame(update)
            print(df)
        elif action == "3":
            print("""
                  Available categories:
                  """)
            catalog = (classification_repository.reader_categories())
            df = pd.DataFrame(catalog)
            print(df)
            target_category = input("Enter the number of the category you want to rename:")
            renamed_category = input("Enter the new name:")
            result = classification_service.rename_categories(target_category,renamed_category)
            update = (classification_repository.reader_categories())
            df = pd.DataFrame(update)
            print(df)
        else:
            print("Please choose one of the displayed options!")
            return
    elif selection == "2":
        print("""
              ___________________________
              1. Open a new fund 
              2. Close an existing fund
              3. Rename an existing fund
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """
        )
        action = input("Which action do you want to perform? Enter the corresponding number:")
        result = None
        if action == "1": 
            new_fund = input("How would you like to name your new fund?").strip().upper()
            result = classification_service.add_funds(new_fund)
            update = (classification_repository.reader_funds())
            df = pd.DataFrame(update)
            print(df)
        elif action == "2":
            print("""
                  Available funds:
                  """)
            catalog = (classification_repository.reader_funds())
            df = pd.DataFrame(catalog)
            print(df)
            unwanted_fund = input("Which fund would you like to close?")
            result = classification_service.eliminate_funds(unwanted_fund)
            update = (classification_repository.reader_funds())
            df = pd.DataFrame(update)
            print(df)
        elif action == "3":
            print("""
                  Available funds:
                  """)
            catalog = (classification_repository.reader_funds())
            df = pd.DataFrame(catalog)
            print(df)
            target_fund = input("Which fund would you like to modify?")
            renamed_fund = input("How would you like to rename it?").strip().upper()
            result = classification_service.rename_funds(target_fund,renamed_fund)
            update = (classification_repository.reader_funds())
            df = pd.DataFrame(update)
            print(df)
        else:
            print("Please choose one of the displayed options!")
            return
    else:
        print("Please choose one of the displayed options!")
        return
    print(result)