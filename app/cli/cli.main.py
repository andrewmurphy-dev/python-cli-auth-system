from app.core.storage import load_cli
from app.core.auth import register_user, login_user, show_users
from app.cli.ui import square_box



def menu_home() -> None:
    """displays main menu and handles user navigation"""
    users = load_cli()

    if users is None:
        return

    while True:
        square_box("Main Menu", [
            "1. Register a new user",
            "2. Login",
            "3. Show users",
            "type exit Logout"
        ])

        option_text = input("Type to choose: ").strip()

        if option_text == "":
            print("error, cannot be blank, please try again")
            continue

        if option_text == "exit":
            print("Thank you: Goodbye!")
            break 

       
        try:
            option = int(option_text)
        except ValueError:
            print("error the choice must be a number!")
            continue 


        if option == 1:
            print("menu: signup selected")
            register_user(users)

        elif option == 2:
            print("menu: login selected")
            login_user(users)

        elif option == 3:
            print("menu: show users selected")
            show_users(users)

        else:
            print("invalid input")
            






if __name__ == "__main__":
    menu_home()

