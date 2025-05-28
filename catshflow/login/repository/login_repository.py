import os
import json
import csv
from catshflow.login.constant.login_constant import USERS_FILE


def get_users():
    """
    Reads and returns all users from the users CSV file.

    Returns:
        list: List of user dictionaries.
    """
    with open(USERS_FILE,"r") as f:
        response = csv.DictReader(f)
        users = list(response)
    return users
    
def save_users(new_user):
    """
    Appends a new user to the users CSV file and creates user files.

    Args:
        new_user (dict): Dictionary with user information.

    Returns:
        str: Path to the users CSV file.
    """
    with open(USERS_FILE,"a",newline="") as f:
        fieldnames = new_user.keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(new_user)
        create_user_files(new_user["EMAIL"])
    return USERS_FILE

def create_user_files(email):
    """
    Creates the user's folder and default files if they do not exist.

    Args:
        email (str): The user's email address.

    Returns:
        str: Path to the user's folder.
    """
    email = email.replace("@","_at_").replace(".","_")
    user_folder = os.path.join("temp", email)
    current_path = os.path.dirname(os.path.abspath(__file__))
    catsh_flow = os.path.sep.join(current_path.split(os.path.sep)[:-2])
    temp_path = os.path.join(catsh_flow, "temp")

    user_folder = os.path.join(temp_path, email)
    os.makedirs(user_folder, exist_ok=True)
    transactions_file = os.path.join(user_folder, "transactions.json")
    if not os.path.exists(transactions_file):
        with open(transactions_file, "w") as f:
            json.dump([], f)

    funds_file = os.path.join(user_folder, "funds.csv")
    if not os.path.exists(funds_file):
        with open(funds_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["FUND", "AMOUNT"])
            writer.writeheader()

    categories_file = os.path.join(user_folder, "categories.csv")
    if not os.path.exists(categories_file):
        with open(categories_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["CATEGORY", "TYPE"])
            writer.writeheader()
            default_categories = [
                {"CATEGORY": "FOOD", "TYPE": "EXPENSE"},
                {"CATEGORY": "TRANSPORT", "TYPE": "EXPENSE"},
                {"CATEGORY": "WORK", "TYPE": "INCOME"},
                {"CATEGORY": "ENTERTAIMENT", "TYPE": "EXPENSE"},
            ]
            writer.writerows(default_categories)
    return user_folder