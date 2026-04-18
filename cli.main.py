from auth import registure_user, login_user


def menu_home() -> None:
    """displays main menu and handles user navigation"""
    while True:
        print("welcome to main menu")
        print("type to choose your option")


        print("press 1: register a new user")
        print("press 2: login")
        print("press: 'exit' logout")

        option = input("type to choose: ").lower().strip()

        if option == "":
            print("error, cannot be blank, please try again")
            continue

        elif option == "1":
            print("menu: registure selected")
            registure_user()

        elif option == "2":
            print("menu: login selected")
            login_user()

        elif option == "exit":
            break

        else:
            print("error, try again")





if __name__ == "__main__":
    menu_home()

