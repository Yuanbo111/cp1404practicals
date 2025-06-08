"""
CP1404/CP5632 - Practical
Random function exercises
"""

import random

# Line 1: random integer from 5 to 20 (inclusive)
print(random.randint(5, 20))  # e.g., 13
# Smallest possible: 5
# Largest possible: 20

# Line 2: random odd number from 3 up to (but not including) 10, step by 2
print(random.randrange(3, 10, 2))  # e.g., 3, 5, 7, 9
# Smallest possible: 3
# Largest possible: 9
# Could this have produced a 4? No, because step=2 from 3 gives only odd numbers

# Line 3: random float between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # e.g., 3.748192
# Smallest possible (close to): 2.5
# Largest possible (close to): 5.5

# Code to generate a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
