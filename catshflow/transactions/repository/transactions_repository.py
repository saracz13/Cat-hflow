import json
from datetime import datetime
from catshflow.transactions.constant.transactions_constant import TRANSACTIONS_FILE
from catshflow.classification.repository import classification_repository


def reader_json():
    with open(TRANSACTIONS_FILE) as f:
        response = json.load(f)        
    return response

def writer_json(transaction):
    with open(TRANSACTIONS_FILE, "r") as f:
        data = json.load(f)
    data.append(transaction)
    with open(TRANSACTIONS_FILE , "w") as f:
        json.dump(data, f, indent=4)

def append_transaction(amount,m_type,category=None,fund=None,note=None):
    categories = classification_repository.reader_categories()
    m_type_replace = {
        "1": "INCOME",
        "2": "EXPENDITURE",
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
        writer_json(transaction)
    elif fund:
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
        writer_json(transaction)
    return transaction

