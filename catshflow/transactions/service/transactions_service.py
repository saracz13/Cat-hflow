from catshflow.transactions.repository import transactions_repository
from catshflow.classification.repository import classification_repository

def balance(email):
    """
    Calculates the user's total balance based on all transactions.

    Args:
        email (str): The user's email address.

    Returns:
        float: The user's total balance.
    """
    total_balance = 0
    data= transactions_repository.reader_json(email)
    for transaction in data:
        if transaction["TYPE"] in ["EXPENSE","SAVINGS"]:
            total_balance -= transaction["AMOUNT"]
        elif transaction["TYPE"] in ["INCOME","WITHDRAWAL"]:
            total_balance += transaction["AMOUNT"]
    return total_balance
   
def confirmation(email,confirmation,amount,m_type,total_balance,category=None,fund=None,note=None):
    """
    Handles user confirmation for a transaction and processes it if confirmed.

    Args:
        email (str): The user's email address.
        confirmation (str): User confirmation ("1" to confirm, "2" to cancel).
        amount (float): The transaction amount.
        m_type (str): The transaction type ("1", "2", "3", or "4").
        total_balance (float): The user's total balance.
        category (str, optional): The category index, if applicable.
        fund (str, optional): The fund index, if applicable.
        note (str, optional): Additional note for the transaction.

    Returns:
        dict: Validation dictionary with operation status and message.
    """
    if confirmation == "1":
        result = new_transaction(email,amount,m_type,total_balance,category,fund,note)
        return result
    elif confirmation =="2":
        return
    else: 
        return {"Type": "ERROR", 
                    "Message": "Please choose one of the displayed options!", 
                    "Status code": 400}
    
def new_transaction(email,amount,m_type,total_balance,category=None,fund=None,note=None):
    """
    Validates and processes a new transaction for the user.

    Args:
        email (str): The user's email address.
        amount (float): The transaction amount.
        m_type (str): The transaction type ("1", "2", "3", or "4").
        total_balance (float): The user's total balance.
        category (str, optional): The category index, if applicable.
        fund (str, optional): The fund index, if applicable.
        note (str, optional): Additional note for the transaction.

    Returns:
        dict: Validation dictionary with operation status and message.
    """
    if amount <= 0:
        return {"Type": "ERROR",
                "Message": "Invalid transaction amount",
                "Status code": 400}
     

    if m_type not in ["1","2","3","4"]:
        return {"Type": "ERROR",
                "Message": "Invalid transaction type",
                "Status code": 400}
    

    if m_type in ["1", "2"]:
        categories = classification_repository.reader_categories(email)
        if int(category) > len(categories):
            return {"Type": "ERROR", 
                    "Message": "Category doesn't exist", 
                    "Status code": 400}
    
    if m_type in ["3", "4"]:
        funds = classification_repository.reader_funds(email)
        if int(fund) > len(funds):
            return {
                    "Type": "ERROR",
                    "Message": "This category doesn't exists",
                    "Status code": 400
                    }
    
    if m_type == "4":
        funds = classification_repository.reader_funds(email)
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
        classification_repository.increase_fund(email,fund, amount)
    elif m_type == "4":
        classification_repository.decrease_fund(email,fund, amount)

    
    transactions_repository.append_transaction(email,amount,m_type,category,fund,note)
    return {"Type": "VALID",
                    "Message": "Valid transaction.",
                    "Status code": 200}

    
   
