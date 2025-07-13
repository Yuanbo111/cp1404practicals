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

def display_guitars(guitars):
    """Display the list of guitars with numbering."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

def add_new_guitars():
    """Prompt user to enter new guitars and return them as a list."""
    print("\nEnter your new guitars (leave name blank to finish):")
    new_guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        new_guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")
    return new_guitars

