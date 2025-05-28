import json
from catshflow.history.constant.history_constant import get_user_paths

def reader_json(email):
    """
    Reads the user's transactions JSON file and returns its content.

    Args:
        email (str): The user's email address.

    Returns:
        list: List of transaction dictionaries.
    """
    paths = get_user_paths(email)
    with open(paths["TRANSACTIONS_FILE"]) as f:
        response = json.load(f)        
    return response