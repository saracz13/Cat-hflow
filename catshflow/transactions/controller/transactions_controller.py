import json
import pandas as pd
from catshflow.transactions.service import transactions_service
from catshflow.transactions.repository import transactions_repository
from catshflow.classification.repository import classification_repository

def balance_format(email):
    """
    Prints the user's total balance in a formatted way.

    Args:
        email (str): The user's email address.

    Returns:
        None
    """
    balance = transactions_service.balance(email)
    print(f"""
    ╔══════════════════════════════════════╗
       💰 Total balance: ${balance:.2f}     
    ╚══════════════════════════════════════╝
    """)
                                 
def transaction(email):
    """
    Handles the transaction menu for the user, allowing them to add income, expense, savings, or withdrawal transactions.

    Args:
        email (str): The user's email address.

    Returns:
        None
    """
    amount = float(input("💵 Amount:"))
    print("""
          ______________________
          💵Transaction type:
          ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          [1] INCOME
          [2] EXPENSE
          [3] SAVINGS
          [4] WITHDRAWAL
          ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          """)
    m_type = input("Enter the number:")
    total_balance = transactions_service.balance(email)
    result = None
    if m_type in ["1","2"]:
        catalog = classification_repository.reader_categories(email)
        df = pd.DataFrame(catalog)
        if m_type == "1":  
            df = df[df["TYPE"] == "INCOME"]
        elif m_type == "2": 
            df = df[df["TYPE"] == "EXPENSE"]
        print(df)
        category = input("Category:")
        note = input("Note:")
        confirmation = input("\n✅ Confirm transaction? YES[1]  NO[2]: ").strip()
        if confirmation == "1":
            result = transactions_service.confirmation(
                email = email,
                confirmation = confirmation,
                amount = amount,
                m_type = m_type,
                total_balance = total_balance,
                category = category,
                note = note)
        elif confirmation == "2":
            return 
        else:
            return({"Type": "ERROR",
                    "Message": "Please choose one of the displayed options!",
                    "Status code": 400})
    elif m_type == "3":
        catalog =classification_repository.reader_funds(email)
        df = pd.DataFrame(catalog)
        print("\n📚 Available categories:\n", df)
        fund = input("Fund:")
        confirmation = input("\n✅ Confirm transaction? YES[1]  NO[2]: ").strip()
        result= transactions_service.confirmation(
            email = email,
            confirmation= confirmation,
            amount = amount,
            m_type = m_type,
            total_balance = total_balance,
            fund = fund)
        for data in classification_repository.reader_funds(email):
            if data["FUND"] == fund:
                print(data)
                print("🎉 Savings added! You're one step closer to your goal.")
    elif m_type == "4":
        catalog=classification_repository.reader_funds(email)
        df = pd.DataFrame(catalog)
        print("\n💰 Available funds:\n", df)
        fund = input("Fund:")
        note = input("Note:")
        confirmation = input("\n✅ Confirm transaction? YES[1]  NO[2]: ").strip()
        result= transactions_service.confirmation(
            email = email,
            confirmation = confirmation,
            amount = amount,
            m_type = m_type,
            total_balance = total_balance,
            fund = fund,
            note = note)
        for data in classification_repository.reader_funds(email):
            if data["FUND"] == fund:
                print(data)
                if result["Status code"] == 200:
                    print("😿 So sorry to hear that. You'll refill it soon!")
    if result["Status code"] == 200:
        data = transactions_repository.reader_json(email)
        print(json.dumps(data[-1], indent=4))
    print(result)