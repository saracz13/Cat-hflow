import csv
from catshflow.classification.constant.classification_constant import FUNDS_FILE,CATEGORIES_FILE

def reader_txt():
    with open(CATEGORIES_FILE) as f:
        response = []
        for line in f.readlines():
            response.append(line.strip())            
    return response


def add_category(new_category):
    with open(CATEGORIES_FILE, "a") as f:
        f.write(new_category + "\n")
    return CATEGORIES_FILE


def eliminate_category(unwated_category):
    with open(CATEGORIES_FILE) as f:
        response = []
        for line in f:
            if unwated_category not in line:
                response.append(line)      
    with open(CATEGORIES_FILE, "w") as f:
        for line in response:
            f.write(line)
    return CATEGORIES_FILE


def rename_category(target_category,renamed_category):
    with open(CATEGORIES_FILE) as f:
        response = []
        for line in f:
            if target_category in line:
                response.append(renamed_category+ "\n") 
            else:
                response.append(line)           
    with open(CATEGORIES_FILE, "w") as f:
        for line in response:
            f.write(line)
    return CATEGORIES_FILE
    

def reader_csv():
    with open(FUNDS_FILE,"r") as f:
        reader = csv.DictReader(f)
        response = []
        for line in reader:
            response.append(line)
    return response


def adding_funds(new_fund):
    with open(FUNDS_FILE,"r") as f:
        reader = csv.DictReader(f)
        response = []
        for line in reader:
            response.append(line)
    response.append(new_fund)
    with open(FUNDS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(response)
    return FUNDS_FILE


def eliminating_funds(unwanted_fund):
    with open(FUNDS_FILE,"r") as f:
        reader = csv.DictReader(f)
        response = []
        for line in reader:
            response.append(line)
        for line in response:
            if line["FUND"] == unwanted_fund["FUND"]:
                response.remove(line)
    with open(FUNDS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(response)
    return FUNDS_FILE


def renaming_funds(target_fund,renamed_fund):
    with open(FUNDS_FILE,"r") as f:
        reader = csv.DictReader(f)
        response = []
        for line in reader:
            response.append(line)
        for line in response:
            if line["FUND"] == target_fund["FUND"]:
                line["FUND"] = renamed_fund["FUND"]
    with open(FUNDS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(response)
    return FUNDS_FILE


def decrease_fund(fund,amount):
    with open(FUNDS_FILE,"r") as f:
        reader = csv.DictReader(f)
        response = []
        for line in reader:
            response.append(line)
        for line in response:
            if line["FUND"] == fund:
                line["AMOUNT"] = float(float(line["AMOUNT"]) - float(amount))
    with open(FUNDS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(response)
    return FUNDS_FILE

def increase_fund(fund, amount):
    with open(FUNDS_FILE,"r") as f:
        reader = csv.DictReader(f)
        response = []
        for line in reader:
            response.append(line)
        for line in response:
            if line["FUND"] == fund:
                line["AMOUNT"] = float(float(line["AMOUNT"]) + float(amount))
    with open(FUNDS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
        writer.writeheader()
        writer.writerows(response)
    return FUNDS_FILE
