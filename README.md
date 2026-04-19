# 🔐 Python CLI Authentication System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📖 Description

A simple Python CLI-based authentication system that allows users to register, log in, and interact with a menu-driven interface.

This project was built to practice core backend concepts such as input validation, control flow, modular design, and dictionary-based data storage.

---

## 🚀 Features

- User registration system
- User login system
- Username validation
- Password validation
- Duplicate username detection
- Error handling for invalid input
- Continuous CLI menu loop
- Modular code structure

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/python-cli-auth-system.git
cd python-cli-auth-system


## 💻 Usage

### Example Menu

```text
welcome to main menu

press 1: register a new user
press 2: login
press 'exit' to quit
```

### Example Registration

```text
Enter a username: andy
Enter a password: password123
Signed up successfully!
```

### Example Login

```text
login name: andy
login password: password123
success, you have logged in successfully!
```

## 🧠 How It Works

### Storage Structure

```python
storage = {
    "andy": "password123"
}
```

- **Key** → username
- **Value** → password

### Login Validation Logic

```python
if username in storage and storage[username] == password:
    print("login successful")
```

## 🗂️ Project Structure

```text
python-cli-auth-system/
│
├── main.py        # Entry point and CLI menu
├── auth.py        # Authentication logic
├── storage.py     # In-memory user storage
└── README.md
```

## 📁 File Breakdown

### main.py

- Handles user input
- Controls program flow (menu loop)

### auth.py

- Contains validation logic
- Handles user registration and login

### storage.py

- Stores user data in a dictionary

## ⚠️ Known Limitations

- Data is not persistent (lost when program exits)
- Passwords are stored in plain text
- No authentication sessions
- No database integration

## 🔧 Future Improvements

- Save users to JSON file
- Add password hashing (bcrypt)
- Add session handling
- Improve CLI UX
- Add unit tests
- Convert to FastAPI backend

## 🤝 Contributing

### Steps to contribute

```bash
git checkout -b feature/your-feature-name
git commit -m "Add meaningful feature"
git push origin feature/your-feature-name
```

Then open a Pull Request.

## 🎯 Purpose

This project demonstrates:

- Control flow design
- Input validation
- Dictionary-based data handling
- Modular Python structure
