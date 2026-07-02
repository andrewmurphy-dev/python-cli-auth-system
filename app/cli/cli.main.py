from app.core.storage import load_cli
from app.core.auth import login_user, sign_up, show_users
from app.cli.ui import square_box




def option_validation():

    option_text = input("Enter your choice: ").strip() 

    if option_text is None:
        print("Error: option cannot be empty, try again!")
        return None
    
    if option_text == "exit":
        print("Exiting the program...")
        return "exit"
    
    try:
        option = int(option_text)
    
    except ValueError:
        print("Error: option must be a number, try again!")
        return None
    
    if option < 1 or option > 3:
        print("Error: option must be between 1 and 3, try again!")
        return None
    
    return option



def menu_home():

    users = load_cli()

    if users is None:
        print("Error: no users found, please register a user first!")
        return
    
    while True:
        square_box(
            "Welcome to the CLI App",
            [
                "1. Register a new user",
                "2. Login as an existing user",
                "3. Show all users",
                "Type 'exit' to quit the program",
            ],
        )

        option = option_validation()

        if option is None:
            continue
        
        if option == "exit":
            print("Thank you for using the CLI App. Goodbye!")
            break

        if option == 1:
            sign_up()
        
        elif option == 2:
            login_user()
        
        elif option == 3:
            show_users()






if __name__ == "__main__":
    menu_home()
