from login.service import login_service

def login():
    email = input("email:")
    password = input("password:")
    response = login_service.login(email,password)
    if response["status_code"] == 200:
        print("Welcome to the aplication!!")
    else:
        print(response["message"])
    return response

def register():
    name = input("name:")
    email = input("email:")
    password = input("password:")
    response = login_service.register(name,email,password)
    if response["status_code"] == 200:
        print("New user created.")
    else:
        print(response["message"])

def lister():
    response = login_service.lister()
    print("id\t NAME \t EMAIL")
    if response["status_code"] == 200:
        for e,user in enumerate(response["data"]):
            print(f"{e}"+ " \t " + user["name"] + " \t " + user["email"])
    else:
        print(response["message"])
