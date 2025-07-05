import random

class Employee:
    def __init__(self, name, worktype):
        self.name = name
        self.is_Present = False
        self.wage_per_hour = 20
        self.full_hours = 8
        self.part_time_hours = 4
        self.worktype = worktype.lower()
        self.total_wage = 0

    def check_attendance(self):
        attendance = random.randint(0, 1)
        if attendance == 1:
            self.is_Present = True
        else:
            self.is_Present = False

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
            return 0

        match self.worktype:
            case "full-time":
                return self.calculate_full_time_wage()
            case "part-time":
                return self.calculate_part_time_wage()
            case _:
                return 0

    def calculate_monthly_wage(self):
        for day in range(1, 21):
            self.check_attendance()
            if self.is_Present:
                wage = self.calculate_wage_switch_case()
                print(f"Day {day}: Present - Daily wage: ₹{wage}")
                self.total_wage += wage
            else:
                print(f"Day {day}: Absent - Daily wage: ₹0")
        print(f"\nTotal Monthly Wage for {self.name}: ₹{self.total_wage}")