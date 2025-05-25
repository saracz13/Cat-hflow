from catshflow.classification.repository import classification_repository
from catshflow.transactions.repository import transactions_repository


def new_categories(new_category):
    categories = classification_repository.reader_txt()
    if new_category in categories:
        return {
                "Type": "ERROR",
                "Message": "This category already exists",
                "Status code": 400
                }
    classification_repository.add_category(new_category)

def eliminate_categories(categories,unwanted_category):
    categories = classification_repository.reader_txt()
    if unwanted_category not in categories:
        return {
                "Type": "ERROR",
                "Message": "This category doesn't exists",
                "Status code": 400
                }
    classification_repository.eliminate_category(unwanted_category)

def rename_categories(categories,target_category,renamed_category):
    categories = classification_repository.reader_txt()
    if target_category not in categories:
        return {
                "Type": "ERROR",
                "Message": "This category doesn't exists",
                "Status code": 400
                }
    if renamed_category in categories:
        return {
                "Type": "ERROR",
                "Message": "This category already exists",
                "Status code": 400
                }
    classification_repository.rename_category(target_category,renamed_category)

def add_funds(new_fund):
    funds = classification_repository.reader_csv()
    for fund in funds:
        if fund["FUND"] == new_fund["FUND"]:
            return {
                    "Type": "ERROR",
                    "Message": "This fund already exists",
                    "Status code": 400
                    }
    classification_repository.adding_funds(new_fund)


def eliminate_funds(funds,unwanted_fund):
    funds = classification_repository.reader_csv()
    for fund in funds:
        if unwanted_fund["FUND"] not in fund["FUND"]:
            return {
                    "Type": "ERROR",
                    "Message": "This fund already exists",
                    "Status code": 400
                    }
    classification_repository.eliminating_funds(unwanted_fund)

def rename_funds(funds,target_fund,renamed_fund):
    funds = classification_repository.reader_csv()
    for fund in funds:
        if target_fund["FUND"] not in fund["FUND"]:
            return {
                    "Type": "ERROR",
                    "Message": "This fund doesn't exists",
                    "Status code": 400
                    }
        if renamed_fund["FUND"] in fund["FUND"]:
            return {
                    "Type": "ERROR",
                    "Message": "This fund already exists",
                    "Status code": 400
                    }
    classification_repository.renaming_funds(target_fund,renamed_fund)

def extract_funds(funds,target_fund,amount,reason):
    funds = classification_repository.reader_csv()
    for fund in funds:
        if target_fund["FUND"] not in fund["FUND"]:
            return {
                    "Type": "ERROR",
                    "Message": "This fund doesn't exists",
                    "Status code": 400
                    }
        if target_fund["FUND"] == fund["FUND"]:
            if target_fund["AMOUNT"] > fund["AMOUNT"]:
                return {
                        "Type": "ERROR",
                        "Message": "You don't have enough money on this fund",
                        "Status code": 400
                        }
    classification_repository.extracting_funds(target_fund,amount)
    transactions_repository.append_transaction(target_fund,amount,reason)
    return funds
