from catshflow.classification.service import classification_service
from catshflow.classification.repository import classification_repository

def classifications():
    print(["CATEGORIES[1]","FUNDS[2]"])
    selection = input("Which one would you like to modify? Enter the corresponding number: ")
    if selection == "1":
        print("""
              1. Add a new category 
              2. Eliminate a category
              3. Rename a category
              """
        )
        action = input("Which action do you want to perform? Enter the corresponding number:")
        result = None
        if action == "1":
            new_category = input("How would you like to name your new category?").strip().upper()
            result = classification_service.new_categories(new_category)
            print(classification_repository.reader_txt())
        elif action == "2":
            print(classification_repository.reader_txt())
            unwanted_category = input("Which category would you like to delete?").strip().upper()
            result = classification_service.eliminate_categories(unwanted_category)
            print(classification_repository.reader_txt())
        elif action == "3":
            print(classification_repository.reader_txt())
            target_category = input("Which category would you like to change?").strip().upper()
            renamed_category = input("How would you like to rename your category:").strip().upper()
            result = classification_service.rename_categories(target_category,renamed_category)
            print(classification_repository.reader_txt())
        else:
            print("Please choose one of the displayed options!")
            return
    elif selection == "2":
        print("""
              1. Open a new fund 
              2. Close an existing fund
              3. Rename an existing fund
              """
        )
        action = input("Which action do you want to perform? Enter the corresponding number:")
        result = None
        if action == "1": 
            new_fund = input("How would you like to name your new fund?").strip().upper()
            result = classification_service.add_funds(new_fund)
            print(classification_repository.reader_csv())
        elif action == "2":
            print(classification_repository.reader_csv())
            unwanted_fund = input("Which fund would you like to close?").strip().upper()
            result = classification_service.eliminate_funds(unwanted_fund)
            print(classification_repository.reader_csv())
        elif action == "3":
            print(classification_repository.reader_csv())
            target_fund = input("Which fund would you like to modify?").strip().upper()
            renamed_fund = input("How would you like to rename it?").strip().upper()
            result = classification_service.rename_funds(target_fund,renamed_fund)
            print(classification_repository.reader_csv())
        else:
            print("Please choose one of the displayed options!")
            return
    else:
        print("Please choose one of the displayed options!")
        return
    print(result)