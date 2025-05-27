from catshflow.history.repository import history_repository

def great_than_amount(filter):
    transactions = history_repository.reader_json()
    filtered_data = []
    for data in transactions:
        if float(data["AMOUNT"]) > filter:
            filtered_data.append(data)
    if not filtered_data:
        return {"Type": "ERROR", 
                "Message": "There is no data over that amount", 
                "Status code": 400}
    return filtered_data,{"Type": "VALID", 
                          "Message": "  Search completed", 
                          "Status code": 200}

def less_than_amount(filter):
    transactions = history_repository.reader_json()
    filtered_data = []
    for data in transactions:
        if float(data["AMOUNT"]) < filter:
            filtered_data.append(data)
    if not filtered_data:
        return {"Type": "ERROR", 
                "Message": "There is no data below that amount", 
                "Status code": 400}
    return filtered_data,{"Type": "VALID", 
                          "Message": "  Search completed", 
                          "Status code": 200}

def same_as_amount(filter):
    transactions = history_repository.reader_json()
    filtered_data = []
    for data in transactions:
        if float(data["AMOUNT"]) == filter:
            filtered_data.append(data)
    if not filtered_data:
        return {"Type": "ERROR", 
                "Message": "There is no data with that amount", 
                "Status code": 400}
    return filtered_data,{"Type": "VALID", 
                          "Message": "  Search completed", 
                          "Status code": 200}