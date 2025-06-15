"""
CP1404/CP5632 Practical
Refactored version of cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)

def print_income_report(incomes):
    """Print the income report with cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for i, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {i:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()
