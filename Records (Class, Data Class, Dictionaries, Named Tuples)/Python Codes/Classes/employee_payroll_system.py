class Employee:
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    def calculate_bonus(self, bonus_percentage):
        bonus_amount = self.salary * (bonus_percentage / 100)
        return bonus_amount

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary for {self.name} updated to {new_salary}")

    def display_employee_details(self):
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Designation: {self.designation}")

# Create an Employee instance
employee1 = Employee("John Doe", 50000, "Software Engineer")

# Display initial details
employee1.display_employee_details()

# Calculate and display bonus
bonus_percentage = 10
bonus_amount = employee1.calculate_bonus(bonus_percentage)
print(f"Bonus amount for {employee1.name}: {bonus_amount}")

# Update salary and display updated details
new_salary = 55000
employee1.update_salary(new_salary)
employee1.display_employee_details()
