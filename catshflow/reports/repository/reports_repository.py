import json
from catshflow.reports.constant.reports_constant import get_user_paths

def reader_json(email):
    """
    Reads the user's transactions JSON file and returns its content.

    Args:
        email (str): The user's email address.

    Returns:
        list: List of transaction dictionaries.
    """
    paths = get_user_paths(email)
    with open(paths["TRANSACTIONS_FILE"], "r") as f:
        data = json.load(f)
    return data