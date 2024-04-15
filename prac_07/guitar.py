import datetime
class Guitar:
    def __init__(self, name='',year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        
    def get_age(self):
        return int(datetime.datetime.now().strftime("%Y")) - self.year
        
    def is_vintage(self):
        return self.get_age() > 50      
        
    def __str__(self):
        return f"Guitar"
    
    def __lt__(self, other):
        """Less than comparison based on year."""
        return self.year < other.year