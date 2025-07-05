import random

class Employee:
    def __init__(self,name,worktype):
        self.name=name
        self.is_Present=False
        self.wage_per_hour = 20
        self.full_hours = 8
        self.part_time_hours = 4
        self.worktype = worktype.lower()

    
    def check_attendance(self):
        attendance=random.randint(0,1)
        if attendance==1:
            self.is_Present=True
            print(f"{self.name} is Present")
        else:
            self.is_Present=False
            print(f"{self.name} is Absent")

    def calculate_full_time_wage(self):
        if self.worktype == "full-time" and self.is_Present:
            return self.wage_per_hour * self.full_hours
        return 0

    

    def calculate_part_time_wage(self):
        if self.worktype == "part-time" and self.is_Present:
            return self.wage_per_hour * self.part_time_hours
        return 0

    def calculate_wage_switch_case(self):
        if not self.is_Present:
            print(f"{self.name} earns ₹0 today (Absent)")
            return

        match self.worktype:
            case "full-time":
                wage = self.calculate_full_time_wage()
                print(f"{self.name}'s Full-Time Wage: ₹{wage}")
            case "part-time":
                wage = self.calculate_part_time_wage()
                print(f"{self.name}'s Part-Time Wage: ₹{wage}")
            case _:
                print(f"Invalid work type for {self.name}")
