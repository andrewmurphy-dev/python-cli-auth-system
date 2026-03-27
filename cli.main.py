from storage import storage



def menu_home():

    name = input("Enter your name: ")


    while True:
        menu = (
            f"menu: hello {name} welcome to main menu, type '1', to enter registure as a new user, type '2' to login! type 'bye' to exit the menu! ")
        print(menu)
        user_input = input("type :")
        if user_input == "bye":
            print("menu: goodbye")
            break





        #sign up !
        elif user_input == "1":
            print("menu: registure selected")

            #step 1
            name = input("make a new username: ")
            #test 1
            #user presses enter !
           if name == "":
               print("menu: error, try again!!!")



            #test 2 registuring a user that already exists!

            elif name in storage:
            print("username is already taken! try again!")




            password = input("Enter your new password: ")
            #test 1
            if password == "":
               print("menu: password cannot be blank!, try again!!!")
               ret

            #test 2

            elif password in storage:
                print("menu: password is already taken! try again!")

             else:
                 print("menu: thank you for signing up!")



            storage[name] = password #this calls ot the storage !
            print(storage)

        else:
            print("menu: not successful, try again!!!")


            #below is day 3
        if name in storage:
            if password == storage[name]:
                    print("menu: success")
            else:
                print("menu: not successful, try again!!!")


        #login
        elif  user_input == "2":
            print("menu: login selected")
            name = input("username: ")
            #test 1 login already exists !
            if name not in storage:
                print("menu: username does not exist, try again!")
                #test 2 menu cannot be blank!
            elif name == "":
                print("menu: username cannot be blank, try again!")

            password = input("password: ")
            #test 1
            if password == "":
                print("menu: password cannot be blank, try again!")
            elif password not in storage:
                print("menu: password does not exist, try again!")


            storage[name] = password
            #below is day 3
            if name in storage:
                if password == storage[name]:
                    print("success")








menu_home()



