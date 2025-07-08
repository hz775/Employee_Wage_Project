from multiple_employee import MultiEmployeeWageCalculator

class MultiCompanyWageCalculator:
    def compute_all_company_employees(self, companies_data):
        print("===== Multiple Company Wage Report =====\n")

        employee_calc = MultiEmployeeWageCalculator()

        for company in companies_data:
            company_name = company["company"]
            employees = company["employees"]

            print(f"\n===== Company: {company_name} =====\n")

            employee_calc.compute_wages_for_multiple_employees(
                [(emp["name"], emp["worktype"]) for emp in employees]
            )
