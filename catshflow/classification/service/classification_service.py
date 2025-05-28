from catshflow.classification.repository import classification_repository

    
def new_categories(email,confirmation,new_category,c_type):
    """
    Adds a new category for the user if it does not already exist.

    Args:
        email (str): The user's email address.
        confirmation (str): User confirmation ("1" to confirm, "2" to cancel).
        new_category (str): Name of the new category.
        c_type (str): Type of the category.

    Returns:
        dict: Validation dictionary with operation status and message.
    """
    categories = classification_repository.reader_categories(email)
    for data in categories:
        if data["CATEGORY"] == new_category:
            if data["TYPE"] == c_type:
                return {
                    "Type": "ERROR",
                    "Message": "This category already exists",
                    "Status code": 400
                    }
    if confirmation == "1":
        classification_repository.add_category(email,new_category,c_type)
        return {
                "Type": "VALID",
                "Message": "Valid category addition",
                "Status code": 200
                }
    elif confirmation == "2":
        return {
                "Type": "CANCELLED",
                "Message": "Category addition cancelled",
                "Status code": 200
                }
    else:
        return {
                "Type": "ERROR",
                "Message": "Please choose one of the displayed options",
                "Status code": 400
                    }

def eliminate_categories(email,confirmation,unwanted_category):
    """
    Eliminates a category for the user.

    Args:
        email (str): The user's email address.
        confirmation (str): User confirmation ("1" to confirm, "2" to cancel).
        unwanted_category (int): Index of the category to eliminate.

    Returns:
        dict: Validation dictionary with operation status and message.
    """
    categories = classification_repository.reader_categories()
    if int(unwanted_category) > len(categories):
        return {
                "Type": "ERROR",
                "Message": "This category doesn't exists",
                "Status code": 400
                }
    if confirmation == "1":
        classification_repository.eliminate_category(email,unwanted_category)
        return {
                "Type": "VALID",
                "Message": "Valid categories modification",
                "Status code": 200
                }
    elif confirmation == "2":
        return {
                "Type": "CANCELLED",
                "Message": "Category elimination cancelled",
                "Status code": 200
                }
    else:
        return {
                    "Type": "ERROR",
                    "Message": "Please choose one of the displayed options",
                    "Status code": 400
                    }

def rename_categories(email,confirmation,target_category,renamed_category):
    """
    Renames a category for the user.

    Args:
        email (str): The user's email address.
        confirmation (str): User confirmation ("1" to confirm, "2" to cancel).
        target_category (int): Index of the category to rename.
        renamed_category (str): New name for the category.

    Returns:
        dict: Validation dictionary with operation status and message.
    """
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
    if confirmation == "1":
        classification_repository.rename_category(email,target_category,renamed_category)
        return {
                "Type": "VALID",
                "Message": "Valid category modification",
                "Status code": 200
                }
    elif confirmation == "2":
        return {
                "Type": "CANCELLED",
                "Message": "Category renaming cancelled",
                "Status code": 200
                }
    else:
        return {
                    "Type": "ERROR",
                    "Message": "Please choose one of the displayed options",
                    "Status code": 400
                    }

def add_funds(email,confirmation,new_fund):
    """
    Adds a new fund for the user if it does not already exist.

    Args:
        email (str): The user's email address.
        confirmation (str): User confirmation ("1" to confirm, "2" to cancel).
        new_fund (str): Name of the new fund.

    Returns:
        dict: Validation dictionary with operation status and message.
    """
    funds = classification_repository.reader_funds(email)
    for data in funds:
        if data["FUND"] == new_fund:
            return {
                    "Type": "ERROR",
                    "Message": "This fund already exists",
                    "Status code": 400
                    }
    if confirmation =="1":
        classification_repository.adding_funds(email,new_fund)
        return {
                "Type": "VALID",
                "Message": "Valid fund addition",
                "Status code": 200
                }
    elif confirmation == "2":
        return {
                "Type": "CANCELLED",
                "Message": "Fund addition cancelled",
                "Status code": 200
                }
    else:
        return {
                    "Type": "ERROR",
                    "Message": "Please choose one of the displayed options",
                    "Status code": 400
                    }


def eliminate_funds(email,confirmation,unwanted_fund):
    """
    Eliminates a fund for the user.

    Args:
        email (str): The user's email address.
        confirmation (str): User confirmation ("1" to confirm, "2" to cancel).
        unwanted_fund (int): Index of the fund to eliminate.

    Returns:
        dict: Validation dictionary with operation status and message.
    """
    funds = classification_repository.reader_funds(email)
    if int(unwanted_fund) > len(funds):
        return {
                "Type": "ERROR",
                "Message": "This fund doesn't exists",
                "Status code": 400
                }
    if confirmation == "1":
        classification_repository.eliminating_funds(email,unwanted_fund)
        return {
                "Type": "VALID",
                "Message": "Valid funds modification",
                "Status code": 200
                }
    elif confirmation == "2":
        return {
                "Type": "CANCELLED",
                "Message": "Fund elimination cancelled",
                "Status code": 200
                }
    else:
        return {
                    "Type": "ERROR",
                    "Message": "Please choose one of the displayed options",
                    "Status code": 400
                    }

def rename_funds(email,confirmation,target_fund,renamed_fund):
    """
    Renames a fund for the user.

    Args:
        email (str): The user's email address.
        confirmation (str): User confirmation ("1" to confirm, "2" to cancel).
        target_fund (int): Index of the fund to rename.
        renamed_fund (str): New name for the fund.

    Returns:
        dict: Validation dictionary with operation status and message.
    """
    funds = classification_repository.reader_funds(email)
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
    
    if confirmation == "1":
        classification_repository.renaming_funds(email,target_fund,renamed_fund)
        return {
                "Type": "VALID",
                "Message": "Valid fund modification",
                "Status code": 200
                }
    elif confirmation == "2":
        return {
                "Type": "CANCELLED",
                "Message": "Fund renaming cancelled",
                "Status code": 200
                }
    else:
        return {
                    "Type": "ERROR",
                    "Message": "Please choose one of the displayed options",
                    "Status code": 400
                    }

    
