import pandas as pd
from catshflow.transactions.service import transactions_service
from catshflow.classification.repository import classification_repository

def balance_format():
    balance = transactions_service.balance()
    print(f"""
        _______________________________
          Total balance: ${balance:.2f}
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾""")
                                 
def transaction():
    amount = float(input("Amount:"))
    print("""
          _______________
          [1] INCOME
          [2] EXPENDITURE
          [3] SAVINGS
          [4] WITHDRAWAL
          ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          """)
    m_type = input("Transaction type(Please enter the number):").strip().upper()
    total_balance = transactions_service.balance()
    result = None
    if m_type in ["1","2"]:
        catalog = classification_repository.reader_categories()
        df = pd.DataFrame(catalog)
        if m_type == "1":  
            df = df[df["TYPE"] == "INCOME"]
        elif m_type == "2": 
            df = df[df["TYPE"] == "EXPENDITURE"]
        df = df.reset_index()
        print(df)
        category = input("Category:")
        note = input("Note:")
        result = transactions_service.new_transaction(
            amount = amount,
            m_type = m_type,
            total_balance = total_balance,
            category = category,
            note = note)
    elif m_type == "3":
        catalog =classification_repository.reader_funds()
        df = pd.DataFrame(catalog)
        print(df)
        fund = input("Fund:").upper()
        result= transactions_service.new_transaction(
            amount = amount,
            m_type = m_type,
            total_balance = total_balance,
            fund = fund)
        for data in classification_repository.reader_funds():
            if data["FUND"] == fund:
                print(data)
                print("Savings added! You're one step closer to your goal.")
    elif m_type == "4":
        catalog=classification_repository.reader_funds()
        df = pd.DataFrame(catalog)
        print(df)
        fund = input("Fund:").upper()
        note = input("Note:")
        result= transactions_service.new_transaction(
            amount = amount,
            m_type = m_type,
            total_balance = total_balance,
            fund = fund,
            note = note)
        for data in classification_repository.reader_funds():
            if data["FUND"] == fund:
                print(data)
                if result["Status code"] == 200:
                    print("So sorry to hear that. You'll refill it soon!")
    print(result)