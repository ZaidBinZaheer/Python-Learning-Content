# Define an Employee class to represent employees
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ${self.salary}"

# Define a Company class to manage employee information
class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        for employee in self.employees:
            print(employee.display_details())

    def fire_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return f"Employee {employee.name} (ID: {employee.emp_id}) has been terminated."
        return "Employee not found."

# Create instances of the Employee class
employee1 = Employee(101, "Alice", 50000)
employee2 = Employee(102, "Bob", 60000)
employee3 = Employee(103, "Charlie", 55000)

# Create an instance of the Company class
company = Company("ABC Corp")

# Hire employees
company.hire_employee(employee1)
company.hire_employee(employee2)
company.hire_employee(employee3)

# List employees
print("Employees in ABC Corp:")
company.list_employees()

# Fire an employee
print("\nTerminating an employee:")
print(company.fire_employee(102))

# List employees after termination
print("\nUpdated list of employees:")
company.list_employees()
