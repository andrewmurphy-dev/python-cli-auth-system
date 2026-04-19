from storage import storage




def is_valid_username(name, storage):
    if not name:
        print("Error: username cannot be empty.")
        return False
    if name in storage:
        print("Username already taken.")
        return False
    return True

def is_valid_password(password):
    if not password:
        print("Error: password cannot be empty.")
        return False
    return True

def register_user(storage):
    """Register a new user by prompting for a unique username and password."""
    while True:
        name = input("Enter a username: ").lower().strip()
        if not is_valid_username(name, storage):
            continue

        password = input("Enter a password: ").strip()
        if not is_valid_password(password):
            continue

        storage[name] = password
        print("Signed up successfully!")
        return


def login_name_validation(name, storage):
    """Validate a username"""
    if not name:
        print("Error: username cannot be empty.")
        return False

    if not name in storage:
        print("Error: username does not exist, try again!")
        return False
    return True


def password_validation(password):
    """Validate a password"""
    if not password:
        print("Error: password cannot be blank, try again!")
        return False
    return True






def login_user(name, password):
    """login a user"""
    while True:
        name = input("login name: ")
        if not login_name_validation(name, storage):
            continue

        password = input("login password: ")
        if not password_validation(password):
            continue

        storage[name] = password
        if name in storage:
            if password == storage[name]:
                print("success, you have logged in successfully!")
                return





