"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from car import Car
import random

class UnreliableCar(Car):
    def __init__(self,name,fuel,reliability):
        super().__init__(name,fuel)
        self.reliability = reliability
        
    def drive(self,distance):
        random_number = random().randint(0,100)
        if random().randint(0,100) < self.reliability:
            
            return super().drive(distance)
        else:
            print("Car cannot be driven")
            return 0