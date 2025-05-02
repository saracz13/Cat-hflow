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
    valid = re.match(r"^[A-Za-z0-9*/-]{9,32}$", password)
    while valid is None:
        print("Invalid password, try again")
        password = input("PASSWORD:")
        valid = re.match(r"^[A-Za-z0-9*/-]{9,32}$", password)
    return password


def main():
    users = []  # In a real app, this would be loaded from a file
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
