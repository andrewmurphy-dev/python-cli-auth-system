from storage import storage




def registure_user():


    name = input("make a new username: ")
    if name == "":
        print("menu: error, try again!!!")

    elif name in storage:
        print("username is already taken! try again!")

    password = input("Enter your new password: ")
    if password == "":
        print("menu: password cannot be blank!, try again!!!")

    elif password in storage:
        print("menu: password is already taken! try again!")

    else:
        print("menu: thank you for signing up!")

        storage[name] = password 
        print(storage)


    if name in storage:
        if password == storage[name]:
               print("menu: success")
        else:
            print("menu: not successful, try again!!!")





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




