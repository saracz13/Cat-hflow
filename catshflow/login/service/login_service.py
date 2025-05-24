from catshflow.login.repository import login_repository
from catshflow.login.exceptions import login_exceptions

def login(email,password):
    users = login_repository.get_users()
    response = {}
    try:
        for user in users:
            if user["email"] == email:
                if user["password"] == password:
                    response["status_code"] = 200
                    response["message"] = "user exist"
                    response["user"] = user
                else:
                    raise login_exceptions.NotFound()
        return response
    except login_exceptions.NotFound as ex:
        response= {}
        response["message"] = "Wrong password"
        response["status_code"]= 400
        return response
    
def register(name,birth,gender,email,password):
    users = login_repository.get_users()
    exists= list(filter(lambda user: user["email"]== email,users))
    if exists:
        response = {}
        response["message"] = "That email already exists"
        response["status_code"] = 400
        return response
    users.append({
        "name":name,
        "birth": birth,
        "gender": gender,
        "email": email,
        "password": password
    })
    response = {}
    response["status_code"] = 200
    response ["user"] = users[-1]
    login_repository.save_users(users)
    return response

def lister():
    response = {}
    data = login_repository.get_users()
    response_data = []
    for user in data:
        response_data.append({
            "name": user["name"],
            "email": user["email"],
            "gender":user["gender"],
            "birth":user["birth"]
            })
    response["status_code"] = 200
    response["data"] = response_data
    return response





import re

def saving_names(name, email, birthdate, gender, password, users):
    new_user = {
        "Name": name,
        "Email": email,
        "Birthdate": birthdate,
        "Gender": gender,
        "Password": password
    }

    for user in users:
        if new_user["Email"] == user["Email"]:
            print("This email is already taken.")
            return None

    users.append(new_user)
    return new_user


def validate_password(password):
    valid = re.match(r"^[A-Za-z0-9*/_.]{9,32}$", password)
    while valid is None:
        print("Invalid password, try again")
        password = input("PASSWORD:")
        valid = re.match(r"^[A-Za-z0-9*/_.]{9,32}$", password)
    return password


def main():
    users = []
    name = input("NAME: ").upper()
    email = input("EMAIL: ")
    birthdate = input("DD/MM/YYYY: ")
    gender = input("GENDER: ").upper()
    password = input("PASSWORD: ")
    correct = validate_password(password)

    new_user = saving_names(name, email, birthdate, gender, correct, users)
    
    if new_user is not None:
        print(f"User registered. Birthdate: {new_user['Birthdate']}")


main()