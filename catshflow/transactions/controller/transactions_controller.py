from catshflow.transactions.service import transactions_service
from catshflow.classification.repository import classification_repository

def balance_format():
    balance = transactions_service.balance()
    print(f"Total balance: ${balance:.2f}")
                                 
def transaction():
    amount = float(input("Amount:"))
    print(["INCOME[1]","EXPENDITURE[2]","SAVINGS[3]","WITHDRAWAL[4]"])
    m_type = input("Transaction type:").strip().upper()
    total_balance = transactions_service.balance()
    result = None
    if m_type in ["EXPENDITURE","INCOME"]:
        print(classification_repository.reader_txt(),"OTHER")
        category = input("Category:").upper()
        note = input("Note:")
        result = transactions_service.new_transaction(
            amount = amount,
            m_type = m_type,
            total_balance = total_balance,
            category = category,
            note = note)
    elif m_type == "SAVINGS":
        print(classification_repository.reader_csv())
        fund = input("Fund:").upper()
        result= transactions_service.new_transaction(
            amount = amount,
            m_type = m_type,
            total_balance = total_balance,
            fund = fund)
        for data in classification_repository.reader_csv():
            if data["FUND"] == fund:
                print(data)
                print("Savings added! You're one step closer to your goal.")
    elif m_type == "WITHDRAWAL":
        print(classification_repository.reader_csv())
        fund = input("Fund:").upper()
        note = input("Note:")
        result= transactions_service.new_transaction(
            amount = amount,
            m_type = m_type,
            total_balance = total_balance,
            fund = fund,
            note = note)
        for data in classification_repository.reader_csv():
            if data["FUND"] == fund:
                print(data)
                print("Your piggy bank cried a little… but it understands. You'll refill it soon!")
    print(result)