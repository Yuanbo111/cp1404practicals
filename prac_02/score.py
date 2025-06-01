"""
CP1404/CP5632 - Practical
Refactored program to determine score status using constants
"""

import random

MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50
MINIMUM_SCORE = 0

def main():
    """Main function to get user input, show result, and generate random score."""
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(result)

    # Generate a random score and show the result
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(f"Random score: {random_score:.2f}")
    print(get_score_result(random_score))

def get_score_result(score):
    """Determine the result category for a given score."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

main()
