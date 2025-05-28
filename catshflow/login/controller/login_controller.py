from catshflow.login.service import login_service

def login():
    """
    Handles the login and registration menu for the user.

    Returns:
        tuple:
            email (str or None): The user's email address if login/registration is successful, otherwise None.
            response (dict): Validation dictionary with operation status, message, and user info if valid.
    """
    print("""
        __________________________________________
               😺 Welcome to Catshflow! 😺
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
         [1] LOGIN
         [2]→ Don't have an account?Sing up here!
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          """
          )
    action = input("👉Enter the corresponding number:")
    if action == "1":
        print("🔐 LOGIN")
        email = input("📧 Email:").strip()
        password = input("🔑 Password:").strip()
        response = login_service.login(email,password)
        if response["Status code"] == 200:
            print(f"Welcome to the Catshflow {response['User']['NAME'].capitalize()}!🐈")
        else:
            print(f"\n❌ {response['Message']}")
            return None,response
        return email, response
    elif action == "2":
        print("📝 SIGN UP") 
        name = input("👤 Name:").strip().upper()
        email = input("📧 Email:")
        password = input("🔑 Password:")
        response = login_service.register(name,email,password)
        if response["Status code"] == 200:
            print(f"Registration succesfully!We are glad to have you here {name.capitalize()}!🐾")
        else:
            print(f"\n❌ {response['Message']}")
            return None,response
        return email, response
    else:
        response = {"Type": "ERROR",
                    "Message": "Please choose one of the displayed options!",
                    "Status code": 400}
    return None, response
