MINIMUM_LENGTH = 5

def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    """Get a valid password with at least MINIMUM_LENGTH characters."""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long.")
        password = input("Enter password: ")
    return password

def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))

main()
