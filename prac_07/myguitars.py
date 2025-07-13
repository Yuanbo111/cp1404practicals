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

def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


