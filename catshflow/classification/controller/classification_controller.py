import pandas as pd
from catshflow.classification.service import classification_service
from catshflow.classification.repository import classification_repository

def classifications(email):
    """
    Displays and manages the classification menu for the user, allowing category and fund operations.

    Args:
        email (str): The user's email address.

    Returns:
        None
    """
    
    print("""
          __________________________________
          🐾 What would you like to modify?
          ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            [1] CATEGORIES
            [2] FUNDS
          ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾""")
    selection = input("Enter the corresponding number: ").strip()
    print()
    if selection == "1":
        print("""
              ____________________________
                📂 Category Management
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                1️⃣  Add a new category
                2️⃣  Eliminate a category
                3️⃣  Rename a category
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                                            """)
        
        action = input("Choose an action (enter the number): ").strip()
        result = None
        if action == "1":
            print("\n🗂️  Current categories:")
            catalog = (classification_repository.reader_categories(email))
            df = pd.DataFrame(catalog)
            print(df)
            new_category = input("Name for your new category:").strip().upper()
            print("""
                  Select the category type:
                  ______________
                  [1]INCOME
                  [2]EXPENSE
                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                  """)
            c_type_index = input("👉Enter the corresponding number:")
            c_type_data = {
                "1": "INCOME",
                "2": "EXPENSE"
            }
            c_type = c_type_data.get(c_type_index)
            confirmation = input("\n✅ Confirm addition? YES[1]  NO[2]: ").strip()
            result = classification_service.new_categories(email,confirmation,new_category,c_type)
            update =classification_repository.reader_categories(email)
            df = pd.DataFrame(update)
            print(df)
        elif action == "2":
            print("\n🗂️  Available categories:")
            catalog = (classification_repository.reader_categories(email))
            df = pd.DataFrame(catalog)
            print(df)
            unwanted_category = input("\n❌ Enter the number of the category to eliminate: ").strip()
            confirmation = input("\n✅ Confirm elimination? YES[1]  NO[2]: ").strip()
            result = classification_service.eliminate_categories(email,confirmation,unwanted_category)
            print("\n🗂️  Updated categories:")
            update = classification_repository.reader_categories(email)
            df = pd.DataFrame(update)
            print(df)
        elif action == "3":
            print("\n🗂️  Available categories:")
            catalog = (classification_repository.reader_categories(email))
            df = pd.DataFrame(catalog)
            print(df)
            target_category = input("\n🔄 Enter the number of the category to rename: ").strip()
            renamed_category = input("New name for the category:").strip().upper()
            confirmation = input("\n✅ Confirm renaming? YES[1]  NO[2]: ").strip()
            result = classification_service.rename_categories(email,confirmation,target_category,renamed_category)
            update = (classification_repository.reader_categories(email))
            df = pd.DataFrame(update)
            print(df)
        else:
            print("Please choose one of the displayed options!")
            return
    elif selection == "2":
        print("💰 Fund Management")
        print("""
              ____________________________
              1️⃣  Open a new fund
              2️⃣  Close an existing fund
              3️⃣  Rename an existing fund
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """
        )
        action = input("Which action do you want to perform? Enter the corresponding number:").strip()
        result = None
        if action == "1": 
            print("\n💰 Your funds:")
            catalog = (classification_repository.reader_funds(email))
            df = pd.DataFrame(catalog)
            print(df)
            new_fund = input("💡 Name for your new fund:").strip().upper()
            confirmation = input("\n✅ Confirm creation? YES[1]  NO[2]: ").strip()
            result = classification_service.add_funds(email,confirmation,new_fund)
            print("\n💰 Updated funds:")
            update = (classification_repository.reader_funds(email))
            df = pd.DataFrame(update)
            print(df)
        elif action == "2":
            print("\n💰 Available funds:")
            catalog = (classification_repository.reader_funds(email))
            df = pd.DataFrame(catalog)
            print(df)
            unwanted_fund = input("\n❌ Which fund would you like to close? Enter the number: ").strip()
            confirmation = input("\n✅ Confirm closure? YES[1]  NO[2]: ").strip()
            result = classification_service.eliminate_funds(email,confirmation,unwanted_fund)
            print("\n💰 Updated funds:")
            update = (classification_repository.reader_funds(email))
            df = pd.DataFrame(update)
            print(df)
        elif action == "3":
            print("\n💰 Available funds:")
            catalog = (classification_repository.reader_funds(email))
            df = pd.DataFrame(catalog)
            print(df)
            target_fund = input("\n🔄 Which fund would you like to modify? Enter the number: ").strip()
            renamed_fund = input("New name for the fund:").strip().upper()
            confirmation = input("\n✅ Confirm renaming? YES[1]  NO[2]: ").strip()
            result = classification_service.rename_funds(email,confirmation,target_fund,renamed_fund)
            print("\n💰 Updated funds:")
            update = (classification_repository.reader_funds(email))
            df = pd.DataFrame(update)
            print(df)
        else:
            print("\n⚠️  Please choose one of the displayed options!")
            return {"Type": "ERROR",
                    "Message": "Please choose one of the displayed options!",
                    "Status code": 400}
    else:
        print("\n⚠️  Please choose one of the displayed options!")
        return {"Type": "ERROR",
                "Message": "Please choose one of the displayed options!",
                "Status code": 400}
    print(result)