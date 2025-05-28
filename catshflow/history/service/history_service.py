from datetime import datetime
from catshflow.history.repository import history_repository
from catshflow.classification.repository import classification_repository

def before_filter(email,date):
    """
    Returns all transactions before a given date.

    Args:
        email (str): The user's email address.
        date (datetime): The reference date.

    Returns:
        tuple: (list of filtered transactions, validation dict)
    """
    transactions = history_repository.reader_json(email)
    filtered_data = []
    for data in transactions:
        transaction_date = datetime.fromisoformat(data["DATE"])
        if transaction_date.date() < date.date():
            filtered_data.append(data) 
    if not filtered_data:
       return [],{"Type": "ERROR", 
                "Message": "There are no transactions made in that date", 
                "Status code": 400}    
    return filtered_data, {"Type": "VALID", 
                           "Message": "Search completed", 
                           "Status code": 200}

def after_filter(email,date):
    """
    Returns all transactions after a given date.

    Args:
        email (str): The user's email address.
        date (datetime): The reference date.

    Returns:
        tuple: (list of filtered transactions, validation dict)
    """
    transactions = history_repository.reader_json(email)
    filtered_data = []
    for data in transactions:
        transaction_date = datetime.fromisoformat(data["DATE"])
        if transaction_date.date() > date.date():
            filtered_data.append(data)    
    if not filtered_data:
       return [],{"Type": "ERROR", 
                "Message": "There are no transactions made in that date", 
                "Status code": 400}   
    return filtered_data, {"Type": "VALID", 
                           "Message": "Search completed", 
                           "Status code": 200}


def exact_filter(email,date):
    """
    Returns all transactions on a given date.

    Args:
        email (str): The user's email address.
        date (datetime): The reference date.

    Returns:
        tuple: (list of filtered transactions, validation dict)
    """
    transactions = history_repository.reader_json(email)
    filtered_data = []
    for data in transactions:
        transaction_date = datetime.fromisoformat(data["DATE"])
        if transaction_date.date() == date.date():
            filtered_data.append(data)
    if not filtered_data:
       return [],{"Type": "ERROR", 
                "Message": "There are no transactions made in that date", 
                "Status code": 400}     
    return filtered_data,{"Type": "VALID", 
                           "Message": "Search completed", 
                           "Status code": 200}


def between_dates_filter(email,start_date,end_date):
    """
    Returns all transactions between two dates (inclusive).

    Args:
        email (str): The user's email address.
        start_date (datetime): The start date.
        end_date (datetime): The end date.

    Returns:
        tuple: (list of filtered transactions, validation dict)
    """
    transactions = history_repository.reader_json(email)
    filtered_data = []
    for data in transactions:
        transaction_date = datetime.fromisoformat(data["DATE"])
        if start_date.date() <= transaction_date.date() <= end_date.date():
            filtered_data.append(data)     
    if not filtered_data:
       return [],{"Type": "ERROR", 
                "Message": "There are no transactions made in that date", 
                "Status code": 400}
    return filtered_data,{"Type": "VALID", 
                           "Message": "Search completed", 
                           "Status code": 200}



def great_than_amount(email,amount):
    """
    Returns all transactions with amount greater than the given value.

    Args:
        email (str): The user's email address.
        amount (float): The minimum amount.

    Returns:
        tuple: (list of filtered transactions, validation dict)
    """
    transactions = history_repository.reader_json(email)
    filtered_data = []
    for data in transactions:
        if float(data["AMOUNT"]) > float(amount):
            filtered_data.append(data)
    if not filtered_data:
        return [],{"Type": "ERROR", 
                "Message": "There is no data over that amount", 
                "Status code": 400}
    return filtered_data,{"Type": "VALID", 
                          "Message": "  Search completed", 
                          "Status code": 200}

def less_than_amount(email,amount):
    """
    Returns all transactions with amount less than the given value.

    Args:
        email (str): The user's email address.
        amount (float): The maximum amount.

    Returns:
        tuple: (list of filtered transactions, validation dict)
    """
    transactions = history_repository.reader_json(email)
    filtered_data = []
    for data in transactions:
        if float(data["AMOUNT"]) < float(amount):
            filtered_data.append(data)
    if not filtered_data:
        return [],{"Type": "ERROR", 
                "Message": "There is no data below that amount", 
                "Status code": 400}
    return filtered_data,{"Type": "VALID", 
                          "Message": "  Search completed", 
                          "Status code": 200}


def between_amounts(email,amount_1,amount_2): 
    """
    Returns all transactions with amount between two values.

    Args:
        email (str): The user's email address.
        amount_1 (float): The lower bound.
        amount_2 (float): The upper bound.

    Returns:
        tuple: (list of filtered transactions, validation dict)
    """
    transactions = history_repository.reader_json(email)
    filtered_data = []
    for data in transactions:
        if float(amount_1) < float(data["AMOUNT"]) < float(amount_2):
            filtered_data.append(data)
    if not filtered_data:
        return [],{"Type": "ERROR", 
                "Message": "There is no data below that amount", 
                "Status code": 400}
    return filtered_data,{"Type": "VALID", 
                          "Message": "  Search completed", 
                          "Status code": 200}

def same_as_amount(email,amount):
    """
    Returns all transactions with amount equal to the given value.

    Args:
        email (str): The user's email address.
        amount (float): The amount to match.

    Returns:
        tuple: (list of filtered transactions, validation dict)
    """
    transactions = history_repository.reader_json(email)
    filtered_data = []
    for data in transactions:
        if float(data["AMOUNT"]) == float(amount):
            filtered_data.append(data)
    if not filtered_data:
        return [],{"Type": "ERROR", 
                "Message": "There is no data with that amount", 
                "Status code": 400}
    return filtered_data,{"Type": "VALID", 
                          "Message": "  Search completed", 
                          "Status code": 200}

def type_filter(email,transaction_type):
    """
    Returns all transactions of a given type.

    Args:
        email (str): The user's email address.
        transaction_type (str): The type of transaction.

    Returns:
        tuple: (list of filtered transactions, validation dict)
    """
    transactions = history_repository.reader_json(email)
    filtered_data = []
    for data in transactions:
        if data["TYPE"] == transaction_type:
            filtered_data.append(data)
    if not filtered_data:
        return [],{"Type": "ERROR", 
                "Message": "There is no data with that type", 
                "Status code": 400}
    return filtered_data,{"Type": "VALID", 
                          "Message": "  Search completed", 
                          "Status code": 200}


def category_filter(email,index_category):
    """
    Returns all transactions for a given category.

    Args:
        email (str): The user's email address.
        index_category (int): Index of the category.

    Returns:
        tuple: (list of filtered transactions, validation dict)
    """
    categories = classification_repository.reader_categories(email)
    transactions = history_repository.reader_json(email)
    target_category = categories[int(index_category)]
    filtered_data = []
    for data in transactions:
        if "CATEGORY" in data:
            if data["CATEGORY"] == target_category["CATEGORY"]:
                if data["TYPE"] == target_category["TYPE"]:
                    filtered_data.append(data)
    if not filtered_data:
        return [],{"Type": "ERROR", 
                "Message": "There is no data with that category", 
                "Status code": 400}
    return filtered_data,{"Type": "VALID", 
                          "Message": "  Search completed", 
                          "Status code": 200}


def fund_filter(email,index_fund):
    """
    Returns all transactions for a given fund.

    Args:
        email (str): The user's email address.
        index_fund (int): Index of the fund.

    Returns:
        tuple: (list of filtered transactions, validation dict)
    """
    funds = classification_repository.reader_funds(email)
    transactions = history_repository.reader_json(email)
    target_fund = funds[int(index_fund)]
    filtered_data = []
    for data in transactions:
        if "FUND" in data:
            if data["FUND"] == target_fund["FUND"]:
                filtered_data.append(data)
    if not filtered_data:
        return [],{"Type": "ERROR", 
                "Message": "There are no transactions made in that fund", 
                "Status code": 400}
    return filtered_data,{"Type": "VALID", 
                          "Message": "  Search completed", 
                          "Status code": 200}
    
