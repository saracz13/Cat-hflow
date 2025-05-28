import re
from catshflow.login.repository import login_repository
from catshflow.login.exceptions import login_exceptions

def login(email,password):
    """
    Authenticates a user by email and password.

    Args:
        email (str): The user's email address.
        password (str): The user's password.

    Returns:
        dict: Validation dictionary with operation status, message, and user info if valid.
    """
    users = login_repository.get_users()
    for user in users:
        if user["EMAIL"] == email:
            if user["PASSWORD"] == password:
                return {"Type": "VALID",
                        "Message": "User found.",
                        "Status code": 200,
                        "User": user}
            else:
                return {"Type": "ERROR",
                        "Message": "Incorrect password.",
                        "Status code": 400}
    return {
            "Type": "ERROR",
            "Message": "Email not registered.",
            "Status code": 404
            }
    
def register(name,email,password):
    """
    Registers a new user if the email is not already taken and the password is valid.

    Args:
        name (str): The user's name.
        email (str): The user's email address.
        password (str): The user's password.

    Returns:
        dict: Validation dictionary with operation status and message.
    """
    users = login_repository.get_users()
    
    for user in users:
        if user["EMAIL"] == email:
            return {"Type": "ERROR",
                    "Message": "This email is already taken.",
                    "Status code": 400}
    valid = re.match(r"^[A-Za-z0-9*/_.]{9,32}$", password)
    while valid is None:
        return {"Type": "ERROR",
                "Message": "Invalid password.",
                "Status code": 400}   
    new_user = {
        "NAME":name,
        "EMAIL": email,
        "PASSWORD": password
        }       
    login_repository.save_users(new_user)
    return {"Type": "VALID",
             "Message": "Valid transaction.",
             "Status code": 200}
