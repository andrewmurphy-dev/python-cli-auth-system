"""
Intermediate signup flow example.

This is a learning file only. It does not change your real CLI app.

The main idea:
- one function gets input
- one function sends the API request
- one function handles the API response
- signup_user() reads like the story of the feature
"""

import requests


BASE_URL = "http://127.0.0.1:8000"


def get_required_input(prompt, empty_error_message):
    """Ask for input and return None if the user typed nothing."""
    value = input(prompt).strip()

    if value == "":
        print(empty_error_message)
        return None

    return value


def get_signup_input():
    """Collect and validate only the signup input."""
    print()
    print("welcome to signup page!")

    name = get_required_input(
        "enter a username: ",
        "Error: username cannot be empty, try again!",
    )

    if name is None:
        return None

    password = get_required_input(
        "enter a password: ",
        "Error: password cannot be empty, try again!",
    )

    if password is None:
        return None

    payload = {
        "name": name.lower(),
        "password": password,
    }

    return payload


def send_signup_request(payload):
    """Send only the API request."""
    response = requests.post(f"{BASE_URL}/users", json=payload, timeout=10)
    return response


def get_json_message(response, fallback_message):
    """Safely read the API's JSON message."""
    try:
        data = response.json()
    except ValueError:
        return fallback_message

    return data.get("message", fallback_message)


def handle_signup_response(response):
    """Handle what the server said back."""
    if response.status_code in (200, 201):
        message = get_json_message(response, "Signup successful.")
        print(message)
        return

    if response.status_code == 400:
        message = get_json_message(response, "Invalid signup details.")
        print(message)
        return

    if response.status_code == 409:
        message = get_json_message(response, "Username already exists.")
        print(message)
        return

    if response.status_code >= 500:
        print("Server error. Please try again later.")
        return

    message = get_json_message(response, "Signup failed. Please try again.")
    print(message)


def signup_user():
    """The full signup flow, written as simple steps."""
    payload = get_signup_input()

    if payload is None:
        return

    try:
        response = send_signup_request(payload)
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server. Please ensure the API is running.")
        return
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
        return
    except requests.exceptions.RequestException:
        print("An error occurred while signing up. Please try again later.")
        return

    handle_signup_response(response)


if __name__ == "__main__":
    signup_user()
