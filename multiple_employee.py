from employee import Employee

class MultiEmployeeWageCalculator:

    def compute_all_for_employee(self, name, worktype):
        print(f"UC6: Wage Calculation for {name} ({worktype})\n")  

        emp = Employee(name, worktype)
        emp.check_attendance()
        emp.calculate_monthly_wage()

        result = emp.calculate_wage_till_limit()
        for line in result:
            if not line.lower().startswith("uc") and "summary for" not in line.lower():
                print(line)

        print(f"\nTotal Days Worked: {emp.total_days}")
        print(f"Total Hours Worked: {emp.total_hours}")
        print(f"Total Monthly Wage: Rs.{emp.total_wage}")
        print("\n" + "=" * 50 + "\n")

    def compute_wages_for_multiple_employees(self, employees_data):
        for name, worktype in employees_data:
            self.compute_all_for_employee(name, worktype)