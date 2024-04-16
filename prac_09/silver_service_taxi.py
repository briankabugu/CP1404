"""
CP1404/CP5632 Practical
Silver Service Taxi class
"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flag_fall = 4.5
    def __init__(self,name,fuel,fanciness):
        super().__init__(name,fuel)
        self.price_per_km = fanciness * super().price_per_km
        
    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flag_fall}"
        
    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        return distance_driven
    
    def get_fare(self):
        fare = (self.price_per_km * self.current_fare_distance) + self.flag_fall
        return round(fare,1)