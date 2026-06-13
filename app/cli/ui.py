

def square_box(title, options):
    width = 34

    def print_line(text):
        print("| " + text.ljust(width - 2) + " |")

    print("+" + "-" * width + "+")
    print("|" + title.center(width) + "|")
    print("+" + "-" * width + "+")

    if not options:
        print_line("No data found")

    elif isinstance(options, dict):
        for username, password in options.items():
            print_line("Username: " + username)
            print_line("Password: " + password)
            print_line("-" * (width - 2))

    else:
        for option in options:
            print_line(option)

    print("+" + "-" * width + "+")





