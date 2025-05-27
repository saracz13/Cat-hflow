import csv
from catshflow.classification.constant.classification_constant import FUNDS_FILE,CATEGORIES_FILE

def reader_categories():
    response = []
    with open(CATEGORIES_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
            response.append(line) 
    return response

def reader_funds():
    response = []
    with open(FUNDS_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
            response.append(line)
    return response

def add_category(new_category,c_type):
    with open(CATEGORIES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_category, c_type])
    return CATEGORIES_FILE


def eliminate_category(unwanted_category):
    categories = reader_categories()
    remove_category = categories[int(unwanted_category)]
    updated_categories = []
    for data in categories:
        if data != remove_category:
            updated_categories.append(data)     
    
    with open(CATEGORIES_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["CATEGORY", "TYPE"])
        writer.writeheader()
        writer.writerows(updated_categories)
    return CATEGORIES_FILE


def rename_category(target_category,renamed_category):
    categories = reader_categories()
    categories[int(target_category)]["CATEGORY"] = renamed_category
    with open(CATEGORIES_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["CATEGORY", "TYPE"])
        writer.writeheader()
        writer.writerows(categories)
    return CATEGORIES_FILE
    

def adding_funds(new_fund):
    with open(FUNDS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_fund, 0])
    return FUNDS_FILE


def eliminating_funds(unwanted_fund):
    funds = reader_funds()
    remove_fund = funds[int(unwanted_fund)]
    updated_funds = []
    for data in funds:
        if data != remove_fund:
            updated_funds.append(data)     
    with open(FUNDS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(updated_funds)
    return FUNDS_FILE


def renaming_funds(target_fund,renamed_fund):
    funds = reader_funds()
    funds[int(target_fund)]["FUND"] = renamed_fund
    with open(FUNDS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(funds)
    return FUNDS_FILE


def decrease_fund(fund,amount):
    funds = reader_funds()
    funds[int(fund)]["AMOUNT"] = str(float(funds[int(fund)]["AMOUNT"]) - float(amount))
    with open(FUNDS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(funds)
    return FUNDS_FILE

def increase_fund(fund, amount):
    funds = reader_funds()
    funds[int(fund)]["AMOUNT"] = str(float(funds[int(fund)]["AMOUNT"]) + float(amount))
    with open(FUNDS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(funds)
    return FUNDS_FILE
