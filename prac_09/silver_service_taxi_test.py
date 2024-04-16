"""
CP1404 Practical
Silver Service Taxi Test
"""
from silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi object
    my_silver_service_taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(my_silver_service_taxi)

    # Test the __str__() method
    expected_str = "Hummer, fuel=200, odometer=0, 0km on current fare, $4.92/km plus flagfall of $4.5"
    assert str(my_silver_service_taxi) == expected_str
    
    another_silver_service_taxi = SilverServiceTaxi("Limo", 100, 2)

    another_silver_service_taxi.drive(18)

    expected_fare = 48.8
    assert float(another_silver_service_taxi.get_fare()) == expected_fare
    
    print("Test passed")
main()