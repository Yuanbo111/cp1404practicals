"""
CP1404/CP5632 - Practical
File reading and writing exercises
"""

# ---- Question 1 ----
# Ask for user's name and write it to a file using open() and close()
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# ---- Question 2 ----
# Read the name back from the file and greet the user
in_file = open("name.txt", "r")
name_from_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_from_file}!")

# ---- Question 3 ----
# Create 'numbers.txt' file manually with:
# 17
# 42
# 400
# Read first two numbers and print their sum (use with + readline)
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    print(first_number + second_number)  # Output: 59

# ---- Question 4 ----
# Read all numbers and print the total (use with + for loop)
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)  # Output: 459 for 17 + 42 + 400
