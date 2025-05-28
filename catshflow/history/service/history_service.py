from datetime import datetime
from catshflow.history.repository import history_repository
from catshflow.classification.repository import classification_repository

def before_filter(date):
    transactions = history_repository.reader_json()
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

def after_filter(date):
    transactions = history_repository.reader_json()
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


def exact_filter(date):
    transactions = history_repository.reader_json()
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


def between_dates_filter(start_date,end_date):
    transactions = history_repository.reader_json()
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



def great_than_amount(amount):
    transactions = history_repository.reader_json()
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

def less_than_amount(amount):
    transactions = history_repository.reader_json()
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


def between_amounts(amount_1,amount_2): 
    transactions = history_repository.reader_json()
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
def same_as_amount(amount):
    transactions = history_repository.reader_json()
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

def type_filter(transaction_type):
    transactions = history_repository.reader_json()
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


def category_filter(index_category):
    categories = classification_repository.reader_categories()
    transactions = history_repository.reader_json()
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


def fund_filter(index_fund):
    funds = classification_repository.reader_funds()
    transactions = history_repository.reader_json()
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
    
