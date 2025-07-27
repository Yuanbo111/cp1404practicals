from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Run the taxi simulator program."""
    print("Let's drive!")

    # Create a list of taxi options
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    bill = 0.0  # Total fare accumulated
    current_taxi = None  # No taxi selected initially

    display_menu()
    choice = input(">>> ").lower()

    # Main command loop
    while choice != "q":
        if choice == "c":
            # Show available taxis and prompt user to choose one
            list_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid taxi choice")

        elif choice == "d":
            # Handle drive request
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()  # Reset the fare for a new trip
                try:
                    distance = float(input("Drive how far? "))
                    if distance < 0:
                        print("Distance must be non-negative")
                        distance = 0
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    distance = 0

                # Drive the selected taxi and calculate fare
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                bill += fare  # Accumulate the total bill

        else:
            # Handle invalid menu options
            print("Invalid option")

        # Show bill after each action
        print(f"Bill to date: ${bill:.2f}")
        display_menu()
        choice = input(">>> ").lower()

    # End of program: show final bill and taxi states
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    list_taxis(taxis)

if __name__ == "__main__":
    main()