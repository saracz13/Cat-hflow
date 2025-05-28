import os

# current_path (str): Absolute path to this file's directory.
current_path = os.path.dirname(os.path.abspath(__file__))
# BASE_PATH (str): Path to the 'temp' directory two levels above this file.
BASE_PATH = os.path.sep.join(current_path.split(os.path.sep)[:-2] + ["temp"])
# USERS_FILE (str): Path to the users CSV file.
USERS_FILE = os.path.join(BASE_PATH, "users.csv")
