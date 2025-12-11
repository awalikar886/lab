def employee_details(name, emp_id, dept, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {dept}\n"
        f"Salary: {salary}"
    )
    return result


if __name__ == "__main__":
    name = "Akash"
    emp_id = 141
    dept = "IT"
    salary = 87000
    print(employee_details(name, emp_id, dept, salary))
