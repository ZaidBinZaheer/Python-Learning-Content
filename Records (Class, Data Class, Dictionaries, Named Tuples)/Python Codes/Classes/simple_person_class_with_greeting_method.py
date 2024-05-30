# Define a Person class
class Person:
    # Constructor to initialize attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to greet
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create an instance of the Person class
person1 = Person("Alice", 30)

# Access attributes and call methods
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.

# Create another instance of the Person class
person2 = Person("Bob", 25)

# Access attributes and call methods for the second person
print(person2.greet())  # Output: Hello, my name is Bob and I am 25 years old.
