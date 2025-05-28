import csv
from catshflow.classification.constant.classification_constant import get_user_paths

def reader_categories(email):
    """
    Reads the user's categories file and returns a list of categories.

    Args:
        email (str): The user's email address.

    Returns:
        list: List of category dictionaries.
    """
    paths = get_user_paths(email)
    response = []
    with open(paths["CATEGORIES_FILE"], newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
            response.append(line) 
    return response

def reader_funds(email):
    """
    Reads the user's funds file and returns a list of funds.

    Args:
        email (str): The user's email address.

    Returns:
        list: List of fund dictionaries.
    """
    paths = get_user_paths(email)
    response = []
    with open(paths["FUNDS_FILE"], newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
            response.append(line)
    return response

def add_category(email,new_category,c_type):
    """
    Adds a new category to the user's categories file.

    Args:
        email (str): The user's email address.
        new_category (str): The name of the new category.
        c_type (str): The type of the category.

    Returns:
        str: Path to the user's categories file.
    """
    paths = get_user_paths(email)
    with open(paths["CATEGORIES_FILE"],"a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_category, c_type])
    return paths["CATEGORIES_FILE"]


def eliminate_category(email,unwanted_category):
    """
    Removes a category from the user's categories file.

    Args:
        email (str): The user's email address.
        unwanted_category (int): Index of the category to remove.

    Returns:
        str: Path to the user's categories file.
    """
    categories = reader_categories(email)
    remove_category = categories[int(unwanted_category)]
    updated_categories = []
    for data in categories:
        if data != remove_category:
            updated_categories.append(data)     
    paths = get_user_paths(email)
    with open(paths["CATEGORIES_FILE"], "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["CATEGORY", "TYPE"])
        writer.writeheader()
        writer.writerows(updated_categories)
    return paths["CATEGORIES_FILE"]


def rename_category(email,target_category,renamed_category):
    """
    Renames a category in the user's categories file.

    Args:
        email (str): The user's email address.
        target_category (int): Index of the category to rename.
        renamed_category (str): New name for the category.

    Returns:
        str: Path to the user's categories file.
    """
    categories = reader_categories(email)
    categories[int(target_category)]["CATEGORY"] = renamed_category
    paths = get_user_paths(email)
    with open(paths["CATEGORIES_FILE"], "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["CATEGORY", "TYPE"])
        writer.writeheader()
        writer.writerows(categories)
    return paths["CATEGORIES_FILE"]
    

def adding_funds(email,new_fund):
    """
    Adds a new fund to the user's funds file.

    Args:
        email (str): The user's email address.
        new_fund (str): The name of the new fund.

    Returns:
        str: Path to the user's funds file.
    """
    paths = get_user_paths(email)
    with open(paths["FUNDS_FILE"], "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_fund, 0])
    return paths["FUNDS_FILE"]


def eliminating_funds(email,unwanted_fund):
    """
    Removes a fund from the user's funds file.

    Args:
        email (str): The user's email address.
        unwanted_fund (int): Index of the fund to remove.

    Returns:
        str: Path to the user's funds file.
    """
    funds = reader_funds()
    remove_fund = funds[int(unwanted_fund)]
    updated_funds = []
    for data in funds:
        if data != remove_fund:
            updated_funds.append(data)    
    paths = get_user_paths(email)
    with open(paths["FUNDS_FILE"], "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(updated_funds)
    return paths["FUNDS_FILE"]


def renaming_funds(email,target_fund,renamed_fund):
    """
    Renames a fund in the user's funds file.

    Args:
        email (str): The user's email address.
        target_fund (int): Index of the fund to rename.
        renamed_fund (str): New name for the fund.

    Returns:
        str: Path to the user's funds file.
    """
    funds = reader_funds()
    funds[int(target_fund)]["FUND"] = renamed_fund
    paths = get_user_paths(email)
    with open(paths["FUNDS_FILE"], "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(funds)
    return paths["FUNDS_FILE"]


def decrease_fund(email,fund,amount):
    """
    Decreases the amount of a fund.

    Args:
        email (str): The user's email address.
        fund (int): Index of the fund to decrease.
        amount (float): Amount to subtract.

    Returns:
        str: Path to the user's funds file.
    """
    funds = reader_funds()
    funds[int(fund)]["AMOUNT"] = str(float(funds[int(fund)]["AMOUNT"]) - float(amount))
    paths = get_user_paths(email)
    with open(paths["FUNDS_FILE"], "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(funds)
    return paths["FUNDS_FILE"]

def increase_fund(email,fund, amount):
    """
    Increases the amount of a fund.

    Args:
        email (str): The user's email address.
        fund (int): Index of the fund to increase.
        amount (float): Amount to add.

    Returns:
        str: Path to the user's funds file.
    """
    funds = reader_funds()
    funds[int(fund)]["AMOUNT"] = str(float(funds[int(fund)]["AMOUNT"]) + float(amount))
    paths = get_user_paths(email)
    with open(paths["FUNDS_FILE"], "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(funds)
    return paths["FUNDS_FILE"]
