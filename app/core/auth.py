import requests


BASE_URL = "http://localhost:8000"

def sign_up_username():
    username = input("enter a username: ").lower().strip()

    if not username:
        print("Error: username cannot be empty, try again!")
        return None
    
    if len(username) < 3:
        print("Error: username must be at least 3 characters long, try again!")
        return None
    

    if len(username) > 14:
        print("Error: username cannot be longer than 14 characters, try again!")
        return None
    
    if " " in username:
        print("Error: username cannot contain spaces, try again!")
        return None
    
    return username
    




def sign_up_password():
    password = input("enter a password: ").strip()

    if not password:
        print("Error: password cannot be empty, try again!")
        return None
    
    if len(password) < 6:
        print("Error: password must be at least 6 characters long, try again!")
        return None
    
    if len(password) > 14:
        print("Error: password cannot be longer than 14 characters, try again!")
        return None
    
    if " " in password:
        print("Error: password cannot contain spaces, try again!")
        return None
    
    return password






def sign_up_dict(username, password):
    signup = {
              "name": username,
              "password": password,
              }
    
    return signup



def post_users_response(signup):
    response = requests.post(f"{BASE_URL}/users", json=signup, timeout=10)
    return response



def validate_post_users_response(response):
    response.raise_for_status()


def parse_post_users_response(response):
    data = response.json()
    return data


def print_signup_message(data):
    print(data["message"])





def sign_up():
    print()
    print("Welcome to the Sign-Up Page!")

    username = sign_up_username()
    if username is None:
        return
    
    password = sign_up_password()
    if password is None:
        return
    
    signup = sign_up_dict(username, password)

    try:

        response = post_users_response(signup)
        validate_post_users_response(response)
        data = parse_post_users_response(response)
        print_signup_message(data)



    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server. Please ensure the API is running.")
    
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")

    except requests.exceptions.HTTPError as error:
        handle_http_error(error)

    except requests.exceptions.RequestException:
        print("An error occurred while signing up. Please try again later.")

    except ValueError:
        print("Error: Received an invalid response from the server.")





def login_username():

    username = input("enter your login username: ").lower().strip()

    if username is None:
        print("username cannot be empty!")
        return None
    
    if len(username) < 3:
        print("username is too short!")
        return None
    
    if len(username) > 14:
        print("username is too long try again!")
        return None 
    
    return username 


def login_password():

    password = input("enter your username login password: ").strip() 

    if password is None:
        print("password cannot be empty!")
        return None 
    
    if len(password) < 3:
        print("password is too short")
        return None
    
    if len(password) > 14:
        print("password is too long")
        return None 
    
    return password 




def login_structure(name, password):

    login = {
        "name": name,
        "password": password,
    }
    return login 


def login_post_request(login):
    response = requests.post(f"{BASE_URL}/login", json=login, timeout=10)
    return response 




def parse_login_response(response):
    data = response.json()
    return data 


def show_login_message(data):
    print(data["message"])


def validate_login_response(response):
    response.raise_for_status() 


def login_user():
    print()
    print("welcome to login page!")

    username = login_username()

    if username is None:
        return 
    
    password = login_password()

    if password is None:
        return 
    

    login = login_structure()

    

    try:
        response = login_post_request(login)
        validate_login_response(response)
        data = parse_login_response(response)
        show_login_message(data)

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server. Please ensure the API is running.")
    
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")

    except requests.exceptions.HTTPError as error:
        handle_http_error(error)

    except requests.exceptions.RequestException:
        print("An error occurred while signing up. Please try again later.")

    except ValueError:
        print("Error: Received an invalid response from the server.")





def handle_http_error(error):
    response = error.response

    if response is None:
        print("HTTP error occurred, but no response was received.")
        return

    status_code = response.status_code

    if status_code == 400:
        print("Error: Bad request. Please check your input.")
        return

    if status_code == 401:
        print("Error: You are not authenticated.")
        return

    if status_code == 403:
        print("Error: You do not have permission to do this.")
        return

    if status_code == 404:
        print("Error: Resource not found.")
        return

    if status_code == 409:
        print("Error: Username already exists. Please try another username.")
        return

    if status_code >= 500:
        print("Error: Server problem. Please try again later.")
        return

    print(f"HTTP error occurred: {status_code}")











def get_users_response():
    response = requests.get(f"{BASE_URL}/users", timeout=10)
    return response

def validate_users_response(response):
    response.raise_for_status()  # Check if the request was successful


def parse_users_response(response):
    data = response.json()
    return data

def print_data(users):
    for user in users:
        print(f"ID: {user['id']} | Name: {user['name']} | Password: {user['password']}")






#so now we need to make a controller funtion 


def show_users():
    try:
        response = get_users_response()
        validate_users_response(response)
        users = parse_users_response(response)
        print_data(users)


    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server. Please ensure the API is running.")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")

    except requests.exceptions.HTTPError as error:
        handle_http_error(error)

    except requests.exceptions.RequestException:
        print("An error occurred while fetching users. Please try again later.")

    except ValueError:
        print("Error: Received an invalid response from the server.")



#http error handler function to handle different status codes and print appropriate messages to the user, this will be used in the except block of the show_users function to handle HTTP errors that may occur when fetching users from the API.

def handle_http_error(error):
    response = error.response

    if response is None:
        print("HTTP error occurred, but no response was received.")
        return

    status_code = response.status_code

    if status_code == 400:
        print("Error: Bad request. Please check your input.")
        return

    if status_code == 401:
        print("Error: You are not authenticated.")
        return

    if status_code == 403:
        print("Error: You do not have permission to do this.")
        return

    if status_code == 404:
        print("Error: Resource not found.")
        return

    if status_code == 409:
        print("Error: Conflict. This action may already exist or cannot be repeated.")
        return

    if status_code >= 500:
        print("Error: Server problem. Please try again later.")
        return

    print(f"HTTP error occurred: {status_code}")













    










