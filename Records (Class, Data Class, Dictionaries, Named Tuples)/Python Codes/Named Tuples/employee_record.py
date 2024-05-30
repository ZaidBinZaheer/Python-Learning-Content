from collections import namedtuple

# Define the namedtuple for employee records
Employee = namedtuple("Employee", ["name", "employee_id", "department"])

# Create a list to store employee records
employee_records = [
    Employee("John Doe", 101, "HR"),
    Employee("Jane Smith", 102, "Finance"),
    Employee("Michael Johnson", 103, "IT"),
    Employee("Emily Williams", 104, "HR"),
    Employee("David Brown", 105, "IT")
]

# Function to search for employees by ID
def search_employee_by_id(employee_id):
    for employee in employee_records:
        if employee.employee_id == employee_id:
            return employee
    return None

# Function to list employees in a specific department
def list_employees_by_department(target_department):
    employees_in_department = []
    for employee in employee_records:
        if employee.department == target_department:
            employees_in_department.append(employee)
    return employees_in_department

# Example usage
print("Employee Search by ID:")
search_id = 103
employee = search_employee_by_id(search_id)
if employee:
    print(f"Employee found: {employee.name}, ID: {employee.employee_id}, Department: {employee.department}")
else:
    print(f"Employee with ID {search_id} not found.")

print("\nEmployees in IT Department:")
it_department_employees = list_employees_by_department("IT")
if it_department_employees:
    for employee in it_department_employees:
        print(f"Name: {employee.name}, ID: {employee.employee_id}")
else:
    print("No employees found in the IT department.")
