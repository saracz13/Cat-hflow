import os

current_path = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.sep.join(current_path.split(os.path.sep)[:-2] + ["temp"])
FUNDS_FILE = os.path.join(BASE_PATH, "funds.csv")
CATEGORIES_FILE = os.path.join(BASE_PATH, "categories.csv")