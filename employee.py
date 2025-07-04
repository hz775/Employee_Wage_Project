import random

class Employee:
    def __init__(self,name):
        self.name=name
        self.is_Present=False
        self.wage_per_hour = 20
        self.full_hours = 8
    
    def check_attendance(self):
        attendance=random.randint(0,1)
        if attendance==1:
            self.is_Present=True
            print(f"{self.name} is Present")
        else:
            self.is_Present=False
            print(f"{self.name} is Absent")

    def calculate_full_time_wage(self):
        if self.is_Present:
            wage = self.wage_per_hour * self.full_hours
            print(f"{self.name}'s Full-Time Daily Wage: ₹{wage}")
        else:
            print(f"{self.name} earns ₹0 today (Absent)")

    

    