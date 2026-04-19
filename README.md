# 🔐 Python CLI Authentication System
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
A simple Python CLI-based authentication system that allows users to register, log in, and interact with a menu-driven interface.
This project was built to practice core backend concepts such as input validation, control flow, modular design, and dictionary-based data storage.
---
## 🚀 Features
- User registration system
- User login system
- Username and password validation
- Duplicate username detection
- Error handling for invalid input
- Continuous CLI menu loop
- Modular code structure
The program runs inside a loop so users can interact with the system multiple times during a single session.
---
## 📦 Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/python-cli-auth-system.git
cd python-cli-auth-system
Run the program:

python main.py
💻 Usage
Example Menu
welcome to main menu
type to choose your option
press 1: register a new user
press 2: login
press 'exit': logout
Example Registration
type to choose: 1
menu: register selected
Enter a username: andy
Enter a password: password123
Signed up successfully!
Example Login
type to choose: 2
menu: login selected
login name: andy
login password: password123
success, you have logged in successfully!
🧠 How It Works
User data is stored in-memory using a Python dictionary:

storage = {
    "andy": "password123"
}
Key → username
Value → password
Login validation checks that:

The username exists in storage
The entered password matches the stored password
if username in storage and storage[username] == password:
    print("login successful")
🗂️ Project Structure
python-cli-auth-system/
│
├── main.py        # Entry point and CLI menu
├── auth.py        # Authentication logic
├── storage.py     # In-memory user storage
└── README.md
File Breakdown
main.py

Displays the main menu
Handles user input
Controls program flow
auth.py

Validates usernames and passwords
Handles registration and login logic
storage.py

Stores user credentials in a dictionary
⚠️ Known Limitations
Data is not persistent and is lost when the program exits
Passwords are stored in plain text with no hashing
No user sessions
No database integration
No unit tests yet
🔧 Future Improvements
Save user data to a JSON file
Hash passwords using bcrypt or hashlib
Add logout and session handling
Improve CLI formatting and user experience
Add unit tests
Refactor into a FastAPI backend project
🤝 Contributing
Contributions are welcome.

Fork the repository
Create a feature branch
git checkout -b feature/your-feature-name
Commit your changes
git commit -m "Add meaningful feature description"
Push your branch
git push origin feature/your-feature-name
Open a Pull Request
🎯 Purpose
This project is part of a structured Python learning roadmap focused on building real programming and backend development skills.

It demonstrates:

Control flow design
Input validation
Dictionary-based data handling
Modular Python code organization
Basic authentication logic
📚 What I Learned
Building a continuous menu loop with while True
Separating logic into reusable functions
Validating user input properly
Using dictionaries to simulate simple data storage
Structuring a Python project across multiple files
