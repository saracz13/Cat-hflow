import json
from catshflow.transactions.constant.transactions_constant import TRANSACTIONS_FILE


def reader_json():
    with open(TRANSACTIONS_FILE) as f:
        response = json.load(f)        
    return response

def writer_json(transaction):
    with open(TRANSACTIONS_FILE, "r") as f:
        data = json.load(f)
    data.append(transaction)
    with open(TRANSACTIONS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def append_transaction(amount,m_type,category=None,fund=None,note=None):
    if category:
        transaction = {"AMOUNT":amount,
                        "TYPE":m_type,
                        "CATEGORY":category,
                        "NOTE": note}
        writer_json(transaction)
    elif fund:
        transaction = {"AMOUNT":amount,
                        "TYPE":m_type,
                        "FUND":fund}
        writer_json(transaction)
    return transaction

