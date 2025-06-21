""""
wimbledon.py
Estimated: 30 minutes
Actual: 20 minutes
"""
FILENAME = "wimbledon.csv"

def main():
    data = read_data(FILENAME)
    champion_to_wins = count_champions(data)
    countries = get_champion_countries(data)
    display_results(champion_to_wins, countries)

