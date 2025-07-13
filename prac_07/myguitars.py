from guitar import Guitar
FILENAME = "guitars.csv"

def main():
    """Main program to load, display, add, sort, and save guitars."""
    guitars = load_guitars(FILENAME)
    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    add_new_guitars(guitars)

    guitars.sort()
    print("\nThese are your guitars (sorted by year):")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)

