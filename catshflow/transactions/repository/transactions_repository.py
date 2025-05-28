import json
from datetime import datetime
from catshflow.classification.repository import classification_repository
from catshflow.transactions.constant.transactions_constant import get_user_paths

def reader_json(email):
    """
    Reads the user's transactions JSON file and returns its content.

    Args:
        email (str): The user's email address.

    Returns:
        list: List of transaction dictionaries.
    """
    paths = get_user_paths(email)
    with open(paths["TRANSACTIONS_FILE"]) as f:
        response = json.load(f)        
    return response

def writer_json(email,transaction):
    """
    Appends a transaction to the user's transactions JSON file.

    Args:
        email (str): The user's email address.
        transaction (dict): The transaction to append.

    Returns:
        None
    """
    paths = get_user_paths(email)
    with open(paths["TRANSACTIONS_FILE"], "r") as f:
        data = json.load(f)
    data.append(transaction)
    with open(paths["TRANSACTIONS_FILE"] , "w") as f:
        json.dump(data, f, indent=4)

def append_transaction(email,amount,m_type,category=None,fund=None,note=None):
    """
    Creates and appends a new transaction for the user.

    Args:
        email (str): The user's email address.
        amount (float or str): The transaction amount.
        m_type (str): The transaction type ("1", "2", "3", or "4").
        category (str, optional): The category index, if applicable.
        fund (str, optional): The fund index, if applicable.
        note (str, optional): Additional note for the transaction.

    Returns:
        dict: The transaction dictionary that was added.
    """
    categories = classification_repository.reader_categories(email)
    funds = classification_repository.reader_funds(email)
    m_type_replace = {
        "1": "INCOME",
        "2": "EXPENSE",
        "3": "SAVINGS",
        "4": "WITHDRAWAL"
    }
    m_type = m_type_replace.get(m_type)
    if category:
        category_data = categories[int(category)]
        category = category_data["CATEGORY"]
        transaction = {"AMOUNT":amount,
                        "TYPE":m_type,
                        "CATEGORY":category,
                        "NOTE": note,
                        "DATE":datetime.now().isoformat()}
        writer_json(email,transaction)
    elif fund:
        fun_data = funds[int(fund)]
        fund = fun_data["FUND"]
        if note:
            transaction = {"AMOUNT":amount,
                            "TYPE":m_type,
                            "FUND":fund,
                            "NOTE":note,
                            "DATE":datetime.now().isoformat()}
        else:
            transaction = {"AMOUNT":amount,
                            "TYPE":m_type,
                            "FUND":fund,
                            "DATE":datetime.now().isoformat()}
        writer_json(email,transaction)
    return transaction

