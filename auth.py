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






def login_user():


    name = input("username: ")
    if name not in storage:
        print("menu: username does not exist, try again!")

    elif name == "":
        print("menu: username cannot be blank, try again!")

    password = input("password: ")
    if password == "":
        print("menu: password cannot be blank, try again!")

    elif password not in storage:
        print("menu: password does not exist, try again!")


    storage[name] = password
    if name in storage:
        if password == storage[name]:
            print("success")




