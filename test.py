form e import employee_details

def test_emplyee_details():
    expected output=(
        "Employee Name:Akash"
        "Employee id: 141"
        "dept:IT"
        "salary:87000"
    )
    assert employee_details("Akash","141","IT",87000)==expected output
