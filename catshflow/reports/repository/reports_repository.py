import json
from catshflow.reports.constant.reports_constant import TRANSACTIONS_FILE

def reader_json(TRANSACTIONS_FILE):
    with open(TRANSACTIONS_FILE) as f:
        response = json.load(f)        
    return response
