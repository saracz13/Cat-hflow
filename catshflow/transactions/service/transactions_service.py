from catshflow.transactions.repository import transactions_repository

def balance():
    total_balance = 0
    data= transactions_repository.reader_json()
    for transaction in data:
        if transaction["TYPE"] == "EXPENDITURE":
            total_balance -= transaction["AMOUNT"]
        elif transaction["TYPE"]== "INCOME":
            total_balance += transaction["AMOUNT"]
        elif transaction["TYPE"]== "SAVINGS":
            total_balance -= transaction["AMOUNT"]
    return total_balance
   

def new_transaction(amount,total_balance,m_type,category=None,fund=None,note=None):
    if amount <= 0:
        return {"Type": "ERROR",
                "Message": "Invalid transaction amount",
                "Status code": 400}
     
    if m_type not in ["INCOME","EXPENDITURE","SAVINGS"]:
        return {"Type": "ERROR",
                "Message": "Invalid transaction type",
                "Status code": 400}
    
    if m_type in ["EXPENDITURE","SAVINGS"]:
        if amount > total_balance:
            return {"Type": "ERROR",
                    "Message": "Invalid transaction. Check your total balance",
                    "Status code": 400}
   
    # AQUI VALIDAR CATEGORIA CON SERVICE DE CATEGORIA
    
    
    transactions_repository.append_transaction(amount,m_type,category,fund,note)
   
