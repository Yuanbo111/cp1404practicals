"""
emails.py
Estimated: 30 minutes
Actual: 27 minutes
"""

def main():
    """ Collect and store email–name pairs, confirming names with the user."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        extracted_name = extract_name(email)
        confirmation = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()

        if confirmation == "" or confirmation == 'y':
            name = extracted_name
        else:
            name = input("Name: ").strip()

        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()