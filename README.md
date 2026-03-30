
# Python CLI Authentication System

A simple command-line authentication system built while learning Python fundamentals.

This project simulates a small **user registration and login system** using a command-line interface (CLI). The goal of the project is to practice core programming concepts such as program flow, input handling, validation logic, and basic data storage.

The system allows users to register accounts, log in, and interact with a menu-based interface that runs continuously until the user exits.

---

## Features

Current functionality includes:

- User signup
- User login
- Username validation
- Password validation
- Detection of duplicate usernames
- Error handling for invalid menu options
- Continuous CLI menu navigation

The program runs inside a loop so users can interact with the system multiple times during a single session.

---

## Example Usage

When the program starts, the user is presented with a simple CLI menu:

```text
menu: hello Andrew welcome to main menu

1 -> Register
2 -> Login
bye -> Exit
````

Example registration flow:

```text
type: 1
menu: register selected
make a new username: andrew
Enter your new password: password123
thank you for signing up!
```

Example login flow:

```text
type: 2
menu: login selected
username: andrew
password: password123
login successful
```

---

## How Data Is Stored

User credentials are stored using a Python dictionary that simulates a very small in-memory database.

Example structure:

```python
storage = {
    "andrew": "password123"
}
```

In this structure:

* **username = dictionary key**
* **password = dictionary value**

This allows the program to quickly check if a user exists and verify their password during login.

---

## Concepts Practiced

This project was built to practice several important Python programming concepts.

### Control Flow

* `while` loops
* `if / elif / else`
* breaking out of loops
* managing user-driven program flow

### Functions

The program logic was broken into reusable functions such as:

* `menu_home()`
* `register_user()`
* `login_user()`

This helped introduce the concept of **modular program design**.

### Dictionaries

Dictionaries were used to simulate a user database.

Example:

```python
storage[username] = password
```

Accessing stored values:

```python
if username in storage:
```

This demonstrates how key-value data structures work in real applications.

### Input Handling

User interaction is handled using:

```python
input()
```

and validated to prevent incorrect or empty input.

### Validation Logic

The program includes checks for:

* empty usernames
* empty passwords
* duplicate usernames
* login attempts with non-existent users
* incorrect passwords
* invalid menu options

This introduces basic **defensive programming patterns**.

---

## Program Flow Design

An important concept discovered during this project was how **function call order affects program architecture**.

An incorrect design might look like this:

```python
menu_home()
register_user()
login_user()
```

This causes all functions to run automatically rather than waiting for user input.

The correct architecture is to let the **menu control which functions are executed**.

Example:

```python
while True:
    user_input = input("Select option: ")

    if user_input == "1":
        register_user()

    elif user_input == "2":
        login_user()

    elif user_input == "bye":
        break
```

In this design:

* `menu_home()` controls program flow
* `register_user()` and `login_user()` are called only when selected by the user

This introduces the concept of a **control layer in software design**.

---

## Challenges Encountered

During development several problems needed to be solved.

### Designing a CLI Menu Loop

Understanding how to keep the program running until the user exits using a loop.

### Dictionary Access

Learning that dictionaries must be accessed using keys:

```python
storage[username]
```

instead of being called like functions.

### Login Verification Logic

Validating login credentials requires checking two conditions:

1. The username exists
2. The stored password matches the entered password

Example logic:

```python
if username in storage and storage[username] == password:
    print("login successful")
```

### Code Organization

The project initially began as a single script and was gradually refactored into functions.

This introduced the idea of **modular program design and code organization**.

---

## Project Structure

```text
cli-auth-system/
│
├── main.py        # Program entry point
├── auth.py        # Login and registration logic
├── storage.py     # User data storage
└── README.md
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/yourusername/cli-auth-system.git
```

2. Navigate into the project folder

```bash
cd cli-auth-system
```

3. Run the program

```bash
python main.py
```

---

## Future Improvements

Planned upgrades include:

* saving user data to a file
* password hashing for security
* separating the CLI interface further from authentication logic
* improved error handling
* persistent user sessions

---

## Project Status

Work in progress.

This project will continue to evolve as new Python concepts are learned and applied.

---

## Purpose of This Project

This project is part of a structured Python learning roadmap focused on building real programming skills through small practical projects.

The long-term goal is to progress from simple scripts toward more advanced backend development and software engineering concepts.

```

Small correction: replace `yourusername` in the clone link with your actual GitHub username.
```
