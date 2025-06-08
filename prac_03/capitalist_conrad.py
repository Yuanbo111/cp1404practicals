"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.

- Price starts at $10.00
- Increases by up to 17.5%
- Decreases by up to 5%
- Simulation ends when price < $1.00 or > $100.00
- Writes output to a file
"""

import random

# Constants
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "output.txt"

# Starting values
price = INITIAL_PRICE
number_of_days = 0

# Open file for writing
out_file = open(FILENAME, 'w')

# Write starting price
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulation loop
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()
