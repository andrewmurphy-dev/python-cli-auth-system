from fastapi import requests


BASE_URL = "http://localhost:8000"


def signup_user():
    print()
    print("welcome to signup page!")

    name = input("enter a username: ").lower().strip()

    if name == "":
        print("Error: username cannot be empty, try again!")
        return
    
    password = input("enter a password: ").strip()
    if password == "":
        print("Error: password cannot be empty, try again!")
        return
    
    dict_to_save = {"name": name, "password": password}
    
    try:
        response = requests.post(f"{BASE_URL}/users", json=dict_to_save, timeout=10)

        response.raise_for_status()  # Check if the request was successful, this will communicate with the API endpoint and raise an error if the response status code indicates a failure (4xx or 5xx).
        #basically its , is the status code an error code? if yes, raise an error and handle it in the except block, if not, continue to the next line of code
        #its checking the requests , checks the HTTP status code 
        #if the status code is successful ots 200, OK , 201 created, 204 no content, then it will continue to the next line of code, which is to parse the response as JSON and print the message from the response.
        #if there is an error in the status code , it will raise an HTTPError
        data = response.json() #response from the endpoint
        print(data["message"])

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server. Please ensure the API is running.")
        return
    
    except requests.exceptions.HTTPError as error:

        try:
            error_data = response.json()
            print(error_data.get("message", "username already exists, please try again with a different username!"))
            #we are using get to get the actual message response from the API !
            return 
        except ValueError:
            print(f"HTTP error occurred: {response.raise_for_status()}")
            return
    
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
        return
    
    except requests.exceptions.RequestException:
        print("An error occurred while signing up. Please try again later.")
        return
    
    except ValueError:
        print("Error: Received an invalid response from the server.")
        return
    








def show_users():

    try:
        response = requests.get(f"{BASE_URL}/users", timeout=10)


        response.raise_for_status()  # Check if the request was successful
        users = response.json()
        #above is the list of dicts ``


        for user in users:
            print(f"ID: {user['id']} | Name: {user['name']} | Password: {user['password']}")



    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server. Please ensure the API is running.")
        return 
            
    except requests.exceptions.HTTPError as error:
        print(f"HTTP error occurred: {error}")
        return
    
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
        return
    
    except requests.exceptions.RequestException:
        print("An error occurred while fetching users. Please try again later.")
        return
    
    except ValueError:
        print("Error: Received an invalid response from the server.")
        return
    




    










