# Create an empty dictionary to store student records
student_database = {}

# Function to add a student record to the database
def add_student(name, roll_number, marks):
    student_database[roll_number] = {'name': name, 'marks': marks}

# Function to calculate the average marks of a student
def calculate_average_marks(roll_number):
    if roll_number in student_database:
        marks = student_database[roll_number]['marks']
        total_marks = sum(marks)
        average = total_marks / len(marks)
        return average
    else:
        return None

# Function to find the top scorer
def find_top_scorer():
    top_scorer = None
    max_average = 0

    for roll_number in student_database:
        average = calculate_average_marks(roll_number)
        if average is not None and average > max_average:
            max_average = average
            top_scorer = student_database[roll_number]['name']

    return top_scorer

# Add student records to the database
add_student('Alice', '101', [90, 85, 95])
add_student('Bob', '102', [78, 92, 87])
add_student('Carol', '103', [95, 88, 92])

# Calculate and print the average marks of a student
roll_number = '102'
average_marks = calculate_average_marks(roll_number)
if average_marks is not None:
    print(f"Average marks of student with roll number {roll_number}: {average_marks:.2f}")
else:
    print(f"Student with roll number {roll_number} not found.")

# Find and print the top scorer
top_scorer = find_top_scorer()
if top_scorer is not None:
    print(f"The top scorer is: {top_scorer}")
else:
    print("No top scorer found.")

