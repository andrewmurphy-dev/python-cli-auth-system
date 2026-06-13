from app.cli.ui import square_box
from app.core.storage import save_cli



def is_valid_username(name, users):
    if name == "":
        print("error, cannot be empty!")
        return False
    if name in users:
        print("Username already taken.")
        return False
    return True

def is_valid_password(password):
    if password == "":
        print("error password cannot empty!")
        return False
    return True

def register_user(users):
    """Register a new user by prompting for a unique username and password."""
    while True:
        name = input("Enter a username: ").lower().strip()
        if not is_valid_username(name, users):
            continue

        password = input("Enter a password: ").strip()
        if not is_valid_password(password):
            continue

        users[name] = password
        save_cli(users)

        print("you have signed up! Thank you!")
        return






def login_name_validation(name, users):
    """Validate a username"""
    if not name:
        print("Error: username cannot be empty.")
        return False

    if not name in users:
        print("Error: username does not exist, try again!")
        return False
    return True


def password_validation(password):
    """Validate a password"""
    if not password:
        print("Error: password cannot be blank, try again!")
        return False
    return True






def login_user(users):
    """login a user"""
    while True:
        name = input("login name: ")
        if not login_name_validation(name, users):
            continue

        password = input("login password: ")
        if not password_validation(password):
            continue

        if password == users[name]:
            print("success you have login successfully!")
            return

        print("error, please try again!")





def show_users(users):
    """Show registered users inside the square box."""
    square_box("User Data", users)











