from storage import storage



def menu_home():

    name = input("Enter your name: ")
    menu = (f"menu: hello {name} welcome to main menu, type '1', to enter registure as a new user, type '2' to login! type 'bye' to exit the menu! ")
    print(menu)

    while True:
        user_input = input("type :")
        if user_input == "bye":
            print("menu: goodbye")
            break


        elif user_input == "1":
            print("menu: registure selected")
            name = input("make a new username: ")
            password = input("Enter your new password: ")
            print("thank you for signing up!")
            storage[name] = password #this calls ot the storage !
            print(storage)


            #below is day 3
            if name in storage:
                if password == storage[name]:
                    print("success")
                else:
                    print("not successful")
            else:
                print("error")


        elif  user_input == "2":
            print("menu: login selected")
            name = input("username: ")
            password = input("password: ")

            storage[name] = password
            #below is day 3
            if name in storage:
                if password == storage[name]:
                    print("success")
                else:
                    return menu_home() + "menu: not successful"
            else:
                return menu_home() + "menu: error"


        else:
            return menu_home() + "menu: invalid option"

         
         if user_input in ["7" , "abc", '']:
         return f"{menu_home()} +  sorry your request is wrong , please try again"




menu_home()



