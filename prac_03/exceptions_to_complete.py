"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # ✅ TODO: set flag to exit the loop if input is valid
    except ValueError:  # ✅ TODO: catch ValueError for invalid int input
        print("Please enter a valid integer.")

print("Valid result is:", result)
