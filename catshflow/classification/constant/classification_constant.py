import os
from catshflow.login.repository import login_repository
from catshflow.login.repository import login_repository

def get_user_paths(email):
    """
    Generates and returns the file paths associated with the user.

    Args:
        email (str): The user's email address.

    Returns:
        dict: Dictionary with the following paths:
            USER_FOLDER (str): Path to the user's folder.
            FUNDS_FILE (str): Path to the user's funds file.
            CATEGORIES_FILE (str): Path to the user's categories file.
    """
    user_folder = login_repository.create_user_files(email)
    current_path = os.path.dirname(os.path.abspath(__file__))
    BASE_PATH = os.path.sep.join(current_path.split(os.path.sep)[:-2] + ["temp"])
    USER_PATH = os.path.join(BASE_PATH, os.path.basename(user_folder))
    FUNDS_FILE = os.path.join(USER_PATH, "funds.csv")
    CATEGORIES_FILE = os.path.join(USER_PATH, "categories.csv")
    return {
        "USER_FOLDER": USER_PATH,
        "FUNDS_FILE": FUNDS_FILE,
        "CATEGORIES_FILE": CATEGORIES_FILE
    }


