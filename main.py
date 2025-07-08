from multiple_company import MultiCompanyWageCalculator

if __name__ == "__main__":
    companies = [
        {
            "company": "TechCorp",
            "employees": [
                {"name": "Alice", "worktype": "full-time"},
                {"name": "Bob", "worktype": "part-time"}
            ]
        },
        {
            "company": "AgriFoods",
            "employees": [
                {"name": "Charlie", "worktype": "full-time"},
                {"name": "Daisy", "worktype": "part-time"}
            ]
        }
    ]

    calculator = MultiCompanyWageCalculator()
    calculator.compute_all_company_employees(companies)
