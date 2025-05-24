import csv
from login.constant.login_constant import USERS_FILE


def get_users():
    with open(USERS_FILE,"r") as f:
        response = csv.DictReader(f)
        users = list(response)
    return users
    
def save_users(new_user):
    with open(USERS_FILE,"a",newline="") as f:
        fieldnames = new_user.keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(new_user)
    return USERS_FILE

print(get_users())