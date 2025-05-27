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
     

    if m_type not in ["1","2","3","4"]:
        return {"Type": "ERROR",
                "Message": "Invalid transaction type",
                "Status code": 400}
    

    if m_type in ["1", "2"]:
        categories = classification_repository.reader_categories()
        if int(category) > len(categories):
            return {"Type": "ERROR", 
                    "Message": "Category doesn't exist", 
                    "Status code": 400}
    
    if m_type in ["3", "4"]:
        funds = classification_repository.reader_funds()
        if int(fund) > len(funds):
            return {
                    "Type": "ERROR",
                    "Message": "This category doesn't exists",
                    "Status code": 400
                    }
    
    if m_type == "4":
        funds = classification_repository.reader_funds()
        for data in funds:
            if data["FUND"] == fund:
                if amount > float(data["AMOUNT"]):
                    return {"Type": "ERROR", 
                            "Message": "Insufficient fund amount", 
                            "Status code": 400}
                
    if m_type == "4":
        if not note:
            return {"Type": "ERROR", 
                            "Message": "Justification required", 
                            "Status code": 400}
    
    if m_type in ["2","3"]:
        if amount > total_balance:
            return {"Type": "ERROR",
                    "Message": "Invalid transaction. Check your total balance",
                    "Status code": 400}
    
    if m_type == "3":
        classification_repository.increase_fund(fund, amount)
    elif m_type == "4":
        classification_repository.decrease_fund(fund, amount)

    
    transactions_repository.append_transaction(amount,m_type,category,fund,note)
    return {"Type": "VALID",
                    "Message": "Valid transaction.",
                    "Status code": 200}

    
   
