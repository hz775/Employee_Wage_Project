from multiple_employee import MultiEmployeeWageCalculator

if __name__ == "__main__":
    print("===== Multiple Employee Wage Report =====")

    employees = [
        ("Alice", "full-time"),
        ("Bob", "part-time"),
        ("Charlie", "full-time"),
        ("Daisy", "part-time")
    ]

    calculator = MultiEmployeeWageCalculator()
    calculator.compute_wages_for_multiple_employees(employees)
