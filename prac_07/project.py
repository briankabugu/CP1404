import datetime

class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion
    
    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"
    
    def start_date_after(self, date):
        project_date = datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()
        filter_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        return project_date > filter_date
    
    def update_completion(self, completion):
        self.completion = completion
    
    def update_priority(self, priority):
        self.priority = priority
        
    def __gt__(self,other):
        return self.priority > other.priority
