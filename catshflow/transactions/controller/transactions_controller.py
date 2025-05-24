from catshflow.transactions.service import transactions_service

def balance_format():
    balance = transactions_service.balance()
    print(f"Total balance: ${balance:.2f}")
                                 
def transaction():
    amount = float(input("Amount:"))
    m_type = input("Transaction type:").upper()
    if m_type in ["EXPENDITURE","INCOME"]:
        category = input("Category:").upper()
        note = input("Note:")
        transactions_service.new_transaction(amount,m_type,category,note)
    elif m_type == "SAVINGS":
        goal = input("Goal:").upper()
        transactions_service.new_transaction(amount,m_type,goal)