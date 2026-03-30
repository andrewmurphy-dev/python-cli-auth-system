from auth import registure_user, login_user


def menu_home():
    name = input("Enter your name: ")
    
    while True:
      menu = (f"menu: hello {name} welcome to main menu, type '1', to enter registure as a new user, type '2' to login! type 'bye' to exit the menu! ")
      print(menu)
      user_input = input("type :")
      if user_input == "bye":
            print("menu: goodbye")
            break

      if user_input == "1":
        print("menu: registure selected")
        registure_user()

      if user_input == "2":
        print("menu: login selected")
        login_user()



menu_home()
registure_user()
login_user()

