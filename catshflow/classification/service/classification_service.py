from catshflow.classification.repository import classification_repository


def new_categories(new_category):
    categories = classification_repository.reader_txt()
    if new_category in categories:
        return {
                "Type": "ERROR",
                "Message": "This category already exists",
                "Status code": 400
                }
    classification_repository.add_category(new_category)
    return {
            "Type": "VALID",
            "Message": "Valid category addition",
            "Status code": 200
            }

def eliminate_categories(unwanted_category):
    categories = classification_repository.reader_txt()
    if unwanted_category not in categories:
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
    categories = classification_repository.reader_txt()
    if target_category not in categories:
        return {
                "Type": "ERROR",
                "Message": "This category doesn't exists",
                "Status code": 400
                }
    if renamed_category in categories:
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
    funds = classification_repository.reader_csv()
    for fund in funds:
        if fund["FUND"] == new_fund["FUND"]:
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
    funds = classification_repository.reader_csv()
    for fund in funds:
        if unwanted_fund["FUND"] not in fund["FUND"]:
            return {
                    "Type": "ERROR",
                    "Message": "This fund already exists",
                    "Status code": 400
                    }
    classification_repository.eliminating_funds(unwanted_fund)
    return {
            "Type": "VALID",
            "Message": "Valid funds modification",
            "Status code": 200
            }

def rename_funds(target_fund,renamed_fund):
    funds = classification_repository.reader_csv()
    target_exists = False
    renamed_exists = False

    for fund in funds:
        fund_name = fund["FUND"]
        if fund_name == target_fund:
            target_exists = True
        if fund_name == renamed_fund:
            renamed_exists = True

    if not target_exists: 
                return {
                        "Type": "ERROR",
                        "Message": "This fund doesn't exists",
                        "Status code": 400
                        }
    
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

    
