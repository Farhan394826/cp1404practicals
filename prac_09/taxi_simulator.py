
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    total_bill = 0
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None

    print("Let's drive!")
    while True:
        print(MENU)
        menu_choice = input(">>> ").strip().lower()

        if menu_choice == "q":
            break
        elif menu_choice == "c":
            current_taxi = choose_taxi(taxis)
        elif menu_choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def choose_taxi(taxis):
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input; please enter a number.")
        return None

def drive_taxi(current_taxi, total_bill):
    if current_taxi:
        current_taxi.start_fare()
        try:
            distance = float(input("Drive how far? "))
            distance_driven = current_taxi.drive(distance)
            trip_cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f} for {distance_driven:.2f} km")
            return total_bill + trip_cost
        except ValueError:
            print("Invalid input; please enter a number.")
            return total_bill
    else:
        print("You need to choose a taxi before you can drive.")
        return total_bill

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
