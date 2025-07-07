""""
wimbledon.py
Estimated: 30 minutes
Actual: 20 minutes
"""
FILENAME = "wimbledon.csv"

def main():
    """ Read Wimbledon data, count champion wins, collect countries, and display results"""
    data = read_data(FILENAME)
    champion_to_wins = count_champions(data)
    countries = get_champion_countries(data)
    display_results(champion_to_wins, countries)

def read_data(filename):
    """Read the data from the given CSV file and return a list of rows."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        return [line.strip().split(",") for line in in_file.readlines()[1:]]

def count_champions(data):
    """Count how many times each champion has won."""
    champion_to_wins = {}
    for row in data:
        champion = row[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins

def get_champion_countries(data):
    """Return a sorted list of unique countries of the champions."""
    countries = {row[1] for row in data}
    return sorted(countries)

def display_results(champion_to_wins, countries):
    """Display champions with their win counts and list of countries."""
    print("Wimbledon Champions:")
    max_name_length = max(len(name) for name in champion_to_wins)
    for name, count in sorted(champion_to_wins.items()):
        print(f"{name:{max_name_length}} : {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

main()