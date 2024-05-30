# Define a TodoList class
class TodoList:
    # Constructor to initialize the list of tasks
    def __init__(self):
        self.tasks = []

    # Method to add a task to the list
    def add_task(self, task):
        self.tasks.append(task)

    # Method to remove a task from the list
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    # Method to display all tasks
    def display_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

# Create an instance of the TodoList class
todo_list = TodoList()

# Add tasks to the list
todo_list.add_task("Buy groceries")
todo_list.add_task("Finish homework")
todo_list.add_task("Call a friend")

# Display tasks
print("Tasks:")
todo_list.display_tasks()

# Remove a task
todo_list.remove_task("Finish homework")

# Display updated tasks
print("\nUpdated Tasks:")
todo_list.display_tasks()
