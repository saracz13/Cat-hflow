import json
from catshflow.reports.constant.reports_constant import MOVEMENTS_FILE

def reader_json(MOVEMENTS_FILE):
    with open(MOVEMENTS_FILE) as f:
        response = json.load(f)        
    return response
