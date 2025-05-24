import json
from catshflow.transactions.constant.transactions_constant import MOVEMENTS_FILE

def reader_json():
    with open(MOVEMENTS_FILE) as f:
        response = json.load(f)        
    return response

def writer_json(transaction):
    with open(MOVEMENTS_FILE, "r") as f:
        data = json.load(f)
    data.append(transaction)
    with open(MOVEMENTS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def append_transaction(amount,m_type,category=None,goal=None,note=None):
    if category:
        transaction = {"AMOUNT":amount,
                        "TYPE":m_type,
                        "CATEGORY":category,
                        "NOTE": note}
        writer_json(transaction)
    elif goal:
        transaction = {"AMOUNT":amount,
                        "TYPE":m_type,
                        "GOAL":goal}
        writer_json(transaction)
    return transaction