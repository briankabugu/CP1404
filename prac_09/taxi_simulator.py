"""
CP1404 Practical
Tax Simulator class
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    """Display available taxis."""
    print("Taxis available")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Choose a taxi."""
    display_taxis(taxis)
    choice = int(input("Choose taxi: "))
    print(choice)
    if 0 <= int(choice) < len(taxis):
        return taxis[int(choice)]
    else:
        print("Invalid taxi choice")

def drive_taxi(taxi):
    """Drive the chosen taxi."""
    distance = float(input("Drive how far? "))
    
    taxi.drive(distance)
    fare = taxi.get_fare()
    
    print(f"Your {taxi.name} trip cost you ${fare:.2f}")
    return fare

def main():
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    
    print("Let's drive")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").strip().lower()
    while choice != 'q': 
        if choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            if current_taxi is not None:
                fare = drive_taxi(current_taxi)             
                total_bill += fare             
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        
        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").strip().lower()
            
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == '__main__':
    main()