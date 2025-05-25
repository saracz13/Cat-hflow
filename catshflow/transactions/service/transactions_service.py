from catshflow.transactions.repository import transactions_repository
from catshflow.classification.repository import classification_repository

def balance():
    total_balance = 0
    data= transactions_repository.reader_json()
    for transaction in data:
        if transaction["TYPE"] in ["EXPENDITURE","SAVINGS"]:
            total_balance -= transaction["AMOUNT"]
        elif transaction["TYPE"] in ["INCOME","WITHDRAWAL"]:
            total_balance += transaction["AMOUNT"]
    return total_balance
   

def new_transaction(amount,m_type,total_balance,category=None,fund=None,note=None):
    if amount <= 0:
        return {"Type": "ERROR",
                "Message": "Invalid transaction amount",
                "Status code": 400}
     

    if m_type not in ["INCOME","EXPENDITURE","SAVINGS","WITHDRAWAL"]:
        return {"Type": "ERROR",
                "Message": "Invalid transaction type",
                "Status code": 400}
    

    if m_type in ["INCOME", "EXPENDITURE"]:
        for data in classification_repository.reader_txt():
            if category not in data:
                if category != "OTHER":
                    return {"Type": "ERROR", 
                            "Message": "Category doesn't exist", 
                            "Status code": 400}
    
    if m_type in ["SAVINGS", "WITHDRAWAL"]:
        fund_exist = False
        for data in classification_repository.reader_csv():
            if fund == data["FUND"]:
                fund_exist = True
        if not fund_exist:
            if fund != "OTHER":
                return {"Type": "ERROR", 
                        "Message": "Fund doesn't exist", 
                        "Status code": 400}
    
    if m_type == "WITHDRAWAL":
        funds = classification_repository.reader_csv()
        for fund in funds:
            if amount > float(fund["AMOUNT"]):
                return {"Type": "ERROR", 
                        "Message": "Insufficient fund amount", 
                        "Status code": 400}
    

    if m_type in ["EXPENDITURE","SAVINGS"]:
        if amount > total_balance:
            return {"Type": "ERROR",
                    "Message": "Invalid transaction. Check your total balance",
                    "Status code": 400}
    
    if m_type == "SAVINGS":
        classification_repository.increase_fund(fund, amount)
    elif m_type == "WITHDRAWAL":
        classification_repository.decrease_fund(fund, amount)

    
    transactions_repository.append_transaction(amount,m_type,category,fund,note)
    return {"Type": "VALID",
                    "Message": "Valid transaction.",
                    "Status code": 200}

    
   
