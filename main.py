from datetime import datetime

class Task:
    def __init__(self, task_id, description, due_date, completed=False):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(
                f"[{'X' if task.completed else ' '}] {task.task_id}: {task.description} (Due: {task.due_date})"
            )

    def mark_task_as_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_as_completed()

    def clear_all_tasks(self):
        self.tasks.clear()

    def edit_task(self, task_id, new_description, new_due_date):
        for task in self.tasks:
            if task.task_id == task_id:
                task.description = new_description
                task.due_date = new_due_date

    def list_uncompleted_tasks(self):
        print("\n--- Uncompleted Tasks ---")
        uncompleted_tasks = [task for task in self.tasks if not task.completed]
        if not uncompleted_tasks:
            print("No uncompleted tasks.")
        else:
            for task in uncompleted_tasks:
                print(f"[{'X' if task.completed else ' '}] {task.task_id}: {task.description} (Due: {task.due_date})")

    def sort_tasks_by_due_date(self):
        sorted_tasks = sorted(self.tasks, key=lambda task: task.due_date)
        self.tasks = sorted_tasks


if __name__ == "__main__":
    manager = ToDoListManager()

    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear all tasks")
        print("5. Edit a task")
        print("6. Show only uncompleted tasks")
        print("7. Sort tasks by due date")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter finishing date (YYYY-MM-DD): ")
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d")
                task = Task(len(manager.tasks) + 1, description, due_date)
                manager.add_task(task)
                print("Task added successfully!")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        elif choice == "2":
            print("\n--- To-Do List ---")
            manager.list_tasks()

        elif choice == "3":
            task_id = int(input("Enter completed the task ID : "))
            manager.mark_task_as_completed(task_id)
            print("Task marked as completed!")

        elif choice == "4":
            manager.clear_all_tasks()
            print("All tasks cleared!")

        elif choice == "5":
            task_id = int(input("Enter the task ID to edit: "))
            new_description = input("Enter the new description: ")
            new_due_date = input("Enter the new finishing date (YYYY-MM-DD): ")
            try:
                new_due_date = datetime.strptime(new_due_date, "%Y-%m-%d")
                manager.edit_task(task_id, new_description, new_due_date)
                print("Task edited successfully!")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        elif choice == "6":
            manager.list_uncompleted_tasks()

        elif choice == "7":
            manager.sort_tasks_by_due_date()
            print("Tasks sorted by due date!")
            manager.list_tasks()

        elif choice == "8":
            print("Exiting the To-Do List Manager.")
            break

        else:
            print("Invalid choice. Please try again.")


