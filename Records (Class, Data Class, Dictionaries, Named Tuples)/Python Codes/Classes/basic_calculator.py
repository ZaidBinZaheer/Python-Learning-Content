# Define a Calculator class
class Calculator:
    # Constructor to initialize the calculator
    def __init__(self):
        pass  # No need for initializations in this case

    # Method to add two numbers
    def add(self, a, b):
        return a + b

    # Method to subtract two numbers
    def subtract(self, a, b):
        return a - b

    # Method to multiply two numbers
    def multiply(self, a, b):
        return a * b

    # Method to divide two numbers
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero."

# Create an instance of the Calculator class
calculator = Calculator()

# Perform arithmetic operations
result1 = calculator.add(5, 3)
result2 = calculator.subtract(10, 2)
result3 = calculator.multiply(4, 7)
result4 = calculator.divide(8, 2)

# Display results
print(f"Addition: {result1}")
print(f"Subtraction: {result2}")
print(f"Multiplication: {result3}")
print(f"Division: {result4}")
