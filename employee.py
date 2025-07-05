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
                self.total_wage += wage
            else:
                pass

    
    def calculate_monthly_wage_with_hour_limit(self, max_hours=100, max_days=20):
        total_hours = 0
        total_days = 0
        self.total_wage = 0

        while total_hours < max_hours and total_days < max_days:
            self.check_attendance()

            if self.is_Present:
                work_hours = self.full_hours if self.worktype == "full-time" else self.part_time_hours

                if total_hours + work_hours > max_hours:
                    work_hours = max_hours - total_hours

                daily_wage = work_hours * self.wage_per_hour
                self.total_wage += daily_wage
                total_hours += work_hours
                total_days += 1

                print(f"Day {total_days}: Present - Worked {work_hours} hrs, Earned ₹{daily_wage}")
            else:
                total_days += 1
                print(f"Day {total_days}: Absent - Earned ₹0")

        print(f"\nTotal Days Worked: {total_days}")
        print(f"Total Hours Worked: {total_hours}")
        print(f"Total Wages Earned by {self.name}: ₹{self.total_wage}")