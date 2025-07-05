import random

class Employee:
    wage_per_hour = 20
    full_hours = 8
    part_time_hours = 4
    max_hours = 100
    max_days = 20

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
            total_days += 1

            if self.is_Present:
                work_hours = self.full_hours if self.worktype == "full-time" else self.part_time_hours

                
                if total_hours + work_hours > max_hours:
                    work_hours = max_hours - total_hours

                daily_wage = work_hours * self.wage_per_hour
                self.total_wage += daily_wage
                total_hours += work_hours

                print(f"Day {total_days}: Present - Worked {work_hours} hrs, Earned ₹{daily_wage}")
            else:
                print(f"Day {total_days}: Absent - Earned ₹0")

        print(f"\nTotal Days Worked: {total_days}")
        print(f"Total Hours Worked: {total_hours}")
        print(f"Total Wages Earned by {self.name}: ₹{self.total_wage}")

        return self.total_wage
    
    @classmethod
    def compute_employee_wage(cls, name, worktype):
        emp = cls(name, worktype)
        total_hours = 0
        total_days = 0
        total_wage = 0

        while total_hours < cls.max_hours and total_days < cls.max_days:
            total_days += 1
            emp.check_attendance()

            if not emp.is_Present:
                continue

            daily_hours = cls.full_hours if emp.worktype == "full-time" else cls.part_time_hours

            if total_hours + daily_hours > cls.max_hours:
                daily_hours = cls.max_hours - total_hours

            total_hours += daily_hours
            total_wage += daily_hours * cls.wage_per_hour

        return total_wage


        


        
        

        
        

            