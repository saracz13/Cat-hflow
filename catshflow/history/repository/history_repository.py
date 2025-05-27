import json
from catshflow.history.constant.history_constant import TRANSACTIONS_FILE

def reader_json():
    with open(TRANSACTIONS_FILE) as f:
        response = json.load(f)        
    return response