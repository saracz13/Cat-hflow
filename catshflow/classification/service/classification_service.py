from catshflow.classification.repository import classification_repository


def new_categories(new_category,c_type):
    categories = classification_repository.reader_categories()
    for data in categories:
        if data["CATEGORY"] == new_category:
            if data["TYPE"] == c_type:
                return {
                    "Type": "ERROR",
                    "Message": "This category already exists",
                    "Status code": 400
                    }
    classification_repository.add_category(new_category,c_type)
    return {
            "Type": "VALID",
            "Message": "Valid category addition",
            "Status code": 200
            }

def eliminate_categories(unwanted_category):
    categories = classification_repository.reader_categories()
    if int(unwanted_category) > len(categories):
        return {
                "Type": "ERROR",
                "Message": "This category doesn't exists",
                "Status code": 400
                }
    classification_repository.eliminate_category(unwanted_category)
    return {
            "Type": "VALID",
            "Message": "Valid categories modification",
            "Status code": 200
            }

def rename_categories(target_category,renamed_category):
    categories = classification_repository.reader_categories()
    renamed_category_exist = False
    if int(target_category) > len(categories):
        return {
                "Type": "ERROR",
                "Message": "This category doesn't exists",
                "Status code": 400
                }
    for data in categories:
        if data["CATEGORY"] == renamed_category:
             renamed_category_exist = True
    if renamed_category_exist:
        return {
                "Type": "ERROR",
                "Message": "This category already exists",
                "Status code": 400
                }
    classification_repository.rename_category(target_category,renamed_category)
    return {
            "Type": "VALID",
            "Message": "Valid category modification",
            "Status code": 200
            }

def add_funds(new_fund):
    funds = classification_repository.reader_funds()
    for data in funds:
        if data["FUND"] == new_fund:
            return {
                    "Type": "ERROR",
                    "Message": "This fund already exists",
                    "Status code": 400
                    }
    classification_repository.adding_funds(new_fund)
    return {
            "Type": "VALID",
            "Message": "Valid fund addition",
            "Status code": 200
            }


def eliminate_funds(unwanted_fund):
    funds = classification_repository.reader_funds()
    if int(unwanted_fund) > len(funds):
        return {
                "Type": "ERROR",
                "Message": "This fund doesn't exists",
                "Status code": 400
                }
    classification_repository.eliminating_funds(unwanted_fund)
    return {
            "Type": "VALID",
            "Message": "Valid funds modification",
            "Status code": 200
            }

def rename_funds(target_fund,renamed_fund):
    funds = classification_repository.reader_funds()
    if int(target_fund) > len(funds):
        return {
                "Type": "ERROR",
                "Message": "This fund doesn't exists",
                "Status code": 400
                }     
    renamed_exists = False
    for data in funds:
        if data["FUND"] == renamed_fund:
            renamed_exists = True
    
    if renamed_exists:
                return {
                        "Type": "ERROR",
                        "Message": "This fund already exists",
                        "Status code": 400
                        }
    
    classification_repository.renaming_funds(target_fund,renamed_fund)
    return {
            "Type": "VALID",
            "Message": "Valid fund modification",
            "Status code": 200
            }

    
