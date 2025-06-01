"""
CP1404/CP5632 - Practical
Menu-driven program for score processing
"""

MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50
MENU = """\nMenu
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""

def main():
    """Main menu loop to manage score input and actions."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell!")

def get_valid_score():
    """Prompt the user for a valid score between MINIMUM_SCORE and MAXIMUM_SCORE."""
    score = float(input("Enter a valid score (0-100): "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter a valid score (0-100): "))
    return score

def determine_score_result(score):
    """Return the classification of a score"""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    """Print as many stars as the score (rounded to int)."""
    print("*" * int(score))

main()
