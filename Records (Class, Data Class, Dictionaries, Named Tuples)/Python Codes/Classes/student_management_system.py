class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []
        
    def add_marks(self, subject, score):
        self.marks.append((subject, score))
        
    def calculate_grade(self):
        total_marks = sum(score for _, score in self.marks)
        average_score = total_marks / len(self.marks)
        
        if average_score >= 90:
            return 'A'
        elif average_score >= 80:
            return 'B'
        elif average_score >= 70:
            return 'C'
        elif average_score >= 60:
            return 'D'
        else:
            return 'F'
        
    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print("Marks:")
        for subject, score in self.marks:
            print(f"  {subject}: {score}")
        print(f"Grade: {self.calculate_grade()}")

# Create a Student instance
student1 = Student("Alice", "2021001")

# Add marks for different subjects
student1.add_marks("Math", 85)
student1.add_marks("Science", 92)
student1.add_marks("History", 78)

# Display student details
student1.display_details()
