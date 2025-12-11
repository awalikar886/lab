from e import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Akash\n"
        "Employee ID: 141\n"
        "Department: IT\n"
        "Salary: 87000"
    )
    
    assert employee_details("Akash", "141", "IT", 87000) == expected_output
