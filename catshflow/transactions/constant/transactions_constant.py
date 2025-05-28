import os
from catshflow.login.repository import login_repository

def get_user_paths(email):
    """
    Generates and returns the file paths associated with the user for transactions operations.

    Args:
        email (str): The user's email address.

    Returns:
        dict: Dictionary with the following paths:
            USER_PATH (str): Path to the user's folder.
            TRANSACTIONS_FILE (str): Path to the user's transactions file (JSON).
    """
    user_folder = login_repository.create_user_files(email)
    current_path = os.path.dirname(os.path.abspath(__file__))
    BASE_PATH = os.path.sep.join(current_path.split(os.path.sep)[:-2] + ["temp"])
    USER_PATH = os.path.join(BASE_PATH, os.path.basename(user_folder))
    TRANSACTIONS_FILE = os.path.join(USER_PATH, "transactions.json")
    return {
        "USER_PATH": USER_PATH,
        "TRANSACTIONS_FILE": TRANSACTIONS_FILE
    }

