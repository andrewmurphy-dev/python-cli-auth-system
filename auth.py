from storage import storage







def registure_user():
    if user_input == "1":
        print("menu: registure selected")

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



storage[name] = password # this calls ot the storage !
print(storage)

else:
print("menu: not successful, try again!!!")


# below is day 3
if name in storage:
    if password == storage[name]:
        print("menu: success")
    else:
        print("menu: not successful, try again!!!")


def login_user():
    if  user_input == "2":
        print("menu: login selected")
        name = input("username: ")
        # test 1 login already exists !
    if name not in storage:
        print("menu: username does not exist, try again!")
        # test 2 menu cannot be blank!
    elif name == "":
        print("menu: username cannot be blank, try again!")

    password = input("password: ")
    # test 1
    if password == "":
        print("menu: password cannot be blank, try again!")
    elif password not in storage:
        print("menu: password does not exist, try again!")


    storage[name] = password
    # below is day 3
    if name in storage:
        if password == storage[name]:
            print("success")

