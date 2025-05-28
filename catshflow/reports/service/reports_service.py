from datetime import datetime,timedelta
from catshflow.reports.repository import reports_repository

def balance_movements(email,frecuency):
    """
    Calculates the user's balance fluctuation history for a given frequency.

    Args:
        email (str): The user's email address.
        frecuency (str): Frequency option ("1"=7 days, "2"=30 days, "3"=180 days).

    Returns:
        tuple: (list of (date, balance) tuples, validation dict)
    """
    transactions = reports_repository.reader_json(email)
    daily_balance = {}
    reference_date = datetime.now()
    if frecuency == "1":
        start_date = reference_date - timedelta(days=7)
    elif frecuency == "2":
        start_date = reference_date - timedelta(days=30)
    elif frecuency == "3":
        start_date = reference_date - timedelta(days=180)
    else:
        return {}, {"Type": "ERROR", 
                    "Message": "Invalid frequency", 
                    "Status code": 400}
    
    for data in transactions:
        transaction_date = datetime.fromisoformat(data["DATE"])
        if start_date <= transaction_date <= reference_date:
            amount = float(data["AMOUNT"])
            daily_date = transaction_date.date()
            if daily_date not in daily_balance:
                daily_balance[daily_date] = 0.0
            if data["TYPE"] in ["INCOME", "SAVINGS"]:
                daily_balance[daily_date] += amount
            elif data["TYPE"] in ["EXPENSE", "WITHDRAWAL"]:
                daily_balance[daily_date] -= amount

    sorted_dates = sorted(daily_balance.keys())
    cumulative_balance = 0
    balance_history = []

    for date in sorted_dates:
        cumulative_balance += daily_balance[date]
        balance_history.append((date, cumulative_balance))

    return balance_history, {"Type": "VALID", 
                             "Message": "Balance fluctuation history ready", 
                             "Status code": 200}



def category_expense(email,frecuency):
    """
    Calculates total expense per category for a given frequency.

    Args:
        email (str): The user's email address.
        frecuency (str): Frequency option ("1"=7 days, "2"=30 days, "3"=180 days).

    Returns:
        tuple: (dict with category totals, validation dict)
    """
    transactions = reports_repository.reader_json(email)
    total_category = {}
    reference_date = datetime.now()

    if frecuency == "1":
        start_date = reference_date - timedelta(days=7)
    elif frecuency == "2":
        start_date = reference_date - timedelta(days=30)
    elif frecuency == "3":
        start_date = reference_date - timedelta(days=180)
    else:
        return {}, {"Type": "ERROR", 
                    "Message": "Invalid frequency", 
                    "Status code": 400}
    for data in transactions:
        transaction_date = datetime.fromisoformat(data["DATE"])
        if start_date <= transaction_date <= reference_date:
            if data["TYPE"] == "EXPENSE":
                category = data.get("CATEGORY")
                amount_category = float(data.get("AMOUNT"))
                if category in total_category:
                    total_category[category] += amount_category
                else:
                    total_category[category] = amount_category
    return total_category,{"Type": "VALID",
                            "Message": "Valid transaction distribution",
                            "Status code": 200}
    
    
def category_income(email,frecuency):
    """
    Calculates total income per category for a given frequency.

    Args:
        email (str): The user's email address.
        frecuency (str): Frequency option ("1"=7 days, "2"=30 days, "3"=180 days).

    Returns:
        tuple: (dict with category totals, validation dict)
    """
    transactions = reports_repository.reader_json(email)
    total_category = {}
    reference_date = datetime.now()

    if frecuency == "1":
        start_date = reference_date - timedelta(days=7)
    elif frecuency == "2":
        start_date = reference_date - timedelta(days=30)
    elif frecuency == "3":
        start_date = reference_date - timedelta(days=180)
    else:
        return {}, {"Type": "ERROR", 
                    "Message": "Invalid frequency", 
                    "Status code": 400}
    for data in transactions:
        transaction_date = datetime.fromisoformat(data["DATE"])
        if start_date <= transaction_date <= reference_date:
            if data["TYPE"] == "INCOME":
                category = data.get("CATEGORY")
                amount_category = float(data.get("AMOUNT"))
                if category in total_category:
                    total_category[category] += amount_category
                else:
                    total_category[category] = amount_category
    return total_category,{"Type": "VALID",
                            "Message": "Valid transaction distribution",
                            "Status code": 200}

def fund_savings(email,frecuency):
    """
    Calculates total savings per fund for a given frequency.

    Args:
        email (str): The user's email address.
        frecuency (str): Frequency option ("1"=7 days, "2"=30 days, "3"=180 days).

    Returns:
        tuple: (dict with fund totals, validation dict)
    """
    transactions = reports_repository.reader_json(email)
    total_funds = {}
    reference_date = datetime.now()

    if frecuency == "1":
        start_date = reference_date - timedelta(days=7)
    elif frecuency == "2":
        start_date = reference_date - timedelta(days=30)
    elif frecuency == "3":
        start_date = reference_date - timedelta(days=180)
    else:
        return {}, {"Type": "ERROR", 
                    "Message": "Invalid frequency", 
                    "Status code": 400}
    for data in transactions:
        transaction_date = datetime.fromisoformat(data["DATE"])
        if start_date <= transaction_date <= reference_date:
            if data["TYPE"] == "SAVINGS":
                fund = data.get("FUND")
                amount_fund = float(data.get("AMOUNT"))
                if fund in total_funds:
                    total_funds[fund] += amount_fund
                else:
                    total_funds[fund] = amount_fund
    return total_funds,{"Type": "VALID",
                            "Message": "Valid transaction distribution",
                            "Status code": 200}

def fund_withdrawal(email,frecuency):
    """
    Calculates total withdrawals per fund for a given frequency.

    Args:
        email (str): The user's email address.
        frecuency (str): Frequency option ("1"=7 days, "2"=30 days, "3"=180 days).

    Returns:
        tuple: (dict with fund totals, validation dict)
    """
    transactions = reports_repository.reader_json(email)
    total_funds = {}
    reference_date = datetime.now()

    if frecuency == "1":
        start_date = reference_date - timedelta(days=7)
    elif frecuency == "2":
        start_date = reference_date - timedelta(days=30)
    elif frecuency == "3":
        start_date = reference_date - timedelta(days=180)
    else:
        return {}, {"Type": "ERROR", 
                    "Message": "Invalid frequency", 
                    "Status code": 400}
    for data in transactions:
        transaction_date = datetime.fromisoformat(data["DATE"])
        if start_date <= transaction_date <= reference_date:
            if data["TYPE"] == "WITHDRAWAL":
                fund = data.get("FUND")
                amount_fund = float(data.get("AMOUNT"))
                if fund in total_funds:
                    total_funds[fund] += amount_fund
                else:
                    total_funds[fund] = amount_fund
    return total_funds,{"Type": "VALID",
                            "Message": "Valid transaction distribution",
                            "Status code": 200}